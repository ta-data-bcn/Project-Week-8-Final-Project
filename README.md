<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Predicting Job Salaries
*Aitor Quinza*

*[Data, Barcelona & March 2020]*

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
This project aims to help people on interviews, helping them to say a salary range.

## Hypotheses / Questions
* Affects the salary depending on the state?
* Affects the salary the company industry?
* Can We predict the salary based on job title, geography and required skills?


## Dataset
* For this project, I scraped GlassDoor website because in EEUU they have in some offers a salary range estimation and I'm going to work with this estimation to make my own.
* The script is in the folder scripts/glassdoor.py

## Cleaning
*	Parsed numeric data out of salary 
*	Removed rows without salary 
*	Made columns for employer provided salary and hourly wages 
*	Made columns for if different skills were listed in the job description:
    * Python  
    * R  
    * Excel  
    * AWS  
    * Spark 
    * SQL
    * Tableau
*	Parsed rating out of company text 
*	Made a new column for company state 
*	Added a column for if the job was at the company’s headquarters 
*	Transformed founded date into age of company 
*	Column for simplified job title and Seniority 
*	Column for description length 


## Analysis
* Overview the general steps you went through to analyze your data in order to test your hypothesis.
* Document each step of your data exploration and analysis.
* Include charts to demonstrate the effect of your work.
* If you used Machine Learning in your final project, describe your feature selection process.

## Model Training and Evaluation
*Include this section only if you chose to include ML in your project.*
* Describe how you trained your model, the results you obtained, and how you evaluated those results.

## Conclusion
* Summarize your results. What do they mean?
* What can you say about your hypotheses?
* Interpret your findings in terms of the questions you try to answer.

## Future Work
Address any questions you were unable to answer, or any next steps or future extensions to your project.

## Workflow
Outline the workflow you used in your project. What were the steps?
How did you test the accuracy of your analysis and/or machine learning algorithm?

## Organization
How did you organize your work? Did you use any tools like a trello or kanban board?

What does your repository look like? Explain your folder and file structure.

## Links
Include links to your repository, slides and trello/kanban board. Feel free to include any other links associated with your project.


[Repository](https://github.com/aitorquinza/Project-Week-8-Final-Project/)  
[Slides](https://docs.google.com/presentation/d/1lD6bA32RghmyEhmh5p3Ni35dZikB0xhQMjr6udIGW9w/edit?usp=sharing)  
[Kanban](https://github.com/aitorquinza/Project-Week-8-Final-Project/projects/1)  
