#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test code for AIND project 2
"""

##################################
### python simple test
##################################

# 1. append text to text file
# append text to end of text file
#with open('test.txt', 'a') as f:
#    f.write('aaa\n')
# works

# 2. get object properties
#a = [1, 2, 3]
#dir(a)
# works

#from layers import ActionNode
#dir(ActionNode)
# works

# 3. .op[3:]
#aaa = ['a','b','c','d','e','f']
#aaa.op[3:]
#dont work

# 4. get properties of Expr
#from aimacode.utils import expr
#dir(expr)
# works

# 5. test a set in another set
#setA = {1}
#setB = {1, 2}
#print (setA.issubset(setB)) #True
#print (setB.issuperset(setA)) #True
# works

# 6. get max value in a list
#numbers = [2,5,1,9,6]
#print (str(max(numbers))) # 9
# works

# 7. get last item
#numbers = [1,2,3,4,5]
#print (numbers[-1])
# works

# 8. loop list with index
#data = ['a', 'b', 'c']
#for i, d in enumerate(data):
#    print (i, d)
# works

# 9. log high skewed values
import pandas as pd
import numpy as np

data = [[0,1,2,3,4,5,6,7,8,9], [10**0,10**1,10**2,10**3,10**4,10**5,10**6,10**7,10**8,10**9]]
data = np.array(data)
print (data)

# rows -> columns
data = np.transpose(data)
print (data)

# log data
data = np.log(data)
print (data)

# dataflame ti use plot()
df = pd.DataFrame(data)
df.columns = ['index', 'values']

#set index
df.set_index('index', inplace=True)

df.plot()

# 10. multi bar bar charts
# example online

import numpy as np
import matplotlib.pyplot as plt
 
# data to plot
n_groups = 4
means_frank = (90, 55, 40, 65)
means_guido = (85, 62, 54, 20)
 
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
 
rects1 = plt.bar(index, means_frank, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Frank')
 
rects2 = plt.bar(index + bar_width, means_guido, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Guido')
 
plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')
plt.xticks(index + bar_width, ('A', 'B', 'C', 'D'))
plt.legend()
 
plt.tight_layout()
plt.show()


########################
# seaborn try - dont work
import seaborn as sns
sns.set(style='whitegrid')

g = sns.factorplot(x='Actions', y='Expansions', data=x1, size=1, kind='bar', palette='muted')
g.despine(left=True)
g.set_ylabels('number')


########################
# dataframe simple pie chart - works

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pie_data = [1, 2, 3]
df = pd.DataFrame(pie_data)
df.columns = ['Numbers']
df.plot(kind='pie', subplots=True)


#####################################
# multi bars bar chart on result data

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# graph functions, shared between each report requirements
def custom_log_data(data, col1_max, col2_max):
    # e.g. 
    # convert expansion values to 0 -> max actions, so top action and top expansion values are the same
    # data = data / max_expansions * max_actions

    data = data / col2_max * col1_max
    return data

def plot_multi_barchart(data, columns, title, xlabel, ylabel, xticks_labels, y_highest_value):
    
    # set figure width and height
    fig = plt.figure(figsize=(8,5))
    
    # graph can have more than one subplot, but we only have one this time
    ax = fig.add_subplot(111)
    
    # index of each algo
    number_of_search_algo = len(data)
    n = number_of_search_algo
    index = np.arange(n)
    
    # graph visual settings
    bar_width = 0.3
    opacity = 0.9
    
    # add a set of bars 
    for i, col in enumerate(columns):
        bars = plt.bar(left=index+bar_width*i, 
                       height=data[col], 
                       width=bar_width, 
                       label=col, 
                       align='center', 
                       alpha=opacity) 
    
    # grid lines
    ax.set_axisbelow(True)
    ax.grid() 
    
    # stretch graph
#    ax.axes([0,2,1,1])

    #y axis limit min max        
    plt.ylim((0, y_highest_value+20))
#    plt.ylim((0, 200))

    # labels
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(index + bar_width/2, xticks_labels, rotation='vertical')
    plt.legend()

    # layout all compacted and not cropped    
    plt.tight_layout()

    # render    
    plt.show()

def plot_multi_barchart_twobar(data, columns, title, xlabel, ylabel):
    
    # set figure width and height
    fig = plt.figure(figsize=(8,5))
        
    ax1 = None
    ax2 = None
        
    # graph visual settings
    bar_width = 0.3
    opacity = 0.9
    
    colors = ['orange', 'lightblue', 'lightgreen', 'lightpurple']
    
    # add a set of bars - max 2 bars for now, not tested with three bars
    for i, col in enumerate(columns):

        # 1st bar
        if i == 0:
            ax1 = fig.add_subplot(111)
            
            data[col].plot(kind='bar', color=colors[i], ax=ax1, width=bar_width, position=(2-i), label=col, alpha=opacity)

            ax1.set_ylabel(col)
            ax1.legend(loc=2)

            # grid lines
            ax1.set_axisbelow(True)
            ax1.grid()     

        # 2nd bar
        else:
            ax2 = ax1.twinx() # add another axis share the same x-axis

            data[col].plot(kind='bar', color=colors[i], ax=ax2, width=bar_width, position=(2-i), label=col, alpha=opacity)

            ax2.set_ylabel(col)
            ax2.legend(loc=1) 

            # grid lines
            # ax1.set_axisbelow(True)
            # ax1.grid() 

    
    # labels
    plt.xlabel(xlabel)
#    plt.ylabel(ylabel)
    plt.title(title)

    # layout all compacted and not cropped    
    plt.tight_layout()

    # render    
    plt.show()
    
def handle_data(df):
    number_of_search_algo = 11
    n = number_of_search_algo
    
    # air cargo problem 1
    acp1 = df[:n]
    # air cargo problem 2
    acp2 = df[n:n*2]
    # air cargo problem 3
    acp3 = df[n*2:n*3]
    # air cargo problem 4
    acp4 = df[n*3:n*4]

    # join all 4 problems data as a list, loop to plot each
    data = [acp1, acp2, acp3, acp4]
    
    return data

# for each air cargo problem, plot a multi barchart of the search algorithms
def report_barchart_1_v1():
    # data
    df = pd.read_csv('./report/run_search_result_data1_actionsexpansions.csv')

    max_actions = max(df['Actions'])
    # 104
    max_expansions = max(df['Expansions'])
    # 113339

    # log value of time
    df['Expansions'] = custom_log_data(df['Expansions'], max_actions, max_expansions)

    # split data from dataframe into each 4 air cargo problems, convert into a list
    data_4_problems = handle_data(df)

    for i, d in enumerate(data_4_problems):
        plot_multi_barchart(data=d, 
                            columns=['Actions', 'Expansions'], 
                            title='Air Cargo Problem '+str(i+1), 
                            xlabel='Search Algorithms', 
                            ylabel='Values',
                            xticks_labels=d['search algorithm'],
                            y_highest_value=max_actions)
        
def report_barchart_1():
    # data
    df = pd.read_csv('./report/run_search_result_data1_actionsexpansions.csv')

    max_actions = max(df['Actions'])
    # 104
    max_expansions = max(df['Expansions'])
    # 113339

    # split data from dataframe into each 4 air cargo problems, convert into a list
    data_4_problems = handle_data(df)

    for i, d in enumerate(data_4_problems):
        
        d.set_index('search algorithm', inplace=True)
        plot_multi_barchart_twobar(data=d, 
                            columns=['Actions', 'Expansions'], 
                            title='Air Cargo Problem '+str(i+1), 
                            xlabel='Search Algorithms', 
                            ylabel='Values')

def report_barchart_2_v1():
    # data
    df = pd.read_csv('./report/run_search_result_data2_actionstime.csv')

    # could remove last 2 row as time value is too big, will skew data, also not needed in project requirements
    # df = df[:-2]
        
    max_actions = max(df['Actions'])
    max_time = max(df['Time'])
    highest_value = max_actions

    # log value of time
    df['Time'] = custom_log_data(df['Time'], max_actions, max_time)

    # split data from dataframe into each 4 air cargo problems, convert into a list
    data_4_problems = handle_data(df)

    for i, d in enumerate(data_4_problems):
        
        plot_multi_barchart(data=d, 
                            columns=['Actions', 'Time'], 
                            title='Air Cargo Problem '+str(i+1), 
                            xlabel='Search Algorithms', 
                            ylabel='Values',
                            xticks_labels=d['search algorithm'],
                            y_highest_value=highest_value)
        
def report_barchart_2():
    # data
    df = pd.read_csv('./report/run_search_result_data2_actionstime.csv')

    # could remove last 2 row as time value is too big, will skew data, also not needed in project requirements
    # df = df[:-2]
        
    # split data from dataframe into each 4 air cargo problems, convert into a list
    data_4_problems = handle_data(df)

    for i, d in enumerate(data_4_problems):
        d.set_index('search algorithm', inplace=True)
        plot_multi_barchart_twobar(data=d, 
                            columns=['Actions', 'Time'], 
                            title='Air Cargo Problem '+str(i+1), 
                            xlabel='Search Algorithms', 
                            ylabel='Values')

def report_barchart_3_v1():
    # data
    df = pd.read_csv('./report/run_search_result_data3_planlength.csv')
            
    max_plan_length = max(df['Plan Length'])
    # 24132
    highest_value = 100

    # log value of time
    df['Plan Length'] = custom_log_data(df['Plan Length'], highest_value, max_plan_length)

    # split data from dataframe into each 4 air cargo problems, convert into a list
    data_4_problems = handle_data(df)

    for i, d in enumerate(data_4_problems):
        
        plot_multi_barchart(data=d, 
                            columns=['Plan Length'], 
                            title='Air Cargo Problem '+str(i+1), 
                            xlabel='Search Algorithms', 
                            ylabel='Values',
                            xticks_labels=d['search algorithm'],
                            y_highest_value=highest_value)
        
def report_barchart_3():
    # data
    df = pd.read_csv('./report/run_search_result_data3_planlength.csv')
            
    # split data from dataframe into each 4 air cargo problems, convert into a list
    data_4_problems = handle_data(df)

    for i, d in enumerate(data_4_problems):
        d.set_index('search algorithm', inplace=True)
        plot_multi_barchart_twobar(data=d, 
                            columns=['Plan Length'], 
                            title='Air Cargo Problem '+str(i+1), 
                            xlabel='Search Algorithms', 
                            ylabel='Values')

#report_barchart_1()
#report_barchart_2()
#report_barchart_3()

report_barchart_1() # uses two axis barchart
report_barchart_2() # uses two axis barchart
report_barchart_3() # uses two axis barchart



######################
# results in table, render as html in jupyter
from IPython.display import display, HTML

def report_table(df):
    data_4_problems = handle_data(df)

    for i, d in enumerate(data_4_problems):
        display(HTML('<hr />'))
        display(HTML('Air Cargo Problem '+str(i+1)))
        display(d)

def report_table_1():
    df = pd.read_csv('./report/run_search_result_data1_actionsexpansions.csv')
    report_table(df)
    
def report_table_2():
    df = pd.read_csv('./report/run_search_result_data2_actionstime.csv')
    report_table(df)

def report_table_3():
    df = pd.read_csv('./report/run_search_result_data3_planlength.csv')
    report_table(df)

report_table_1()
report_table_2()
report_table_3()

##########################
# pie chart example online

import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()




##########################
# pie chart on result data

def report_pie_1():
    # data
    df = pd.read_csv('./report/run_search_result_data1_actionsexpansions.csv')

#    max_actions = max(df['Actions'])
    # 104
#    max_expansions = max(df['Expansions'])
    # 113339

    # log value of time
#    df['Expansions'] = custom_log_data(df['Expansions'], max_actions, max_expansions)

    # split data from dataframe into each 4 air cargo problems, convert into a list
    data_4_problems = handle_data(df)

    for i, d in enumerate(data_4_problems):
#        plot_pie_chart(data=d, 
#                            columns=['Actions', 'Expansions'], 
#                            title='Air Cargo Problem '+str(i+1), 
#                            xlabel='Search Algorithms', 
#                            ylabel='Values',
#                            xticks_labels=d['search algorithm'],
#                            y_highest_value=max_actions)
        labels = d['search algorithm']
        data = d
        
        fig, ax = plt.subplots()
        
#        ax.pie()
        d.set_index('search algorithm', inplace=True)
        d['Expansions'].plot.pie(subplots=True, autopct='%.2f%%', title='Air Cargo Problem '+str(i)+' - Expansions', shadow=True, figsize=(3,3))

report_pie_1()

def report_pie_2():
    # data
    df = pd.read_csv('./report/run_search_result_data1_actionsexpansions.csv')

#    max_actions = max(df['Actions'])
    # 104
#    max_expansions = max(df['Expansions'])
    # 113339

    # log value of time
#    df['Expansions'] = custom_log_data(df['Expansions'], max_actions, max_expansions)

    # split data from dataframe into each 4 air cargo problems, convert into a list
    data_4_problems = handle_data(df)

    for i, d in enumerate(data_4_problems):
#        plot_pie_chart(data=d, 
#                            columns=['Actions', 'Expansions'], 
#                            title='Air Cargo Problem '+str(i+1), 
#                            xlabel='Search Algorithms', 
#                            ylabel='Values',
#                            xticks_labels=d['search algorithm'],
#                            y_highest_value=max_actions)
        labels = d['search algorithm']
        data = d
        
        fig, ax = plt.subplots()
        
#        ax.pie()
        d.set_index('search algorithm', inplace=True)
        d['Expansions'].plot.pie(subplots=True, autopct='%.2f%%', title='Air Cargo Problem '+str(i)+' - Expansions', shadow=True, figsize=(3,3))

report_pie_1()

#########################
# bar chart with two axis - test on data

def report_barchart_two_axis_2():
    # data
    df = pd.read_csv('./report/run_search_result_data1_actionsexpansions.csv')
    df.set_index('search algorithm', inplace=True)

    # air cargo problem 1
    data = df[:11]

    # plot
    fig = plt.figure()

    ax1 = fig.add_subplot(111)
    ax2 = ax1.twinx() # add another axis share the same x-axis

    ax1.set_axisbelow(True)
    ax2.set_axisbelow(True)
#    ax1.grid() 
#    ax2.grid() 

    data['Actions'].plot(kind='bar', color='red', ax=ax1, width=0.3, position=2, label='Action')
    data['Expansions'].plot(kind='bar', color='blue', ax=ax2, width=0.3, position=1, label='Expansions')

    ax1.set_ylabel('Actions')
    ax2.set_ylabel('Expansions')

    ax1.legend(loc=1)
    ax2.legend(loc=2)    

    plt.tight_layout()
    plt.show()

report_barchart_two_axis_2()








