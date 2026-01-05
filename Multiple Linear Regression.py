#!/usr/bin/env python
# coding: utf-8

# In[53]:


# Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LassoCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression


# In[54]:


# Doanloading data
# Direct link to the UCI dataset file
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00242/ENB2012_data.xlsx"

# Read directly from the web (Excel format)
df = pd.read_excel(url)

# Optional: rename columns (for clarity)
df.columns = [
    "Relative_Compactness", "Surface_Area", "Wall_Area", "Roof_Area",
    "Overall_Height", "Orientation", "Glazing_Area", "Glazing_Area_Distribution",
    "Heating_Load", "Cooling_Load"]

print(df.head())


# In[55]:


# Heat map to see the correlation between variables
X_features = df.columns[:-2]
corr_heating = df[X_features.tolist() + ["Heating_Load"]].corr()
plt.figure(figsize=(12, 8))
plt.imshow(corr_heating, vmin=0, vmax=1, cmap='coolwarm')
plt.colorbar()
plt.xticks(range(len(corr_heating.columns)), corr_heating.columns, rotation=90)
plt.yticks(range(len(corr_heating.columns)), corr_heating.columns)
plt.title("Correlation Heatmap: Features vs Heating Load")
plt.tight_layout()
plt.show()


# In[56]:


# Separate dependant and independent variables
X = df.drop(columns=["Heating_Load", "Cooling_Load"])
# target is y
y = df["Heating_Load"]   


# In[57]:


# Split data to test and train 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# In[58]:


# Deploy linear regression model
model = LinearRegression()
model.fit(X_train, y_train)


# In[59]:


# Prediction on test data 
y_pred = model.predict(X_test)


# In[60]:


# Reporting on evaluation metric
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)
print(f"RMSE: {rmse:.2f}")
print(f"R²: {r2:.3f}")


# In[61]:


# Reporting on the coefficients of the multiLinearRegression
coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
})

print(coefficients)


# In[63]:


# Finding the best ultiLinear regression with LassoCV
# 4) Pipeline: Scaling + LassoCV
# 0.001 to 10 (log scale)
alphas = np.logspace(-3, 1, 30)  

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("lasso", LassoCV(alphas=alphas, cv=5, max_iter=100000, random_state=42))
])

# Train
pipeline.fit(X_train, y_train)

# Predict
y_pred = pipeline.predict(X_test)

# Evaluate
rmse = mean_squared_error(y_test, y_pred, squared=False)
r2 = r2_score(y_test, y_pred)

print(f"RMSE: {rmse:.2f}")
print(f"R²: {r2:.3f}")

# 5) Best alpha + coefficients

best_alpha = pipeline.named_steps["lasso"].alpha_
print("Best alpha:", best_alpha)

coef = pipeline.named_steps["lasso"].coef_

results = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": coef
}).sort_values(by="Coefficient", key=lambda s: s.abs(), ascending=False)

print("\nLasso Coefficients (sorted by absolute value):")
print(results)

# Selected features (non-zero coefficients)
selected = results[results["Coefficient"] != 0]
print("\nSelected Features (non-zero coefficients):")
print(selected)


# In[64]:


# Residuals plots
residuals = y_test - y_pred

plt.figure()
plt.scatter(y_pred, residuals)
plt.axhline(0)
plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.title("Residuals vs Predicted Values")
plt.show()

