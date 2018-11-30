
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

    #establish the export file
    csvwrite = os.path.join("pypollwrite.txt")

    # read the header and go to the next row
    csv_header = next(csvread)

    #set variables
    totalcandidates = []
    candidatesnames = []
    candyvotes = {}
    winner = 0
    totalvotes = 0
    votespercand = 0
    voteperc = 0

    #read the data and put in a new list, count the total votes
    for eachrow in csvread:

        totalcandidates.append(eachrow)
        totalvotes = totalvotes + 1

    #open the text file to export to
    with open(csvwrite, "w", encoding='utf8') as txtout:
    #create the text
        pypollvotes = (
            f"Election Results\n"
            f"-------------------------------\n"
            f"Total Votes: {totalvotes}\n"
            f"-------------------------------\n")

        #print to screen
        print(pypollvotes)
        #print to file
        txtout.write(pypollvotes)


     #total up the candidates votes each and put in a new list, add percentages

    for eachrow in totalcandidates:
        #set the candidate to the row
        newcandidate = eachrow[2]

        #if the candidate is not in the list
        if newcandidate not in candidatesnames:
            #add the candidate
            candidatesnames.append(newcandidate)
            #and set the votes to zero
            candyvotes[newcandidate] = 0

        #now add a vote to the count for the candidate
        candyvotes[newcandidate] = candyvotes[newcandidate] + 1

    #re-open the text file, append
    with open(csvwrite, "a", encoding='utf8') as newtxt:

        #do the calculations

        for eachrow in candyvotes:

            #get each row in candyvotes and store the value
            votespercand = candyvotes.get(eachrow)

            #calculate the percentages
            voteperc = (float(votespercand) / float(totalvotes) * 100)

            #find the winner. "winner" stores highest number, "windcand" stores the name
            if votespercand > winner:
                winner = votespercand
                wincand = eachrow

            #create field with  each candidate's votes and percentages
            prcand = f"{eachrow}: {voteperc:.3f}% ({votespercand})\n"

            #print to screen
            print(prcand)
            #print to file
            newtxt.write(prcand)

    #reopen the text file for the final printing
    with open(csvwrite, "a", encoding='utf8') as fintxt:

        #set the text
        printfinal = (
            f"-------------------------------\n"
            f"Winner:  {wincand}\n"
            f"-------------------------------\n"
            )
        # print to screen
        print(printfinal)
        # print to file
        fintxt.write(printfinal)
