
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.transform import Rotation as Rot
import time


plt.cla()
# for stopping simulation with the esc key.
plt.gcf().canvas.mpl_connect('key_release_event',
        lambda event: [exit(0) if event.key == 'escape' else None])


with open('./project7/GPRMC.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            #print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            print(f'\tlatitude : {row[2]}  longitude:{row[4]}')
            line_count += 1
    print(f'Processed {line_count} lines.')

# plotting lattitude/longitude ratio graph
x=[1,2,3,4,5,6]
y=[1,2,3,4,5,6]

for i in range(701):


    plt.plot(x[i], y[i], ".g")
    time.sleep(2) # increment every 2 second
    plt.grid(True)
    plt.pause(0.1)



   