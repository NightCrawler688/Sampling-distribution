import plotly.figure_factory as ff 
import statistics
import csv
import pandas as pd
import plotly.graph_objects as go
import random

df = pd.read_csv('data1.csv')
data = df['temp'].tolist()
population_mean = statistics.mean(data)
population_std_deviation = statistics.stdev(data)
fig = ff.create_distplot([data],['Temp'],show_hist = False)
fig.show()
print('Population mean: ',population_mean) 
print('Population Standard deviation: ',population_std_deviation)
data_set = []
for i in range(0,100):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        data_set.append(value)
mean = statistics.mean(data_set)
std_deviation = statistics.stdev(data_set)
print('Mean of sample: ',mean)
print('Standard deviation of sample: ',std_deviation)

