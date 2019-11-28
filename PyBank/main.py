import os
import csv

csvpath = os.path.join('..', 'budget_data.csv')

budget_dict={}
change_dict = {}
change_list = ()

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header= next(csvreader)
    net_total = 0
    profitloss = 0
    #loops through all rows of csv and adds each to the dictionary. Adds each profit/loss to the net_total
    for row in csvreader:
        #budget_dict.update({row[0]:row[1]})
        net_total += int(row[1])

        # calculates change in proit/loss from previous month to this month
        change = int(row[1]) - int(profitloss)
        change_dict.update({row[0]:change})

        #profitloss tracks the profit/loss of the previous month
        profitloss = row[1]

#calculates number of months in data set based on the length of the dictonary
num_of_months = len(change_dict)

#take out first value of change_dict because not a real change calculation since first value of the series    
change_dict.pop("Jan-10")




change_list = list(change_dict.values())
average_change = sum(change_list)/len(change_list)
print(average_change)



