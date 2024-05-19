#MLOps Backend
### The backend portion for MLops project involving flask

## Table of contents
* [Overview](#overview)
* [Dataset](#dependencies)
* [Process Flow](ProcessFlow)
* [Future Application](#FutureApplication)
* [Usage](#usage)
* [References](References)

## Overview

This application is used to predict house rent prediction for the city of Delhi
This repository is for the backend portion of the application and contains the dataset, ipynb file where the machine learning flow was executed and the resulting pickle (model.pkl) file of the 
selected model along with the dockerfile,render.yaml as well as the 

## Dataset

The dataset used for this problem is available on kaggle and linked [here](https://www.kaggle.com/datasets/iamsouravbanerjee/house-rent-prediction-dataset).
This repository contains the dataset, .ipynb file where the machine learninng is porcessed as well as the pickle (model.pkl) file of the selected model for the backend section of our project.

## Process Flow

1). Downloaded the dataset from Kaggle
2). Performed exploratory data analysis 
3). Subset the data for City=Delhi

![image](https://github.com/HarshSingh18/MLOps_backend/assets/32611475/8d73ad94-6ccc-41f9-8b8e-f67fd04557df)


4). Selected input features 
5). Tried different regression algorithms

![image](https://github.com/HarshSingh18/MLOps_backend/assets/32611475/492caa5d-3abb-4cd5-8df8-92d493163960)

6). Selected randomforestregressor with hyperparameter tuning as it had best accuracy 
7). Created a pickle file of that model
8). deployed all the files on github
9). Edited the dockerfile accordingly
9). Registered on render and deployed as webservice
10). Tested the resulting weblink on postman api.

![postman](https://github.com/HarshSingh18/MLOps_backend/assets/32611475/d94b8f46-6320-41df-b508-dbe4693438a2) 


