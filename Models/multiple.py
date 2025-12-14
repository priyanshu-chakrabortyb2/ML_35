import numpy as np
from sklearn.linear_model import LinearRegression

# Example dataset
X = np.array([
    [2100, 3],
    [1600, 2],
    [2400, 4],
    [1416, 2],
    [3000, 4]
])

y = np.array([400000, 330000, 369000, 232000, 540000])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Print coefficients
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

# Predict
pred = model.predict([[2000, 3]])
print("Predicted price for 2000 sq ft, 3 rooms:", pred)