import os
import csv

csvpath = os.path.join('..', 'budget_data.csv')

budget_dict={}
change_dict = {}

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

#lists of values and keys
change_listv = list(change_dict.values())
change_listk = list(change_dict.keys())

#finds average change in profit/loss by dividing the sum of the list of change by the length
average_change = round((sum(change_listv)/len(change_listv)),2)

#calculates max and min values of the change list(made of values of the change dictonary)
#then finds the matching month(by index) in the change list(made of keys)
greatest_increase = max(change_listv)
greatest_increase_mon = change_listk[change_listv.index(max(change_listv))]

greatest_decrease = min(change_listv)
greatest_decrease_mon= change_listk[change_listv.index(min(change_listv))]

#print out results
print(
    f"""Total Months: {num_of_months}
Total ${net_total}
Average Change ${average_change}
Greatest Increase in Profits: {greatest_increase_mon} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_mon} (${greatest_decrease})"""
    )

#write results to a text file
results_file = open("results.txt","w") 
results_file.write( f"""Total Months: {num_of_months}
Total ${net_total}
Average Change ${average_change}
Greatest Increase in Profits: {greatest_increase_mon} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_mon} (${greatest_decrease})"""
    )