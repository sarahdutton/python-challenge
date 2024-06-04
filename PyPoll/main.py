import os
import csv
from pathlib import Path

# find path 
pypollPath = Path('/Users/sarahdutton/challenge 3/python-challenge/PyPoll/Resources/election_data.csv')

# declare variables
totalVotes = 0
stockhamVotes = 0
degetteVotes = 0
doaneVotes = 0

# open csv file
with open(pypollPath, newline='', encoding="utf-8") as csvfile:
   
    csvReader= csv.reader(csvfile, delimiter=",")
    
    csvHeader = next(csvReader)
   
    
# total number of votes per candidate 

    for row in csvReader:
        
        totalVotes += 1
        
        if row[2] == "Charles Casper Stockham": 
            stockhamVotes += 1
        elif row[2] == "Diana DeGette":
            degetteVotes += 1
        elif row[2] == "Raymon Anthony Doane": 
            doaneVotes += 1
       

           
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]          
votes = [stockhamVotes, degetteVotes, doaneVotes]

# find winner
candidatesAndVotes = list(zip(candidates, votes))
winner = max(candidatesAndVotes)

# find percentage 
stockhamPercent = (stockhamVotes/totalVotes) * 100
degettePercent = (degetteVotes/totalVotes) * 100
doanePercent = (doaneVotes/totalVotes)* 100

print(f"Election Results")
print(f"----------------")
# total number of votes cast
print(f"Total Votes: {totalVotes}")
print(f"-----------------")
print(f"Charles Casper Stockham: {stockhamPercent:.3f}% ({stockhamVotes})")
print(f"Diana Degette: {degettePercent:.3f}% ({degetteVotes})")
print(f"Raymon Anthony Doane: {doanePercent:.3f}% ({doaneVotes})")
print(f"-----------------")
print(f"Winner: {winner}")
print(f"-----------------")

# print to txt file
PypollTxt = Path("/Users/sarahdutton/challenge 3/python-challenge/PyPoll/analysis/pypoll.txt")

with open(PypollTxt,"w") as file:

    file.write(f"Election Results")
    file.write("\n")
    file.write(f"---------------------")
    file.write("\n")
    file.write(f"Total Votes: {totalVotes}")
    file.write("\n")
    file.write(f"-----------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {stockhamPercent:.3f}% ({stockhamVotes})")
    file.write("\n")
    file.write(f"Diana Degette: {degettePercent:.3f}% ({degetteVotes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {doanePercent:.3f}% ({doaneVotes})")
    file.write("\n")
    file.write(f"------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write(f"------------------------")