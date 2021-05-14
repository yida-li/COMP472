####################################################
# 6. Imutable List
####################################################

f1 = (17, 'S', 'stave')   # tuple
f2 = ['steve', 'theive', 'stave']   # list

print(type(f1))
print(type(f2))


print('tuples has the values : ', f1)
f1 = f1 + ('mieve', 70.77, 'kief')
print('tuples now have the values : ', f1)


print('\n assigning variables of f1 into seperate variables')
a, b, c, d, e, f = f1

print('variable a is : ', a, ' and of type ', type(a))
print('variable b is : ', b, ' and of type ', type(b))
print('variable e is : ', e, ' and of type ', type(e))


print('f1[3]= literally anything will result in error because tuples are static once declared')
f1[3] = 'try it'
