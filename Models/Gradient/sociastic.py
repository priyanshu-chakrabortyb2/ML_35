import numpy as np

# Sample dataset
X = np.array([1, 2, 3, 4, 5])
y = np.array([3, 4, 2, 4, 5])

# Reshape for consistency
X = X.reshape(-1, 1)

# Initialize parameters
theta_0 = 0
theta_1 = 0

# Hyperparameters
alpha = 0.01   # learning rate
epochs = 1000   # iterations

m = len(X)

# Gradient Descent
for i in range(epochs):
    y_pred = theta_0 + theta_1 * X.flatten()
    
    d_theta_0 = (-2/m) * sum(y - y_pred)
    d_theta_1 = (-2/m) * sum((y - y_pred) * X.flatten())
    
    theta_0 = theta_0 - alpha * d_theta_0
    theta_1 = theta_1 - alpha * d_theta_1

print("Theta 0 (intercept):", theta_0)
print("Theta 1 (slope):", theta_1)

# Predict
x_new = 6
prediction = theta_0 + theta_1 * x_new
print("Prediction for x = 6:", prediction)