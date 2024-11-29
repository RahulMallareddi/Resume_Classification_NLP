# Resume Classification NLP

## Overview

This repository contains a project aimed at classifying resumes based on job roles. Leveraging machine learning, this project assists HR in efficiently sorting resumes.

## Dataset

The dataset consists of resumes collected from four different job roles: Workday, Peoplesoft, SQL Developer, and React Developer. These resumes can be in various formats, including DOC, DOCX, and PDF.

The Tika server is used to extract text from resumes. Then, NLP techniques are applied to clean the data and prepare it for transformation using TF-IDF.

## Model Architecture

The model employed includes KNN, Logistic Regression, Decision Tree, Random Forest, SVM, Naive Bayes and XGBoost to classify resumes into different categories. Different methods, implementations, and strategies have been used in some of the models.

## Training and Evaluation

The model is trained using 70% of the entire dataset and tested with the remaining 30%. The model is evaluated using metrics such as accuracy, precision, recall, and F1-score. The model is also visualized using AUROC and AUPRC curves.

## Deployment

A user-friendly interface has been developed using Streamlit to facilitate uploading resumes and receiving predictions. To use it, simply run the following command:
**streamlit run Home.py**

![alt text](https://github.com/RahulMallareddi/Resume_Classification_NLP/blob/main/img/app_screenshot.png)
