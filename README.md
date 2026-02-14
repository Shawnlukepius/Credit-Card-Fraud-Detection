Credit Card Fraud Detection System

An end-to-end machine learning project that detects fraudulent credit card transactions using classification algorithms and handles class imbalance using SMOTE.

🚀 Live Demo

🔗 (https://credit-card-fraud-detection-duirzk9g9wrcsjgz3qqxsu.streamlit.app/)

📌 Problem Statement

Credit card fraud detection is a highly imbalanced classification problem where fraudulent transactions are rare compared to legitimate ones.

This project builds and deploys a machine learning model capable of identifying fraudulent transactions with high recall and ROC-AUC performance.

📊 Dataset

Source: Kaggle Credit Card Fraud Dataset

284,807 transactions

492 fraud cases

Highly imbalanced dataset

Features:

Time

Amount

V1–V28 (PCA-transformed features)

Class (Target variable)

🛠 Tech Stack

Python

Pandas

NumPy

Scikit-learn

SMOTE (Imbalanced-learn)

Streamlit

Joblib

⚙️ Model Development

Data preprocessing and scaling

Handled class imbalance using SMOTE

Trained Random Forest classifier

Evaluated using:

Precision

Recall

F1-score

ROC-AUC

Saved trained model using Joblib

🌐 Deployment

Developed an interactive Streamlit web application for real-time fraud prediction and deployed online.

📈 Results

High Recall for Fraud Detection

ROC-AUC Score > 0.98

Balanced performance on both classes
