#!/usr/bin/env python

# /*
# * -----------------------------------------------------------------------------------------------
# * "THE APPRECIATION LICENSE" (Revision 0xFF):
# * Copyright (c) 2013 M. Joosten
# * You can do anything with this program and its code, even use it to run a nuclear reactor (why should you)
#   But I won't be responsible for possible damage and mishap, because i never tested it on a nuclear reactor (why should I..)
#   If you think this program/code is absolutely great and supercalifragilisticexpialidocious (or just plain useful), just
#   let me know by sending me a nice email or postcard from your country of origin and leave this header in the code
#   See my blog (http://keigezellig.blog.com), for contact info
# * ---------------------------------------------------------------------------------------------------
# */

import sys
from app.statemachine import StateMachine, TransitionError

from app.command import construct_argparser
from app.task import Tasklist
from app.taskwarrior import TaskWarrior


__version__ = '1.0'

if __name__ == "__main__":

    try:

        task_warrior: TaskWarrior = TaskWarrior()
        print("Loading task list..")
        tasklist = Tasklist(task_warrior)
        sm = StateMachine(task_warrior)

        argParser = construct_argparser()
        args = argParser.parse_args()

        print(args.command)

        if args.command == 'addtobacklog':
            task_warrior.add_to_backlog(args.taskname, args.projectname, args.priority)
            sys.exit(0)

        if args.command != 'list':
            task = tasklist.get_task_by_id(args.taskid)
            if task is None:
                sys.exit('Unknown task specified. Aborting program')
            if args.command == 'addtowip':
                sm.add_to_wip(task)
            elif args.command == 'start':
                sm.start(task)
            elif args.command == 'stop':
                sm.stop(task)
            elif args.command == 'finish':
                sm.finish(task)
            elif args.command == 'hold':
                sm.hold(task, args.reason)

        else:
            if args.report == 'backlog':
                task_warrior.get_backlog_report(args.projectname)
            elif args.report == 'wip':
                task_warrior.get_wip_report(args.projectname)
            elif args.report == 'done':
                task_warrior.get_finished_tasks_report()
            elif args.report == 'onhold':
                task_warrior.get_onhold_report(args.projectname)

    except (IOError,  LookupError,  TransitionError) as e:
        sys.exit('Error: '+str(e))
