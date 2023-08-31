#!/usr/bin/env python
# coding: utf-8

# In[23]:


import csv
import os

election_csv = os.path.join(".", "Resources", "election_data.csv")
export_file = os.path.join(".", "Analysis.txt")

total_votes = 0
candidate_votes = {}
candidate_list = []
winning_candidate = ""
winning_vote = 0

with open(election_csv) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
    
    for row in reader:
        total_votes += 1
        candidate_name = row[2]
        
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1

with open (export_file, "w") as txt_file:
    
    results = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes : {total_votes}\n"
    f"-------------------------\n")
    print(results)

    txt_file.write(results)

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        
        if(votes > winning_vote):
            winning_vote = votes
            winning_candidate = candidate
            
        voter_results = f"{candidate} : {vote_percentage:.3f}% ({votes})\n"
        print(voter_results)
    
        txt_file.write(voter_results)
        
    winner = (
        f"-------------------------\n"
        f"Winner : {winning_candidate}\n"
        f"-------------------------\n")
    print(winner) 
    
    txt_file.write(winner)


# In[ ]:




