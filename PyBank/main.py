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
    print(f"CSV Header: {csv_header}")


    # set total to 0 so header isn't counted, set all other int variables to 0
    totmon = 0
    total = 0
    currell = 0
    prevcell = 0
    greatinc = 0
    greatdec = 0
    diffcell = 0


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

    avenum = (total/totmon)

    #print everything
    print(f'There are ' + 	str(totmon) + ' different months in the csv file.')

    print(f'The total/net of Profit/Loss is ' + str(total))

    print(f'The average change is ' + str(avenum))

    print(f'The month and year with the greatest increase was ' + greatmon + ', and that amount was ' + str(greatinc))

    print(f'The month and year with the greatest decrease was ' + decmon + ', and that amount was ' + str(greatdec))

