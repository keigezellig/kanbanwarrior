__version__ = '1.0'

from app.task import States, Task
from app.taskwarrior import TaskWarrior


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
    def __init__(self, taskwarrior: TaskWarrior):
        self._taskwarrior = taskwarrior

    def add_to_wip(self, task: Task):
        if (task.state != States.BACKLOG) and (task.state != States.ONHOLD):
            raise TransitionError(task.state,  States.INPROGRESS_INACTIVE,
                                  "Task must be in backlog or on hold")

        self._tw_add_to_wip(task)

    def _tw_add_to_wip(self, task: Task):
        verb = "-backlog"

        if (task.state == States.ONHOLD):
            verb = "-onhold"

        self._taskwarrior.set_in_progress(str(task.taskid), verb)

    def start(self, task: Task):
        if (task.state != States.BACKLOG) and (task.state != States.ONHOLD) and (task.state != States.INPROGRESS_INACTIVE):
            raise TransitionError(task.state,  States.INPROGRESS_ACTIVE,
                                  "Task must be in backlog or on hold or inactive")

        if (task.state == States.BACKLOG) or (task.state == States.ONHOLD):
            self._tw_add_to_wip(task)

        self._taskwarrior.start_task(str(task.taskid))

    def stop(self, task: Task):
        if (task.state != States.INPROGRESS_ACTIVE):
            raise TransitionError(task.state,  States.INPROGRESS_INACTIVE,  "Task must be active")

        self._taskwarrior.stop_task(str(task.taskid))

    def hold(self, task: Task,  reason: str):
        if (task.state != States.INPROGRESS_ACTIVE) and (task.state != States.INPROGRESS_INACTIVE):
            raise TransitionError(task.state,  States.ONHOLD,  "Task must be in progress")

        if (task.state == States.INPROGRESS_ACTIVE):
            self._taskwarrior.stop_task(str(task.taskid))

        self._taskwarrior.hold_task(str(task.taskid), reason)

    def finish(self, task: Task):
        if (task.state != States.INPROGRESS_ACTIVE) and (task.state != States.INPROGRESS_INACTIVE):
            raise TransitionError(task.state,  States.INPROGRESS_INACTIVE,
                                  "Task must be in progress")

        self._taskwarrior.finish_task(str(task.taskid))
