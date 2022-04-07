import pandas as pd
import csv
import os

path=open("C:/Users/anahi/OneDrive/Desktop/PyPoll/Resources/election_data.csv")
df=pd.read_csv(path)

print("Election Results")
print("-------------------------")

#Print the total number of votes cast
print("Total Votes:", len(df))

print("-------------------------")

#A complete list of candidates who received votes and
#The total number of votes each candidate won
counts= df["Candidate"].value_counts()

#The percentage of votes each candidate won
percent = df_percentage=df["Candidate"].value_counts(normalize=True).mul(100).round(3).astype(str)+ '%' 

#show result
df2=pd.DataFrame({" ": percent,"":counts})

print(df2)

print("\n -------------------------")

#The winner of the election based on popular vote.
print("Winner: ", df['Candidate'].value_counts().idxmax())

#Print to text
with open('Analysis\Analysis.txt', 'w') as f:
    print("Election Results", file=f)
    print("-------------------------", file=f)
    print("Total Votes:", len(df), file=f)
    print("-------------------------", file=f)
    #counts= df["Candidate"].value_counts()
    #percent = df_percentage=df["Candidate"].value_counts(normalize=True).mul(100).round(3).astype(str)+ '%' 
    #df2=pd.DataFrame({" ": percent,"":counts})
    print(df2 , file=f)
    print("\n -------------------------" , file=f)
    print("Winner: ", df['Candidate'].value_counts().idxmax(), file=f)



