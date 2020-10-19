# Colorado's 1st Congressional District Election Audit

## Overview
The objective is to automate the election results audit on behalf of the Colorado Board of Elections. We will do this by creating a python file to read the election results excel file and collect the needed data. 

### Results
The results of the election were processed and printed to the attached .txt file.

![election_results](https://github.com/watsonlarry/Election_Analysis/blob/main/Resources/Screen%20Shot%202020-10-18%20at%2010.28.11%20PM.png)

- Total votes cast: 369,711
  - Jefferson County: 38,855 votes (10.5%of total votes cast) 
  - Denver County: 306,055 votes (82.8% of total votes cast) 
  - Arapahoe County: 24,801 votes (6.7% of total votes cast)

- Denver County cast the largest number of votes.

- Candidate Results:
  - Charles Casper Stockham: 85,213 votes (23.0% of total votes cast)  
  - Diana DeGette: 272,892 votes (73.8% of total votes cast)
  - Raymon Anthony Doane: 11,606 votes (3.1% of total votes cast)

- Diana Degette was the winner of the election with 272,892 votes (73.8% of total votes cast).

### Summary

The python code developed can be reused in future audits, with minimal alterations to the existing code, if the election data is collected in similarly styled excel files. For example, if auditing the results from a new election, the code will need to reflect the new read file location. So this line of code will need to be changed to represent the new read file's location:

![file_to_read](https://github.com/watsonlarry/Election_Analysis/blob/main/Resources/file_to_load.png)

Additionally, if the formatting in the new file is different, changes to the code will need to be made. Let's say the county name is now located in column 3 instead of column 2 of the new election file. In that case, this line of code will need to candidate_name = row[3]:

![row_location](https://github.com/watsonlarry/Election_Analysis/blob/main/Resources/row_location.png)

Besides redefining a few variables and file locations, the code should not require any large structural changes to be used by the committee in the future.
