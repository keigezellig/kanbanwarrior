__version__ = '1.0'

import subprocess
from app.common.task import States


class TransitionError(Exception):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        prev -- state at beginning of transition
        next -- attempted new state
        msg  -- explanation of why the specific transition is not allowed
    """

    def __init__(self, prev, next_state, msg):
        super().__init__()
        self.prev = prev
        self.next = next_state
        self.msg = msg
    
    def __str__(self):
        return self.msg
    
class StateMachine:
     taskwarrior_path = None
    
     def __init__(self, taskwarrior_path):
        self.taskwarrior_path = taskwarrior_path;
        
     def add_to_wip(self, task):
         if (task.state != States.BACKLOG) and (task.state != States.ONHOLD):
             raise TransitionError(task.state,  States.INPROGRESS_INACTIVE,  "Task must be in backlog or on hold")
         
         self._tw_add_to_wip(task)
         
         
        
     def _tw_add_to_wip(self, task):
        # Command line is:  task <taskid> modify +inprogress -backlog|-onhold
        verb = "-backlog"
        
        if (task.state == States.ONHOLD):
            verb = "-onhold"
        
        subprocess.call([self.taskwarrior_path, str(task.taskid), 'modify',  '+inprogress',  verb  ])
       

     def start(self, task):
         if (task.state != States.BACKLOG) and (task.state != States.ONHOLD) and (task.state != States.INPROGRESS_INACTIVE):
             raise TransitionError(task.state,  States.INPROGRESS_ACTIVE,  "Task must be in backlog or on hold or inactive")
         
         if (task.state == States.BACKLOG) | (task.state  == States.ONHOLD) :
            self.add_to_wip(task)
         
         self._tw_start_task(task)
         
        
     def _tw_start_task(self, task):
         # Command line is:  task <taskid> start
        subprocess.call([self.taskwarrior_path, str(task.taskid), 'start'  ])

     def stop(self, task):
         if (task.state != States.INPROGRESS_ACTIVE):
             raise TransitionError(task.state,  States.INPROGRESS_INACTIVE,  "Task must be active")
         
         self._tw_stop_task(task)
       
        
     def _tw_stop_task(self, task):
         # Command line is:  task <taskid> stop
       subprocess.call([self.taskwarrior_path,  str(task.taskid), 'stop'  ])

     def hold(self, task,  reason):
         if (task.state != States.INPROGRESS_ACTIVE) and (task.state != States.INPROGRESS_INACTIVE):
             raise TransitionError(task.state,  States.ONHOLD,  "Task must be in progress")
         
         if (task.state == States.INPROGRESS_ACTIVE):
             self.stop(task)
             
         self._tw_hold_task(task,  reason)
        
        
     def _tw_hold_task(self, task,  reason):
          # Command line is:  task <taskid> modify -inprogress +onhold 
          #                                   task <taskid> annotate <reason>
         subprocess.call([self.taskwarrior_path,  str(task.taskid), 'modify', '+onhold',  '-inprogress'  ])
         subprocess.call([self.taskwarrior_path,  str(task.taskid), 'annotate',  'PUT ON HOLD: '+reason  ])

     def finish(self, task):
         if (task.state != States.INPROGRESS_ACTIVE) and (task.state != States.INPROGRESS_INACTIVE):
             raise TransitionError(task.state,  States.INPROGRESS_INACTIVE,  "Task must be in progress")
         
         self._tw_finish_task(task)
         
        
     def _tw_finish_task(self, task):
        # Command line is:  task <taskid> modify -inprogress  
          #                               task <taskid> done
         subprocess.call([self.taskwarrior_path,  str(task.taskid), 'modify', '-inprogress'  ])
         subprocess.call([self.taskwarrior_path,  str(task.taskid),'done'  ])
