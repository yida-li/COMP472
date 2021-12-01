####################################################
# 13. : File Read/Write
####################################################
import json

f1 = ('A', 'B', 'C')

print("\nWriting a tuple into file and reading it\n")
with open('practice/practice.txt', 'a+') as f:

    for f1 in f1:
        f.write(f1)
        f.write('\n')




with open('practice/practice.txt', 'r') as f2:
    for f3 in f2:
        print(f3)


print("\nWriting a dictionary(json) into file and reading it\n")
# also the stuff written earlier is overwritten magically inexplicably mysteriously
3
f4 = {"dictionary": 1, "bible": 2, "Bescherelle": 3}
f5 = {'name': 'person', 'box_points': [88, 206, 491, 520]}
f6 = {'name': 'person', 'box_points': [86, 205, 496, 520]}

f7 = []
f7.append(f5)
f7.append(f6)

f9 = 1
f8 = {}

f8.setdefault(f9, f7)

print(type(f8))
print(f8)


with open('practice/practice.json', 'w+') as writer:
    writer.write(json.dumps(f8))


with open('practice/practice.json', 'r+') as reader:
    rereader = json.load(reader)
    print(rereader)


with open('practice/practice.txt', 'r+') as f:

    for f1 in f:
        print(f1)