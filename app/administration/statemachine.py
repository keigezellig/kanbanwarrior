from app.common.task import *
from app.common.taskwarrior import *

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
     pathToTaskWarrior = None
    
     def __init__(self):
        self.pathToTaskWarrior = FindTaskWarrior();
        if (self.pathToTaskWarrior == None):
            raise IOException("Cannot find Task Warrior program. Please install it")
        
        
     def AddToWip(self, task):
         if (task.state != States.BACKLOG) & (task.state != States.ONHOLD):
             raise TransitionError(task.state,  States.INPROGRESS_INACTIVE,  "Task must be in backlog or on hold")
         
         self.TaskwarriorAddToWip(task)
         
         task.state = States.INPROGRESS_INACTIVE
        
     def TaskwarriorAddToWip(self, task):
        # Command line is:  task <taskid> +inprogress -backlog|-onhold
        verb = "-backlog"
        
        if (task.state == States.ONHOLD):
            verb = "-onhold"
        
        verb = "modify " + verb + " +inprogress"
        
        commandline = self.pathToTaskWarrior + " " +task.taskid.__str__() + " " + verb
        print "TaskwarriorAddToWip => "+commandline

     def Start(self, task):
         if (task.state != States.BACKLOG) & (task.state != States.ONHOLD) & (task.state != States.INPROGRESS_INACTIVE):
             raise TransitionError(task.state,  States.INPROGRESS_ACTIVE,  "Task must be in backlog or on hold or inactive")
         
         if (task.state == States.BACKLOG) | (task.state  == States.ONHOLD) :
            self.AddToWip(task)
         
         self.TaskwarriorStartTask(task)
         task.state = States.INPROGRESS_ACTIVE
        
     def TaskwarriorStartTask(self, task):
         # Command line is:  task <taskid> start
        verb = "start"
        commandline = self.pathToTaskWarrior + " " +task.taskid.__str__() + " " + verb
        print "TaskwarriorStartTask => "+commandline

     def Stop(self, task):
         if (task.state != States.INPROGRESS_ACTIVE):
             raise TransitionError(task.state,  States.INPROGRESS_INACTIVE,  "Task must be active")
         
         self.TaskwarriorStopTask(task)
         task.state = States.INPROGRESS_INACTIVE
        
     def TaskwarriorStopTask(self, task):
         # Command line is:  task <taskid> stop
        verb = "stop"
        commandline = self.pathToTaskWarrior + " " +task.taskid.__str__() + " " + verb
        print ("TaskwarriorStopTask => "+commandline)

     def Hold(self, task,  reason):
         if (task.state != States.INPROGRESS_ACTIVE) & (task.state != States.INPROGRESS_INACTIVE):
             raise TransitionError(task.state,  States.ONHOLD,  "Task must be in progress")
         
         if (task.state == States.INPROGRESS_ACTIVE):
             self.Stop(task)
             
         self.TaskwarriorHoldTask(task,  reason)
         task.state = States.ONHOLD
        
     def TaskwarriorHoldTask(self, task,  reason):
          # Command line is:  task <taskid> modify -inprogress +onhold 
          #                                   task <taskid> annotate <reason>
         verb = "modify -inprogress +onhold"
         verbAnnotate = "annotate " + reason
         commandlineModify = self.pathToTaskWarrior + " " +task.taskid.__str__() + " " + verb
         commandlineAnnotate = self.pathToTaskWarrior + " " +task.taskid.__str__() + " " + verbAnnotate
         print "TaskwarriorHoldTask => " + commandlineModify + "\n " +commandlineAnnotate

     def Finish(self, task):
         if (task.state != States.INPROGRESS_ACTIVE) & (task.state != States.INPROGRESS_INACTIVE):
             raise TransitionError(task.state,  States.INPROGRESS_INACTIVE,  "Task must be in progress")
         
         self.TaskwarriorFinishTask(task)
         task.state = States.DONE
        
     def TaskwarriorFinishTask(self, task):
        # Command line is:  task <taskid> modify -inprogress  
          #                               task <taskid> done
         verb = "modify -inprogress"
         verbDone = "done"
         commandlineModify = self.pathToTaskWarrior + " " +task.taskid.__str__() + " " + verb
         commandlineDone = self.pathToTaskWarrior + " " +task.taskid.__str__() + " " + verbDone
         print "TaskwarriorFinishTask => " + commandlineModify + "\n " +commandlineDone
