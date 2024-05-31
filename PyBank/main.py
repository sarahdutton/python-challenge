# python-challenge
import os
import csv

# declare file location
csvpath = os.path.join('python-challenge', 'PyBank', 'Resources', 'budget_data.csv')

# create the lists needed
total_months = []
total_profit = []
profit_change = []

# read csv
with open(csvpath,newline="", encoding="utf-8") as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader)
    
    print(csvreader)
    
    for row in csvreader:
        
# total number of months
        total_months.append(row[0])

# net total amount of profits and losses 
        total_profit.append(int(row[1]))

# changes in profits and losses and average of those changes
    for i in range(len(total_profit)-1):
        profit_change.append(total_profit[i+1] - total_profit[i])

# greatest increase in profits (date and amount) 
max_increase_amount = max(profit_change)

max_increase_date = profit_change.index(max(profit_change)) + 1

# greatest decrease in profits (date and amount) 
max_decrease_amount = min(profit_change)

max_decrease_date = profit_change.index(min(profit_change)) + 1

# print all

print("Financial Analysis")
print("------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_date]} (${(str(max_increase_amount))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_date]} (${(str(max_decrease_amount))})")

# export files
export_pybank = os.path.join("python-challenge", "Pybank", "analysis", "Pybank.txt")

with open(export_pybank, "w") as csvfile:
    
    csvwriter = csv.writer(csvfile, delimiter=',')
    
    csvfile.write("financial Analysis")
    csvfile.write("/n")
    csvfile.write("------------------")
    csvfile.write("\n")
    csvfile.write(f"Total Months: {len(total_months)}")
    csvfile.write("\n")
    csvfile.write(f"Total: ${sum(total_profit)}")
    csvfile.write("\n")
    csvfile.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
    csvfile.write("\n")
    csvfile.write(f"Greatest Increase in Profits: {total_months[max_increase_date]} (${(str(max_increase_amount))})")
    csvfile.write("\n")
    csvfile.write(f"Greatest Decrease in Profits: {total_months[max_decrease_date]} (${(str(max_decrease_amount))})")
