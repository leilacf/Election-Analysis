# Election-Analysis
## 1. Overview of Election Audit
  The purpose of this analysis was to inspect election data and report the total amount of votes cast, highlight the candidates and the total votes per candidate, percentage of votes per candidate, and to determine the winning elected official of the race. In being presented with this data in .csv format, we utilized Python to code and create these calculations in a concise and transparent manner. The data visualizations that the analysis is bassed off on, can be seen in the .txt file. We delved even deeper into this data by presenting an elaborate analysis on voter turnout per county, county with the highest turnout, and the percentage of votes in each county from the total count. Adding more refined layers into this analysis was quite a simple task to do due to the high-level and general purpose nature of this programming tool.
  
  ## 2. Election-Audit Results 
  The visual production based off of the election data can be seen below:
  
  ![This is an image](https://github.com/leilacf/Election-Analysis/blob/main/Election-Analysis/Resources/Election%20data%20full.png)
  
- (a) How many votes were cast in this congressional election?
  - A total of 369,711 votes were cast in this election

![This is an image](https://github.com/leilacf/Election-Analysis/blob/main/Election-Analysis/Resources/total%20votes%20from%20election.png)

Using Python, we followed these steps:
- Added our dependencies and initialized a total vote counter

![This is an image](https://github.com/leilacf/Election-Analysis/blob/main/Election-Analysis/Resources/1.%20added%20dependencies.png)

- Initialized election data variable to pull data from the .csv file and created a for loop to iterate through each row

![This is an image](https://github.com/leilacf/Election-Analysis/blob/main/Election-Analysis/Resources/2.%20for%20loop%2C%20vote%20count%20variable.png)

- and lastly, used an f string to save our results on the .txt file

![This is an image](https://github.com/leilacf/Election-Analysis/blob/main/Election-Analysis/Resources/2.%20for%20loop%2C%20vote%20count%20variable.png)

- (b) Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  - Below is a screenshot of the county votes and percentage of total votes

![This is an image](https://github.com/leilacf/Election-Analysis/blob/main/Election-Analysis/Resources/breakfown%20numb%20of%20votes%20and%20%25%20county.png)

- In terms of the code created in Python:
  - first step was to extract the county names 

![This is an image](https://github.com/leilacf/Election-Analysis/blob/main/Election-Analysis/Resources/county%20name.png)

- Then, using an if statement we created the list of county names and the vote count associated with each, to get the county results

![This is an image](https://github.com/leilacf/Election-Analysis/blob/main/Election-Analysis/Resources/if%20statement%20county%20votes.png)

- And lastly, created a for loop to iterate through the dictionary to calculate the vote count and total percentage of votes

![This is an image](https://github.com/leilacf/Election-Analysis/blob/main/Election-Analysis/Resources/for%20loop%20county%20votes.png)

- (c) Which county had the largest number of votes?
  - Denver was the county with the largest number of votes, as seen below:

![This is an image](https://github.com/leilacf/Election-Analysis/blob/main/Election-Analysis/Resources/Denver%20largest%20num%20votes.png)

- This was calculated by creating an if statement to determine the county with the largest voter turnout

![This is an image](https://github.com/leilacf/Election-Analysis/blob/main/Election-Analysis/Resources/code%20for%20largest%20county.png)

- (d) Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  - Below is the breakdown of votes, percentages of total votes, and candidates:
  
![This is an image](https://github.com/leilacf/Election-Analysis/blob/main/Election-Analysis/Resources/each%20cand%20votes.png)

- Initially, in Python we extracted the candidate names

![This is an image](https://github.com/leilacf/Election-Analysis/blob/main/Election-Analysis/Resources/candidate%20names.png)

- Then used an if statement to iterate through the rows and add the candidate vote count

![This is an image](https://github.com/leilacf/Election-Analysis/blob/main/Election-Analysis/Resources/if%20statement%20candidate%20votes.png)

- And lastly, used a for loop to calculate the percentage, and an f string to print this into the .txt file

![This is an image](https://github.com/leilacf/Election-Analysis/blob/main/Election-Analysis/Resources/candidate%20total%20votes.png)

- (e) Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

![This is an image](https://github.com/leilacf/Election-Analysis/blob/main/Election-Analysis/Resources/winning%20candidate.png)

- As seen above, Diana DeGette won with 272,892 votes and 73.8% of the total votes
- This was calculated with the following code where we created an if statement to determine the winning count, candidate, and percentage

![This is an image](https://github.com/leilacf/Election-Analysis/blob/main/Election-Analysis/Resources/winning%20cand%20code.png)

## 3. Election-Audit Summary
As seen with the clear analysis created for this election, through the use of Python, the versatility of this program allows for the same steps to be used in analysis for other elections! With mild modifications, this level of analysis can be highly beneficial for any election commission. 

For example:
- larger data sets incorporating more detailed columns can be used, however, additional for loops and if statements would have to be added to the code in order to pull and work with the right data set, or portion of a data set
- For a deeper understanding as to what made a particular winning candidate popular, modified additional code which sets a number value to the person, in comparison with others or with historical patterns, can serve to create a predictive analytical tool

