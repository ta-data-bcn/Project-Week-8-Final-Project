<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Title of My Project
*Victoria Zauner*

*DAFT BCN 03/20]*

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
Out of personal interest for the topic, I chose to work on determining personality types according to the Myer-Briggs-Type-Indicator Theory from the text of comments on Social Media. I applied two different approaches to the problem: First I used the NLTK library to determine the personality types with Natural Language Processing, second I tried a quantitative approach by taking factors into account with include: the average length of a comment, the variance in length per comment, the average number of links used, the average number of questionmarks used, the average number of excalamtion marks used, the average number of dots used, the the average number of hashtags used and the average number of the words "me", "myself" or "I" used per comment. A variety of Algorithms was tested to maximize accuracy. In the end, the best model was tested on real life data. 

## Hypotheses / Questions
* Can the personality type of a person be determined merely by the language they use when posting on social media?
* In what ways can the ability of this determination or even of singular traits be useful for HR, Consulting and team building purposes?
* What are the highly correlated properties/features/words of posts with personality types/traits?
* What are the main indicators to determine the personality traits of a person?

## Dataset

[Dataset](https://www.kaggle.com/datasnaek/mbti-type?select=mbti_1.csv)  

* The data was retreived publicly from Kaggle.
* The original table contained 8675 clean rows with two columns: The personality Type classified with the four letter indicator frame and the text from 50 comments of the same person.
* From this data, I extracted quantitative characteristics for the second part of my analysis.
* To retreive the real life test data I chose not to scrape Instagram but to build the Dataframe manually due to the network's protection.
* To improve the success of the model, data retrieved particularly from the network it would be applied to later to accurately regard the vibe of the context reflected in the tone of the posts would have been very helpful. Also interesting insights could be gained with further in depth analysis of images matching the text and general activity and behavior in form of dates, comments, likes, follows, followers, fluctuations etc. 

## Cleaning
* For the natural language processing I cleaned the Data using regular expressions and the nltk library to apply the PorterStemmer, lemmatize and remove stopwords from the text.
* For the quantitative data I used string operations to extend the dataframe by the features desired. 
* In both cases the target in form of the 4 letter indicator was seperated in order to allow dicisions and determinations by 2 each and not by 16.

## Analysis

Description is in the [Workflow](#workflow).

## Model Training and Evaluation

Description is in the [Workflow](#workflow).

## Conclusion

* Personality Types and traits can be roughly determined by language only.
* The accuracy can still be improved and would significantly profit from the model being trained on the same network as it is being used on.
* The model could be used on profiles of companies, on the character of their social media marketing as well as on the companies followers to determine buyer personas, which would allow adapting and consequently improving successful marketing.
* According to experience and by analysing the personality type of current employees and their performance and the way they flourish in the company culture can allow HR departments to detemrine a new employee's desired personality type.

## Future Work

Adding furter data would help to make the model more universally applicable: Images, body language, behavior on the platform would certainly be of interest. Also the model could be further improved by finding and cleaning misleading words.

## Workflow

1. After initial alaysis of the data (Code 1), I cleaned and modified the dataframe to prepare it for NLP (Code 2).

2. In the following step I vectorized the text using the Count Vectorizer for feature extraction and I tried a variety of algorithms on the data including Multinomial Naive Bayes, the Decision Tree and K-Nearest Neighbor. In this case the Decision Tree Algorithm gave me the hightest overall accuracy of 49% for determining one of the 16 personalities correctly. (Code 2)

3. Next, I decided to split the target into the four traits concluding the personality type in order to be able to make a decision between two options each rather than 16 at the same time. (Code 3)

Following this I tried a variety of algorithms on the four traits seperately including Multinomial Naive Bayes, the Decision Tree, K-Nearest Neighbor and Random Forests. 

4. At first, I looked for the best performing algorithm for every trait and pieced a model together accordingly. (Code 4):
IE: K-Nearest Neighbors
NS: Random Forests
TF: Multinomial Naive Bayes
JP: Multinomial Naive Bayes

5. In order to inrease accuracy I used PCA on the features extracted by the vectorizer and also used MinMaxScaler to scale the reduced features.
Additionally, I tested every algorithm on different parameters (n_neighbors, max_depth etc.) to insure optimized modelling. After this process, I decided to use the Random Forest Model on the fully reduced and scales training data to maximize accuracy. 

6. Parallel to this process, I was working on my extended dataframe, which featured quatitative characteristics of the posts such as the average length of a comment, the variance in length per comment, the average number of links used, the average number of questionmarks used, the average number of excalamtion marks used, the average number of dots used, the the average number of hashtags used and the average number of the words "me", "myself" or "I" used per comment and inspected the data for correlations with the personality types. (Code 4)

7. In the following step I created a Neural Network Model for the Quantitative Data which resulted in decent accuracy for two of the four traits, IE and JP. (Code 5)

8. When trying the other algorithms on the quantitative data, the Random Forests and Multinomial Naive Bayes Models performed best but not significantly better - if even - than when run on NLP. (Code 8)

9. To test the model on real life data, I asked friends for permission to let me analyse their posts on Instagram and to take the test [online](https://www.16personalities.com) and retrieved a dataframe from it which I tested my algorithms on. (Code 7)

10. In the Jupyter Notbook file Code 9 I started building an Instagram scraper, that should retreive verbal captions form people's profile, process the text, feed it to the model and return the user's personality type. It is still in progress.


## Organization

I used a Trello Board to keep an overview of pending tasks and kept notes on paper.

My repository is organized in two folders: data and code. 

*Data*
* The remote Repo does not contain the larger files, those can be found zipped in my [Google Drive](https://drive.google.com/drive/u/1/my-drive).
* The file quant_personalities.csv holds the dataframe with the quantitative measures I created.
* The file reallife_data_insta.csv includes the caption of the friends that allowed me to use them.


*Code*

Includes the 9 Jupyter Notbooks mentioned above.

Also you find the saved model (Random Forests for each of the four Personality Features on the reduced and scaled nlp data)


## Links

[Repository](https://github.com/VickyZauner/Project-Week-8-Final-Project)  
[Slides](https://docs.google.com/presentation/d/10Yu48XyE_rS521vREW13zlOzsgoRrV4sjKo4MVCjjs0/edit#slide=id.g85e9335f2e_0_70)  
[Trello](https://trello.com/b/b9H0SKTx/project-5)  
