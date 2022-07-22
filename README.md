# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received vote.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote. 
6. Calculate the voter tournout for each county.
7. Calculate the percentage of votes from each county out of the total count.
8. Determine the county with the highest turnout.

Although this task could have been performed in Excel, the tool used to work with the database was Python, with the purpose of automating the process. This will allow the Board to use the code to obtain and analyze information from other campaigns, such as Senatorial elections and Local District elections. Three primary voting methods were taken in account: mail-in ballot, punch cards and direct recording electronic. All together determined the total election results. Additionally, a text file containing the results of the election was delivered.

## Resources 
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Election-Audit Results
The analysis of the election show that:
- The were **369,711 votes** cast in the election.
- The voter tournout for each county was:
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306, 055)
  - Arapahoe: 6.7% (24,801)
- The county with the **highest tournout** was:
  - **Denver** with 82.8% of the voter tournout.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The **winner** of the election was:
  - Candidate **Diana DeGette**, who received 73.8% of the vote and 272,892 number of votes.

<img width="298" alt="election_analysis" src="https://user-images.githubusercontent.com/107893200/180316245-df9c6764-ad58-4cf4-8f07-abea94bef6f2.png">

## Election-Audit Summary
In addition to providing the results of the election audit, the project sought to provide a code that could be reused to obtain data for future elections.The code will be broken down to review how it can be adapted to work with any election information.

In the first place, the program will allow us to upload any data base that is stored in a CSV file. 

```
# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join('Resources', 'election_results.csv')
# Add a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")
```

Subsequently, we execute the following steps:
  - Initialize a total vote counter.
  - Create a candidate and county list and dictionaries that will containe the information we will collect.
  - Initialize the empty variables that will hold the candidates and counties names and counts.
  -  **This variables can be adapted to any data base who containes candidate and counties information**
  - Read the CSV file and convert it into a list of dictionaries.
  - Read the header.
  - Create a for loop to obtain the total votes, the number of candidate names and county names.
  - Next we will initialize a if condition that will iterate on the selected columns of our file to obtaine the total votes, the candidate names and the county names and add them to a list if not repeated. **The if condition is the element that will help the Colorado Board of Elections to use this code on other elections, not only with this particular election. The loop will hold only the information that we need. It doesn't matter if there are three, five, eight or ten candidates and counties, this formula will retrieve each one of them.** 
      _Example: Imagine you have five candidates instead of three.
                candidate_names: Charles Casper Stockham, Diana DeGette, Raymon Anthony Doane, Jonathan Simons, Stephanie Miller.
                The if condition will append each name in the 'candidate_options' list.
                The same scenario will happen with the counties. It doesn't matter how many counties you have in the database, the code will not append                   the name if it is repeated, and it will continue to do the search till it completes the row._
 - The if condition will add the new information on the lists.
 - Print the final vote count in the terminal.
 - And save the results to our text file.
 
```
# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
counties = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county = ""
county_voter_turnout = 0
winning_turnout_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        counties_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if counties_name not in counties:

            # 4b: Add the existing county to the list of counties.
            counties.append(counties_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[counties_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[counties_name] += 1
        
        # Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results)

    txt_file.write(election_results)
 ```
 
 In the last part of the code we will use the information we gathered to obtain:
 - Percentage of votes for the county.
 - Determine the winning county and get its vote count.
 - Retrieve the vote count and the percentage of each candidate.
 - Determine winning vote count, winning percentage, and candidate.
 - Print the information on the terminal.
 - Save the information on a text file.

**To obtain this information we have to write a for loop that will help us retrieve the information an easily calculate th percentages. In addition we have to write and if statment that will determine the winner candidate and the winning county based on the vote count.** _To replecate this part of the script with other data bases we have to pay attention on the list and dictionaries we created in the first section. It can be easilly change for other information, the only importan part is to maintain the same if statement and respect the indentation. It won't change if you are more or less information to the database._
 
  ```
  # 6a: Write a for loop to get the county from the county dictionary
    for counties_name in county_votes:

        # 6b: Retrieve the county vote count.
        vote_count = county_votes.get(counties_name)
        
        # 6c: Calculate the percentage of votes for the county.
        vote_count_percentage = float(vote_count) / float(total_votes) * 100
        county_results = (
            f"{counties_name}: {vote_count_percentage:.1f}% ({vote_count:,})\n")
            
         # 6d: Print the county results to the terminal
        print(county_results)
         
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (vote_count > county_voter_turnout) and (vote_count_percentage > winning_turnout_percentage):
                        county_voter_turnout = vote_count
                        winning_turnout_percentage = vote_count_percentage
                        largest_county = counties_name

    # 7: Print the county with the largest turnout to the terminal.
    largest_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n")
    print(largest_county_summary)
    
                # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_county_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
  ```
 ### Adapt the script to other elections
 Remember, the stepts you have to follow to use the script and get the same results. 
 1. Change the path to upload and save the csv file.
```
file_to_load = os.path.join()
file_to_save = os.path.join("Analysis", "election_analysis.txt")
```
2. Start the total vote counter.
```
total_votes = 0
```
3. Generete your lists that will contain the candidates name or the counties. 
4. Create the dictionaries that will retrieve each candidates and counties name and add the votes.
5. Create the variables that will hold the winning candidate, the vout count and the vote percentage.
6. Add the total votes count.
```
total_votes = total_votes + 1
```
7. Epecify the row in which the information is displayed, it may vary according to ypur database.
```
 candidate_name = row[2]
 counties_name = row[1]
 ```
 8. Use the if condition to iterate through the rows to search and append the information you need.
 9. Write a for loop to retrieve the vote count and calculate the percentage.
```
for counties_name in county_votes:

        vote_count = county_votes.get(counties_name)
        
        vote_count_percentage = float(vote_count) / float(total_votes) * 100
        county_results = (
            f"{counties_name}: {vote_count_percentage:.1f}% ({vote_count:,})\n")
```

 11. Additionally, write and if statment that will determine a winner.
```
if (vote_count > county_voter_turnout) and (vote_count_percentage > winning_turnout_percentage):
                        county_voter_turnout = vote_count
                        winning_turnout_percentage = vote_count_percentage
                        largest_county = counties_name
```
 13. Don't forget to print and save your information in a text file on every step.   

