#Main PY File for PyBank

    
# Importing os module
import os
  
# Get the current working directory (CWD)
cwd = os.getcwd()
     
# Print the current working directory (CWD)

# print("Current working directory:", cwd)


#Your task is to create a Python script that analyzes the records to calculate each of the following:
# Import the necessary dependencies for os.path.join()
 
 
import csv

# Read in a .csv file
budget_data_file = os.path.join("Resources","budget_data.csv")

#print("CSV file:", budget_data_file)


with open(budget_data_file) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    #for row in csvreader:
    #     print(row)


# Print Title 
print("Financial Analysis")
print("----------------------------")


# Calculate and Print the Total # of Months    

file = open(budget_data_file)
reader = csv.reader(file)
months = len(list(reader)) 
months = months - 1
print("Total Months:", months)

# Read the CSV into a Pandas DataFrame
import pandas 

df = pandas.read_csv(budget_data_file)
 

#'Calculate and Print the changes in "Profit/Losses" over the entire period

total =df['Profit/Losses'].sum()
print("Total Profit: $" + str(total))

# Calculate the Average Amount of Profit Change
average = total / months

print ("Average Profit Increase",'${:.2f}'.format(average))


# Calculate the Delta Between Each Month Profit/Loss and Store in Dataframe under "DiffPL"

df["DiffPL"] = df["Profit/Losses"].diff(+1)


# Calculate and Print the Average Change 

averagecalc =df['DiffPL'].mean()
print ("Average Change:",'${:.2f}'.format(averagecalc))



# Calculate and Print the Greatest increase in profits over the entire period

# Calculate the Max Profit

# Get the String of Maximum Values

df[df["Profit/Losses"]==df["Profit/Losses"].max()]

# Put the Max Values in an Array for easy Access
import numpy as np

max_values = np.array(df[df["Profit/Losses"]==df["Profit/Losses"].max()])
high_amount = (max_values[0, 2]) 
high_amount = str(high_amount).rstrip('.0')


# Separate out Highest Profit Date for Printing
high_date = (max_values[0, 0]) 
high_month = (high_date[0:3])
high_year = (high_date[4:6])

print("Greatest Increase in Profits: " + high_month + "-20" + high_year, (f"${high_amount}"))


# Calculate and Print the greatest decrease in profits over the entire period

# Get the String of the Minimum Values
df[df["Profit/Losses"]==df["Profit/Losses"].min()]

# Put the Min Values in an Array for easy Access
min_values = np.array(df[df["Profit/Losses"]==df["Profit/Losses"].min()])
low_amount = (min_values[0, 2]) 
low_amount = str(low_amount).rstrip('.0')


# Separate out Lowest Profit Date for Printing
low_date = (min_values[0, 0]) 
low_month = (low_date[0:3])
low_year = (low_date[4:6])

# Print Greatest Decrease
print("Greatest Decrease in Profits: " + low_month + "-20" + low_year, (f"${low_amount}"))


# Module to write data to myfile.

file1 = open("myfile.txt","w")

file1.write("Financial Analysis \n")
file1.write("--------------------------------- \n")

str_months = repr(months)
file1.write("Total Months: " + str_months + "\n")

str_total = repr(total)
file1.write("Total Profit: $" + str_total + "\n")

file1.write("Average Change: " + '${:.2f}'.format(averagecalc) + "\n")

file1.write("Greatest Increase in Profits: " + high_month + "-20" + high_year + " " + (f"${high_amount}" +"\n"))

file1.write("Greatest Decrease in Profits: " + low_month + "-20" + low_year + " " + (f"${low_amount}"))

file1.close() 


