import pandas
import matplotlib.pyplot as plt
dataset = pandas.read_csv('/home/openbs/power-consumption-prediction/CPall_Dataset_Store/2635.csv', usecols=[1], engine='python')
plt.plot(dataset)
plt.show()
