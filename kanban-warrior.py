#!/usr/bin/env python

from app.administration.statemachine import *
from app.common.task import *
from app.common.taskwarrior import *
from app.common.command import *

import subprocess

import sys

__version__ = '0.1'

if __name__=="__main__":   
    
    try:
        argParser = constructArgParser() 
        args = argParser.parse_args()
        
        pathToTW =  findTaskWarrior()
       
        
        if args.command=='addtobacklog':
            subprocess.check_call(['task', 'add', args.taskname,  'project:'+args.projectname,  'priority:'+args.priority,  '+backlog'  ])
            sys.exit(0)
        
      
        if args.command != 'list':
            print "Loading task list.."
            tasklist = Tasklist(pathToTW)
            sm = StateMachine(pathToTW)
            task = tasklist.getTaskById(args.taskid)
            if task == None:
                sys.exit('Unknown task specified. Aborting program')
            
            if args.command == 'addtowip':
                sm.addToWip(task)
            elif args.command == 'start':
                sm.start(task)
            elif args.command == 'stop':
                sm.stop(task)
            elif args.command == 'finish':
                sm.finish(task)
            elif args.command == 'hold':
                sm.hold(task, args.reason)
            sys.exit(0)
        else:
            print "Sorry, not implemented yet"
        
       
        
    except (IOError,  LookupError,  TransitionError) as e:
       sys.exit('Error: '+e.__str__()) 
        
    
    
    
    
    
    


