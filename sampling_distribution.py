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

def random_set_of_mean(count):
        data_set = []
        for i in range(0,count):
                random_index = random.randint(0,len(data) - 1)
                value = data[random_index]
                data_set.append(value)
        mean = statistics.mean(data_set)
        return mean

def showFig(mean_list):
        df = mean_list
        fig = ff.create_distplot([df],['Temp'],show_hist = False)
        fig.show()

def setup():
        mean_list = []
        for o in range(0,1000):
                set_of_means = random_set_of_mean(300)
                mean_list.append(set_of_means)
        showFig(mean_list)
        std_deviation = statistics.stdev(mean_list)
        print('Standard deviation of the mean: ',std_deviation)
setup()