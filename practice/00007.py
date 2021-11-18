####################################################
# 7. Effortless Dictionary
####################################################
import numpy as np
f1 = {}
f2 = {"samsung": 1, "volantis": 2, "cameron": 3}
f3 = {("fido", "fizz", "telus", "fonus"): [4, 3, 2, 1]}

print(f2)


print('\nlooking up the value for key samsung')
print(f2["samsung"])
print('\nPrint out the keys')
print(list(f2.keys()))
print('\nPrinting out the values')
print(list(f2.values()))
print('\nPrinting the items')
print(list(f2.items()))

print('\nInserting another item( key+ value) with setdefault')
f2.setdefault("exodia", 5)
print(f2)

print('\nUpdating the value of a key')
f2.update({"volantis": 22.2})
print(f2)

print('\nDeleting')
del f2["cameron"]
print(f2)

print('\nSorting')
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
a = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(a)

print("\n\ntesting multi-dimensional array")
f4 = [f1, f2]
print(f4)

print("\n\nadding f3 into f4 array")
f4.append(f3)
print(f4)

with open('your_file.txt', 'w') as f:
    for item in f4:
        f.write("%s\n" % item)

print('\n\n')

f5 = [{'name': 'potted plant', 'percentage_probability': 27.477523684501648, 'box_points': [24, 139, 162, 230]}, {'name': 'potted plant', 'percentage_probability': 30.623388290405273, 'box_points': [66, 122, 127, 242]}], [], [], [], [], [], [], [], [], [{'name': 'person', 'percentage_probability': 23.357592523097992, 'box_points': [191, 247, 250, 302]}], [], [], [], [], [{'name': 'potted plant',
                                                                                                                                                                                                                                                                                                                                                                                       'percentage_probability': 23.02028089761734, 'box_points': [95, 143, 231, 238]}, {'name': 'potted plant', 'percentage_probability': 24.544420838356018, 'box_points': [136, 128, 198, 242]}], [], [], [], [{'name': 'potted plant', 'percentage_probability': 24.137406051158905, 'box_points': [62, 134, 200, 235]}], [{'name': 'person', 'percentage_probability': 26.431801915168762, 'box_points': [155, 242, 215, 300]}]


# for x in f5:
# if(len(x) > 0):
# print(type(x))
# print(len(x))
# print(x)

# for y in x:
# print(type(y))
# print(y["name"], ' detected at ', y["box_points"])  # (x1,y1,x2,y2)


for x in f5:
    if x:  # if the list is not empty at least
        for y in x:
            # print(type(y))
            print(y["name"], ' detected at ', y["box_points"])  # (x1,y1,x2,y2)


f6 = {'name': 'bicycle', 'percentage_probability': 62.77880668640137,
      'box_points': [1277, 746, 1443, 993]}

f6.pop('percentage_probability')
f6.pop('efef',None) #<--------- will not get an eerror
#f6.pop('asdasds') <--------- will get an error due to the fact that it doesnt exist
print(f6)
print(type(f6))
