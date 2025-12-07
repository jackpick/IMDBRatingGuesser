# IMDBRatingGuesser
A program that predicts a film's IMDB rating, based on the types of words and number of tokens in its script


This project can be split into 2 sections:

1 - Data Collection
The MAT (Multidimensional Analysis Tagger - download linked below) by Andrea Nini was used on a number of film scripts found on the internet (that came with each film's IMDB title code) to tag each word in each film script. These tags were then counted and this data was combined with their film rating, gained by web scraping IMDB with the program IMDBRatingGetter. The result of this can be seen in the CSV file "Statistics_MAT_raw_texts.csv".

2 - Data Analysis
A multiple regression model was then created with the program IMDBRatingGuesser. This can be used to predict other film's ratings by also putting their script through Andrea Nini's MAT (an example script and tag count can be found in the repository for the 2024 Deadpool/Wolverine film). However, it isn't overly accurate - it's R-squared value being only 0.0789.

MAT download: https://sites.google.com/site/multidimensionaltagger
