
import json

with open('dictionaryReview.json', 'r+') as Observer:
    ultimateDictionary = json.load(Observer)


totalWordsInPositive = 0
totalWordsInNegative = 0

for key in ultimateDictionary:
    ultimateDictionary[key][0] += 1
    ultimateDictionary[key][1] += 1
    ultimateDictionary[key][2] += 2
    totalWordsInPositive += ultimateDictionary[key][0]
    totalWordsInNegative += ultimateDictionary[key][1]


Positive = 75
Negative = 115

ProbablityPositive = 75/(75+115)
ProbablityNegative = 115/(75+115)

# model for txt format
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

with open('smoothfiltering/model.txt', 'w') as f:

    for i in model:
        f.write(i)


with open('smoothfiltering/model2.json', 'w') as json_file:
    json.dump(model2, json_file)

f.close()
json_file.close()


############################################################################
############################################################################

with open('dictionaryReview.json', 'r+') as Observer:
    ultimateDictionary1 = json.load(Observer)


totalWordsInPositive1 = 0
totalWordsInNegative1 = 0

for key in ultimateDictionary1:
    ultimateDictionary1[key][0] += 1.2
    ultimateDictionary1[key][1] += 1.2
    ultimateDictionary1[key][2] += 2.4
    totalWordsInPositive1 += ultimateDictionary1[key][0]
    totalWordsInNegative1 += ultimateDictionary1[key][1]


# model1 for txt format
# model2Point1 for json format
modelPoint1 = ''
model2Point1 = {}


count = 1
for key in ultimateDictionary1:
    modelPoint1 += 'No.'+str(count)+' ' + key+'\n'
    modelPoint1 += str(ultimateDictionary1[key][0]) + ', ' + \
        str(ultimateDictionary1[key][0]/totalWordsInPositive1)+', '
    modelPoint1 += str(ultimateDictionary1[key][1]) + ', ' + \
        str(ultimateDictionary1[key][1]/totalWordsInNegative1)+'\n'
    model2Point1.update({key: [ultimateDictionary1[key][0], round((ultimateDictionary1[key][0]/totalWordsInPositive1), 6),
                               ultimateDictionary1[key][1], round((ultimateDictionary1[key][1]/totalWordsInNegative1), 6)]})
    count += 1

with open('smoothfiltering/modelPoint1.txt', 'w') as f:

    for i in modelPoint1:
        f.write(i)


with open('smoothfiltering/model2Point1.json', 'w') as json_file:
    json.dump(model2Point1, json_file)

f.close()
json_file.close()

############################################################################
############################################################################

with open('dictionaryReview.json', 'r+') as Observer:
    ultimateDictionary2 = json.load(Observer)


totalWordsInPositive2 = 0
totalWordsInNegative2 = 0

for key in ultimateDictionary2:
    ultimateDictionary2[key][0] += 1.4
    ultimateDictionary2[key][1] += 1.4
    ultimateDictionary2[key][2] += 2.8
    totalWordsInPositive2 += ultimateDictionary2[key][0]
    totalWordsInNegative2 += ultimateDictionary2[key][1]


# model1 for txt format
# model2Point2 for json format
modelPoint2 = ''
model2Point2 = {}


count = 1
for key in ultimateDictionary2:
    modelPoint2 += 'No.'+str(count)+' ' + key+'\n'
    modelPoint2 += str(ultimateDictionary2[key][0]) + ', ' + \
        str(ultimateDictionary2[key][0]/totalWordsInPositive2)+', '
    modelPoint2 += str(ultimateDictionary2[key][1]) + ', ' + \
        str(ultimateDictionary2[key][1]/totalWordsInNegative2)+'\n'
    model2Point2.update({key: [ultimateDictionary2[key][0], round((ultimateDictionary2[key][0]/totalWordsInPositive2), 6),
                               ultimateDictionary2[key][1], round((ultimateDictionary2[key][1]/totalWordsInNegative2), 6)]})
    count += 1

with open('smoothfiltering/modelPoint2.txt', 'w') as f:

    for i in modelPoint2:
        f.write(i)


with open('smoothfiltering/model2Point2.json', 'w') as json_file:
    json.dump(model2Point2, json_file)

f.close()
json_file.close()


############################################################################
############################################################################

with open('dictionaryReview.json', 'r+') as Observer:
    ultimateDictionary3 = json.load(Observer)


totalWordsInPositive3 = 0
totalWordsInNegative3 = 0

for key in ultimateDictionary3:
    ultimateDictionary3[key][0] += 1.6
    ultimateDictionary3[key][1] += 1.6
    ultimateDictionary3[key][2] += 3.2
    totalWordsInPositive3 += ultimateDictionary3[key][0]
    totalWordsInNegative3 += ultimateDictionary3[key][1]


# model1 for txt format
# model2Point3 for json format
modelPoint3 = ''
model2Point3 = {}


count = 1
for key in ultimateDictionary3:
    modelPoint3 += 'No.'+str(count)+' ' + key+'\n'
    modelPoint3 += str(ultimateDictionary3[key][0]) + ', ' + \
        str(ultimateDictionary3[key][0]/totalWordsInPositive3)+', '
    modelPoint3 += str(ultimateDictionary3[key][1]) + ', ' + \
        str(ultimateDictionary3[key][1]/totalWordsInNegative3)+'\n'
    model2Point3.update({key: [ultimateDictionary3[key][0], round((ultimateDictionary3[key][0]/totalWordsInPositive3), 6),
                               ultimateDictionary3[key][1], round((ultimateDictionary3[key][1]/totalWordsInNegative3), 6)]})
    count += 1

with open('smoothfiltering/modelPoint3.txt', 'w') as f:

    for i in modelPoint3:
        f.write(i)

with open('smoothfiltering/smooth-model.txt', 'w') as f:

    for i in modelPoint3:
        f.write(i)


with open('smoothfiltering/model2Point3.json', 'w') as json_file:
    json.dump(model2Point3, json_file)

f.close()
json_file.close()


############################################################################
############################################################################


with open('dictionaryReview.json', 'r+') as Observer:
    ultimateDictionary4 = json.load(Observer)


totalWordsInPositive4 = 0
totalWordsInNegative4 = 0

for key in ultimateDictionary4:
    ultimateDictionary4[key][0] += 1.8
    ultimateDictionary4[key][1] += 1.8
    ultimateDictionary4[key][2] += 3.6
    totalWordsInPositive4 += ultimateDictionary4[key][0]
    totalWordsInNegative4 += ultimateDictionary4[key][1]


# model1 for txt format
# model2Point4 for json format
modelPoint4 = ''
model2Point4 = {}


count = 1
for key in ultimateDictionary4:
    modelPoint4 += 'No.'+str(count)+' ' + key+'\n'
    modelPoint4 += str(ultimateDictionary4[key][0]) + ', ' + \
        str(ultimateDictionary4[key][0]/totalWordsInPositive4)+', '
    modelPoint4 += str(ultimateDictionary4[key][1]) + ', ' + \
        str(ultimateDictionary4[key][1]/totalWordsInNegative4)+'\n'
    model2Point4.update({key: [ultimateDictionary4[key][0], round((ultimateDictionary4[key][0]/totalWordsInPositive4), 6),
                               ultimateDictionary4[key][1], round((ultimateDictionary4[key][1]/totalWordsInNegative4), 6)]})
    count += 1

with open('smoothfiltering/modelPoint4.txt', 'w') as f:

    for i in modelPoint4:
        f.write(i)


with open('smoothfiltering/model2Point4.json', 'w') as json_file:
    json.dump(model2Point4, json_file)

f.close()
json_file.close()


with open('dictionaryReview.json', 'r+') as Observer:
    ultimateDictionary5 = json.load(Observer)


totalWordsInPositive5 = 0
totalWordsInNegative5 = 0

for key in ultimateDictionary5:
    ultimateDictionary5[key][0] += 2.0
    ultimateDictionary5[key][1] += 2.0
    ultimateDictionary5[key][2] += 4.0
    totalWordsInPositive5 += ultimateDictionary5[key][0]
    totalWordsInNegative5 += ultimateDictionary5[key][1]


# model1 for txt format
# model2Point5 for json format
modelPoint5 = ''
model2Point5 = {}


count = 1
for key in ultimateDictionary5:
    modelPoint5 += 'No.'+str(count)+' ' + key+'\n'
    modelPoint5 += str(ultimateDictionary5[key][0]) + ', ' + \
        str(ultimateDictionary5[key][0]/totalWordsInPositive5)+', '
    modelPoint5 += str(ultimateDictionary5[key][1]) + ', ' + \
        str(ultimateDictionary5[key][1]/totalWordsInNegative5)+'\n'
    model2Point5.update({key: [ultimateDictionary5[key][0], round((ultimateDictionary5[key][0]/totalWordsInPositive5), 6),
                               ultimateDictionary5[key][1], round((ultimateDictionary5[key][1]/totalWordsInNegative5), 6)]})
    count += 1

with open('smoothfiltering/modelPoint5.txt', 'w') as f:

    for i in modelPoint5:
        f.write(i)


with open('smoothfiltering/model2Point5.json', 'w') as json_file:
    json.dump(model2Point5, json_file)

f.close()
json_file.close()
