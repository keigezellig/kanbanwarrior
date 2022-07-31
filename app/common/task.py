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
           self.path_to_tw = pathToTW;
           if (self.path_to_tw is None):
               raise IOError("Cannot find Task Warrior program. Please install it")
           self.__list = self._get_task_list()
           

       def get_task_by_id(self, task_id):           
           taskfilter = filter(lambda x: x.taskid == task_id, self.__list)
           if not taskfilter:
               raise LookupError('Unknown task specified.')
           else:
               return list(taskfilter)[0]
       
       def _map_to_task(self, taskitem):
            if ('tags' in taskitem) and (len(taskitem['tags']) == 1) and ('backlog' in taskitem['tags']): 
                return Task(taskitem['id'], States.BACKLOG)
               
            if ('tags' in taskitem) and (len(taskitem['tags']) == 1) and ('inprogress' in taskitem['tags']):
                if ('start' in taskitem):
                    return Task(taskitem['id'], States.INPROGRESS_ACTIVE)
                else:
                    return Task(taskitem['id'], States.INPROGRESS_INACTIVE)
            
            if ('tags' in taskitem) and (len(taskitem['tags']) == 1) and ('onhold' in taskitem['tags']): 
                return Task(taskitem['id'], States.ONHOLD)
     

       def _filter_illegal_tasks(self,  listitem):
            return listitem is not None and listitem.taskid != 0
    

       def _get_task_list(self):
        # excecute and get output from task export command
        export_output = subprocess.check_output([self.path_to_tw,'export']).decode() 
        print(export_output)
        
        # # strip funky header (goes until first \n)
        # jsonstring = export_output[export_output.index('\n')+1:] 
        # # add array brackets for json deserialization
        # jsonstring = '[' + jsonstring
        # jsonstring = jsonstring + ']' 
        
        tasklist = json.loads(export_output)

        # map it to a list of task objects
        tasklist = map(self._map_to_task, tasklist)
        # filter out the illegal ones
        tasklist = filter(self._filter_illegal_tasks, tasklist)
        
        return tasklist
