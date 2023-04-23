# Modules
import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

totalMonths = 0
netprofit = 0
monthlyChanges = []
prevmonth = 0
greatestIncrease = ['date', '0']
greatestDecrease = ['date', '0']
monthlyChanges = 0

# Open the CSV
with open(csvpath, encoding='utf') as csvfile:
    budgetData = csv.reader(csvfile, delimiter=",")
    next(budgetData)
    for row in budgetData:
        totalMonths = totalMonths + 1
        netprofit += int(row[1])
        change = int(row[1])-prevmonth
        if change > 0:
            if change > int(greatestIncrease[1]):
                greatestIncrease = [row[0], str(change)]
        if change < 0: 
            if change < int(greatestDecrease[1]):
                greatestDecrease = [row[0], str(change)]
        monthlyChanges += change
        prevmonth = int(row[1])
    print(f"Total Months: {totalMonths}")
    print(f"Total: {netprofit}")
    print(f"Average Change: ${monthlyChanges/(totalMonths-1)}")
    print(f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})")
    print(f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})")

