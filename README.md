kanbanwarrior
=============

A python script supporting my kanban workflow for Task Warrior.
For more info about the workflow itself see http://blog.joosten-industries.nl/2013/03/07/kanban-warrior/

Installation
------------
- Make sure Python 2.7.x is installed. (see http://wiki.python.org/moin/BeginnersGuide/Download)
- Make sure Taskwarrior 2.1.2 or higher is installed. (see http://taskwarrior.org/projects/taskwarrior/wiki/Download)
- Download the scripts by cloning this repository (if you have a git client) or click the link above to download it as an archive.
- Unzip or copy the downloaded files to a directory of your choice (preferably on your path)
- (optional) Set execute bit of the main kanban-warrior.py script by executing: chmod kanban-warrior.py u+x, if you don't want to type 'python' everytime when you
  execute a command.
- Setting up TaskWarrior:
  task config journal.time=on
  task config dateformat.annotation=d-m-Y H:N
  task config dateformat=d-m-Y H:N	
  task config dateformat.report=d-m-Y H:N
  task config dateformat.edit=d-m-Y H:N
  task config dateformat.info=d-m-Y H:N
  task config xterm.title=on
  Of course you can use another date format if you want by replacing the d-m-Y. See the Task Warrior website for more information about this

  

Short usage summary
-------------------

Commands
--------
- Add task to backlog: **kanban-warrior addtobacklog [projectname.storyname] [taskdescription] [priority]**
- Add task to In Progress: **kanban-warrior addtowip [taskid]**
- Start task: **kanban-warrior start [taskid]**
- Stop task: **kanban-warrior stop [taskid]**
- Set task on hold: **kanban-warrior hold [taskid] [reason]**
- Finish a task: **kanban-warrior finish [taskid]**

Reports
--------
- List backlog: **kanban-warrior list backlog [projectname]**
- List work in progress: **kanban-warriot list wip [projectname]**
- List finished work: **kanban-warrior list done [projectname]**
- List work in progress: **kanban-warrior list onhold [projectname]**


