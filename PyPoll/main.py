#Import modules
import os
import csv

# File variables
file_input = os.path.join("Resources","election_data.csv")
file_output = os.path.join("analysis", "election_analysis.txt")

# Data variables
candidates = {}
total_votes = 0
winner_percentage = 0.00
winner = ""

# Output variables
section_break = "----------------------------------"
output_rows = []

# Read data file
with open(file_input, 'r', encoding='utf-8') as csv_file:
    # Read as CSV file
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Store header row
    csv_header = next(csv_reader)

    # Read data rows
    for row in csv_reader:
        # Read the candidate's name for this vote
        current_candidate = row[2]

        # Check if this candidate has previously been recorded. If not, add it to the dictionary.
        if (current_candidate not in candidates):
            # List is [vote count, vote percentage] per candidate
            candidates[current_candidate] = [0, 0.0]

        # Increment the vote count for this candidate
        candidates[current_candidate][0] += 1        

# Calculate grand total number of votes
for candidate in candidates:
    total_votes += candidates[candidate][0]

# Calculate percentage of votes for each candidate
for candidate in candidates:
    candidates[candidate][1] = candidates[candidate][0] / total_votes * 100
    if candidates[candidate][1] > winner_percentage:
        winner_percentage = candidates[candidate][1]
        winner = candidate

# Create output list
output_rows.append("Election Results\n")
output_rows.append(f"{section_break}\n")
output_rows.append(f"Total Votes: {total_votes}\n")
output_rows.append(f"{section_break}\n")
for candidate in candidates:
    output_rows.append(f"{candidate}: {candidates[candidate][1]:.3f}% ({candidates[candidate][0]})\n")
output_rows.append(f"{section_break}\n")
output_rows.append(f"Winner: {winner}\n")
output_rows.append(f"{section_break}\n")

# Output to terminal
for row in output_rows:
    print(row)

# Output to file
with open(file_output, 'w') as text_file:
    text_file.writelines(output_rows)