import os
import csv

#PyBank
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
    f"""Financial Analysis
    Total Months: {num_of_months}
    Total ${net_total}
    Average Change ${average_change}
    Greatest Increase in Profits: {greatest_increase_mon} (${greatest_increase})
    Greatest Decrease in Profits: {greatest_decrease_mon} (${greatest_decrease})


"""
    )

#write results to a text file
txtpath_bank = os.path.join('..', 'bankresults.txt')
bankresults_file = open(txtpath_bank,"w") 
bankresults_file.write( f"""Financial Analysis
    Total Months: {num_of_months}
    Total ${net_total}
    Average Change ${average_change}
    Greatest Increase in Profits: {greatest_increase_mon} (${greatest_increase})
    Greatest Decrease in Profits: {greatest_decrease_mon} (${greatest_decrease})"""
    )


#PyPoll
csvpath_poll = os.path.join('..', 'election_data.csv')

vote_dict = {}
khan_total = 0
correy_total = 0
li_total = 0
otooley_total = 0

with open(csvpath_poll, newline='') as csvfile_poll:

    csvreaderpoll = csv.reader(csvfile_poll, delimiter=',')
    csv_header_poll= next(csvreaderpoll)

    #loops through the rows to find each candidate name. Adds value to candidate total when found.
    for row in csvreaderpoll:

        if row[2] == "Khan":
             khan_total += 1
        elif row[2] == "Correy":
            correy_total += 1
        elif row[2] == "Li":
            li_total += 1
        elif row[2] == "O'Tooley":
            otooley_total += 1
        
# dictionary of each candidate and the number of votes they received
vote_dict.update({"Khan":khan_total,
    "Correy": correy_total,
     "Li": li_total,
     "O' Tooley": otooley_total,
    })
    
#calculates each candiate's percentage of vote by dividing candidate total by total number of votes
total_votes = sum(vote_dict.values())

khan_percent = round((vote_dict["Khan"]/total_votes)*100)
correy_percent = round((vote_dict["Correy"]/total_votes)*100)
li_percent = round((vote_dict["Li"]/total_votes)*100)
otooley_percent = round((vote_dict["O' Tooley"]/total_votes)*100)

#list of values and keys
vote_listv = list(vote_dict.values())
vote_listk = list(vote_dict.keys())
    
#uses index of the max of the list of values to find the winner name in the list of keys
winner = vote_listk[vote_listv.index(max(vote_listv))]

#print out results
print(
    f"""Election Results
    Total Votes: {total_votes}
    Khan: {khan_percent}% ({khan_total})
    Correy: {correy_percent}% ({correy_total})
    Li: {li_percent}% ({li_total})
    O'Tooley: {otooley_percent}% ({otooley_total})
    Winner: {winner}"""
    )
#write results to a text file
txtpath_poll = os.path.join('..', 'pollresults.txt')
pollresults_file = open(txtpath_poll,"w") 
pollresults_file.write( f"""Election Results
    Total Votes: {total_votes}
    Khan: {khan_percent}% ({khan_total})
    Correy: {correy_percent}% ({correy_total})
    Li: {li_percent}% ({li_total})
    O'Tooley: {otooley_percent}% ({otooley_total})
    Winner: {winner}"""
    )