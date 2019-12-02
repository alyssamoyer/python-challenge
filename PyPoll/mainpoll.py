import os
import csv

csvpath_poll = os.path.join('..', 'election_data.csv')

vote_dict = {}
khan_total = 0
correy_total = 0
li_total = 0
otooley_total = 0

with open(csvpath_poll, newline='') as csvfile_poll:

    csvreaderpoll = csv.reader(csvfile_poll, delimiter=',')
    csv_header_poll= next(csvreaderpoll)

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
    
    total_votes = sum(vote_dict.values())

    khan_percent = round(vote_dict["Khan"]/total_votes,2)
    correy_percent = round(vote_dict["Correy"]/total_votes,2)
    li_percent = round(vote_dict["Li"]/total_votes,2)
    otooley_percent = round(vote_dict["O' Tooley"]/total_votes,2)

    vote_listv = list(vote_dict.values())
    vote_listk = list(vote_dict.keys())
    
    winner = vote_listk[vote_listv.index(max(vote_listv))]
