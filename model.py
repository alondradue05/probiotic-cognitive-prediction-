import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load your dataset
data = pd.read_csv('your_data.csv')  # Replace 'your_data.csv' with your actual file name

# Prepare your features and target
X = data[['Probiotic Dose (mg)']]  # Features: Probiotic Dose in mg
y = data['Cognitive Improvement (%)']  # Target: Cognitive Improvement in %

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test data
predictions = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

# Plot the results
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, predictions, color='red', label='Predicted')
plt.title('Probiotic Dose vs. Cognitive Improvement')
plt.xlabel('Probiotic Dose (mg)')
plt.ylabel('Cognitive Improvement (%)')
plt.legend()
plt.show()
