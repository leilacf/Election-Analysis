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

![This is an image](
