# Analysis of Heart Disease Diagnosis #

Zak Abou Merieme

[DAFT, Barcelona Jan 2020]

## Content ##

* [Project Description](#Project-Description "Goto Project-Description")
* [Questions](#Questions "Goto Questions")
* [Dataset](#Dataset "Goto Dataset")
* [Cleaning](#Cleaning "Goto Cleaning")
* [Analysis](#Analysis "Goto Analysis")
* [Model Training and Evaluation](#Model-Training-and-Evaluation "Goto Model-Training-and-Evaluation")
* [Conclusions](#Conclusions "Goto Conclusions")
* [Future Work](#Future-Work "Goto Future-Work")
* [Workflow](#Workflow "Goto Workflow")
* [Repo structure](#Repo-structure "Goto Repo-structure")
* [Links](#Links "Goto Links")


## Project Description ##

The idea behind this project is to analyse the Heart Disease UCI dataset, find insights about people diagnosed with heart disease, and train a machine learning model to predict the diagnosis.

to achieve that, the breakdown of the project goes as described below:

 * Data cleaning: A deepdive into the dataset, and get it ready for EDA
 * Exploratory Data Analysis (EDA): Aims to appraoch the data from both a qualitative and a quantitative approach for main insights
 * Diagnose prediction using Machine Learning: A look into the different algorithms to predict the diagnosis, and choose the best one (hightest accuracy)
 

## Questions ##

1. describe the features in this dataset.

2. What are the features that most correlate to having a heart disease? 

3. What features (simptoms) can help with diagnosis of a heart disease?

4. What is the best algorithm to predict the diagnosis


## Dataset ##

The dataset is acquired online through the use of [Kaggle](https://www.kaggle.com/ronitf/heart-disease-uci "Kaggle")

Which, can also be found in [UCI](https://archive.ics.uci.edu/ml/datasets/Heart+Disease "UCI") website


## Cleaning ##

The cleaning process starts off with having a look at the data types and records available in the dataset.

The dataset was very clean, no missing values at all


## Analysis ##

Exploratory Data Analysis refers to the critical process of performing initial investigations on data so as to discover patterns,to spot anomalies,to test hypothesis and to check assumptions with the help of summary statistics and graphical representations.

Here we aim to apply EDA to:

Maximize insight into a data set;
Uncover underlying structure;
Extract important variables;
Detect outliers and anomalies;
Test underlying assumptions

link to [EDA](http://www.google.fr/ "EDA") notebook

## Model Training and Evaluation ##

Once we are done with the EDA, we gonna try several methods of Machine Learning to see which model is the most accurate.

link to the Machine Learning notebook

as the results were not as expected, let's scale our data and try again

link to the Scaled data Machine Learning notebook

## Conclusions ##

It's hard to diagnose heart disease just by common knowledge of medicine, in fact having an anginal chest pain is negatively correllated, which means people that have never experienced this pain are prune to have a heart disease.
Regarding Cholesterol, people with heart disease diagnose have overall lower cholesterol than people without heart disease.
And a downsloping in the ST segment depression test does correlate, it is an indicator of having a heart disease.

In order to have a machine learning model trained to predict new data, the algorithm with highest accuracy was the Random Forest Regressor (max depth of 6) which achived 83% accuracy.
Although this result can be improved by scaling the data first, then applying the previous algorithm we reach 88% accuracy, which is quite high, and special mention to the SVM algorithm that reached 84% accuracy.


## Future Work ##

Next step is to try neural network, although the amount of data is low (only 300 rows) 


## Workflow ##

First of all, was to get a dataset with a target (0 or 1) to which I could apply several processes, to name some:

  * Data Cleaning
  * Data Analysis
  * Scaling
  * Machine learning

Heart Disease is one of the major concerns for society today, after searching for a suitable dataset on the internet, I found this dataset on [Kaggle](https://www.kaggle.com/ronitf/heart-disease-uci "Kaggle")

Then what's explained in this file was applied

## Repo structure ##

My repo has the following folders and structure:

code:
* EDA.ipynb
* Machine Learning.ipynb
* Scaling.ipynb

datasets:
* heart.csv (original dataset from kaggle)

This README file

.gitignore file

## Links ##

[Repository](https://github.com/Zak-ScorpiuS/Project-Week-8-Final-Project)  
[Presentation](https://docs.google.com/presentation/d/160yekMr4LnS_HnE-x0Hdr0Vmo_vUbpn95FNOjZfQ5RY/edit?usp=sharing)  
