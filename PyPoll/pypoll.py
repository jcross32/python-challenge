#!/usr/bin/env python
# coding: utf-8

# In[25]:


#dependencies
import csv
import os

#file to load path and output path
file_to_load = os.path.join (".", "Resources", "election_data.csv")
file_to_output = os.path.join (".", "election_analysis.txt")

#total vote counter
total_votes = 0

#candidate options and vote counters {} and [] are place holders for a blank variable
candidate_votes = {}
candidate_options = []

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0

with open(file_to_load) as election_data:
    
    
    reader = csv.reader(election_data)
    
    #reading header
    header = next(reader)
    
    for row in reader:
        
        #add to total vote count
        total_votes = total_votes + 1
        
        
        #gets candidate name from each row, value 2 = the second index value in that row
        candidate_name = row[2]
        
        
        #if candidate does not match any existing candidate
        #loop is trying to find candidates as it goes
        
        if candidate_name not in candidate_options:
            
            #add to list of candidates in running
            candidate_options.append(candidate_name)
        
            candidate_votes[candidate_name] = 0
            
        candidate_votes[candidate_name] += 1
            
#print(candidate_votes)
#print(candidate_options)

with open (file_to_output, "w") as txt_file:
    
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes {total_votes}\n"
        f"-------------------------\n"
    )

    print (election_results, end="")
    
    txt_file.write(election_results)

    for candidate in candidate_votes:
        
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        
        
    
        if(votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        

        print(voter_output, end="")
        
        txt_file.write(voter_output)
        
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)
    
    txt_file.write(winning_candidate_summary)


# In[ ]:


# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------

