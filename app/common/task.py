#/*
# * -----------------------------------------------------------------------------------------------
# * "THE APPRECIATION LICENSE" (Revision 0xFF):
# * Copyright (c) 2013 M. Joosten
# * You can do anything with this program and its code, even use it to run a nuclear reactor (why should you)
#   But I won't be responsible for possible damage and mishap, because i never tested it on a nuclear reactor (why should I..)  
#   If you think this program/code is absolutely great and supercalifragilisticexpialidocious (or just plain useful), just
#   let me know by sending me a nice email or postcard from your country of origin and leave this header in the code
#   See my blog (http://keigezellig.blog.com), for contact info
# * ---------------------------------------------------------------------------------------------------
# */
import json
import subprocess

__version__ = '1.0'

class States:
    NONE = 0
    BACKLOG = 1
    INPROGRESS_INACTIVE = 2
    INPROGRESS_ACTIVE = 3
    DONE = 4
    ONHOLD = 5

class Task:
    taskid = 0
    state  = States.NONE
    
    def __init__(self,  taskid,  state):
        self.taskid = taskid
        self.state = state

class Tasklist:
       __list = []
       
       def __init__(self,  pathToTW):
           self.pathToTaskWarrior = pathToTW;
           if (self.pathToTaskWarrior == None):
               raise IOException("Cannot find Task Warrior program. Please install it")
           self.__list = self.__getTaskList()
           

       def getTaskById(self, id):           
           taskfilter = filter(lambda x: x.taskid == id, self.__list)
           if taskfilter == []:
               raise LookupError('Unknown task specified.')
           else:
               return taskfilter[0]
       
       def __mapToTask(self, taskitem):
            if ('tags' in taskitem) and (len(taskitem['tags']) == 1) and ('backlog' in taskitem['tags']): 
                return Task(taskitem['id'], States.BACKLOG)
               
            if ('tags' in taskitem) and (len(taskitem['tags']) == 1) and ('inprogress' in taskitem['tags']):
                if ('start' in taskitem):
                    return Task(taskitem['id'], States.INPROGRESS_ACTIVE)
                else:
                    return Task(taskitem['id'], States.INPROGRESS_INACTIVE)
            
            if ('tags' in taskitem) and (len(taskitem['tags']) == 1) and ('onhold' in taskitem['tags']): 
                return Task(taskitem['id'], States.ONHOLD)
     

       def __filterIllegalTasks(self,  listitem):
            return listitem != None and listitem.taskid != 0
    

       def __getTaskList(self):
        # excecute and get output from task export command
        exportOutput = subprocess.check_output([self.pathToTaskWarrior,'export']) 
        
        # strip funky header (goes until first \n)
        jsonstring = exportOutput[exportOutput.index('\n')+1:] 
        # add array brackets for json deserialization
        jsonstring = '[' + jsonstring
        jsonstring = jsonstring + ']' 
        
        tasklist = json.loads(jsonstring)

        # map it to a list of task objects
        tasklist = map(self.__mapToTask, tasklist)
        # filter out the illegal ones
        tasklist = filter(self.__filterIllegalTasks, tasklist)
        
        return tasklist
