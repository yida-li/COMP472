####################################################
# 11. Typical Exception
####################################################

try:
    with open('file_does_not_exist.txt') as f:
        print("Opened the file")
except:
    print("Exception caught!File not found")


print("\nNow opening practice.txt\n")

try:
    with open('practice/practice.txt') as f:
        print("Opened the file")
except:
    print("Exception caught!")
