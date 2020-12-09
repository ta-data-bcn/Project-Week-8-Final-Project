<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Detecting Pneumonia with Machine Learning and Neural Networks
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
In this project, my main objective is to be able to successfully differentiate between pneumonia, COVID-19 
and normal lungs using a convolutional neural network using image classification. This would be 
achieved by analysing X-Ray scans from an anteroposterior, ie: from front to back, perspective of the lungs.
Ultimately, the aim of the project would be to develop a means of rapidly analysing pneumonia, and pneumonia induced by COVID, thereby saving time
and offering radiologists and doctors a second opinion.
The datasets were obtained from Kaggle and the other from Github, they are referenced below. The first 
dataset contains images of both pneumonia infected and normal X-Ray scans as a means of training, testing and validation.
The other datasets contains a mixture of X-Ray scans of lungs infected by pneumonia caused by COVID-19. All the scans
in the dataset are verified by radiologists. 


## Hypotheses / Questions
* Can we identify the presence of pneumonia using image recognition?
* How accurately can we identify pneumonia and COVID?
* Are we able to differentiate between pneumonia and COVID induced pneumonia?

## Datasets
* [Github](https://github.com/UCSD-AI4H/COVID-CT) - This repo contains COVID X-Ray images which I implimented into the dataset.
* [Github](https://github.com/peiriant/COVID19) - This repo also contains COVID X-Ray images.
* [Kaggle](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia) - The kaggle contains a library of normal and pneumonia X-Rays.

## Cleaning
* The images obtained from the GitHub dataset needed to be categorised based on the type of illness
that the patient suffered from, in order to ensure only COVID-19 images were being analysed.
* Additionally, only the AP view of the X-Ray scan was to be analysed, thus additional filtering was required.
* All the images were resized to a standard size, decolourised and normalized in order to be fed into the
CNN. 
* Various different parameters for the importing, normalizing and mean reduction of the image were investigated.

## Model Training and Evaluation
The model for the CNN is described in more detail below. 
- 1) Classification of Pneumonia and Normal lungs = 90% accurate
- 2) Classification of Pneumonia / COVID-19 and Normal lungs = 85% accurate

## Conclusion
* After tailoring the Convolutional Neural Network, by altering it's parameters and exploring several means of 
filtering the data, a model with an accuracy of 85% for the analysis of normal vs. pneumonia AP X-Ray scans 
was obtained.
* Following this, due to the imbalance of the dataset I decided to reduce the number of pneumonia images to be
more in line with the normal images. This resulted in an increase in the accuracy, up to 88%.
* The model was then applied to the analysis of the COVID-19 infected pneumonia AP CT scans and an accuracy of 
84% was obtained. 
* Similarly, I decided to balance the dataset further by reducing the number of pneumonia images. This led to an
increase of accuracy up to 87.5% percent.


## Future Work
* Increase the size of the dataset for normal, pneumonia and COVID-19 induced pneumonia datasets.
* Apply the CNN to deduce the difference between bacteria, viral and fungal pneumonia.
* Apply the CNN to differentiate other lung based diseases. 
* Fine tune the hyperparameters of the CNN further.
* Center the images in the dataset, highlight focus on the lungs.

## Workflow
I began my work by looking for the datasets available to me. I discovered that many of the COVID-19 datasets
do not provide images of normal lung X-Ray scans as a reference. They also have X-ray images taken from several
different viewpoints. 
As such, I decided to investigate both the Kaggle Pneumonia images and COVID-19 images that I found on several GitHub repoistories. 
In order to utilise the Kaggle photoset, I extracted all the photos, converted them to 
numpy arrays of RGB numbers using CV2 and then assigned them to the correct class based on which folder they were
located in (eg: Normal, Pneumonia, Test, Train etc). This data was then normalized in order to reduce the 
amount of information needed to be commit to memory when running the CNN, and also normalizing the gray scale images
in the process. The data was then fed into the CNN and the accuracy and loss of the model was evaluated. A confusion matrix was also
generated in order to determine the distribution of the CNN's predictions with regards to the prognosis (ie: normal / pneumonia lungs).

The process was repeated with the addition of the COVID-19 image sets. One dataset provided only X-ray images, thus this was easy to utilise. 
The other image set imageset contained numerous images from different positions, thus, using the metadata, only the correct X-Ray AP (anterior posterior) images were utilised. 
I explored using various methods to split and train the data in order to improve the accuracy of the model, whilst trying to avoid overfitting and underfitting. 
In particular I utilised ImageDataGenerator, a function which automatically skews, rotates and alters the zoom of images fed into the training and validation set. This means that the dataset is seeing new data continuously thus
it helps avoid overfitting. I also investigated reducing the size of the overall dataset which led to an improvement in the accuracy of the CNN.

Finally, I utilised the models to predict the class of the images contained with the testing dataset. These were then plotted as confusion matrixes in order to be able to deduce
how well the CNN worked "seeing" new images. Ultimately, both the classification of Pneumonia/Normal and Pneumonia/Normal/COVID-19 x-rays resulted in accuracies above 
85% which suggests that our CNN is robust, accurate and is avoiding overfitting / underfitting. 

## Organization
- I utilised a Trello board to map out my overall plan and for check-points along the way.
- The work is organised into two Notebooks, which read chronologically describe the work process.
- The first notebook (01 Image Processing_CNN Model_Pneumonia.ipynb) details the development of a image classifier for the presence of pneumonia in X-Ray scans.
- The second notebook (02 Image Processing_CNN Pneumonia_and_COVID19.ipynb) details the development of a multi-class image classifier for COVID-19, Pneumonia and normal lungs.
- The CNN_Models_Weights and Dataset folders contain text files with links to the models I utilised as they're both too
big to be uploaded to Github.
- The CNN_Models_Weights folder contains a link to a GoogleDrive which has the model and the weights for each notebook.

## Links

[Repository](https://github.com/peiriant/Project-Week-8-Final-Project/tree/master/your-project)  
[Slides](https://docs.google.com/presentation/d/1EOBTjrrSqtab0Yp7QVxBku-6PXEwTSGyHm1JzJkU20Q/edit?usp=sharing)  
[Trello](https://trello.com/b/CDl7EYhV/project-5)
