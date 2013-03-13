from app.common.task import *
  
def filterfunction(listitem,  id):
    return listitem.taskid == id
    
a = Tasklist()
b = a.getTaskList()

c = [x for x in b if x.taskid == 1] 
d = filter(lambda x: x.taskid == 55, b)
if c == []:
    print "leeg"
else:
    print c[0].taskid
