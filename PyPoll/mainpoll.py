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

        if row[3] == "Khan":
             khan_total += 1
        elif row[3] == "Correy":
            correy_total += 1
        elif row[3] == "Li":
            li_total += 1
        elif row[3] == "O'Tooley":
            otooley_total += 1

    vote_dict.update({"Khan":khan_total,
     "Correy": correy_total,
     "Li": li_total,
     "O' Tooley": otooley_total})

     