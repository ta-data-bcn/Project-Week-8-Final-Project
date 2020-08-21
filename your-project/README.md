<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Woodoc: the plant disease identifier
*Mireia Guinovart*

*[0620, Iornahck-Barcelona & August 2020]*

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

Have you ever had a plant that was dying and you had no clue why? This project pretends to put an end to that by creating an image recognition model that will not only tell you what the problem is but that it will also tell you the solution. Welcome to the modern era!

## Hypotheses / Questions
My main questions were the following:
* Why is my plant dying? which illness does it have? how do I treat it?
I did not have hypotheses for this project since it was primarely dedicated to a visual identification model that could predict whether the plant was sick and of what. Ideally it would also give you a simple, straight forward solution with simple non technical vocabulary and easy to apply at home.
The motivation for the project was the lack of apps that can actually tell you what is wrong and provide help that is useful.



## Dataset

The initial idea was to create a dataset of my own but due to time restrictions an alreeady available dataset had to be used.
The data set used is the created by Hughes and Salathé (2015) in order to precisely enable mobile disease diagnostics that can be fully download on https://data.mendeley.com/datasets/tywbtsjrjv/1 or partially download on https://github.com/spMohanty/PlantVillage-Dataset

* For all types of datasets, provide a description of the size, complexity, and data types included in your dataset, as well as a schema of the tables if necessary.
The Plant village dataset is available with and without data augmentation and it contains information about 14 crop species from which only 9 (those that also had information about the diseased plant) were used. Each species and condition (eg: healthy, black rot or mildery powder) were placed in a folder and would contain at least 1000 pictures (.jpg) if not more. Data was distributed in alternative folders so it would be separate between the data required for the train set (around 77 %), for the validation (around 15 %) and for the test (around 8 %). Therefore, the data structure that I had was the following:

<img src="https://github.com/mg365/Project-Week-8-Final-Project/blob/master/images/folder%20structure.png" alt="Folder structure" width="500"/>

Although the dataset was large enough to perfom the convolutional neural network models, the images were not varied enough (they all followed the same structure) or had the best image quality (some were blurred) and so, it would be prefered to redo the dataset oneself.

## Cleaning
Data cleaning consisted in data renaming and reformating to be able to get analised by the neural network model. It consisted in renaming the images and the folders as well as to order them using the appropiate structure and altering to pass them through the model.

## Analysis

* If you used Machine Learning in your final project, describe your feature selection process.

## Model Training and Evaluation
*Include this section only if you chose to include ML in your project.*
* Describe how you trained your model, the results you obtained, and how you evaluated those results.

## Conclusion
* Summarize your results. What do they mean?
* What can you say about your hypotheses?
* Interpret your findings in terms of the questions you try to answer.

## Future Work
The model needs to be retrained with more varied images and of typical household species so it is useful. Moreover, in order to be user-friendly, it needs a user interface that allows people to actually use it.

## Workflow
The steps that I followed were:
- find dataset
- rename dataset
- structure dataset
- preprocess data set
- create VGG16 altered model
- fit the model to my data
- check accuracy
- test the model

Accuracy was tested using pictures not included in the modelling and also images available in google.

## Organization
The work structure was initially and also later designed in an analogic way in order to describe the idea, the model, the user interface, the presentation and the article.

What does your repository look like? Explain your folder and file structure.
The repository is structure in two main folders one that includes all the jupyter notebooks with the code used to perform the data preprocessing and the models and another with images necessary for the readme explanation and so on.

## References
- Hughes, D., & Salathé, M. (2015). An open access repository of images on plant health to enable the development of mobile disease diagnostics. arXiv preprint arXiv:1511.08060.

## Links
Include links to your repository, slides and trello/kanban board. Feel free to include any other links associated with your project.


[Repository](https://github.com/mg365/Project-Week-8-Final-Project)  
[Slides](https://docs.google.com/presentation/d/1a7bX3XEloPRaH4IqMNVdVLKxmUGP6gqi2twcYJcHhoE/edit#slide=id.g919713cf3c_0_623)  

