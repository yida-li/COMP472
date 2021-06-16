from typing import Text
import pandas as pd
import requests
from requests import get
from bs4 import BeautifulSoup
import re
import json
from time import time
from random import randint
from time import sleep
sloth = "\n\n\n"
ultimateDictionary = {}
positivity = True
start_time = time()
requests = 0
with open('training_data_set.txt', 'r') as f2:
    for f3 in f2:

        response = get(
            f3.strip())
        requests += 1
        elapsed_time = time() - start_time
        sleep(randint(1, 2))
        print('Request:{}; Frequency: {} requests/s'.format(requests,
                                                            requests/elapsed_time))
        tomyum = BeautifulSoup(response.content, 'html.parser')
        Text = tomyum.find(class_='text show-more__control').text
        sleep(0.05)

        Rating = tomyum.find(class_='ipl-ratings-bar')
        sleep(0.05)
        ExceptionHandler = Rating
        if ExceptionHandler is None:
            print("Skipping this review, error detected")
            continue
        ultimateExtraction = str(Rating.span.text)
        num_strs = re.findall('[0-9,]+', ultimateExtraction)
        numbers = [int(ns.replace(',', '')) for ns in num_strs]

        if numbers[0] >= 8:
            positive = True
        else:
            positive = False
        result = re.sub(r'[^A-Za-z]', ' ', Text)
        print(sloth, f3, sloth)
        f1 = result.lower().split()

        for i in range(len(f1)):
            tempWord = f1[i]
            if len(tempWord) >= 3:
                if tempWord in ultimateDictionary:
                    if positive == True:
                        # dictionary { key, [#positive, #negative, #total]}     [0] = pos, [1]= neg ,[2]=sum
                        ultimateDictionary[tempWord][0] = ultimateDictionary[tempWord][0]+1
                        ultimateDictionary[tempWord][2] = ultimateDictionary[tempWord][2]+1
                    else:
                        # or else update the dictionary and  [1]++   [2]++
                        ultimateDictionary[tempWord][1] = ultimateDictionary[tempWord][1]+1
                        ultimateDictionary[tempWord][2] = ultimateDictionary[tempWord][2]+1
                else:
                    if positive == True:

                        ultimateDictionary.update({tempWord: [1, 0, 1]})
                    else:
                        ultimateDictionary.update({tempWord: [1, 0, 1]})


with open('lengthfiltering/length-resultMin3Dictionary.json', 'w') as json_file:
    json.dump(ultimateDictionary, json_file)


sloth = "\n\n\n"
ultimateDictionary = {}
positivity = True
start_time = time()
requests = 0
with open('training_data_set.txt', 'r') as f2:
    for f3 in f2:

        response = get(
            f3.strip())
        requests += 1
        elapsed_time = time() - start_time
        sleep(randint(1, 2))
        print('Request:{}; Frequency: {} requests/s'.format(requests,
                                                            requests/elapsed_time))
        tomyum = BeautifulSoup(response.content, 'html.parser')
        Text = tomyum.find(class_='text show-more__control').text
        sleep(0.05)

        Rating = tomyum.find(class_='ipl-ratings-bar')
        sleep(0.05)
        ExceptionHandler = Rating
        if ExceptionHandler is None:
            print("Skipping this review, error detected")
            continue
        ultimateExtraction = str(Rating.span.text)
        num_strs = re.findall('[0-9,]+', ultimateExtraction)
        numbers = [int(ns.replace(',', '')) for ns in num_strs]

        if numbers[0] >= 8:
            positive = True
        else:
            positive = False
        result = re.sub(r'[^A-Za-z]', ' ', Text)
        print(sloth, f3, sloth)
        f1 = result.lower().split()

        for i in range(len(f1)):
            tempWord = f1[i]
            if len(tempWord) >= 5:
                if tempWord in ultimateDictionary:
                    if positive == True:
                        # dictionary { key, [#positive, #negative, #total]}     [0] = pos, [1]= neg ,[2]=sum
                        ultimateDictionary[tempWord][0] = ultimateDictionary[tempWord][0]+1
                        ultimateDictionary[tempWord][2] = ultimateDictionary[tempWord][2]+1
                    else:
                        # or else update the dictionary and  [1]++   [2]++
                        ultimateDictionary[tempWord][1] = ultimateDictionary[tempWord][1]+1
                        ultimateDictionary[tempWord][2] = ultimateDictionary[tempWord][2]+1
                else:
                    if positive == True:

                        ultimateDictionary.update({tempWord: [1, 0, 1]})
                    else:
                        ultimateDictionary.update({tempWord: [1, 0, 1]})


with open('lengthfiltering/length-resultMin5Dictionary.json', 'w') as json_file:
    json.dump(ultimateDictionary, json_file)


sloth = "\n\n\n"
ultimateDictionary = {}
positivity = True
start_time = time()
requests = 0
with open('training_data_set.txt', 'r') as f2:
    for f3 in f2:

        response = get(
            f3.strip())
        requests += 1
        elapsed_time = time() - start_time
        sleep(randint(1, 2))
        print('Request:{}; Frequency: {} requests/s'.format(requests,
                                                            requests/elapsed_time))
        tomyum = BeautifulSoup(response.content, 'html.parser')
        Text = tomyum.find(class_='text show-more__control').text
        sleep(0.05)

        Rating = tomyum.find(class_='ipl-ratings-bar')
        sleep(0.05)
        ExceptionHandler = Rating
        if ExceptionHandler is None:
            print("Skipping this review, error detected")
            continue
        ultimateExtraction = str(Rating.span.text)
        num_strs = re.findall('[0-9,]+', ultimateExtraction)
        numbers = [int(ns.replace(',', '')) for ns in num_strs]

        if numbers[0] >= 8:
            positive = True
        else:
            positive = False
        result = re.sub(r'[^A-Za-z]', ' ', Text)
        print(sloth, f3, sloth)
        f1 = result.lower().split()

        for i in range(len(f1)):
            tempWord = f1[i]
            if len(tempWord) >= 5 and len(tempWord) <= 9:
                if tempWord in ultimateDictionary:
                    if positive == True:
                        # dictionary { key, [#positive, #negative, #total]}     [0] = pos, [1]= neg ,[2]=sum
                        ultimateDictionary[tempWord][0] = ultimateDictionary[tempWord][0]+1
                        ultimateDictionary[tempWord][2] = ultimateDictionary[tempWord][2]+1
                    else:
                        # or else update the dictionary and  [1]++   [2]++
                        ultimateDictionary[tempWord][1] = ultimateDictionary[tempWord][1]+1
                        ultimateDictionary[tempWord][2] = ultimateDictionary[tempWord][2]+1
                else:
                    if positive == True:

                        ultimateDictionary.update({tempWord: [1, 0, 1]})
                    else:
                        ultimateDictionary.update({tempWord: [1, 0, 1]})


with open('lengthfiltering/length-resultMax9Dictionary.json', 'w') as json_file:
    json.dump(ultimateDictionary, json_file)
