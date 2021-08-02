import csv
import plotly.figure_factory as ff
import statistics
import pandas as pd
import random
import plotly.graph_objects as go
df = pd.read_csv("medium_data.csv")
data = df["math"].tolist()
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means= random_set_of_mean(100)
    mean_list.append(set_of_means)

std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("mean of sampling distribution:- ",mean)
print("Standard deviation of sampling distribution:- ", std_deviation)

math_first_std_deviation_start, id_score_first_std_deviation_end = data-mean_list, data+mean_list
id_score_second_std_deviation_start, id_score_second_std_deviation_end = data-(2*mean_list), data+(2*mean_list)
id_score_third_std_deviation_start, id_score_third_std_deviation_end = data-(3*mean_list), data+(3*mean_list)

print("std1",id_score_first_std_deviation_start,id_score_first_std_deviation_end)
print("std2",id_score_second_std_deviation_start,id_score_second_std_deviation_end)
print("std3",id_score_third_std_deviation_start,id_score_third_std_deviation_end)
std_deviation = statistics.stdev(data)
mean = statistics.mean(data)
print("mean of population distribution:- ",mean)
print("Standard deviation of population distribution:- ", std_deviation)

fig = ff.create_distplot([mean_list],["StudentMarks"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.20],mode = "lines",name = "Mean"))
fig.add_trace(go.Scatter(x = [id_score_first_std_deviation_start,id_score_first_std_deviation_start],y = [0,0.20],mode = "lines",name = "Standard deviation 1 start"))
fig.add_trace(go.Scatter(x = [id_score_first_std_deviation_end,id_score_first_std_deviation_end],y = [0,0.20],mode = "lines",name = "Standard deviation 1 end"))
fig.add_trace(go.Scatter(x = [id_score_second_std_deviation_start,id_score_second_std_deviation_start],y = [0,0.20],mode = "lines",name = "Standard deviation 2 start"))
fig.add_trace(go.Scatter(x = [id_score_second_std_deviation_end,id_score_second_std_deviation_end],y = [0,0.20],mode = "lines",name = "Standard deviation 2 end"))
fig.add_trace(go.Scatter(x = [id_score_third_std_deviation_start,id_score_third_std_deviation_start],y = [0,0.20],mode = "lines",name = "Standard deviation 3 start"))
fig.add_trace(go.Scatter(x = [id_score_third_std_deviation_end,id_score_third_std_deviation_end],y = [0,0.20],mode = "lines",name = "Standard deviation 3 end"))
fig.show()
