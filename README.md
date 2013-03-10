kanbanwarrior
=============

A python script supporting my kanban workflow for Task Warrior.
For more info about the workflow itself see http://keigezellig.blog.com/2013/03/07/kanban-warrior/

Installation
------------
- Make sure Python 2.7.3 or higher is installed. (see http://wiki.python.org/moin/BeginnersGuide/Download)
- Make sure Taskwarrior 2.1.2 or higher is installed. (see http://taskwarrior.org/projects/taskwarrior/wiki/Download)
- Copy the scripts to a directory of your choice.

Usage
-----

Commands
--------
- <b>Add task to backlog:</b> kanban-warrior addtobacklog [projectname.storyname] [taskdescription] [priority]
- <b>Add task to In Progress</b>: kanban-warrior addtowip [taskid]
- <b>Start task</b>: kanban-warrior start [taskid]
- <b>Stop task</b>: kanban-warrior stop [taskid]
- <b>Set task on hold</b>: kanban-warrior hold [taskid] [reason]
- <b>Finish a task: </b> kanban-warrior finish [taskid]

Reports
--------
- <b>List backlog</b>: kanban-warrior list [projectname] backlog 
- <b>List work in progress</b>: kanban-warriot list [projectname] wip 
- <b>List finished work</b>: kanban-warrior list [projectname] done 
- <b>List work in progress</b>: kanban-warrior list [projectname] onhold 


