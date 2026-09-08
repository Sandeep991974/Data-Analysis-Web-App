# 📊 Data Analysis Web App

A beginner-friendly **Data Analysis Web App** built using Python and Streamlit.

This application allows users to upload a CSV dataset and perform various basic data analysis and data cleaning operations without writing Python code.

## 🚀 Live Demo

https://sandeep99-data-analysis.streamlit.app/

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Seaborn

## ✨ Features

### 📁 Dataset Upload
- Upload CSV datasets directly through the web interface.

### 👀 Dataset Preview
- View the first few rows of the dataset.
- View the last few rows of the dataset.

### 📋 Dataset Information
- Check data types of columns.
- Check total number of rows.
- Check total number of columns.

### 🧹 Data Cleaning
- Detect missing values.
- Remove rows containing missing values.
- Fill missing numerical values using:
  - Mean
  - Median
- Fill missing values using Mode.

### 🗑️ Column Operations
- Remove unwanted columns.
- Rename columns.
- Change column data types.

### 📊 Exploratory Data Analysis

The application provides basic EDA operations:

- Value Counts
- Sorting
- Filtering
- Group By
- Column Statistics

### 🎯 Dataset Dashboard

The dashboard provides:

- Total Rows
- Total Columns
- Missing Values
- Duplicate Rows
- Numerical Columns
- Categorical Columns
- Numerical Summary

### 💾 Export Dataset

After performing data analysis and cleaning, users can download the dataset as a CSV file.

## 📂 Project Structure

```text
Data-Analysis-Web-App/
│
├── DAW_app.py
├── requirements.txt
└── README.md

