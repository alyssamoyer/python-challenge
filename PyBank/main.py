import os
import csv

csvpath = os.path.join('..', 'budget_data.csv')

budget_dict={}
changelist = []

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header= next(csvreader)
    net_total = 0
    #loops through all rows of csv and adds each to the dictionary. Adds each profit/loss to the net_total
    for row in csvreader:
        budget_dict.update({row[0]:row[1]})
        net_total += int(row[1])
        # error bc for the first iteration profit loss not defined, set profitloss to zero and then take out the first value of the changelist, possibly create a dict instead of list for greatest increase/decrease
        # dict of row[0]: change value
        change = int(row[1]) - profitloss
        changelist.append(change)
        profitloss = row[1]
        #change.append(row[1].next(row) - row[1])

#calculates number of months in data set based on the length of the dictonary
num_of_months = len(budget_dict)
print(changelist)
 #calculates average profit/loss over full time period
#avg_changes = (net_total/num_of_months)
#print(avg_changes)

#greatest_increase = max(budget_dict, key=budget_dict.get)
#print(greatest_increase)
