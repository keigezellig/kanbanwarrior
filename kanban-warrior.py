#!/usr/bin/env python

#/*
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

from app.administration.statemachine import *
from app.common.task import *
from app.common.taskwarrior import *
from app.common.command import *

import subprocess

import sys

__version__ = '1.0'

if __name__=="__main__":   
    
    try:
        argParser = constructArgParser() 
        args = argParser.parse_args()
        
        pathToTaskWarrior =  findTaskWarrior()
       
        
        if args.command=='addtobacklog':
            subprocess.check_call([pathToTaskWarrior, 'add', args.taskname,  'project:'+args.projectname,  'priority:'+args.priority,  '+backlog'  ])
            sys.exit(0)
        
      
        if args.command != 'list':
            print "Loading task list.."
            tasklist = Tasklist(pathToTaskWarrior)
            sm = StateMachine(pathToTaskWarrior)
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
            
        else:
            if args.report == 'backlog':
                subprocess.call([pathToTaskWarrior, 'long' , 'project:'+args.projectname,  '+backlog'  ])
            elif args.report == 'wip':
                subprocess.call([pathToTaskWarrior, 'long' ,  'project:'+args.projectname,  '+inprogress'  ])
            elif args.report == 'done':
                subprocess.call([pathToTaskWarrior, 'completed' ])
            elif args.report == 'onhold':
                subprocess.call([pathToTaskWarrior, 'long' , 'project:'+args.projectname,  '+onhold'  ])
                
                
            
            
        
       
        
    except (IOError,  LookupError,  TransitionError) as e:
       sys.exit('Error: '+e.__str__()) 
        
    
    
    
    
    
    


