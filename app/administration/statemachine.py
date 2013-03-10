from app.common.task import *

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
        
    
class StateMachine:
     def AddToWip(self, task):
         if (task.state != States.BACKLOG) & (task.state != States.ONHOLD):
             raise TransitionError(task.state,  States.INPROGRESS_INACTIVE,  "Task must be in backlog or on hold")
         
         self.TaskwarriorAddToWip(task)
         
         task.state = States.INPROGRESS_INACTIVE
        
     def TaskwarriorAddToWip(self, task):
        print "TaskwarriorAddToWip => task = "+task.taskid.__str__()

     def Start(self, task):
         if (task.state != States.BACKLOG) & (task.state != States.ONHOLD) & (task.state != States.INPROGRESS_INACTIVE):
             raise TransitionError(task.state,  States.INPROGRESS_ACTIVE,  "Task must be in backlog or on hold or inactive")
         
         if (task.state == States.BACKLOG) | (task.state  == States.ONHOLD) :
            self.TaskwarriorAddToWip(task)
         
         self.TaskwarriorStartTask(task)
         task.state = States.INPROGRESS_ACTIVE
        
     def TaskwarriorStartTask(self, task):
        print "TaskwarriorStartTask => task = "+task.taskid.__str__()

     def Stop(self, task):
         if (task.state != States.INPROGRESS_ACTIVE):
             raise TransitionError(task.state,  States.INPROGRESS_INACTIVE,  "Task must be active")
         
         self.TaskwarriorStopTask(task)
         task.state = States.INPROGRESS_INACTIVE
        
     def TaskwarriorStopTask(self, task):
        print "TaskwarriorStopTask => task = "+task.taskid.__str__()

     def Hold(self, task):
         if (task.state != States.INPROGRESS_ACTIVE) & (task.state != States.INPROGRESS_INACTIVE):
             raise TransitionError(task.state,  States.ONHOLD,  "Task must be in progress")
         
         self.TaskwarriorHoldTask(task)
         task.state = States.ONHOLD
        
     def TaskwarriorHoldTask(self, task):
        print "TaskwarriorHoldTask => task = "+task.taskid.__str__()

     def Finish(self, task):
         if (task.state != States.INPROGRESS_ACTIVE) & (task.state != States.INPROGRESS_INACTIVE):
             raise TransitionError(task.state,  States.INPROGRESS_INACTIVE,  "Task must be in progress")
         
         self.TaskwarriorFinishTask(task)
         task.state = States.DONE
        
     def TaskwarriorFinishTask(self, task):
        print "TaskwarriorFinishTask => task = "+task.taskid.__str__()
