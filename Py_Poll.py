# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_results.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Declare the empty dictionary.
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_list = []
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2. Track the largest county and county voter turnout

largest_turnout_county = ""
largest_turnout_county_votes = 0
largest_turnout_county_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

   # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # 3. Extract the county name from each row.

        county_name = row[1]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
# Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a. Write a decision that checks that the county doesn't match any county in the county list
        if county_name not in county_list:
            # 4b. Add existing county to list of counties
            county_list.append(county_name)
            # 4c. Begin Tracking the county's vote count
            county_votes[county_name] = 0
        # 5. Add a vote to that county's vot count.
        county_votes[county_name] += 1

# Print the candidate vote dictionary.
with open(file_to_save, "w") as txt_file:

# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # 6a. Write a repetition statement to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b. Retrieve the county vote count.
        votes_of_county = county_votes[county_name]
        # 6c. Calculate the percent of total votes for the county.
        vote_percentage_county = round(float(votes_of_county) / float(total_votes) * 100, 1)
        # 6d. Print the county results to the terminal.
        county_results = (f"{county_name}: {vote_percentage_county:.1f}% ({votes_of_county:,})\n")
        # 6e. Save the county votes to a text file.
        print(county_results)
        # 6f. Write a decision statement to determine the winning county and get its vote count.
        txt_file.write(county_results)
    # 7. Print the countyresults to the terminal
        if (votes_of_county > largest_turnout_county_votes) and (vote_percentage_county > largest_turnout_county_percentage):
            largest_turnout_county_votes = votes_of_county
            largest_turnout_county_percentage = vote_percentage_county 
            largest_turnout_county = county_name
    # 8. Save the county with the largest turnout to  a text file
    largest_turnout_county_summary = (
    f"-------------------------\n"
    f"Largest County Turnout: {largest_turnout_county}\n"
    f"-------------------------\n")
    
    print(largest_turnout_county_summary)
    txt_file.write(largest_turnout_county_summary)

    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = round(float(votes) / float(total_votes) * 100, 1)
        # 4. Print the candidate name and percentage of votes.
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
# Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

    # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    # Save the winning candidate's name to the text file.
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
#print(winning_candidate_summary)