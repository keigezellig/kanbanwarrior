import json
import os
import subprocess


class TaskWarrior():
    """
    This class wraps all relevant TaskWarrior commands and executes them accordingly.
    """

    def __init__(self, path_to_binary: str = '/usr/bin') -> None:
        self._executable: str = os.path.join(path_to_binary, 'task')
        if not os.path.exists(self._executable):
            raise IOError(
                f"Task Warrior cannot be found at {self._executable}. Is Task Warrior installed?")

    def add_to_backlog(self, taskname: str, project: str, priority: str):
        subprocess.check_call([self._executable, 'add', taskname,  'project:'+project,  'priority:'+priority,  '+backlog'  ])

    def set_in_progress(self, task_id: str, tag_to_be_removed: str):
        # Command line is:  task <taskid> modify +inprogress -backlog|-onhold
        subprocess.call([self._executable, task_id, 'modify',  '+inprogress',  tag_to_be_removed])

    def start_task(self, task_id: str):
        # Command line is:  task <taskid> start
        subprocess.call([self._executable, task_id, 'start'])

    def stop_task(self, task_id: str):
        # Command line is:  task <taskid> stop
        subprocess.call([self._executable,  task_id, 'stop'])

    def hold_task(self, task_id: str,  reason: str):
        # Command line is:  task <taskid> modify -inprogress +onhold
        #                                   task <taskid> annotate <reason>
        subprocess.call([self._executable,  task_id, 'modify', '+onhold',  '-inprogress'])
        subprocess.call([self._executable,  task_id, 'annotate',  'PUT ON HOLD: '+reason])

    def finish_task(self, task_id: str):
        # Command line is:  task <taskid> modify -inprogress
        #                               task <taskid> done
        subprocess.call([self._executable,  task_id, 'modify', '-inprogress'])
        subprocess.call([self._executable,  task_id, 'done'])

    def get_task_list(self):
        # excecute and get output from task export command
        export_output = subprocess.check_output([self._executable, 'export']).decode()
        tasklist = json.loads(export_output)

        return tasklist

    def get_backlog_report(self, project: str):           
        subprocess.call([self._executable, 'long' , 'project:'+project,  '+backlog'  ])
    
    def get_wip_report(self, project: str):
        subprocess.call([self._executable, 'long' ,  'project:'+project,  '+inprogress'  ])

    def get_finished_tasks_report(self):
        subprocess.call([self._executable, 'completed' ])
    
    def get_onhold_report(self, project: str):
        subprocess.call([self._executable, 'long' , 'project:'+project,  '+onhold'  ])
