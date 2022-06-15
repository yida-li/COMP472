vowel='hello, secret meeting tonight'
v=vowel
print('the number of strings is',len(vowel))
temp=''
counter=0
predecessor=''
for i in vowel:
    #print(i)
    if i=='e' and predecessor != 'e' and predecessor != 'a'\
        and predecessor != 'i' and predecessor != 'o' and predecessor != 'u':
    #if i=='e'or i=='o'or i=='i' or i=='u' or i=='a':
        #print(vowel[counter-1])
        vowel=vowel[:counter]+"YL"+vowel[counter:]
        counter=counter+3
    elif i=='a'and predecessor != 'e' and predecessor != 'a'\
        and predecessor != 'i' and predecessor != 'o' and predecessor != 'u':
        vowel=vowel[:counter]+"YL"+vowel[counter:]
        counter=counter+3
    elif i=='i'and predecessor != 'e' and predecessor != 'a'\
        and predecessor != 'i' and predecessor != 'o' and predecessor != 'u':
        vowel=vowel[:counter]+"YL"+vowel[counter:]
        counter=counter+3            
    elif i=='o'and predecessor != 'e' and predecessor != 'a'\
        and predecessor != 'i' and predecessor != 'o' and predecessor != 'u':
        vowel=vowel[:counter]+"YL"+vowel[counter:]
        counter=counter+3
    elif i=='u'and predecessor != 'e' and predecessor != 'a'\
        and predecessor != 'i' and predecessor != 'o' and predecessor != 'u':
        vowel=vowel[:counter]+"YL"+vowel[counter:]
        counter=counter+3  
    else:
        counter=counter+1
    predecessor=i
    
#print(vowel[counter-1])
#print(stringtemp)
print(v)
print(vowel)
#print(counter)