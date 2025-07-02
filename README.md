# Energy Usage Predictor (Regression Analysis)
This project uses regression analysis to predict energy consumption (in watts) based on input features like temperature, time of day, etc.
Accurately forecasting energy usage helps optimize resource allocation, reduce costs, and support sustainability efforts. This project builds and evaluates regression model to predict wattage usage.

# dataset
The data set contains hourly power usage of a residential building in Houston, Texas, collected from smart meters.
The link: https://www.kaggle.com/datasets/srinuti/residential-power-usage-3years-data-timeseries

# The steps are outlined below
Step1: Import libraries<br>
Step2: load data<br>
Step3: Exploratory ddata analysis (EDA). This step consists of the following actions:<br>
       &nbsp;&nbsp;&nbsp;A: report on the general info like, the number of rows and columns and missing points<br>
       &nbsp;&nbsp;&nbsp;B: Outlier detection. If you are doing the root cause analysis you should keep these outliers but if you are building a predictive model , these outliers should be deleted.<br>




# Analysis
1: Based on the plot in Step 3, energy usage decreased during the period of 2020–2021. Additionally, a shift in seasonal usage patterns is observed: in 2016–2017, higher energy consumption occurred toward the end of the year, whereas in 2020–2021, more energy was used in the early months. This pattern is evident from the density and distribution of data points on the plot.<br>
2: When comparing the plots for these four years, we observe subsequence outliers in the early months of 2016 and the later months of 2020—periods where consecutive data points display unusual behavior. If we plan to build a predictive model, such as a regression, it would be advisable to remove these time segments from the dataset to avoid distortion in the model's performance
