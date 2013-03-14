kanbanwarrior
=============

A python script supporting my kanban workflow for Task Warrior.
For more info about the workflow itself see http://keigezellig.blog.com/2013/03/07/kanban-warrior/

Installation
------------
- Make sure Python 2.7.3 or higher is installed. (see http://wiki.python.org/moin/BeginnersGuide/Download)
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
- Add task to backlog: <b>kanban-warrior addtobacklog [projectname.storyname] [taskdescription] [priority]</b>
- Add task to In Progress: <b>kanban-warrior addtowip [taskid]</b>
- Start task: kanban-warrior <b>start [taskid]</b>
- Stop task: kanban-warrior <b>stop [taskid]</b>
- Set task on hold: <b>kanban-warrior hold [taskid] [reason]</b>
- Finish a task: <b>kanban-warrior finish [taskid]</b>

Reports
--------
- List backlog</b>: <b>kanban-warrior list backlog [projectname]</b> 
- List work in progress</b>: <b>kanban-warriot list wip [projectname]</b>
- List finished work</b>: <b>kanban-warrior list done [projectname]</b> 
- List work in progress</b>: <b>kanban-warrior list onhold [projectname]</b> 


