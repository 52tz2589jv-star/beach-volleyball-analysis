#---QUESTION---
#What beach volleyball Stat Actually Matters?
#Which team stat plays the biggest role in whether a team wins or loses a match?

#Although beach volleyball may seem like a relatively simple sport, there are actually a number of different statistics that can be tracked to determine how well a team is performing. Some of the most important stats include: hitting percentage, aces, digs, blocks, errors, and kills.
#But which of these stats actually best determines a winning team from a losing one?
#This project aims to answer that question using real professional match data.

#---DATA---
#Data comes from BigTimeStats/beach-volleyball GitHub repository and includes 85,509 real AVP and FIVB beach volleyball matches dating back to the year 2000.
#It includes match results, player info, and detailed box score stats.
#However, compared to the 85,509 matches displayed, only about 15,000 display important box score stats(kills, digs, blocks, aces, hitting percentage, and errors).
#The analysis is only built on the matches with complete stats because that is the subset that can be used to answer the question.

#---METHODOLOGY---
#Matches were kept only if hitting percentage and errors were recorded for all four players. Additionally, matches with immpossible hitting percentages were removed. This left about 15,000 matches with complete data across all stats used in this analysis.
#Beach volleyball is played in 2-player teams, and the raw data records each player's stats separately. To measure team performance as opposed to individual performance, each pair of stats were averaged together into one team number per match, per stat.
#Refining this from an earlier version of the project that treated each teammate as a separate data point strengthened the correlation found between each stat.
#For each stat, winning teams were compared against losing teams in three ways:
#Average difference - how much higher/lower is the stat for winners vs losers?
#Statistical significance - is the difference large enough that it's unlikely to be due to random chance? 
#Correlation - how strongly does the stat relate to winning, on a scale of -1 to 1

#--RESULTS---
#Stat | Winner Avg | Loser Avg | Correlation with Winning
#Hitting % | 0.474 | 0.310 | 0.555
#Errors | 2.92 | 4.36 | -0.385
#Blocks | 1.73 | 1.06 | 0.306
#Kills | 14.78 | 12.70 | 0.285
#Aces | 1.33 | 0.82 | 0.269
#Digs | 8.43 | 7.15 | 0.177

#Each stat showed a statistically significant difference between winners and losers with extremely low p-values for each stat (confirmed by independent t-tests).

#---CONCLUSION---
#Hitting percentage is the strongest predictor of winning a beach volleyball match.
#Hitting percentage is a calculated average measured by Kills-Errors/Attempts.
#This, combined with errors being the second strongest factor (correlated negatively, less errors = winning). This suggests that efficiency or how well a team converts attacking opportunities into kills while keeping errors low is more important than other stats such as kills, digs, and blocks, and therefore most influences winning.
#Blocks, kills, and aces still show a positive relationship with winning although it is less dramatic than errors and hitting percentage.
#Digs, while still positively correlated, are the weakest predictor suggesting that defensive recovery matters less to the final outcome of the match as opposed to offensive efficiency and consistency.

#---TECH-USED---
#Python, Pandas (data loading, cleaning, aggregation)
#scipy.stats (significance testing)
#matplotlib (visualization)

#---HOW TO RUN---
#pip install pandas matplotlib scipy
#python3 analyze.py

#---FUTURE WORK---
#This project currently measures association between stats and winning, but does not possess the capabilities to make predictions.
#A natural next step other than making the code itself more efficient would be to build a machine learning classification model that predicts match winners/loser based on team stats.