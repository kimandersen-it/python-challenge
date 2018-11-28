
encoding = "ISO-8859-1"
# importing the operating system
import os

# importing module for reading CSV files
import csv

# show the path
mypath = os.path.join('election_data.csv')

# open file
with open(mypath, 'r' ) as pypollcsv:
    # establish reader and show delimiter
    csvread = csv.reader(pypollcsv, delimiter=',')

    print(csvread)

    # read the header and go to the next row
    csv_header = next(csvread)


    totalvotes = 0
    totalcandidates = []
    candidatesnames = []
    candyvotes = {}
    candidateperc = ["Candidate Name", "Percentage"]
    calcperc = 0
    winner = 0
    votecount = 0
    totalvotes = 0
    votespercand = 0
    voteperc = 0

    #read the data and put in a new list, count the total votes
    for eachrow in csvread:

        totalcandidates.append(eachrow)
        totalvotes = totalvotes + 1

print("Election Results")
print("-------------------------")
print("Total Votes:" + str(totalvotes)
print("-------------------------")

    #total up the candidates votes each and put in a new list
    for eachrow in totalcandidates:
        newcandidate = eachrow[2]

        if newcandidate not in candidatesnames:
            candidatesnames.append(newcandidate)
            candyvotes[newcandidate] = 0

        candyvotes[newcandidate] = candyvotes[newcandidate] + 1


    for eachrow in candyvotes:



        votespercand = candyvotes.get(eachrow)

        voteperc = float(votespercand) / float(totalvotes) * 100

       if (votespercand > winner):
            winner = votespercand

            wincand = eachrow
    print("-------------------------")
    print(wind)
print(candidatesnames)
print(candyvotes)
print (votespercand)
print (wincand)
print (voteperc)