import os
file_path = '/Users/alondraduenas/PycharmProjects/alzheimersdetection/data/alzheimers_disease_data.csv'
print("File exists:", os.path.exists(file_path))  # Should return True

import os
import pandas as pd

# File path
file_path = '/Users/alondraduenas/PycharmProjects/alzheimersdetection/data/alzheimers_disease_data.csv'

# Check if file exists
print("File exists:", os.path.exists(file_path))

# Load the CSV file
data = pd.read_csv(file_path)

# Verify data load
print("Data loaded successfully!")

# Display the first few rows of the dataset
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Display dataset shape (rows, columns)
print("Dataset Shape:", data.shape)
