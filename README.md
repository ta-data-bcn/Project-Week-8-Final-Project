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
- [Future Work](#future-work)
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
Visit my [Tableau Graphs](https://public.tableau.com/profile/aitor2544#!/vizhome/DataScienceJobEEUU/Story1)

## Model Training and Evaluation
I used 3 Algorithms:
* Multivariable Linear Regression
* Lasso Regression
* Random FOrest



## Future Work
* Test SVM algorithm
* Improve skills extraction
* Add more keywords for jobs


## Organization
The structure has 3 folders:
* Datasets -> CSV files
* Notebooks -> Data cleaning, EDA and model building
* Scripts -> Python scripts for scraping and save the the model

## Links

[Repository](https://github.com/aitorquinza/Project-Week-8-Final-Project/)  
[Slides](https://docs.google.com/presentation/d/1lD6bA32RghmyEhmh5p3Ni35dZikB0xhQMjr6udIGW9w/edit?usp=sharing)  
[Kanban](https://github.com/aitorquinza/Project-Week-8-Final-Project/projects/1)  
