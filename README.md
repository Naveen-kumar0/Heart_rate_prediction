# Heart_rate_prediction

## Team : Victor
 - Leader : Naveenkumar S , Phn: 9344241718
 - Member2 : Yaadhav R, Phn: 6369493519

## Overview
This project aims to predict heart rates based on certain features. The prediction model utilizes a machine learning algorithm trained on a dataset of heart rate observations.

## Features
- Heart rate prediction based on input features.
- Simple command-line interface for making predictions.

## Getting Started
To get started with the heart rate prediction model, follow these steps:

### Prerequisites
- Make sure you have Python installed. 
- Once you try to run "run.py"
- use command: py run.py sample_test_data.csv
- Here replace the sample_test_data.csv with the actual file name

## Model Details
- The heart rate prediction model is built using a Support Vector Machine algorithm. 
- The dataset is preprocessed to handle missing values and normalize features.
- The training data is scaled using MinMaxScaler to fall in range [0,1]
- Hyper Parameter Tuning is performed to select the best model
- Model performed at Accuracy of 99% with 0.05 Mean Squared Error

## Future Work 
- Now I am having an idea of deploying the model to AWS EC2 instance
- Soon I will make this happen by creating user friendly website where you can drop the CSV file and download the results
  
  
## Contact
For questions or feedback, please contact naveenkumarsathish03@gmail.com.
