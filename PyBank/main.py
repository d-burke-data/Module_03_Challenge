# Import modules
import csv

# File variables
file_input = "Resources/budget_data.csv"
file_output = "analysis/bank_analysis.txt"

# Data variables
total_months = 0
net_profit = 0
total_change = 0
last_profit = 0

mean_change = 0.00

greatest_increase_month = ""
greatest_increase_amount = 0

greatest_decrease_month = ""
greatest_decrease_amount = 0

# Output variables
section_break = "----------------------------------"
output_rows = []

# Read data file
with open(file_input, encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)

    for row in csv_reader:
        current_month = row[0]
        current_profit = int(row[1])

        total_months += 1
        net_profit += current_profit
        current_change = 0

        # Calculate change from last month
        # Do not calculate for the first month since there is no previous month
        if total_months > 1:
            current_change = current_profit - last_profit
        
        last_profit = current_profit
        total_change += current_change

        print (f"Current Change: {current_change}  Total Change: {total_change}")

        # Check if the current row has the greatest increase or decrease in profit
        if current_change > greatest_increase_amount:
            greatest_increase_amount = current_change
            greatest_increase_month = current_month
        elif current_change < greatest_decrease_amount:
            greatest_decrease_amount = current_change
            greatest_decrease_month = current_month

# Calculate average month-over-month change
# Reduce total months by 1 because there's no change for the first month
mean_change = total_change / (total_months - 1)

# Create output list
output_rows.append("Financial Analysis\n")
output_rows.append(f"{section_break}\n")
output_rows.append(f"Total Months: {total_months}\n")
output_rows.append(f"Total: ${net_profit}\n")
output_rows.append(f"Average Change: ${mean_change:.2f}\n")
output_rows.append(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amount})\n")
output_rows.append(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amount})\n")

# Output to terminal
for row in output_rows:
    print(row)

# Output to file
with open(file_output, 'w') as text_file:
    text_file.writelines(output_rows)
