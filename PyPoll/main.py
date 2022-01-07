#Main PY File for PyPoll
#PYPOLL  PYPOLL

    
# Importing os module
import os
  
# Get the current working directory (CWD)
cwd = os.getcwd()
     
#print the current working directory (CWD)

# print("Current working directory:", cwd)


#Your task is to create a Python script Automate Poll Counting
# Import the necessary dependencies for os.path.join()
 
 
import csv

# Read in a .csv file
election_data_file = os.path.join("Resources","election_data.csv")

#print("CSV file:", election_data_file)


with open(election_data_file) as csvfile:

#   CSV reader specifies delimiter and variable that holds contents
   csvreader = csv.reader(csvfile, delimiter=',')

#      print(csvreader)

#   Read the header row first (skip this step if there is no header)
#   csv_header = next(csvreader)
#print(f"CSV Header: {csv_header}")

#    Read each row of data after the header
#   for row in csvreader:
#    print(row)


# Print Title 
print("Election Results")
print("----------------------------")


# Calculate and Print the Total # of Votes
file = open(election_data_file)
reader = csv.reader(file)
votes = len(list(reader)) 
votes = votes - 1
print("Total Votes:", votes)

print("----------------------------")

# Read the CSV into a Pandas DataFrame
import pandas 

df = pandas.read_csv(election_data_file)
 

# count occurrences a particular column
occur = df.groupby(['Candidate']).size()
 
# display occurrences of a particular column
#print(occur)
 
 
import numpy as np

df_votes = np.array(occur)
#print(df_votes)

correy_percent = df_votes[0]/votes
#print (correy_percent)

khan_percent = df_votes[1]/votes
#print(khan_percent)

li_percent = df_votes[2]/votes
#print (li_percent)

otooley_percent = df_votes[3]/votes
#print (otooley_percent)

df = pandas.DataFrame(
{  
        "Candidate" : ["Correy", "Khan","Li","O'Tooley"],
        "Num_Votes": [df_votes[0], df_votes[1], df_votes[2], df_votes[3]],
        "Percent_Votes" : [correy_percent,khan_percent,li_percent,otooley_percent]
         }
)
#print(df)
# Get the String of Maximum Values

df[df["Num_Votes"]==df["Num_Votes"].max()]

# Put the Max Values in an Array for easy Access
import numpy as np

max_values = np.array(df[df["Num_Votes"]==df["Num_Votes"].max()])
winner = (max_values[0, 0]) 

print(df['Candidate'][1]+ ":    ",'{:.3f}'.format(df['Percent_Votes'][1]*100) +"%", "(" + str(df['Num_Votes'][1]) + ")")
print(df['Candidate'][0]+ ":  ",'{:.3f}'.format(df['Percent_Votes'][0]*100) +"%", "(" + str(df['Num_Votes'][0]) + ")")
print(df['Candidate'][2]+ ":      ",'{:.3f}'.format(df['Percent_Votes'][2]*100) +"%", "(" + str(df['Num_Votes'][2]) + ")")
print(df['Candidate'][3]+ ":",'{:.3f}'.format(df['Percent_Votes'][3]*100) +"%", "(" + str(df['Num_Votes'][3]) + ")")

print("----------------------------")

print("Winner:", winner)

print("----------------------------")

file1 = open("myvotefile.txt","w")

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



#str_total = repr(total)
#file1.write("Total Profit: $" + str_total + "\n")

#file1.write("Average Change: " + '${:.2f}'.format(averagecalc) + "\n")

#file1.write("Greatest Increase in Profits: " + high_month + "-20" + high_year + " " + (f"${high_amount}" +"\n"))

#file1.write("Greatest Decrease in Profits: " + low_month + "-20" + low_year + " " + (f"${low_amount}"))

#file1.close() 


