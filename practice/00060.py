data=[1,2,2,4,-3,5,43,43,3,23,12031203120,5,6]
data1=[-1,-2,-3,-4,-5,-6,-7,5,3,3,3,23414134,797,69,69,-6969,-69,69]  

def tee(data):    
    temp=[]
    for i in data:
        if i not in temp:
            temp.append(i)


    return(temp)

yida=tee(data)
print(yida)
yida=tee(data1) 
print(yida)