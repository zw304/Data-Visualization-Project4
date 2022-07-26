# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import altair as alt
import pandas as pd
import sys
print(sys.executable)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
os.getcwd()
os.chdir('/Users/wuzehui/Desktop/ANLY503/hw4-spring-2022-zw304')  # Provide the new path here
data_al = pd.read_csv("data_munging.csv")
data_al.head()

data_al.info() ## check the datatype:
data_al['Date'] = pd.to_datetime(data_al['Date'])

## link for knowledge reference: https://altair-viz.github.io/user_guide/interactions.html

## interactive features:
#interval = alt.selection_interval() ## the code is too slow to run, so try the following ways:

## working and study usage:
line_lamp = alt.Chart(data_al).mark_line(interpolate='basis',color="pink").encode(
    x='Date',
    y=alt.Y('Lamp', title='Power Usage in Lamp (10 Watts)'),
).interactive().properties(
    title='Lamp',
)

line_Laptop = alt.Chart(data_al).mark_line(interpolate='basis',color="orange").encode(
    x='Date',
    y=alt.Y('Laptop', title='Power Usage in Laptop & Printer (10 Watts)'),
).interactive().properties(
    title='Laptop & Printer',
)

line_router = alt.Chart(data_al).mark_line(interpolate='basis',color="red").encode(
    x='Date',
    y=alt.Y('Router', title='Power Usage in Router & Sheeva Plug Computer (10 Watts)'),
).interactive().properties(
    title='Router & Sheeva Plug Computer',
)

## daily usage usage:
line_coffee = alt.Chart(data_al).mark_line(interpolate='basis',color="blue").encode(
    x='Date',
    y=alt.Y('Coffee', title='Power Usage in Coffee (10 Watts)'),
).interactive().properties(
    title='Coffee',
)
line_fridge = alt.Chart(data_al).mark_line(interpolate='basis',color="green").encode(
    x='Date',
    y=alt.Y('Fridge', title='Power Usage in Fridge (10 Watts)'),
).interactive().properties(
    title='Fridge',
)

line_Kettle = alt.Chart(data_al).mark_line(interpolate='basis',color="purple").encode(
    x='Date',
    y=alt.Y('Kettle', title='Power Usage in Kettle (10 Watts)'),
).interactive().properties(
    title='Kettle',
)

## entertainment usage:
line_entertainment = alt.Chart(data_al).mark_line(interpolate='basis',color="yellow").encode(
    x='Date',
    y=alt.Y('Entertainment', title='Power Usage in Entertainment(TV & Stereo) (10 Watts)'),
).interactive().properties(
    title='Entertainment (TV & Stereo)',
)



total = ((line_lamp | line_Laptop | line_router |line_entertainment) & (line_coffee | line_fridge |line_Kettle) )
total_graphs = alt.concat(total).properties(
    title = "Power Usage trend in 8 months for Household 6").configure_title(
    anchor='middle')
## combine and display multiple plots in altair:
total_graphs.save('altair.html')
