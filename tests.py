
from app.administration.statemachine import *


def AddCorrectTaskToWipTest():
     print "***** AddCorrectTaskToWipTest ********"
     task1 = Task(1,States.BACKLOG) 
     task2 = Task(1,States.ONHOLD)
     sm = StateMachine()
     sm.AddToWip(task1)
     sm.AddToWip(task2)
     print task1.state
     print task2.state
     

def AddWrongTaskToWipTest():
     print "***** AddWrongTaskToWipTest ********"
     try:
         task = Task(1,States.INPROGRESS_INACTIVE) 
         sm = StateMachine()
         sm.AddToWip(task)
         print task.state
     except TransitionError as e:
        print e.msg, e.prev,  e.next
      
     try: 
         task = Task(1,States.INPROGRESS_ACTIVE) 
         sm = StateMachine()
         sm.AddToWip(task)
         print task.state
     except TransitionError as e:
        print e.msg, e.prev,  e.next
     
     try:    
         task = Task(1,States.DONE) 
         sm = StateMachine()
         sm.AddToWip(task)
         print task.state
     except TransitionError as e:
        print e.msg, e.prev,  e.next

def StartCorrectTaskTest():
     print "***** StartCorrectTaskTest ********"
     task1 = Task(1,States.BACKLOG) 
     task2 = Task(1,States.ONHOLD)
     task3 = Task(1,States.INPROGRESS_INACTIVE)
     sm = StateMachine()
     sm.Start(task1)
     sm.Start(task2)
     print task1.state
     print task2.state


def StartWrongTaskTest():
     print "***** StartWrongTaskTest ********"    
     try: 
         task = Task(1,States.INPROGRESS_ACTIVE) 
         sm = StateMachine()
         sm.Start(task)
         print task.state
     except TransitionError as e:
        print e.msg, e.prev,  e.next
     
     try:    
         task = Task(1,States.DONE) 
         sm = StateMachine()
         sm.Start(task)
         print task.state
     except TransitionError as e:
        print e.msg, e.prev,  e.next

def StopCorrectTaskTest():
     print "***** StopCorrectTaskTest ********"
     task1 = Task(1,States.INPROGRESS_ACTIVE) 
     sm = StateMachine()
     sm.Stop(task1)
     print task1.state
    

def StopWrongTaskTest():
     print "***** StopWrongTaskTest ********"    
     try: 
         task = Task(1,States.INPROGRESS_INACTIVE) 
         sm = StateMachine()
         sm.Stop(task)
         print task.state
     except TransitionError as e:
        print e.msg, e.prev,  e.next
     
     try:    
         task = Task(1,States.DONE) 
         sm = StateMachine()
         sm.Stop(task)
         print task.state
     except TransitionError as e:
        print e.msg, e.prev,  e.next

     try:    
         task = Task(1,States.BACKLOG) 
         sm = StateMachine()
         sm.Stop(task)
         print task.state
     except TransitionError as e:
        print e.msg, e.prev,  e.next

     try:    
         task = Task(1,States.ONHOLD) 
         sm = StateMachine()
         sm.Stop(task)
         print task.state
     except TransitionError as e:
        print e.msg, e.prev,  e.next


def HoldCorrectTaskTest():
     print "***** HoldCorrectTaskTest ********"
     task1 = Task(1,States.INPROGRESS_ACTIVE)
     task2 =  Task(2,States.INPROGRESS_INACTIVE)
     sm = StateMachine()
     sm.Hold(task1)
     sm.Hold(task2)
     print task1.state,  task2.state
    

def HoldWrongTaskTest():
     print "***** HoldWrongTaskTest ********"    
     try:    
         task = Task(1,States.DONE) 
         sm = StateMachine()
         sm.Hold(task)
         print task.state
     except TransitionError as e:
        print e.msg, e.prev,  e.next

     try:    
         task = Task(1,States.BACKLOG) 
         sm = StateMachine()
         sm.Hold(task)
         print task.state
     except TransitionError as e:
        print e.msg, e.prev,  e.next

     try:    
         task = Task(1,States.ONHOLD) 
         sm = StateMachine()
         sm.Hold(task)
         print task.state
     except TransitionError as e:
        print e.msg, e.prev,  e.next

def DoneCorrectTaskTest():
     print "***** DoneCorrectTaskTest ********"
     task1 = Task(1,States.INPROGRESS_ACTIVE)
     task2 =  Task(2,States.INPROGRESS_INACTIVE)
     sm = StateMachine()
     sm.Finish(task1)
     sm.Finish(task2)
     print task1.state,  task2.state
    

def DoneWrongTaskTest():
     print "***** HoldWrongTaskTest ********"    
     try:    
         task = Task(1,States.DONE) 
         sm = StateMachine()
         sm.Finish(task)
         print task.state
     except TransitionError as e:
        print e.msg, e.prev,  e.next

     try:    
         task = Task(1,States.BACKLOG) 
         sm = StateMachine()
         sm.Finish(task)
         print task.state
     except TransitionError as e:
        print e.msg, e.prev,  e.next

     try:    
         task = Task(1,States.ONHOLD) 
         sm = StateMachine()
         sm.Finish(task)
         print task.state
     except TransitionError as e:
        print e.msg, e.prev,  e.next

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
