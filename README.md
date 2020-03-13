<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Seeking Enlightment
*[Anna Riera Pascual]*

*[Data Analytics, Ironhack BCN & Jauary - March, 2020]*

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

When someone starts the process of searching for a flat, multiple criteria needs to be considered: Price, Location, N of Rooms, etc... and online flat portals are great at supporting with the filtering efforts and narrowing our search.

Nonetheless, the search can still be overwhelming and there are still many factors which cannot be included in our search parameters: Flat luminosity is one of them.



## Hypotheses / Questions

Questions I have asked myself prior to the project:

* Is luminosity an important factor for people when looking to rent/buy a flat?
* Could there be a demand for this parameter to be included in Flat Search portals?
* Is there any way we could establish a measurement for luminosity in a flat?
* Does the luminosity of a flat have an impact on the price of a flat? 

My hypotehsis:

* I belive the luminosty and natural light of a flat is a factor many people would care about.
* I believe that a flat with greater luminosity would be priced higher.


## Dataset

Before starting the actual analysis, I wanted to validate the interest for "Luminosity" in a slat. To do so, I ran a survey amongst 58 respondents.


In order to start our analysis, I had to extract a big dataset on flat images. After trying different renamed flat portals in Barcelona : Idealista.com ; Engel&Volkers ; Fotocasa.es I found multple difficulties to access datasets (limited calls, robot blockers, etc...). Eventually I decided to opt for a smaller real estate site, but with enought data to run my analysis.

I explored and scraped the following site : www.eixhabitat.es/

I selected the following parameters : Flats for Sale in Barcelona

The size of my dataset is:

> 96 individual flats analysed
> 1080 images analysed
> 11 - 12 images per flat analysed in average
> 2688 Objects identified with Object detection in our dataset


## Cleaning

As mentioned above, I had to scrape a smaller real estate website. Doing it was a challenging task given that the JSON structure was all over the place. I had to scrape each individual flat link, and extract flat information as well as all the images of each.

I also focused my efforts on scraping the important images since my code was initially extracting irrelevant imagery: such as logos, company branding and generic images.


## Analysis

I had 3 goals for my analysis : 
1. Understanding the overall interest of the population in "Luminosity" as a parameter
2. If the response was positive, establishing a luminosity score for each individual flat.
3. Replicating and visualising an test site, called lightorflight.com, which reflected my Luminosity Score as a filtering parameter. 


1. The survey and it´s results:


 - 100% of people believe having natural light on a flat (to rent or buy) is an important factor.
 - When asked to choose from 1 to 5 "the importance of having natural light in your flat", 97% of respondents selected 5 (71%) and 4 (26%).
 - When asked if they would rather choose A) A bigger flat BUT with poor natural light OR B) A smaller flat BUT with great natural light, 93% of respondents chose option B.

Therefore, it is clear that there is an appeal for "luminosity" in flats, but no real estate online agency is offering this paramenter as a classifier. Therefore, i decided to create a Luminosity score myself.

2. Establishing a Luminosity Score

To do this, I analysed into different parameters which I then combined in my overall score:

1. Object recognition : Identifying if the images of a flat had, or not, windows.

I initially tried to create my own algorythm to identify windows but found a lot of difficulties. For example, I tried looking into the window detection by a square/rectangular shape analysis, but this resulted very challenging given that it would also class object such as doors, wardrobes, drawers inefficiently.

Finally, I managed to connect my imagery to a Google Vision algorythm which gave me a dataframe with all the objects classified as well as the accuracy score per each image.

2. Pixel mean analysis: Getting an overall score of the "colour" average of each image.

In this analysis, I split the image into individual pixels, getting an array of values for each. I did a mean analysis for this values and established a pixel mean for each image. Since the values ranged from 0(black) to 255 (white), I normalised the values to be able to get a comparable metric to all the parameters.

3. % of Brightness: Getting the % distribution of the brightness of an image.

In this analysis, I also split the image into individual pixels but this time each pixel was classed (based on the colour) as a "white/bright" pixel or a "black/dark". This allowed me to get a % of brightness in each individual image. This value was also normalised.


Finally, considering the 3 parameters analysed, I created an overall Luminosity score per image. I then took this one level up, and managed to get an overall luminosity score for each individual flat.

3. Lightorflight.com

Finally, I created a dummy version of a potential site including the new Luminosity Score as a paramenter. Once you establish the filters, a map get filtered with all individual flats complying your criters. From each flat, you can get it´s individual information, showcasing the Luminosity score as well as the other 3 sub paramenters. It also has an interactive link which takes you to the real site and the relevant information. 
Please test and play of the following link: https://public.tableau.com/shared/GZW6NBJPM?:display_count=y&:origin=viz_share_link


## Conclusion

There is a clear interest amongst the population in this type of parameter.

Having looked at the luminosity score achieved and revising the actual flat imagery, I can positively say the score was useful at classifying flats which were more luminous versus those that were not.

## Future Work

Eventually, given the scraping limitations I found, I was not able to scrape a massive dataset for analysis. If done in the future, I would like to expand my analysis by understanding the relationship between luminosity scoring and flat prices. Could we see any pattern between higher luminosity scores and bigger price uplifts per sqm? Something to look out for in the future.

## Workflow

- Finding a topic of interest to me
- Exploring what was available on the market in terms of similar concepts
- Generating a survey to gauge people´s interest
- Establishing the framework to establish the Luminosity Score
- Finding a relevant site for imagery analysis
- Scraping the real estate site
- Undertaking the analysis
- Finding the results
- Creating a visualization to mirror a new potential real estate site introducing the new score


## Organization

My repository includes:
- Code folder: Different codes I have trialed and tested for the project
- Datasets folder: The imagery extracted from the relevant site
- Final code foler: A version of the latest copy of my code including all documentation
- Presentation folder : Content used in my final presentation

## Links

[Repository](https://github.com/) 
[Tableau_Viz](https://public.tableau.com/shared/GZW6NBJPM?:display_count=y&:origin=viz_share_link) 
[Slides](https://slides.com/arierapa/seeking-enlightment-2f81da)  
 
