# Multiple Linear Regression Analysis for Predicting Building Heating Load

# Overview
Reducing heating load can lead to significant cost savings for households, particularly for low-income households.
There are two findings based on this analysis.

First finding: Analysis indicates that heating load is most strongly influenced by overall building height, as shown in the heat map. This finding is further supported by the multilinear regression results, where overall height has the largest and positive coefficient, indicating a strong direct relationship with heating load. Relative compactness and wall area are the next most influential factors. Both variables have negative coefficients in the regression model, suggesting that increasing relative compactness and wall area is associated with a reduction in heating load.

Second finding: When the results are plotted, the scatter reveals clear nonlinearity in the dataset, indicating that the underlying relationships are not linear. In fact, load data are inherently nonlinear in nature, which explains why linear models may struggle to fully capture the observed patterns.

# Dataset
The dataset includes simulated energy data coming from buildings that vary in glazing area, glazing area distribution, orientation, and other design parameters. Different combinations of these characteristics result in 768 distinct building configurations. The dataset contains 768 samples with 8 features and is used to predict two continuous target variables. 


# Source: 

Dataset name: Building Energy Efficiency datset
Link: [https://www.kaggle.com/datasets/srinuti/residential-power-usage-3years-data-timeseries](https://archive.ics.uci.edu/dataset/242/energy+efficiency)

# Data Usage Notice

No personally identifiable information (PII) is included.

This project is intended for educational and research purposes only.



# Project Workflow
Step 1: Import libraries

Step 2: Load the open source 

Step 3: Reporting on the collinearity between variables by Heatmap chart

Step 4: Train a multiple linear regression  and make a prediction

Step 7: Evaluate performance using RMSE and R² and reporting on the coefficients

Step 8: Optimize the multiple linear regression to find the best fit with LassoCV

Step 8: Visualize predictions

Step 9: Visualize residuals

# Key Observations

First finding: Analysis indicates that heating load is most strongly influenced by overall building height, as shown in the heat map. This finding is further supported by the multilinear regression results, where overall height has the largest and positive coefficient, indicating a strong direct relationship with heating load. Relative compactness and wall area are the next most influential factors. Both variables have negative coefficients in the regression model, suggesting that increasing relative compactness and wall area is associated with a reduction in heating load.


![2026MLR_heatmap](https://github.com/user-attachments/assets/80faa222-8e3c-41ef-ba06-60651cb1a325)

Second finding: When the results are plotted, the scatter reveals clear nonlinearity in the dataset, indicating that the underlying relationships are not linear. In fact, load data are inherently nonlinear in nature, which explains why linear models may struggle to fully capture the observed patterns.


<img width="384" height="278" alt="2026 residuals" src="https://github.com/user-attachments/assets/e1aa8800-d474-4835-be8c-488bbb60970f" />

# Legal and Open-Source Considerations
This project does not involve personal data or restricted systems. Data is available for public.

All code is intended for open-source use.

Suitable for educational and research purposes.

