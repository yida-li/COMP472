####################################################
# 5. Lazy Stack and Queue
####################################################
from queue import PriorityQueue
f1 = ['jack', 'mack', 'pack', 'sack', 'yack']
print(f1)

print('\nappend on top')
f1.append('zack')
print(f1)
for x in range(len(f1)):
    print(f1[x])

print('\npop the top')
t = f1.pop()
print(t)


f2 = 'back'
print('\n\nRight now the queue has the items :', f1)

print(f'\ninsert {f2} into the front of queue')
f1.insert(0, f2)
print(f1)

print('\npop the the bottom(dequeue)')
f1.pop(0)
print(f1)


q = PriorityQueue()
q.put(5)
q.put(3)
q.put(12)
q.put(10)
q.put(1)
q.put(5)
while not q.empty():
    print(q.get())
