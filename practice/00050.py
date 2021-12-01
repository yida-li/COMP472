import sys

stdout = sys.stdout

try:
    sys.stdout = open('file.txt', 'w')
    print('blah\nisthisworking?')

finally:
    sys.stdout.close()  # close file.txt
    sys.stdout = stdout
