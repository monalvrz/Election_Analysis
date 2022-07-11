#The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

#Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

#Open the election results and read the file.
with open (file_to_load) as election_data:

    #To do: perform analysis.
    print(election_data)


# 1) Add our dependencies
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Open the election results and read the file.
with open (file_to_load) as election_data:

    #Print the file object.
    print(election_data)


# 2) Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    #Write some data to the file.
    #txt_file.write("Hello World")

# 3) Open the election results and read the file.
with open (file_to_load) as election_data:

  #To do: read and analyze the date here.
  # Read the file object with the reader function.
  file_reader = csv.reader(election_data)

  #Print each row in the CSV file.
#for row in file_reader:
        #print(row)

  #Read and print the header row.
  headers = next(file_reader)
  print (headers)


    

