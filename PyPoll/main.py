import os
import csv

pypoll = os.path.join("..", "Resources", "election_data.csv")

# open csv file
with open(pypoll, newline="", encoding="utf-8") as csvfile:
    csvreader= csv.reader(pypoll, delimiter=",")
    
    next(csvreader)
    
# total votes cast
    data = list(csvreader)
    row_count = len(data)

# create lists
    candidate_list = []
    tally = []
    votes = []
    percentage = []
    
 # complete list of cadidates who recieved votes   
    for i in range (0,row_count):
        candidate = [i][2]
        votes.append(candidate)
        if candidate not in candidate_list:
            candidate_list.append(candidate)
        candidate_count = len(candidate_list)
        
# percentage of votes each candidate won
# total number of votes each candidate won        
    for j in range (0,candidate_count):
        name = candidate_list[j]
        votes.append(tally.count(name))
        votes_percent = votes[j]/row_count
        percentage.append(votes_percent)            
            
# the winner of the election by popular vote
    winner = votes.index(max(votes))
    
# print all to terminal
    print("Election Results")
    print("----------------")
    print(f"Total Votes: {row_count:,}")
    print("----------------")
    for k in range (0,candidate_count): 
        print(f"{candidate_list[k]}: {percentage[k]:.3%} ({votes[k]:,})")
    print("----------------")
    print(f"Winner: {candidate_list[winner]}")
    print("----------------")

  # Print the results to text file
    print("Election Results", file=open("PyPoll.txt", "a"))
    print("----------------", file=open("PyPoll.txt", "a"))
    
    print(f"Total Votes: {row_count:,}", file=open("PyPoll.txt", "a"))
    print("----------------", file=open("PyPoll.txt", "a"))
    
    for k in range (0,candidate_count): 
        print(f"{candidate_list[k]}: {percentage[k]:.3%} ({votes[k]:,})", file=open("PyPoll.txt", "a"))
    
    print("------------------", file=open("PyPoll.txt", "a"))
    
    print(f"Winner: {candidate_list[winner]}", file=open("PyPoll.txt", "a"))
    print("--------------------", file=open("PyPoll.txt", "a"))
