# Thyroid Disease Detection

Thyroid disease a very common problem in India, more than one crore people are suffering with the disease every year. Thyroid disorder can speed up or slow down the metabolism of the body.

The main objective of this project is to predict if a person is having compensated hypothyroid, primary hypothyroid, secondary hypothyroid or negative (no thyroid) with the help of Machine Learning. Classification algorithms such as Logistic regression, Random Forest, Decision Tree, Naïve Bayes, Support Vector Machine have been trained on the thyroid dataset, UCI Machine Learning repository. Random Forest performed well with better accuracy (98%), precision and recall. After hyper parameter tuning, application has deployed on Heroku with the help of flask.

## Website link
https://thyroid-detection-api.herokuapp.com/

## Demo

https://user-images.githubusercontent.com/59659818/140499629-ceefc4e6-b1d9-4a31-9fc3-d73f9ffc6dad.mp4



## Technical aspect
* Python 3.8
*	Front-end: HTML, CSS
*	Back-end: Flask
*	IDE: Jupyter Notebook, PyCharm
*	Deployment: Heroku

## Workflow

### Data Collection
Thyroid Disease Data Set from UCI Machine Learning Repository

### Data Pre-processing
* Missing values handling by Simple imputation (median strategy)
*	Outliers detection and removal by boxplot and percentile methods
*	Categorical features handling by ordinal encoding and label encoding
*	Feature scaling done by Standard Scalar method
*	Imbalanced dataset handled by SMOTE
*	Feature selection done by forward feature selection

### Model Creation and Evaluation
*	Various classification algorithms like Logistic Regression, Random Forest, Decision Tree, Naïve Bayes, Support Vector Machine tested.
*	Random Forest, Decision Tree and Logistic regression were given better results. Random Forest was chosen for the final model training and testing.
*	Hyper parameter tuning was performed.
*	Model performance evaluated based on accuracy, confusion matrix, classification report.


### Model Deployment
The final model is deployed on Heroku using Flask framework

## Authors
**Amber Gupta** - www.linkedin.com/in/amber-gupta-a314a21b6/



### If you like this project, please do give the star. If you have any suggestions or issues, please drop a message. 


