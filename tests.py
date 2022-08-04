




from app.statemachine import StateMachine, TransitionError
from app.task import States, Task
from app.taskwarrior import TaskWarrior


tw = TaskWarrior()

def AddCorrectTaskToWipTest():
     print("***** AddCorrectTaskToWipTest ********")
     task1 = Task(1,States.BACKLOG) 
     task2 = Task(1,States.ONHOLD)
     sm = StateMachine(tw)
     sm.add_to_wip(task1)
     sm.add_to_wip(task2)
     print (task1.state)
     print (task2.state)
     

def AddWrongTaskToWipTest():
     print("***** AddWrongTaskToWipTest ********")
     try:
         task = Task(1,States.INPROGRESS_INACTIVE) 
         sm = StateMachine(tw)
         sm.add_to_wip(task)
         print (task.state)
     except TransitionError as e:
        print (e.msg, e.prev,  e.next)
      
     try: 
         task = Task(1,States.INPROGRESS_ACTIVE) 
         sm = StateMachine(tw)
         sm.add_to_wip(task)
         print (task.state)
     except TransitionError as e:
        print (e.msg, e.prev,  e.next)
     
     try:    
         task = Task(1,States.DONE) 
         sm = StateMachine(tw)
         sm.add_to_wip(task)
         print (task.state)
     except TransitionError as e:
        print (e.msg, e.prev,  e.next)

def StartCorrectTaskTest():
     print ("***** StartCorrectTaskTest ********")
     task1 = Task(1,States.BACKLOG) 
     task2 = Task(1,States.ONHOLD)
     task3 = Task(1,States.INPROGRESS_INACTIVE)
     sm = StateMachine(tw)
     sm.start(task1)
     sm.start(task2)
     sm.start(task3)
     print (task1.state)
     print (task2.state)
     print (task3.state)


def StartWrongTaskTest():
     print ("***** StartWrongTaskTest ********"    )
     try: 
         task = Task(1,States.INPROGRESS_ACTIVE) 
         sm = StateMachine(tw)
         sm.start(task)
         print (task.state)
     except TransitionError as e:
        print (e.msg, e.prev,  e.next)
     
     try:    
         task = Task(1,States.DONE) 
         sm = StateMachine(tw)
         sm.start(task)
         print (task.state)
     except TransitionError as e:
        print (e.msg, e.prev,  e.next)

def StopCorrectTaskTest():
     print ("***** StopCorrectTaskTest ********")
     task1 = Task(1,States.INPROGRESS_ACTIVE) 
     sm = StateMachine(tw)
     sm.stop(task1)
     print (task1.state)
    

def StopWrongTaskTest():
     print ("***** StopWrongTaskTest ********")    
     try: 
         task = Task(1,States.INPROGRESS_INACTIVE) 
         sm = StateMachine(tw)
         sm.stop(task)
         print (task.state)
     except TransitionError as e:
        print (e.msg, e.prev,  e.next)
     
     try:    
         task = Task(1,States.DONE) 
         sm = StateMachine(tw)
         sm.stop(task)
         print (task.state)
     except TransitionError as e:
        print (e.msg, e.prev,  e.next)

     try:    
         task = Task(1,States.BACKLOG) 
         sm = StateMachine(tw)
         sm.stop(task)
         print (task.state)
     except TransitionError as e:
        print (e.msg, e.prev,  e.next)

     try:    
         task = Task(1,States.ONHOLD) 
         sm = StateMachine(tw)
         sm.stop(task)
         print (task.state)
     except TransitionError as e:
        print (e.msg, e.prev,  e.next)


def HoldCorrectTaskTest():
     print ("***** HoldCorrectTaskTest ********")
     task1 = Task(1,States.INPROGRESS_ACTIVE)
     task2 =  Task(2,States.INPROGRESS_INACTIVE)
     sm = StateMachine(tw)
     sm.hold(task1, "Oops")
     sm.hold(task2, "Oops")
     print (task1.state,  task2.state)
    

def HoldWrongTaskTest():
     print ("***** HoldWrongTaskTest ********"    )
     try:    
         task = Task(1,States.DONE) 
         sm = StateMachine(tw)
         sm.hold(task,  "Oops")
         print (task.state)
     except TransitionError as e:
        print (e.msg, e.prev,  e.next)

     try:    
         task = Task(1,States.BACKLOG) 
         sm = StateMachine(tw)
         sm.hold(task,  "Oops")
         print (task.state)
     except TransitionError as e:
        print (e.msg, e.prev,  e.next)

     try:    
         task = Task(1,States.ONHOLD) 
         sm = StateMachine(tw)
         sm.hold(task,  "Oops")
         print (task.state)
     except TransitionError as e:
        print (e.msg, e.prev,  e.next)

def DoneCorrectTaskTest():
     print ("***** DoneCorrectTaskTest ********")
     task1 = Task(1,States.INPROGRESS_ACTIVE)
     task2 =  Task(2,States.INPROGRESS_INACTIVE)
     sm = StateMachine(tw)
     sm.finish(task1)
     sm.finish(task2)
     print (task1.state,  task2.state)
    

def DoneWrongTaskTest():
     print ("***** DoneWrongTaskTest ********"    )
     try:    
         task = Task(1,States.DONE) 
         sm = StateMachine(tw)
         sm.finish(task)
         print (task.state)
     except TransitionError as e:
        print (e.msg, e.prev,  e.next)

     try:    
         task = Task(1,States.BACKLOG) 
         sm = StateMachine(tw)
         sm.finish(task)
         print (task.state)
     except TransitionError as e:
        print (e.msg, e.prev,  e.next)

     try:    
         task = Task(1,States.ONHOLD) 
         sm = StateMachine(tw)
         sm.finish(task)
         print (task.state)
     except TransitionError as e:
        print (e.msg, e.prev,  e.next)

if __name__=="__main__":
    AddCorrectTaskToWipTest()
    AddWrongTaskToWipTest()
    StartCorrectTaskTest()
    StartWrongTaskTest()
    StopCorrectTaskTest()
    StopWrongTaskTest()
    HoldCorrectTaskTest()
    HoldWrongTaskTest()
    DoneCorrectTaskTest()
    DoneWrongTaskTest()
