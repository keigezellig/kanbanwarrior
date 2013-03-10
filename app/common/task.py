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

