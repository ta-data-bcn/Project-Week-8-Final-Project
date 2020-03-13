<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Size & Intelligence in Dogs
*Santiago Mougán*

*Data Analytics (BCN - 01/20)*

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
Analysis and observations on size, mass and intelligence relationships on dogs, and exploration of prediction possibilities between this parameters.

## Hypotheses / Questions
* Is there a connection between physical features and intelligence?
* Can intelligence be predicted from physical features?

## Dataset
* Dataset on dog breeds and intelligence measurements from task competences from data.world.
* Dataset on dog breeds related to height and weight from data.world.
* Dataset with the info from the two main tables combined and clean.

## Cleaning
* The numerical measurements were actually strings, that had to be converted to integers. Also some non numerical characters had to be fixed.
* Height and weight data were presented in pairs (minimun and maximum for each breed), so I converted them to unique (mean) values to ease the analysis.
* Since height and weight data corresponded to specific breeds, the NaNs could be easily investigated and fixed one by one.
* A few outlyiers were actually mistakes (e.g. weight value in the place of the height value), but again, easy to investigate and fix.
* There were NaNs on intelligence measurementes with complete and good data about the tasks response, so it could be assigned to their correct measurements instead of deleted.
* With the intelligence measurements fixed, there is no need for the details about tasks.
* Once height, weight and intelligence classification are related and fixed, there is no need for the breed label.

## Analysis
* First analysis with plotting of all parameters, getting an obvious relationship between height and weight.
* Further analysis through observation of both physical parameters versus intelligence measurements.
![Height&Weight vs Intelligence categories](https://raw.githubusercontent.com/Yaguit/Project-Week-8-Final-Project/master/your-project/HW-I.PNG)
* The machine learning work was through clustering, since there are six defined intelligence groups.

## Model Training and Evaluation
All the data was clustered in six main groups, corresponding to the six intelligence categories. From this a function can be made to input new data on height and weight and get the corresponding intelligence level in return.

## Conclusion
* Relationship between intelligence and height and weight is not obvious to the human eye.
* The hypothesis of their relation should be discarded.
* More information about other physical features may rescue a modified version of the hypothesis.

## Future Work
The relationship between height, weight and intelligence is not clear, so further investigation should be done to determine if phsysical differences and similarities between breeds are related to ther intelligence differences and similarities.

## Workflow
* Looking for topics and general ideas
* I started growing interest in relationship between physical and mental features
* Finding the data on dog intelligence and physical measurements
* Once started the coding, ohter ideas were found and tested 

## Organization
Trello:
* List of general brainstorm ideas
* To do list
* Tasks in progress
* Tasks already done
Github repository:
* Original datasets on .csv format
* Jupyter notebook file with all the coding
* Graph example image
* ReadMe

## Links

[Repository](https://github.com/Yaguit/Project-Week-8-Final-Project)  
[Slides](https://slides.com/srmg/size-intelligence/#/)  
[Trello](https://trello.com/b/PCUuBxi8/final-project)  
