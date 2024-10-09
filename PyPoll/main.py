#Import modules
#import os
import csv

# File variables
file_input = "Resources/election_data.csv"
file_output = "analysis/election_analysis.txt"

# Data variables
candidates = []
total_votes_per_candidate = []
percentage_per_candidate = []
total_votes = 0

winner_percentage = 0.00
winner = ""

# Output variables
section_break = "----------------------------------"
output_rows = []

# Read data file
with open(file_input, encoding='utf-8') as csv_file:
    # Read as CSV file
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Read header row
    csv_header = next(csv_reader)

    # Read data rows
    for row in csv_reader:
        # Read the candidate's name for this vote
        current_candidate = row[2]

        # Check if this candidate has previously been recorded. If not, add it to the lists.
        if (not candidates.__contains__(current_candidate)):
            candidates.append(current_candidate)
            total_votes_per_candidate.append(0)
            percentage_per_candidate.append(0.0)

        # Increment the total votes for this candidate
        total_votes_per_candidate[candidates.index(current_candidate)] += 1

# Calculate grand total number of votes
for i in range(len(total_votes_per_candidate)):
    total_votes += total_votes_per_candidate[i]

# Calculate percentage of votes for each candidate
for i in range(len(percentage_per_candidate)):
    percentage_per_candidate[i] = total_votes_per_candidate[i] / total_votes * 100
    if (percentage_per_candidate[i] > winner_percentage):
        winner_percentage = percentage_per_candidate[i]
        winner = candidates[i]

# Create output list
output_rows.append("Election Results\n")
output_rows.append(f"{section_break}\n")
output_rows.append(f"Total Votes: {total_votes}\n")
output_rows.append(f"{section_break}\n")
for i in range(len(candidates)):
    output_rows.append(f"{candidates[i]}: {percentage_per_candidate[i]:.3f}% ({total_votes_per_candidate[i]})\n")
output_rows.append(f"{section_break}\n")
output_rows.append(f"Winner: {winner}\n")
output_rows.append(f"{section_break}\n")

# Output to terminal
for row in output_rows:
    print(row)

# Output to file
with open(file_output, 'w') as text_file:
    text_file.writelines(output_rows)