<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# TESLA Stock Projection - Based on Car Production, Stock & Twitter Analysis
*[Robin Langlois]*

*[DAFT BARCELONA - Jan-Mar 2020]*

## Content
- [Project Description](#project-description)
- [Hypotheses / Questions](#hypotheses-questions)
- [Dataset](#dataset)
- [Cleaning](#cleaning)
- [Analysis](#analysis)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [Conclusion](#conclusion)
- [Future Work](#future-work)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
This project aims at analyzing Tesla stock evolution from 2010 onwards (IPO on January 2010).
The project has 3 chapters analyzing the evolution of the stock on 3 metrics :
- Elon Musk's past tweets habits and how they may have had a strong impact on Tesla's stock value
- Tesla car production history and future previsions on its stock evolution
- General trends of stocks & competitors from 2010 onwards

## Hypotheses / Questions
* What data/business/research/personal question you would like to answer?

* My original project was to measure the impact of past Musk tweets, especially from 2018 onwards, to measure their impact on the actual stock value :
	* Do the stock markets react strongly to Musk tweets ?
	* Does Musk influence greatly the stock prices when tweeting - general or Tesla related - information ?
	* Do his Twitter controversies harm badly Tesla's stock evolution ?

* To measure various potential influences over the stock price evolution, other KPIs were taken into account :
	* Car production history from 2010 onwards
	* general stock market environment evolution

* What is the context for the question and the possible scientific or business application?

* What are the hypotheses you would like to test in order to answer your question?  
Frame your hypothesis with statistical/data languages (i.e. define Null and Alternative Hypothesis). You can use formulas if you want but that is not required.

## Dataset
Each Dataset creation & its scraping are detailed in their respective Notebooks.

I used 3 distinct datasets to measure my various metrics :
- Musk's Twitter database from Twitter scraping - based on [GetOldTweet3 Python script]('https://github.com/Jefferson-Henrique/GetOldTweets-python')	
	* 8797 tweets gathered - 1 row per tweet - 8 columns :
														date
														text
														retweets
														replies
														favorites
														tweet_interactions
														permalink
														to
														hashtags
														mentions

	* Divided into 4 datasets :
		- general topic unique tweets (8797 tweets) & groupby days
		- Tesla related tweets (1100 tweets) & groupby days

- Tesla car history sales, based on scraping (Pandas function pd.read_html) & download of existing datasets (Kaggle & DataWorld)

- Stocks database for several Tech & Car companies from web data scraping  based on web.DataReader scraping of Yahoo Finance! data
	* dataset for each company - 7 columns from scraping :
								High (highest price of the day)
								Low (lowest price of the day)
								Open (Opening price)
								Close (Closing price)
								Volume (Volume of stock sold a day)
								Adj Close (Adjusted Closing price)
								avg_price (Average price of the day)

	* Car stock values merged into one Car Company dataset
	* Tech stock values merged into one Tech company dataset

## Cleaning
Describe your full process of data wrangling and cleaning. Document why you chose to fill missing values, extract outliers, or create the variables you did as well as your reasoning behind the process.

### Custom variable created #### 

###Twitter analysis
#### Twitter interactions #### 
	sum of all interactions over a tweet (retweets, replies, favourites) - asumption that tweet generating an important amount of interactions convey important piece of information (business related, funny original content, controversies etc. )

## Analysis
* Overview the general steps you went through to analyze your data in order to test your hypothesis.
* Document each step of your data exploration and analysis.
* Include charts to demonstrate the effect of your work.
* If you used Machine Learning in your final project, describe your feature selection process.

## Model Training and Evaluation
Stock prediction based on [Facebook Prophet]('https://facebook.github.io/prophet/docs/saturating_forecasts.html#forecasting-growth') growth prediction model . 
cf. two detailed articles on Medium used during the research phase: 
	- [Using Facebook’s Prophet to Predict Mongolian Stocks]('https://medium.com/mongolian-data-stories/using-facebooks-prophet-to-predict-mongolian-stocks-cdf4feabd558')
	- [Forecasting Stock Prices using Prophet]('https://towardsdatascience.com/forecasting-stock-prices-using-prophet-652b31fb564e'))

#### 2 Prediction Models developed ####
To compare Prophet predictions, two Models based on different datasets have been developed :
	 * Evolution of Car production VS. Stock price for 2020-2022
	 * Evolution of Stock price for 2020-2022 based on previous values


- Stock Price Model Training & Evaluation based on 2010-2018 stock value to compare them with actual results from 2019-2020
	* overall growth trend well predicted, even if Tesla last year very important spike in stock value has not been predicted. May be considered an anomaly and is rather hard to predict

## Conclusion
* Summarize your results. What do they mean?
* What can you say about your hypotheses?
* Interpret your findings in terms of the questions you try to answer.

## Future Work
Address any questions you were unable to answer, or any next steps or future extensions to your project.

## Workflow
My workflow consisted on working sucessively on my 3 chapters to measure, for each part, the correlation and the potential impact on the stock.
Each Workflow is detailed in its respective Notebooks.

1 - the stock evolution analysis was the most straighforward : clear & efficent data scraper to gather all needed data. I  gather the data from a range of Tech & Car making companies, to then compare them to Tesla stock.
Applying same methodology for each financial sets : gathering data, grouping together, measuring the correlation)

2 - car making history : collecting & cleaning the data took some time, due to the various range of data structure I gathered. Important phase of datawrangling in order to create a clean dataset of the history of car from 2010 onwards.
I then plot the evolution of car making to Tesla's stock evolution to measure correlation.
Finally I applied Facebook Prophet to create car making prediction for a 2-year period/

3 - 

## Organization
How did you organize your work? Did you use any tools like a trello or kanban board?

What does your repository look like? Explain your folder and file structure.

## Links
[Repository](https://github.com/Binardino/Project-Week-8-Final-Project)  
[Slides](https://slides.com/)  
[Trello](https://trello.com/b/QR7DdjqV/tslafinaleproject)  
