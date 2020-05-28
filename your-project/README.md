<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# ML Growth Hacking
*Francesco Baldissera*

*DAFT, Barcelona. March-2020*

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
Introduction
One of the major innovations in the digital marketing industry is optimizing your processes by using different machine learning algorithms to feed your marketing intelligence.

This tools could be crucial to truly hack your growth and boost the efficiency of your sales team. The main objectives of this paper are to use both unsupervised as unsupervised machine learning algorithm to first do a customer segmentation over CRM data and then try to predict customers subscribing/buying/registaring to a product/service.

This is intended as a framework to apply for fueling market intelligence in any given customer oriented company.

## Hypotheses / Questions:
The paper main objectives are divided as such:

Campaign Marketing Customer Segmentation: Using K-means unsupervised learning algorithm to stretch the RFM growth market model and clusterize clients according to those three criterions.

Predictions: Using supervised learning to predict if a customer will subscribe a term deposit

## Dataset
### Where did I get the data? 

I gathered it from [Machine Learning UCI Repository](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II) I loaded the data as a CSV file to the repository in the directory 'data'. Loaded it to JupyterNotebook using the 'load_csv' function of the Pandas library.


### Data structure
#### Data Set Information:

The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed.


## Cleaning
Data was pretty clena althought I decided to drop some columns that didn't make much sense to have for predicting the desired outcome.

## Analysis
* Exploratory Data Analysis. Distribution of features and target.
* K-Means clustering using the elbow method and strategic marketing approach. Analyzed the "area under the curve" for the ROC graph.
* Logistic Regression for the two types of features, discovered that for categorical features the DecissionTree algorithm works better.

## Model Training and Evaluation
* Data splitted 80% train and 20% test for Logistic Regression and 95% train 5% test for DT.
* Accuracy 89% for LR and 88% for DT

## Conclusion
* Data Analysis and its structure is key to perform good GrowthHacking tactics. Its a starting point where marketers should always formulate hypothesis, test and optimize.

## Future Work
* Perform A/B test on future campaigns 
* Deploy the algorithms to perform real time classification and predictions

## Workflow
* Data Gathering
* EDA
* Built machine learning algorithms
* K-means using the Elbow Method
* Tested them using sklearn performance statistics

## Organization
* Kanban board on Trello
* Jupyter Notebook paper

## Links
[Repository](https://github.com/franbaldi/Project-Week-8-Final-Project)  
[Slides](https://drive.google.com/file/d/17oQQpQeBTHpaNoRUJ1cSfKRy0ENxQAMZ/view?usp=sharing)  
[Trello](https://trello.com/invite/b/9HgRmLlo/b4ab49219ae21ae052c2c83dd935372b/final-project-data-fueling-growth)  
