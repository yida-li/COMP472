yida=-2.2

yi=abs(yida)

yid=str(yi)
yid=yid.replace('.','')
temp=[]
counter=0
for i in yid:
    if i not in temp:
        temp.append(i)
        counter+=1
       

if counter<=2:
    print('contains less than 3 unique number')
else:
    print('contains 3 or more unique number')