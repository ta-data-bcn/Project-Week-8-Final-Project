<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# GOING TO A MUSIC FESTIVAL
*Josep Foradada* 

*Data Analytics June 2019*

## Content
- [Project Description](#project-description)
- [Hypotheses / Questions](#hypotheses-/-questions)
- [Dataset](#dataset)
- [Cleaning](#cleaning)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [Conclusion](#conclusion)
- [Future Work](#future-work)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

<a name="project-description"></a>

## Project Description
This project had 2 main objectives, first of all to get a recomendation from spotify based on all my playlist and at the same time, compare songs from a music festival and check if they match with the bigger cluster generated from mines.

<a name="hypotheses-/-questions"></a>

## Hypotheses / Questions
* Will be able to clusterify the songs from my playlist into music styles?
* Is it possible to request specific recomendations to spotify? 
* Would be a great idea to go to next music festival after the bootcamp?

<a name="dataset"></a>

## Dataset
* For this project all data was request from SPOTIFY API using the library spotipy. Spotipy recommendations function has a bug that splits the variables of the request into characters joined by commas. This was really difficult to find due to cannot see the request url using python. Finally I had to modify the function inside the library to get the recommendations request. 

<a name="cleaning"></a>

## Cleaning
The main step here is twrangle and normalize data from requests. The answers are huge json files, with several levels of jsons or list of dictionaries


<a name="model-training-and-evaluation"></a>

## Model Training and Evaluation
Model used is the K-Means clustering. I would prefer using DBScan because will be scalable to any user playlists. But was not able to find the correct epsilon, neither the min_samples. So I used K-Means and tested with diferent number of clusters since i was able to split classic music from opera. All other clusters are so similar, probably because there is no such a much difference between Pop, Indie, Rock or Folk.
The same model was used to analyze the Gigante Music Festival, here I decided to try 3 cluster because it sells that they do Pop, Indie and Rock
<a name="conclusion"></a>

## Conclusion

The main conclusion is that spotify song features are not enough relevant to label songs just with that parameters

<a name="future-work"></a>

## Future Work
First of all I will contact to spotipy to inform for the bug. After this I would like to improve clustering using other methods or try to analyze the segments, beats,etc for each song to see if could be a more accurate clustering without using labels.

<a name="workflow"></a>

## Workflow
-Get the Data
-Wrangling data


<a name="organization"></a>

## Organization

Usually when I work alone I prefer to draw my schemas on paper using a pencil. I visualize it much better, than into any board. Probably because of my design and 3d background, I use to do sketches and storyboards. On the other hand I can handle all that information and structure also in my brain.

<a name="links"></a>

## Links
I want to share this medium article where I get the idea for the polar plots:
https://towardsdatascience.com/profiling-my-favorite-songs-on-spotify-through-clustering-33fee591783d

[Repository](https://github.com/josepforadada/Project-Week-8-Final-Project)  
[Slides](https://slides.com/josepforadada/deck-6#/)  
[Trello](https://trello.com/b/qJ7IIpgt/final-project)  