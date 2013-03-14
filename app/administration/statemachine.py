from app.common.task import *
from app.common.taskwarrior import *

__version__ = '1.0'

class TransitionError(Exception):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        prev -- state at beginning of transition
        next -- attempted new state
        msg  -- explanation of why the specific transition is not allowed
    """

    def __init__(self, prev, next, msg):
        self.prev = prev
        self.next = next
        self.msg = msg
    
    def __str__(self):
        return self.msg
    
class StateMachine:
     pathToTaskWarrior = None
    
     def __init__(self, pathToTW):
        self.pathToTaskWarrior = pathToTW;
        
     def addToWip(self, task):
         if (task.state != States.BACKLOG) and (task.state != States.ONHOLD):
             raise TransitionError(task.state,  States.INPROGRESS_INACTIVE,  "Task must be in backlog or on hold")
         
         self.__taskwarriorAddToWip(task)
         
         
        
     def __taskwarriorAddToWip(self, task):
        # Command line is:  task <taskid> modify +inprogress -backlog|-onhold
        verb = "-backlog"
        
        if (task.state == States.ONHOLD):
            verb = "-onhold"
        
        subprocess.call([self.pathToTaskWarrior, task.taskid.__str__(), 'modify',  '+inprogress',  verb  ])
       

     def start(self, task):
         if (task.state != States.BACKLOG) and (task.state != States.ONHOLD) and (task.state != States.INPROGRESS_INACTIVE):
             raise TransitionError(task.state,  States.INPROGRESS_ACTIVE,  "Task must be in backlog or on hold or inactive")
         
         if (task.state == States.BACKLOG) | (task.state  == States.ONHOLD) :
            self.addToWip(task)
         
         self.__taskwarriorStartTask(task)
         
        
     def __taskwarriorStartTask(self, task):
         # Command line is:  task <taskid> start
        subprocess.call([self.pathToTaskWarrior, task.taskid.__str__(), 'start'  ])

     def stop(self, task):
         if (task.state != States.INPROGRESS_ACTIVE):
             raise TransitionError(task.state,  States.INPROGRESS_INACTIVE,  "Task must be active")
         
         self.__taskwarriorStopTask(task)
       
        
     def __taskwarriorStopTask(self, task):
         # Command line is:  task <taskid> stop
       subprocess.call([self.pathToTaskWarrior,  task.taskid.__str__(), 'stop'  ])

     def hold(self, task,  reason):
         if (task.state != States.INPROGRESS_ACTIVE) and (task.state != States.INPROGRESS_INACTIVE):
             raise TransitionError(task.state,  States.ONHOLD,  "Task must be in progress")
         
         if (task.state == States.INPROGRESS_ACTIVE):
             self.stop(task)
             
         self.__taskwarriorHoldTask(task,  reason)
        
        
     def __taskwarriorHoldTask(self, task,  reason):
          # Command line is:  task <taskid> modify -inprogress +onhold 
          #                                   task <taskid> annotate <reason>
         subprocess.call([self.pathToTaskWarrior,  task.taskid.__str__(), 'modify', '+onhold',  '-inprogress'  ])
         subprocess.call([self.pathToTaskWarrior,  task.taskid.__str__(), 'annotate',  'PUT ON HOLD: '+reason  ])

     def finish(self, task):
         if (task.state != States.INPROGRESS_ACTIVE) and (task.state != States.INPROGRESS_INACTIVE):
             raise TransitionError(task.state,  States.INPROGRESS_INACTIVE,  "Task must be in progress")
         
         self.__taskwarriorFinishTask(task)
         
        
     def __taskwarriorFinishTask(self, task):
        # Command line is:  task <taskid> modify -inprogress  
          #                               task <taskid> done
         subprocess.call([self.pathToTaskWarrior,  task.taskid.__str__(), 'modify', '-inprogress'  ])
         subprocess.call([self.pathToTaskWarrior,  task.taskid.__str__(),'done'  ])
