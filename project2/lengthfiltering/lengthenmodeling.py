import json

nn = '\n'


with open('lengthfiltering/length-resultMin3Dictionary.json', 'r+') as Observer:
    ultimateDictionary = json.load(Observer)


totalWordsInPositive = 0
totalWordsInNegative = 0

for key in ultimateDictionary:
    ultimateDictionary[key][0] += 1
    ultimateDictionary[key][1] += 1
    ultimateDictionary[key][2] += 2
    totalWordsInPositive += ultimateDictionary[key][0]
    totalWordsInNegative += ultimateDictionary[key][1]


print(nn, 'total pos after lengthening procedure', totalWordsInPositive)
print(nn, 'total neg after lengthening procedure', totalWordsInNegative)


# model1 for txt format
# model2 for json format
model = ''
model2 = {}


count = 1
for key in ultimateDictionary:
    model += 'No.'+str(count)+' ' + key+'\n'
    model += str(ultimateDictionary[key][0]) + ', ' + \
        str(ultimateDictionary[key][0]/totalWordsInPositive)+', '
    model += str(ultimateDictionary[key][1]) + ', ' + \
        str(ultimateDictionary[key][1]/totalWordsInNegative)+'\n'
    model2.update({key: [ultimateDictionary[key][0], round((ultimateDictionary[key][0]/totalWordsInPositive), 6),
                  ultimateDictionary[key][1], round((ultimateDictionary[key][1]/totalWordsInNegative), 6)]})
    count += 1

with open('lengthfiltering/length3Min-model.txt', 'w') as f:

    for i in model:
        f.write(i)

# open hash if file needed again
#
with open('lengthfiltering/length3Min-model2.json', 'w') as json_file:
    json.dump(model2, json_file)


f.close()
Observer.close()


###################################################################################


with open('lengthfiltering/length-resultMin5Dictionary.json', 'r+') as Observer:
    ultimateDictionary = json.load(Observer)


totalWordsInPositive = 0
totalWordsInNegative = 0

for key in ultimateDictionary:
    ultimateDictionary[key][0] += 1
    ultimateDictionary[key][1] += 1
    ultimateDictionary[key][2] += 2
    totalWordsInPositive += ultimateDictionary[key][0]
    totalWordsInNegative += ultimateDictionary[key][1]


print(nn, 'total pos after lengthening procedure', totalWordsInPositive)
print(nn, 'total neg after lengthening procedure', totalWordsInNegative)


# model1 for txt format
# model2 for json format
model = ''
model2 = {}


count = 1
for key in ultimateDictionary:
    model += 'No.'+str(count)+' ' + key+'\n'
    model += str(ultimateDictionary[key][0]) + ', ' + \
        str(ultimateDictionary[key][0]/totalWordsInPositive)+', '
    model += str(ultimateDictionary[key][1]) + ', ' + \
        str(ultimateDictionary[key][1]/totalWordsInNegative)+'\n'
    model2.update({key: [ultimateDictionary[key][0], round((ultimateDictionary[key][0]/totalWordsInPositive), 6),
                  ultimateDictionary[key][1], round((ultimateDictionary[key][1]/totalWordsInNegative), 6)]})
    count += 1

with open('lengthfiltering/length5Min-model.txt', 'w') as f:

    for i in model:
        f.write(i)

# open hash if file needed again
#
with open('lengthfiltering/length5Min-model2.json', 'w') as json_file:
    json.dump(model2, json_file)


f.close()
Observer.close()


###################################################################################


with open('lengthfiltering/length-resultMax9Dictionary.json', 'r+') as Observer:
    ultimateDictionary = json.load(Observer)


totalWordsInPositive = 0
totalWordsInNegative = 0

for key in ultimateDictionary:
    ultimateDictionary[key][0] += 1
    ultimateDictionary[key][1] += 1
    ultimateDictionary[key][2] += 2
    totalWordsInPositive += ultimateDictionary[key][0]
    totalWordsInNegative += ultimateDictionary[key][1]


print(nn, 'total pos after lengthening procedure', totalWordsInPositive)
print(nn, 'total neg after lengthening procedure', totalWordsInNegative)


# model1 for txt format
# model2 for json format
model = ''
model2 = {}


count = 1
for key in ultimateDictionary:
    model += 'No.'+str(count)+' ' + key+'\n'
    model += str(ultimateDictionary[key][0]) + ', ' + \
        str(ultimateDictionary[key][0]/totalWordsInPositive)+', '
    model += str(ultimateDictionary[key][1]) + ', ' + \
        str(ultimateDictionary[key][1]/totalWordsInNegative)+'\n'
    model2.update({key: [ultimateDictionary[key][0], round((ultimateDictionary[key][0]/totalWordsInPositive), 6),
                  ultimateDictionary[key][1], round((ultimateDictionary[key][1]/totalWordsInNegative), 6)]})
    count += 1

with open('lengthfiltering/length9Max-model.txt', 'w') as f:

    for i in model:
        f.write(i)

with open('lengthfiltering/length-model.txt', 'w') as f:

    for i in model:
        f.write(i)


# open hash if file needed again
#
with open('lengthfiltering/length9Max-model2.json', 'w') as json_file:
    json.dump(model2, json_file)


f.close()
Observer.close()
