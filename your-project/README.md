<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Title of My Project
*[Gareth Hughes]*

*[Data Analytics, Barcelona,  May 2020]*

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
In this project, my main objective is to train, test and apply a convolutional neural network which can be 
applied to the detection of pneumonia, and COVID-19 induced pneumonia, using image classification. This would be 
achieved by analysing computerized tomography (CT) scans from an anteroposterior (AP) perspective of the lungs.
Ultimately, the aim of the project would be to develop a means of rapidly analysing Pneumonia, thereby saving time
and offering radiologists and doctors a second opinion.
The two datasets were obtained from Kaggle and the other from Github, they are referenced below. The first 
dataset contains images of both pneumonia infected and normal CT scans as a means of training, testing and validation.
The second dataset contains a mixture of CT scans of lungs infected by pneumonia caused by COVID-19. All the scans
in the dataset are verified by radiologists. 


## Hypotheses / Questions
* By analysing the image metadata, what age groups and gender have suffered from COVID-19?
* Can we identify the presence of pneumonia using image recognition?
* Are we able to differentiate between pneumonia and COVID induced pneumonia?

## Dataset
* [Github](https://github.com/UCSD-AI4H/COVID-CT)
* [Kaggle](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)

## Cleaning
* The images obtained from the GitHub dataset needed to be categorised based on the type of illness
that the patient suffered from, in order to ensure only COVID-19 images were being analysed.
* Additionally, only the AP view of the CT scan was to be analysed, thus additional filtering was required.
* All the images were resized to a standard size, decolourised and normalized in order to be fed into the
CNN. 

## Analysis
* Overview the general steps you went through to analyze your data in order to test your hypothesis.
* Document each step of your data exploration and analysis.
* Include charts to demonstrate the effect of your work.
* If you used Machine Learning in your final project, describe your feature selection process.

## Model Training and Evaluation
The model for the CNN is described in more detail below. 

## Conclusion
* After tailoring the Convolutional Neural Network, by altering it's parameters and exploring several means of 
filtering the data, a model with an accuracy of 86.2% for the analysis of normal vs. pneumonia AP CT scans 
was obtained.
* The model was then applied to the analysis of the COVID-19 infected pneumonia AP CT scans and an accuracy of 
XX% was obtained. 

## Future Work
* Increase the size of the dataset for normal, pneumonia and COVID-19 induced pneumonia datasets.
* Apply the CNN to deduce the difference between bacteria, viral and fungal pneumonia.
* 

## Workflow
Outline the workflow you used in your project. What were the steps?
How did you test the accuracy of your analysis and/or machine learning algorithm?

## Organization
How did you organize your work? Did you use any tools like a trello or kanban board?

What does your repository look like? Explain your folder and file structure.

## Links
Include links to your repository, slides and trello/kanban board. Feel free to include any other links associated with your project.


[Repository](https://github.com/)  
[Slides](https://slides.com/)  
[Trello](https://trello.com/en)  
