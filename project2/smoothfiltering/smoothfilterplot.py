import matplotlib.pyplot as plt


x = ['δ=1', 'δ=1.2', 'δ=1.4', 'δ=1.6', 'δ=1.8', 'δ=2']


y = [0.631578, 0.631578, 0.636842,
     0.636842, 0.631578, 0.636842]


plt.barh(x, y, color=['red', 'red', 'blue', 'blue', 'red', 'blue'])

for index, value in enumerate(y):
    plt.text(value, index, str(value))
plt.ylabel('types of models')
plt.xlabel('accuracy in % out of 1')
plt.title(' Performance of Smooth-Filtering Classifiers ')

plt.show()
