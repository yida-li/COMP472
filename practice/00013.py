####################################################
# 13. : File Read/Write
####################################################
import json

f1 = ('A', 'B', 'C')

print("\nWriting a tuple into file and reading it\n")
with open('practice/practice.txt', 'w') as f:

    for f1 in f1:
        f.write(f1)


with open('practice/practice.txt', 'r') as f2:
    for f3 in f2:
        print(f3)


print("\nWriting a dictionary(json) into file and reading it\n")
# also the stuff written earlier is overwritten magically inexplicably mysteriously

f4 = {"dictionary": 1, "bible": 2, "Bescherelle": 3}

with open('practice/practice.txt', 'w+') as f5:
    f5.write(json.dumps(f4))


with open('practice/practice.txt', 'r+') as f6:
    f7 = json.load(f6)
    print(f7)
