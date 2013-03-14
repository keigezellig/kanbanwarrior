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
 
import os

__version__ = '1.0'

def findTaskWarrior():
     #Default path for now, maybe in the future configurable
     filename='task'
     path='/usr/bin'
     for root, dirs, names in os.walk(path):
            if filename in names:
                return os.path.join(root, filename)
            else:
                raise IOError('Cannot find TaskWarrior binary. It should be located in the /usr/bin folder')
            
     


    
    
