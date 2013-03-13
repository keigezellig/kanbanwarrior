
import json
import subprocess

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
