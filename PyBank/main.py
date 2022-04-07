import csv
import pandas as pd
import sys
import os

#open the csv file .open()
file=open('C:/Users/anahi/OneDrive/Documents/UCI/LearnPython/Python project/python-challenge/PyBank/Resources/budget_data.csv')
csvfile=csv.reader(file)
df=pd.read_csv('C:/Users/anahi/OneDrive/Documents/UCI/LearnPython/Python project/python-challenge/PyBank/Resources/budget_data.csv')

#defining variables
rows=[]
pl_list=[]
row_count=-1
total_pl = 0
i=1
v1=0
v2=0
average=0
total=0
maximumdec=0
maxinc=0
row=0

#print (df)

#The total number of months included in the dataset
for row in csvfile:
    row_count = row_count +1
rows

total_pl = df['Profit/Losses'].sum()

for i in range(row_count-1):
    change = 0
    v1=df.loc[i+1, "Profit/Losses"]
    v2= df.loc[i, "Profit/Losses"]
    change = change+(v1-v2)
    #print('total change',change)
    total=total + change
    if maximumdec>change: #Greatest Decrease in Profits
        maximumdec=change
        date = df.loc[i+1, "Date"]
    if maxinc<change: #Greatest Increase in Profits:
        maxinc=change
        date2 = df.loc[i+1, "Date"]
#print('total', total)
average = round(total/(row_count-1))

#Print to text
with open('Analysis\Analysis.txt', 'w') as f:
    print('Total Months: ', row_count, file=f)
    print('The net total amount of "Profit/Losses" over the entire period: ', total_pl, file=f)
    print('Average Change:', average, file=f)
    print('Greatest Increase in Profits:',date2, maxinc, file=f)
    print('Greatest Decrease in Profits:',date, maximumdec, file=f)    

#Print result 
print("Financial Analysis")
print("----------------------------")
print('Total Months: ', row_count)
print('The net total amount of "Profit/Losses" over the entire period: ', total_pl)
print('Average Change:', average)
print('Greatest Increase in Profits:',date2, maxinc)
print('Greatest Decrease in Profits:',date, maximumdec)

#Show result on terminal
with open('Analysis\Analysis.txt', 'r') as f:
    print(f.read())