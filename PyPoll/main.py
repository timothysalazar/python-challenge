#import libraries
import os
import csv

#define file path relative to current working directory
dataPath = os.path.join("Resources", "election_data.csv")

#initialize variables
totalVotes = 0 #count of total votes cast
candidates = {} #dictionary to hold the inidividual results of candidates


#open the file using "read" mode and assign to a variable
with open(dataPath, 'r', encoding='utf') as csvfile:
    pollData = csv.reader(csvfile, delimiter=",") #read the file
    next(pollData) #skip the header
    for i in pollData: #iterate through all rows containing data
        if i[2] not in candidates: #check if candidate voted for is in dictionary if not:
            candidates[str(i[2])] = [1, 0] #add an entry with key = candidate name and values = vote count and percentage of total votes
        else: #if candidate is already in dictionary then add a vote to their tally
            candidates[str(i[2])][0] += 1
        totalVotes += 1 #add a vote to to the total vote count
    for i in candidates: #iterate through candidates to calculate their percentage of total vote
        candidates[f'{i}'][1] = candidates[f'{i}'][0]/totalVotes

#print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------")
for i in candidates:
    print(f"{i}: {round(candidates[f'{i}'][1]*100,3)}% ({candidates[f'{i}'][1]})")
print("-------------------------")
#compare to see the winner
winner = 0
for i in candidates:
    if candidates[f'{i}'][0] > winner:
        chickenDinner = i
        winner = candidates[f'{i}'][0]
print(f"Winner: {chickenDinner}")
print("-------------------------")

#write to a text file
with open("analysis\election_results.txt", 'w') as file:
    print("Election Results", file=file)
    print("-------------------------", file=file)
    print(f"Total Votes: {totalVotes}", file=file)
    print("-------------------------", file=file)
    for i in candidates:
        print(f"{i}: {round(candidates[f'{i}'][1]*100,3)}% ({candidates[f'{i}'][1]})", file=file)
    print("-------------------------", file=file)
    print(f"Winner: {chickenDinner}", file=file)
    print("-------------------------", file=file)
