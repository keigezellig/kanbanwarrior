#!/usr/bin/env python
import argparse

def ConstructArgParser():
    parser = argparse.ArgumentParser()
    
    subparsers = parser.add_subparsers(title='subcommands', description='Valid subcommands are:',  dest="command")
    addtobacklog_parser = subparsers.add_parser('addtobacklog', help='Adds a new task to the backlog')
    addtowip_parser = subparsers.add_parser('addtowip', help='Adds an existing task from the backlog to the in progress queue')
    start_parser = subparsers.add_parser('start', help='Starts a task from the in progress queue')
    stop_parser = subparsers.add_parser('stop', help='Stops a task from the in progress queue')
    finish_parser = subparsers.add_parser('finish', help='Finishes a task')
    hold_parser = subparsers.add_parser('hold', help='Puts a task on hold')

    report_parser = subparsers.add_parser('list', help='Reports')
    reportsubparsers = report_parser.add_subparsers(title='report types',  description='Valid reports are:',  dest='report' )
    backlog_reportparser = reportsubparsers.add_parser('backlog',  help='Displays the contents of the backlog')
    wip_reportparser = reportsubparsers.add_parser('wip',  help='Displays the contents of the in progress queue')
    done_reportparser = reportsubparsers.add_parser('done',  help='Displays finished tasks')
    onhold_reportparser = reportsubparsers.add_parser('onhold',  help='Displays tasks on hold')

    addtobacklog_parser.add_argument('projectname',  help='The name of project for which the task is added. May be in the form project.subproject')
    addtobacklog_parser.add_argument('taskname', help='Task description')
    addtobacklog_parser.add_argument('--priority', choices=['H', 'M', 'L'],  help='Optional task priority. H=High, M=Medium, L=Low. When not specified,  no priority is assigned')
    addtowip_parser.add_argument('taskid', type=int,  help='Id of the task to be added to the In Progress queue (can be obtained by executing ''task list'' )')
    start_parser.add_argument('taskid', type=int,  help='Id of the task to be started (can be obtained by executing ''task list'' )')
    stop_parser.add_argument('taskid', type=int,  help='Id of the task to be stopped (can be obtained by executing ''task list'' )')
    finish_parser.add_argument('taskid', type=int,  help='Id of the task to be finished (can be obtained by executing ''task list'' )')
    hold_parser.add_argument('taskid', type=int,  help='Id of the task to be put on hold (can be obtained by executing ''task list'' )')
    hold_parser.add_argument('reason', help='Reason of putting task on hold')

    backlog_reportparser.add_argument('projectname',  help='The project for which the report is generated. May be in the form project.subproject')
    wip_reportparser.add_argument('projectname',  help='The project for which the report is generated. May be in the form project.subproject')
    done_reportparser.add_argument('projectname',  help='The project for which the report is generated. May be in the form project.subproject')
    onhold_reportparser.add_argument('projectname',  help='The project for which the report is generated. May be in the form project.subproject')

    return parser
    
    
argParser = ConstructArgParser() 

args = argParser.parse_args()
print args


