<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Title of My Project
*[Octavi Fernández]*

*[Data Analysis, Barcelona & March 2020]*

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
The project is an analysis of the data on the impact of different techniques from Tae-Kwon-Do students into an ADC sensor (Analog to Digital Converter).
I chose this project because I was looking for data on this martial art, as I am a practicioner myself too.
My goal was to deliver some insights about the data found by cleaning and ordering the different readings of the 115 strikes.

## Hypotheses / Questions
* What data/business/research/personal question you would like to answer?
* I would like to know if there is a correlation between the weight and experience of the students to the intensity of the impact delivered.
* Is the intensity difference between the strikes related to the experience?
* Is there any kind of consistency on the different students? Do they strike with the same intensity for every technique?
* What is the context for the question and the possible scientific or business application?
* The business application could be to develop an app to help the teachers know the fortes and train on the weak points regarding to data.
* What are the hypotheses you would like to test in order to answer your question?  
Frame your hypothesis with statistical/data languages (i.e. define Null and Alternative Hypothesis). You can use formulas if you want but that is not required.

## Dataset
* The dataset was downloaded from a Kaggle file (https://www.kaggle.com/ali2020armor/taekwondo-techniques-classification).
* For all types of datasets, provide a description of the size, complexity, and data types included in your dataset, as well as a schema of the tables if necessary.
* There are two CSV files in the dataset:
- The first one describes the six participants of the readings. 
- The second, and largest one, contains the readings. There are 115 columns, each for one reading. Each participant had 5 trials on 4 different kind of strikes: Round kick, Back kick, Cut kick and Punch. The sixth participant was the only one not to perform the trials for the Back kick.
* If the question cannot be answered with the available data, why not? What data would you need to answer it better?

## Cleaning
Describe your full process of data wrangling and cleaning. Document why you chose to fill missing values, extract outliers, or create the variables you did as well as your reasoning behind the process.

The first thing I noticed is that there is not a transformation from the reading to any known scale. We can not extrapolate into any kind of energy output. We then can only evaluate the data in between itself.
Also, the data had not the same length on every reading. I deduced it responded to the fact that the timeframes were not standardized.
This meant I had to cut the non-numerical data out. Then I had to clear the offset (usually on 1026) and reduce the noise.
The only interesting part of the data was concentrated around the moment of the impact. In order to have representative data, this meant centering on it. I decided to take a window of 80ms where the impact would be on 30ms. This reduced the data from 4000+ rows to 80 rows.
Finally, knowing when the impact happened, it was easy to extract the peak moment and arrange it for different kind of visualizations.


## Analysis
* Overview the general steps you went through to analyze your data in order to test your hypothesis.
* Document each step of your data exploration and analysis.
* Include charts to demonstrate the effect of your work.
* If you used Machine Learning in your final project, describe your feature selection process.


## Conclusion
* Summarize your results. What do they mean?
* What can you say about your hypotheses?
* Interpret your findings in terms of the questions you try to answer.

## Future Work
I would love to be able to have more consistent data, as in values more around a mean for each kind of strike and participant to see if the intensity can really depend on weight and/or experience.

## Workflow
Outline the workflow you used in your project. What were the steps?
How did you test the accuracy of your analysis and/or machine learning algorithm?

## Organization
As I was discovering what to do with the data, I could not rely on a Trello board to organize my work.

My repository consists on the main Jupyter Notebook file, and two different folders: one containing the dowloaded data and the cleaned data; the other with the figures obtained for the analysis.

## Links
Include links to your repository, slides and trello/kanban board. Feel free to include any other links associated with your project.


[Repository](https://github.com/Octavifdez/Project-Week-8-Final-Project/tree/master/your-project)  
[Slides](https://slides.com/octavifernandez/analysis-of-tae-kwon-do-strikes/fullscreen)  
