####################################################
# 8. : Plain Loop
####################################################

print('\n loop through list')
for f2 in ["seventy-seven", "four", "4", "22.2"]:
    print("{} is a number".format(f2))


print('\n loop with range')
for f3 in range(5):
    print(f3)

print('\n loop with while statement ')
f4 = 0
while f4 < 5:
    print(f4)
    f4 += 1

print('\nLoop from range of 4 to 10 with step unit of 2')
for f5 in range(4, 12, 2):
    print(f5)


print('\n loop through tuples')
f6 = {1, 4, 5, 15, 21}
for f7 in f6:
    print(f7)

print('\n loop through dictionary')
f8 = {"wow": 23, "mane": 12, "gse3": 12}
for f9 in f8:
    print(f9)
