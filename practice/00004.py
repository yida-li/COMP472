####################################################
# 4. Generic List
####################################################

f1 = []
f2 = [11, 33, 11.1, 33.3]
f3 = [333333]
f4 = f2+f3
print(f1, f2)
print(f4)

print('\nf1 append 23')
f1.append(23)
print(f1)
print('\nf1 append 11.111')
f1.append(11.111)
print(f1)

print('\nf1 extend f2')
f1.extend(f2)
print(f1)

print('\nf1 pop(0) ')
f1.pop(0)
print(f1)

print('\nf1 pop() ')
f1.pop()
print(f1)

print('\nf1 pop(2)')
f1.pop(2)
print(f1)

print('\nf1 insert 99 at start of list')
f1.insert(0, 99)
print(f1)


print('\nf1 insert 88 at end of list')
f1.insert(len(f1), 88)
print(f1)

print('\nthe last element is : ', f1[-1])
print(f'the second element of {f1} is ', f1[1])
print(f'the first element of {f1} is ', f1[0])
f1.clear()
print(f1)
