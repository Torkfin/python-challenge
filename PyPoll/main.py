#Python Code Chris Torkelson for PyPoll
 
# Importing Modules
import os
import csv 
import pandas 
import numpy as np



# Read in a .csv file
election_data_file = os.path.join("Resources","election_data.csv")
file = open(election_data_file)
csvreader = csv.DictReader(file)
    
# Print Title 

print("Election Results")
print("----------------------------")


# Calculate and Print the Total # of Votes

votes = len(list(csvreader)) 
votes = votes 
print("Total Votes:", votes)

print("----------------------------")

# Read the CSV into a Pandas DataFrame

df = pandas.read_csv(election_data_file)
 

# Count occurrences of votes for each Candidate

occur = df.groupby(['Candidate']).size()
 
# Import numpy function and create a Dataframe for Vote Information and Calculate % of Votes

df_votes = np.array(occur)
 
correy_percent = df_votes[0]/votes
 
khan_percent = df_votes[1]/votes

li_percent = df_votes[2]/votes

otooley_percent = df_votes[3]/votes


#Create a Dataframe for Voter Information 

df = pandas.DataFrame({  
                      "Candidate" : ["Correy", "Khan","Li","O'Tooley"],
                      "Num_Votes": [df_votes[0], df_votes[1], df_votes[2], df_votes[3]],
                      "Percent_Votes" : [correy_percent,khan_percent,li_percent,otooley_percent]
                      })
 

# Determine the Election Winner by Finding the Candidate with the Maximum # of Votes

df[df["Num_Votes"]==df["Num_Votes"].max()]

# Put the Max Values in an Array for easy Access
import numpy as np

max_values = np.array(df[df["Num_Votes"]==df["Num_Votes"].max()])

winner = (max_values[0, 0]) 

#Print the Candidate Votes and % and Winner

print(df['Candidate'][1]+ ":    ",'{:.3f}'.format(df['Percent_Votes'][1]*100) +"%", "(" + str(df['Num_Votes'][1]) + ")")
print(df['Candidate'][0]+ ":  ",'{:.3f}'.format(df['Percent_Votes'][0]*100) +"%", "(" + str(df['Num_Votes'][0]) + ")")
print(df['Candidate'][2]+ ":      ",'{:.3f}'.format(df['Percent_Votes'][2]*100) +"%", "(" + str(df['Num_Votes'][2]) + ")")
print(df['Candidate'][3]+ ": ",'{:.3f}'.format(df['Percent_Votes'][3]*100) +"%", "(" + str(df['Num_Votes'][3]) + ")")

print("----------------------------")

print("Winner:", winner)

print("----------------------------")


# Write the TXT file of Information

file1 = open(os.path.join("Analysis","myvotefile.txt"),"w")

file1.write("Election Results \n")
file1.write("--------------------------------- \n")

file1.write("Total Votes:  " + str(votes) +"\n")

file1.write("--------------------------------- \n")

file1.write(df['Candidate'][1]+ ":      " + '{:.3f}'.format(df['Percent_Votes'][1]*100) +"%  "+ "(" + str(df['Num_Votes'][1]) + ")" + "\n")
file1.write(df['Candidate'][0]+ ":    " + '{:.3f}'.format(df['Percent_Votes'][0]*100) +"%  " + "(" + str(df['Num_Votes'][0]) + ")" + "\n")
file1.write(df['Candidate'][2]+ ":        " + '{:.3f}'.format(df['Percent_Votes'][2]*100) +"%  " + "(" + str(df['Num_Votes'][2]) + ")" + "\n")
file1.write(df['Candidate'][3]+ ":   " + '{:.3f}'.format(df['Percent_Votes'][3]*100) +"%  " + "(" + str(df['Num_Votes'][3]) + ")" + "\n")

file1.write("--------------------------------- \n")

file1.write("Winner:  " + str(winner) + "\n")

file1.write("--------------------------------- \n")

