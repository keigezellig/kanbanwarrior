import os

def FindTaskWarrior():
    
     filename='task'
     path='/usr/bin'
     for root, dirs, names in os.walk(path):
            if filename in names:
                return os.path.join(root, filename)
            
     return None


    
    
