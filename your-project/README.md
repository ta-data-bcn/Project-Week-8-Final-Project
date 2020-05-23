<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Data fueled growth
*[Francesco Baldissera]*

*[DAFT, Barcelona. March-2020]*

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
My project is a complete growth marketing framework for an online store. Ranging from analysis of the data, customer segmentation and sales predictions. This is intended to be used as a starting point to analyze how well does an online store does and gather insights on next actions to make it grow. Even if it's aimed at a marketplace business type it can be tweaked for any other kind of online business.

## Hypotheses / Questions
* What data/business/research/personal question you would like to answer?
* What is the context for the question and the possible scientific or business application?
* What are the hypotheses you would like to test in order to answer your question?  
Frame your hypothesis with statistical/data languages (i.e. define Null and Alternative Hypothesis). You can use formulas if you want but that is not required.

## Dataset
### Where did I get the data? 

I gathered it from [Kaggle] (https://www.kaggle.com/mkechinov/ecommerce-behavior-data-from-multi-category-store) I loaded the data as a CSV file to the repository in the directory 'data'. Loaded it to JupyterNotebook using the 'load_csv' function of the Pandas library.

Special thanks also to [REES46 Marketing Platform.] (https://rees46.com/)

As both provided datasets are considerably large I sliced it to a smaller sample of 20000 rows.

### Data structure
#### event_time

Time when event happened at (in UTC).

#### event_type

Events can be:

* view - a user viewed a product
* cart - a user added a product to shopping cart
* removefromcart - a user removed a product from shopping cart
* purchase - a user purchased a product

*Typical funnel:* view => cart => purchase.

#### product_id

ID of a product

#### category_id

Product's category ID

#### category_code

Product's category taxonomy (code name) if it was possible to make it. Usually present for meaningful categories and skipped for different kinds of accessories.

#### brand

Downcased string of brand name. Can be missed.

#### price

Float price of a product. Present.

#### user_id

Permanent user ID.

#### user_session

Temporary user's session ID. Same for each user's session. Is changed every time user come back to online store from a long pause.

#### Multiple purchases per session
A session can have multiple purchase events. It's ok, because it's a single order.


## Cleaning
Describe your full process of data wrangling and cleaning. Document why you chose to fill missing values, extract outliers, or create the variables you did as well as your reasoning behind the process.

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


[Repository](https://github.com/franbaldi/Project-Week-8-Final-Project)  
[Slides](https://slides.com/)  
[Trello](https://trello.com/invite/b/9HgRmLlo/b4ab49219ae21ae052c2c83dd935372b/final-project-data-fueling-growth)  
