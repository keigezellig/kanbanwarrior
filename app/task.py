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

from app.taskwarrior import TaskWarrior
from typing import List

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
       
       def __init__(self,  task_warrior: TaskWarrior):
           self._list = self._get_task_list(task_warrior)
           

       def get_task_by_id(self, task_id):           
           task_to_be_found = [task for task in self._list if task.taskid==task_id]
           if not task_to_be_found:
               raise LookupError('Unknown task specified.')
           else:
               return task_to_be_found[0]
       
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
     

       def _is_valid_task(self,  listitem):
            return listitem is not None and listitem['id'] != 0
    

       def _get_task_list(self, task_warrior: TaskWarrior) -> List[Task]:
        
        raw_list = task_warrior.get_task_list()
    
        # map it to a list of task objects and filter out the illegal ones
        tasklist: List[Task] = [self._map_to_task(item) for item in raw_list if self._is_valid_task(item)]  
        return tasklist
