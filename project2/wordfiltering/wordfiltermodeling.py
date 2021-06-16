import json
import math
with open('dictionaryReview.json', 'r+') as Observer:
    ultimateDictionary = json.load(Observer)


removedWords = []

totalWordsInPositive = 0
totalWordsInNegative = 0

for key in ultimateDictionary:

    if ultimateDictionary[key][2] >= 2:

        ultimateDictionary[key][0] += 1
        ultimateDictionary[key][1] += 1
        ultimateDictionary[key][2] += 2
        totalWordsInPositive += ultimateDictionary[key][0]
        totalWordsInNegative += ultimateDictionary[key][1]
    else:
        removedWords.append(key)

# model1 for txt format
# model2 for json format
model = ''
model2 = {}


count = 1
for key in ultimateDictionary:
    if ultimateDictionary[key][2] >= 4:
        model += 'No.'+str(count)+' ' + key+'\n'
        model += str(ultimateDictionary[key][0]) + ', ' + \
            str(ultimateDictionary[key][0]/totalWordsInPositive)+', '
        model += str(ultimateDictionary[key][1]) + ', ' + \
            str(ultimateDictionary[key][1]/totalWordsInNegative)+'\n'
        model2.update({key: [ultimateDictionary[key][0], round((ultimateDictionary[key][0]/totalWordsInPositive), 6),
                             ultimateDictionary[key][1], round((ultimateDictionary[key][1]/totalWordsInNegative), 6)]})
        count += 1

with open('wordfiltering/modelMin2.txt', 'w') as f:

    for i in model:
        f.write(i)

# open hash if file needed again
#
with open('wordfiltering/model2Min2.json', 'w') as json_file:
    json.dump(model2, json_file)

removedWords = sorted(removedWords, key=str.lower)
# different way with the same result
textfile = open("wordfiltering/RemovedMin2.txt", "w")
for i in removedWords:
    textfile.write(i + "\n")
textfile.close()


##########################################################################################################


with open('dictionaryReview.json', 'r+') as Observer:
    ultimateDictionary = json.load(Observer)


removedWords = []

totalWordsInPositive = 0
totalWordsInNegative = 0

for key in ultimateDictionary:

    if ultimateDictionary[key][2] > 10:
        ultimateDictionary[key][0] += 1
        ultimateDictionary[key][1] += 1
        ultimateDictionary[key][2] += 2
        totalWordsInPositive += ultimateDictionary[key][0]
        totalWordsInNegative += ultimateDictionary[key][1]
    else:
        removedWords.append(key)

# model1 for txt format
# model2 for json format
model = ''
model2 = {}


count = 1
for key in ultimateDictionary:
    # > 12 because the words are smoothen by 2 to avoid a log10(0)
    if ultimateDictionary[key][2] > 12:
        model += 'No.'+str(count)+' ' + key+'\n'
        model += str(ultimateDictionary[key][0]) + ', ' + \
            str(ultimateDictionary[key][0]/totalWordsInPositive)+', '
        model += str(ultimateDictionary[key][1]) + ', ' + \
            str(ultimateDictionary[key][1]/totalWordsInNegative)+'\n'
        model2.update({key: [ultimateDictionary[key][0], round((ultimateDictionary[key][0]/totalWordsInPositive), 6),
                             ultimateDictionary[key][1], round((ultimateDictionary[key][1]/totalWordsInNegative), 6)]})
        count += 1

with open('wordfiltering/modelMin10.txt', 'w') as f:

    for i in model:
        f.write(i)

# open hash if file needed again
#
with open('wordfiltering/model2Min10.json', 'w') as json_file:
    json.dump(model2, json_file)


removedWords = sorted(removedWords, key=str.lower)
# different way with the same result
textfile = open("wordfiltering/RemovedMin10.txt", "w")
for i in removedWords:
    textfile.write(i + "\n")
textfile.close()


##########################################################################################################


with open('dictionaryReview.json', 'r+') as Observer:
    ultimateDictionary = json.load(Observer)


removedWords = []

totalWordsInPositive = 0
totalWordsInNegative = 0

for key in ultimateDictionary:

    if ultimateDictionary[key][2] > 20:
        ultimateDictionary[key][0] += 1
        ultimateDictionary[key][1] += 1
        ultimateDictionary[key][2] += 2
        totalWordsInPositive += ultimateDictionary[key][0]
        totalWordsInNegative += ultimateDictionary[key][1]
    else:

        removedWords.append(key)

# model1 for txt format
# model2 for json format
model = ''
model2 = {}


count = 1
for key in ultimateDictionary:

    # > 22 because the words are smoothen by 2 to avoid a log10(0)
    if ultimateDictionary[key][2] > 22:
        model += 'No.'+str(count)+' ' + key+'\n'
        model += str(ultimateDictionary[key][0]) + ', ' + \
            str(ultimateDictionary[key][0]/totalWordsInPositive)+', '
        model += str(ultimateDictionary[key][1]) + ', ' + \
            str(ultimateDictionary[key][1]/totalWordsInNegative)+'\n'
        model2.update({key: [ultimateDictionary[key][0], round((ultimateDictionary[key][0]/totalWordsInPositive), 6),
                             ultimateDictionary[key][1], round((ultimateDictionary[key][1]/totalWordsInNegative), 6)]})
        count += 1

with open('wordfiltering/modelMin20.txt', 'w') as f:

    for i in model:
        f.write(i)

# open hash if file needed again
#
with open('wordfiltering/model2Min20.json', 'w') as json_file:
    json.dump(model2, json_file)

removedWords = sorted(removedWords, key=str.lower)
# different way with the same result
textfile = open("wordfiltering/RemovedMin20.txt", "w")
for i in removedWords:
    textfile.write(i + "\n")
textfile.close()


for i in removedWords:
    del ultimateDictionary[i]

# the remaing of the top 5% 10% 20% words will be removed from the same ultimateDictionary and added to the same removedwords.txt


######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
# Perhaps the most important part here because i will reverse the dicitonary values so that the [0] positive frequency
# will switch places with [2] total frequency in order to the the sorting right
######################################################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################


ultimateDictionary5Percent = ultimateDictionary


# exact amount to remove from top to bottom 5% top frequent
number = math.ceil(len(ultimateDictionary5Percent)*0.05)


for i in ultimateDictionary5Percent:

    temp = ultimateDictionary5Percent[i][2]
    ultimateDictionary5Percent[i][0] = ultimateDictionary5Percent[i][2]
    ultimateDictionary5Percent[i][0] = temp

# the x[3] is the sum of all frequency, and will be sorted in desc order

for i in range(number):
    temp = 0

    for key in ultimateDictionary5Percent:
        if ultimateDictionary5Percent[key][0] > temp:
            temp = ultimateDictionary5Percent[key][0]
            inkey = key
    del ultimateDictionary5Percent[inkey]
    removedWords.append(inkey)

model = ''
model2 = {}


totalWordsInPositive = 0
totalWordsInNegative = 0

for key in ultimateDictionary5Percent:
    ultimateDictionary5Percent[key][0] += 1
    ultimateDictionary5Percent[key][1] += 1
    ultimateDictionary5Percent[key][2] += 2
    totalWordsInPositive += ultimateDictionary5Percent[key][0]
    totalWordsInNegative += ultimateDictionary5Percent[key][1]


count = 1
for key in ultimateDictionary5Percent:

    model += 'No.'+str(count)+' ' + key+'\n'
    model += str(ultimateDictionary5Percent[key][0]) + ', ' + \
        str(ultimateDictionary5Percent[key][0]/totalWordsInPositive)+', '
    model += str(ultimateDictionary5Percent[key][1]) + ', ' + \
        str(ultimateDictionary5Percent[key][1]/totalWordsInNegative)+'\n'
    model2.update({key: [ultimateDictionary5Percent[key][0], round((ultimateDictionary5Percent[key][0]/totalWordsInPositive), 6),
                         ultimateDictionary5Percent[key][1], round((ultimateDictionary5Percent[key][1]/totalWordsInNegative), 6)]})
    count += 1


with open('wordfiltering/modelPercent5.txt', 'w') as f:

    for i in model:
        f.write(i)

# open hash if file needed again
#
with open('wordfiltering/model2Percent5.json', 'w') as json_file:
    json.dump(model2, json_file)


removedWords = sorted(removedWords, key=str.lower)
# different way with the same result
textfile = open("wordfiltering/RemovedPercent5.txt", "w")
for i in removedWords:
    textfile.write(i + "\n")
textfile.close()


######################################################################################################################


ultimateDictionary10Percent = ultimateDictionary


# exact amount to remove from top to bottom 10% top frequent
number = math.ceil(len(ultimateDictionary10Percent)*0.10)


for i in ultimateDictionary10Percent:

    temp = ultimateDictionary10Percent[i][2]
    ultimateDictionary10Percent[i][0] = ultimateDictionary10Percent[i][2]
    ultimateDictionary10Percent[i][0] = temp

# the x[3] is the sum of all frequency, and will be sorted in desc order

for i in range(number):
    temp = 0

    for key in ultimateDictionary10Percent:
        if ultimateDictionary10Percent[key][0] > temp:
            temp = ultimateDictionary10Percent[key][0]
            inkey = key
    del ultimateDictionary10Percent[inkey]
    removedWords.append(inkey)

model = ''
model2 = {}


totalWordsInPositive = 0
totalWordsInNegative = 0

for key in ultimateDictionary10Percent:
    ultimateDictionary10Percent[key][0] += 1
    ultimateDictionary10Percent[key][1] += 1
    ultimateDictionary10Percent[key][2] += 2
    totalWordsInPositive += ultimateDictionary10Percent[key][0]
    totalWordsInNegative += ultimateDictionary10Percent[key][1]


count = 1
for key in ultimateDictionary10Percent:

    model += 'No.'+str(count)+' ' + key+'\n'
    model += str(ultimateDictionary10Percent[key][0]) + ', ' + \
        str(ultimateDictionary10Percent[key][0]/totalWordsInPositive)+', '
    model += str(ultimateDictionary10Percent[key][1]) + ', ' + \
        str(ultimateDictionary10Percent[key][1]/totalWordsInNegative)+'\n'
    model2.update({key: [ultimateDictionary10Percent[key][0], round((ultimateDictionary10Percent[key][0]/totalWordsInPositive), 6),
                         ultimateDictionary10Percent[key][1], round((ultimateDictionary10Percent[key][1]/totalWordsInNegative), 6)]})
    count += 1


with open('wordfiltering/modelPercent10.txt', 'w') as f:

    for i in model:
        f.write(i)

# open hash if file needed again
#
with open('wordfiltering/model2Percent10.json', 'w') as json_file:
    json.dump(model2, json_file)


removedWords = sorted(removedWords, key=str.lower)
# different way with the same result
textfile = open("wordfiltering/RemovedPercent10.txt", "w")
for i in removedWords:
    textfile.write(i + "\n")
textfile.close()


######################################################################################################################


ultimateDictionary20Percent = ultimateDictionary


# exact amount to remove from top to bottom 5% top frequent
number = math.ceil(len(ultimateDictionary20Percent)*0.05)


for i in ultimateDictionary20Percent:

    temp = ultimateDictionary20Percent[i][2]
    ultimateDictionary20Percent[i][0] = ultimateDictionary20Percent[i][2]
    ultimateDictionary20Percent[i][0] = temp

# the x[3] is the sum of all frequency, and will be sorted in desc order

for i in range(number):
    temp = 0

    for key in ultimateDictionary20Percent:
        if ultimateDictionary20Percent[key][0] > temp:
            temp = ultimateDictionary20Percent[key][0]
            inkey = key
    del ultimateDictionary20Percent[inkey]
    removedWords.append(inkey)

model = ''
model2 = {}


totalWordsInPositive = 0
totalWordsInNegative = 0

for key in ultimateDictionary20Percent:
    ultimateDictionary20Percent[key][0] += 1
    ultimateDictionary20Percent[key][1] += 1
    ultimateDictionary20Percent[key][2] += 2
    totalWordsInPositive += ultimateDictionary20Percent[key][0]
    totalWordsInNegative += ultimateDictionary20Percent[key][1]


count = 1
for key in ultimateDictionary20Percent:

    model += 'No.'+str(count)+' ' + key+'\n'
    model += str(ultimateDictionary20Percent[key][0]) + ', ' + \
        str(ultimateDictionary20Percent[key][0]/totalWordsInPositive)+', '
    model += str(ultimateDictionary20Percent[key][1]) + ', ' + \
        str(ultimateDictionary20Percent[key][1]/totalWordsInNegative)+'\n'
    model2.update({key: [ultimateDictionary20Percent[key][0], round((ultimateDictionary20Percent[key][0]/totalWordsInPositive), 6),
                         ultimateDictionary20Percent[key][1], round((ultimateDictionary20Percent[key][1]/totalWordsInNegative), 6)]})
    count += 1


ultimateDictionary20Percent = sorted(
    ultimateDictionary20Percent.items(), key=lambda x: x[1], reverse=True)


with open('wordfiltering/modelPercent20.txt', 'w') as f:

    for i in model:
        f.write(i)

with open('wordfiltering/frequency-mode.txt', 'w') as f:

    for i in model:
        f.write(i)

# open hash if file needed again
#
with open('wordfiltering/model2Percent20.json', 'w') as json_file:
    json.dump(model2, json_file)


removedWords = sorted(removedWords, key=str.lower)
# different way with the same result
textfile = open("wordfiltering/RemovedPercent20.txt", "w")
for i in removedWords:
    textfile.write(i + "\n")
textfile.close()

textfile = open("wordfiltering/removed.txt", "w")
for i in removedWords:
    textfile.write(i + "\n")
textfile.close()
