#import dependencies
import os
import csv

#Path to csv file
filepath = os.path.join("Resources","02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

# Define the function and have it accept the 'pol_data' as its sole parameter

#assign variables
candidate_list=[]
candidates=[]
candidate_votes=[]
voters=[]
unique_candidates:[]
    # winner = max()
    

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

    #calc votes and vote percentage for first candidate
    Can1_votes = candidate_list.count(unique_candidates[0])
    Can1_perc = Can1_votes/total_votes*100
    #calc votes and vote percentage for second candidate
    Can2_votes = candidate_list.count(unique_candidates[1])
    Can2_perc = Can2_votes/total_votes*100
    #calc votes and vote percentage for third candidate
    Can3_votes = candidate_list.count(unique_candidates[2])
    Can3_perc = Can3_votes/total_votes*100
    #calc votes and vote percentage for third candidate
    Can4_votes = candidate_list.count(unique_candidates[3])
    Can4_perc = Can4_votes/total_votes*100
    
    #build list with candidate votes to extract max votes (winner)
    candidate_votes=[Can1_votes,Can2_votes,Can3_votes,Can4_votes]
    #calc max votes
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
print(f"{unique_candidates[0]} : {Can1_perc:0.3f}% : ({Can1_votes})")
print(f"{unique_candidates[1]} : {Can2_perc:0.3f}% : ({Can2_votes})")
print(f"{unique_candidates[2]} : {Can3_perc:0.3f}% : ({Can3_votes})")
print(f"{unique_candidates[3]} : {Can4_perc:0.3f}% : ({Can4_votes})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

#print to text file
text_file = open("Analysis/Output.txt", "w")
text_file.writelines(f"Election Results\n--------------------------- \nTotal Votes: {total_votes} \n---------------------------\n{unique_candidates[0]} : {Can1_perc:0.3f}% : ({Can1_votes}) \n{unique_candidates[1]} : {Can2_perc:0.3f}% : ({Can2_votes}) \n{unique_candidates[2]} : {Can3_perc:0.3f}% : ({Can3_votes}) \n{unique_candidates[3]} : {Can4_perc:0.3f}% : ({Can4_votes}) \n--------------------------- \nWinner: {winner} \n---------------------------")
text_file.close()