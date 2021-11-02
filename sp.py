import random
import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd 
import csv

df = pd.read_csv('StudentsPerformance.csv')
data = df["reading score"].tolist()

mean = statistics.mean(data)
print(mean)

sd = statistics.stdev(data)
print(sd)

median = statistics.median(data)
print(median)

mode = statistics.mode(data)
print(mode)

first_sd_start, first_sd_end = mean - sd, mean + sd
second_sd_start, second_sd_end = mean - (2*sd), mean + (2*sd)
third_sd_start, third_sd_end = mean - (3*sd), mean + (3*sd)

fig = ff.create_distplot([data],["result"],show_hist = False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))

fig.add_trace(go.Scatter(x=[first_sd_start,first_sd_start],y=[0,0.17],mode="lines",name="Standard Deviation 1"))
fig.add_trace(go.Scatter(x=[first_sd_end,first_sd_end],y=[0,0.17],mode="lines",name="Standard Deviation 1"))

fig.add_trace(go.Scatter(x=[second_sd_start,second_sd_start],y=[0,0.17],mode="lines",name="Standard Deviation 2"))
fig.add_trace(go.Scatter(x=[second_sd_end,second_sd_end],y=[0,0.17],mode="lines",name="Standard Deviation 2"))

fig.add_trace(go.Scatter(x=[third_sd_start,third_sd_start],y=[0,0.17],mode="lines",name="Standard Deviation 3"))
fig.add_trace(go.Scatter(x=[third_sd_end,third_sd_end],y=[0,0.17],mode="lines",name="Standard Deviation 3"))

fig.show()

list_first_sd = [result for result in data if result > first_sd_start and result < first_sd_end]
list_second_sd = [result for result in data if result > second_sd_start and result < second_sd_end]
list_third_sd = [result for result in data if result > third_sd_start and result < third_sd_end]

print("Mean of the data is {}".format(mean))
print("Median of the data is {}".format(median))
print("Mode of the data is {}".format(mode))
print("Standard Deviation of the data is {}".format(sd))

print("{}% of data lies in first standard deviation".format(len(list_first_sd)*100.0/len(dice)))
print("{}% of data lies in second standard deviation".format(len(list_second_sd)*100.0/len(dice)))
print("{}% of data lies in third standard deviation".format(len(list_third_sd)*100.0/len(dice)))

print(list_first_sd)
print(list_second_sd)
print(list_third_sd)



