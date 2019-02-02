import os
import csv

csvpath = os.path.join('..', 'resourses', 'budget_data.cvs')
total_months = []
total_profit_losses = []
average_change = []

with open(csvpath, newline='') as total:
    csvreader = csv.reader(total, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        total_months.append(row[0])
        total_profit_losses.append(int(row[1]))
    for i in range(len(total_profit_losses)-1):
        average_change.append(total_profit_losses[i+1]-total_profit_losses[i])


max_increase_total = max(average_change)
max_decrease_total = max(average_change)
max_increase_month = average_change.index(max(average_change)) + 1
max_decrease_month = average_change.index(min(average_change)) + 1

print("financial analysis")
print("------------------------")
print(f"total months:{len(total_months)}")
print(f"total: ${sum(total_profit_losses)}")
print(f"average change: {round(sum(average_change)/len(average_change),2)}")
print(f"greatest increase in profits: {total_months[max_increase_month]} (${(str(max_increase_total))})")
print(f"greatest increase in profits: {total_months[max_decrease_month]} (${(str(max_decrease_total))})")

output_file = Path("Python-Challnge", "PyBank", "financial_analysis.txt")

with open(output_file,"w") as file:
file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")