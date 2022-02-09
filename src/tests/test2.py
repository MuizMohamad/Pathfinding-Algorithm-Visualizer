lst = []

def test(lst,i):
    if (i == 5):
      return lst
    
    return test(lst+[i],i+1)

print(test(lst,1))

import time
l = [1,2,3,4,5]
for i in l:
    print(i)
    time.sleep(1)