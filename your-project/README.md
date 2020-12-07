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

* The business application could be to develop an app to help the teachers know the fortes and train on the weak points regarding to data.

## Dataset
* The dataset was downloaded from a Kaggle file (https://www.kaggle.com/ali2020armor/taekwondo-techniques-classification).
* For all types of datasets, provide a description of the size, complexity, and data types included in your dataset, as well as a schema of the tables if necessary.
* There are two CSV files in the dataset:
- The first one describes the six participants of the readings. 
- The second, and largest one, contains the readings. There are 115 columns, each for one reading. Each participant had 5 trials on 4 different kind of strikes: Round kick, Back kick, Cut kick and Punch. The sixth participant was the only one not to perform the trials for the Back kick.
* If the question cannot be answered with the available data, why not? What data would you need to answer it better?

## Cleaning

The first thing I noticed is that there is not a transformation from the reading to any known scale. We can not extrapolate into any kind of energy output. We then can only evaluate the data in between itself.
Also, the data had not the same length on every reading. I deduced it responded to the fact that the timeframes were not standardized.
This meant I had to cut the non-numerical data out. Then I had to clear the offset (usually on 1026) and reduce the noise.
The only interesting part of the data was concentrated around the moment of the impact. In order to have representative data, this meant centering on it. I decided to take a window of 80ms where the impact would be on 30ms. This reduced the data from 4000+ rows to 80 rows.
Finally, knowing when the impact happened, it was easy to extract the peak moment and arrange it for different kind of visualizations.

## Analysis
* Except for the round kick of P2, or P4's punch, every strike follows a clear progression line related to the age/weight/experience of the participant.

## Conclusion
* We can observe the strongest strike is the back kick, but it needs more technique and only the more experienced participants are able to perform it. It would have been interesting to see what P6 would have scored.
* The students don't seem to have a "best" strike. Some have a peak, but, for most of the strikes, they stay around their own mean.
* Unfortunately, there was not enough data to corroborate the hypothesis.

## Future Work
I would love to be able to have more consistent data, as in values more around a mean for each kind of strike and participant to see if the intensity can really depend on weight and/or experience.

## Workflow
The workflow started with cleaning the data so it could become readable and comparable to the other inputs. Then, it was possible to gather information and make questions/hypotheses.

## Organization
As I was discovering what to do with the data, I could not rely on a Trello board to organize my work.

My repository consists on the main Jupyter Notebook file, and two different folders: one containing the dowloaded data and the cleaned data; the other with the figures obtained for the analysis.

## Links
[Repository](https://github.com/Octavifdez/Project-Week-8-Final-Project/tree/master/your-project)  
[Slides](https://slides.com/octavifernandez/analysis-of-tae-kwon-do-strikes/fullscreen)  
