import os

__version__ = '0.1'

def findTaskWarrior():
     #Default path for now, maybe in the future configurable
     filename='task'
     path='/usr/bin'
     for root, dirs, names in os.walk(path):
            if filename in names:
                return os.path.join(root, filename)
            else:
                raise IOError('Cannot find TaskWarrior binary. It should be located in the /usr/bin folder')
            
     


    
    
