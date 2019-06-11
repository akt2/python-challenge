import os
import csv

csvpath=os.path.join('budget_data.csv')
# bank=pd.read_csv('budget_data.csv')

with open(csvpath,newline='') as file:
    budget=csv.reader(file,delimiter=',')
    # print(budget)
    header=next(budget)
    # print(f'Header: {header}')
    rows=[]
    date=[]
    prolo=[]
    for row in budget:
        # print(row)
        rows.append(row)
        date.append(row[0])
        prolo.append(row[1])


# The total number of months included in the dataset
# print(type(row))
# print(len(row))
# print(rows)
    # Ok, so now I have a list of lists. So I'll count the length of rows.
monthcount=(len(rows))
    # yay! it's 86.

# The net total amount of "Profit/Losses" over the entire period
#   prolo.sum()
    # woops
#   sum(prolo)
    # didn't like that. ok
# print(type(prolo))
# print(len(prolo))
    # wow, everything i did above was pointless.
# print(type(prolo[0]))
    # ok, it's a list of strings.
prolo=[int(x) for x in prolo]
# print(type(prolo[0]))
    # yay, much better. round two:
prolosum=sum(prolo)

# The average of the changes in "Profit/Losses" over the entire period
shift=[]
for x in range(86):
    ran=prolo[x]-prolo[x-1]
    shift.append(ran)
    
# print(shift)
# print(sum(shift)/len(shift))
    # that didn't work
# print(sum(shift))
    # oh wait i bet it's type related. wait no, it shouldn't be. check anyway.
# print(type(shift[0]))
    # yep, that's not it.
# print(shift[0])
sum(shift)
    # OHH! i'm dumb. I need to make everything absolute.
ashift=[abs(x) for x in shift]
# print(ashift)
    # boom. round two:
boom=sum(ashift)/len(ashift)
change=round(boom,2)
# The greatest increase in profits (date and amount) over the entire period
maxchange=max(shift)

# The greatest decrease in losses (date and amount) over the entire period
minchange=min(shift)

# lovely. all variables are made.

# ugh, i need to grab the dates. Also format the average change.
# oh wait, the average change is supposed to remain a vector. 

# print(shift)   
import pandas as pd
import numpy as np

# i don't understand. why is the average coming out as 0.0?
bank=pd.read_csv('budget_data.csv')
# print(bank)
bank['Shift']=bank['Profit/Losses'].shift(1)
bank['Change']=bank['Profit/Losses']-bank['Shift']
avg=bank['Change'].mean()
# print(avg)
ll=round(avg,2)
# There we go. 

bank['Change']==avg
mxi=shift.index(maxchange)
mni=shift.index(minchange)
mxd=date[mxi]
mnd=date[mni]

print('Financial Analysis\n----------------------------')
print(f'Total Months: {monthcount}\nTotal: ${prolosum}')
print(f'Average Change: ${ll}\nGreatest Increase in Profits: {mxd} (${maxchange})')
print(f'Greatest Decrease in Profits: {mnd} (${minchange})')

txtfile=open('PyBank.txt','w')
txtfile.write('Financial Analysis\n----------------------------')
txtfile.write(f'\nTotal Months: {monthcount}\nTotal: ${prolosum}')
txtfile.write(f'\nAverage Change: ${ll}\nGreatest Increase in Profits: {mxd} (${maxchange})')
txtfile.write(f'\nGreatest Decrease in Profits: {mnd} (${minchange})')
txtfile.close()