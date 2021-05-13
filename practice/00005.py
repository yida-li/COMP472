####################################################
# 5. Lazy Stack and Queue
####################################################

f1 = ['jack', 'mack', 'pack', 'sack', 'yack']
print(f1)

print('\nappend on top')
f1.append('zack')
print(f1)

print('\npop the top')
f1.pop()
print(f1)


f2 = 'back'

print(f'\ninsert {f2} into the front of queue')
f1.insert(0, f2)
print(f1)

print('\npop the the bottom(dequeue)')
f1.pop(0)
print(f1)
