#import dependencies
import os
import csv

#Path to csv file
filepath = os.path.join("Resources","02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

#assign variables
candidate_list=[]
candidates=[]
candidate_votes=[]
candidate_percent=[]
voters=[]
unique_candidates=[]
    

#open and read csv
with open(filepath) as csvfile:
    datareader = csv.reader(csvfile,delimiter=",")
    header = next(datareader)
    #print(header)

    # create list using voter id, count for total votes
    voters = [pol_data[0] for pol_data in datareader]
    total_votes=(len(voters))
    #print(total_votes)


with open(filepath) as csvfile:
    datareader = csv.reader(csvfile,delimiter=",")
    header = next(datareader)

    #Create a list of all candidates, find set of unique candidate names and create list
    candidate_list = [pol_data[2] for pol_data in datareader]
    unique_candidates = list(set(candidate_list))
    #print(unique_candidates)

    
    #find total votes for each candidate
    for politicians in unique_candidates:
        can_votes= candidate_list.count(politicians)
        candidate_votes.append(can_votes)
    #print(candidate_votes)

    #find % votes for each candidate
    for politicians in unique_candidates:
        can_perc= candidate_list.count(politicians)/total_votes*100
        candidate_percent.append(can_perc)
    #print(candidate_percent)
    
    max_candidate_votes=max(candidate_votes)
    #print(max_candidate_votes)
    #find index for max votes
    index_max_votes = candidate_votes.index(max_candidate_votes)
    #print(index_max_votes)
    #use max votes index to extract winner from candidates list
    winner=unique_candidates[index_max_votes]
    #print(winner)


#print results
print("Election Results")
print("---------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------")
for i, politicians in enumerate(unique_candidates):
    print(f"{politicians} : {candidate_percent[i]:0.3f}% : ({candidate_votes[i]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

#print to text file
text_file = open("Analysis/Output.txt", "w")
text_file.writelines(f"Election Results\n--------------------------- \nTotal Votes: {total_votes} \n---------------------------\n")
for i, politicians in enumerate(unique_candidates):
    text_file.writelines(f"{politicians} : {candidate_percent[i]:0.3f}% : ({candidate_votes[i]})\n")
text_file.writelines(f"--------------------------- \nWinner: {winner} \n---------------------------")
text_file.close()