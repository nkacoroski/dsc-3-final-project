# Classifier for Invasive Species in North America

This is the Module 3 Final Project for the Flatiron Seattle Data Science Program by [Natasha Kacoroski]
(https://github.com/nkacoroski) and [Jacob Crabb](https://github.com/AlludedCrabb). The goal of this project was to 
demonstrate our ability to select and gather information from a dataset create a classification model.
company/stakeholder. For our dataset, we chose the [USDA Plants Database](Welcome to the PLANTS Database | USDA PLANTS) and
attempted to classify whether or not a plant is invasive based on its characteristics. This has real-world applications in
agriculture and invasive species management. The slide deck for our presentation can be found [here](slide_presentation.pdf).

## [Methodology](student.ipynb)
### Data Processing
The dataset contains 38,186 plants with 78 features (12 numeric and 66 categorical). To preprocess the data we built a
pipeline to fill nulls for all values, standard scale numeric data, simplify select categories, and one-hot-encode. After
preprocessing our dataset had 2,063 plants with 56 features (8 numeric and categorical).

## Modeling
We tested logistic regression, random forest, and xgboost models. We tried tuning hyperperameters with grid search and only
modeling on significant data from logistic coefficients. We did not conduct principal component analysis. Metrics we used
to evaluate models were the roc curve, f1_score, and auc.

## Results
None of our models had the skill to predict whether or not a species was invasive. 

## Recommendations
We recommend researching invasives species and acquiring more relevant data.
