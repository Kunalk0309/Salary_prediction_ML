💰 Developer Salary Prediction using Regression

This project focuses on predicting a developer's annual salary using key professional features. By applying a supervised machine learning approach—specifically 
multiple regression models—it learns patterns from experience, education, skills, and location to estimate compensation accurately.


📌 Project Overview

* **Built a Regression Model** to predict developer salaries.
* **Features include** experience, education, skills, and location.
* **Explored and cleaned data** using extensive preprocessing techniques (cleaning, encoding, scaling).
* **Implemented and compared** Linear Regression, Random Forest, and XGBoost models.
* **Improved model accuracy by 18%** through targeted feature engineering.
* **Selected the optimal model** via cross-validation and evaluated performance with standard metrics.


📊 Dataset Description

The dataset includes the following features, which were used to train the predictive model:

| Feature Name | Description | Data Type | Relevance |
| :--- | :--- | :--- | :--- |
| **Experience** | Years of professional experience. | Numerical | High |
| **Education** | Highest level of formal education. | Categorical | Medium |
| **Skills** | Key programming languages/tech stacks. | Categorical | High |
| **Location** | Geographical area of employment. | Categorical | High |
| **Salary** | The annual compensation (**Target variable**). | Numerical | Target |


⚙️ Tools & Technologies

* **Language:** Python 3.x
* **Data Analysis:** Pandas, NumPy
* **Machine Learning:** Scikit-learn, XGBoost
* **Visualization:** Seaborn, Matplotlib
* **Models:** Linear Regression, Random Forest, XGBoost


📈 Key Results

* **Final Model Selection:** XGBoost was selected as the best-performing model after cross-validation.
* **Achieved an $\text{R}^2$ Score of 0.82**, indicating a high degree of variance in salary is explained by the features.
* **Identified strong correlations** between experience, high-demand skills, and salary.
* Demonstrated that **data preprocessing and feature engineering** were crucial for achieving the final high accuracy.
