import matplotlib.pyplot as plt


x = ['original', 'min3', 'min5', 'max9']
y = [0.631578, 0.605263, 0.615789,
     0.610526]
yy = [1, 2, 3, 4]
plt.barh(x, y, color=['blue', 'red', 'red', 'red'])

for index, value in enumerate(y):
    plt.text(value, index, str(value))
plt.ylabel('types of models')
plt.xlabel('accuracy in % out of 1')
plt.title(' Performance of Lengthening-Filtering Classifiers ')
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.xticks(yy, y)
plt.show()
