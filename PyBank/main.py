#importing the operating system
import os

# importing module for reading CSV files
import csv

#show the path
mypath = os.path.join('budget_data.csv')

#open file
with open(mypath, 'r' ) as budgetcsv:

    # establish reader and show delimiter
    csvread = csv.reader(budgetcsv, delimiter=',')

    print(csvread)


    # read the header
    csv_header = next(csvread)

    # set total to 0 so header isn't counted, set all other int variables to 0
    totmon = 0
    total = 0
    currell = 0
    prevcell = 0
    greatinc = 0
    greatdec = 0
    diffcell = 0
    avesum = 0
    avenum = 0.0


    #begin the calculations
    for eachrow in csvread:
        # total months (rows)
        totmon += 1

        # total of second column
        total = (int(eachrow[1]) + total)

        #increase and decrease

        #sets the previous cell value to the current cell only the first time
        if prevcell == 0:
            prevcell = (int(eachrow[1]))
        else:
         #if not the first time, sets it to the current cell BEFORE the current cell is assigned
            prevcell = currcell

        #now assign the current cell
        currcell = (int(eachrow[1]))

        #look at the difference
        diffcell = (currcell - prevcell)

        #total up the differences for the average
        avesum = (avesum + diffcell)

        #if the greatest increase so far is less than the difference
        if greatinc < diffcell:
            #set the greatest increase to the current difference
           greatinc = diffcell
            #and grab the first column of the cell for month/year
           greatmon = (eachrow[0])


        #if the greatest decrease so far is more than the difference
        if greatdec > diffcell:
            #set the greatest decrease to the current difference
           greatdec = diffcell
            # and grab the first column of the cell for month/year
           decmon = (eachrow[0])

    #figure out the average of the changes
    avenum = (avesum / (totmon - 1))

    #format and print everything

    printall = (
        f"Financial Analysis\n"
        f"-----------------------------\n"
        f"Total Months: {totmon}\n"
        f"Total : ${total}\n"   
        f"Average Change: ${avenum:.2f}\n"   
        f"Greatest Increase in Profits: {greatmon} (${greatinc})\n"
        f"Greatest Decrease in Profits: {decmon} (${greatdec})\n"
         )
    print(printall)


