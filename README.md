# 💰 Data-Driven Ad Spend Optimization for Sales Forecasting


---

## 🧠 Overview

This project focuses on **optimizing advertising spend across multiple marketing channels** — such as TV, Social Media, Google Ads, Influencers, and Email — to **maximize total sales** using machine learning and regression-based forecasting.

It leverages **historical marketing spend data (2023–2025)** to analyze patterns, model sales response curves, and recommend the **optimal budget allocation strategy** that yields the highest revenue.

---

## 🎯 Objective

The main goal of this project is to answer:

> **"How should we allocate our marketing budget across different channels to maximize sales?"**

By using regression models and optimization techniques, the notebook provides **data-backed insights** into ad effectiveness and forecasts sales outcomes for different spending strategies.

---

## ⚙️ Methodology

### 🔹 1. Data Preprocessing
- Load and inspect dataset (marketing_spend_daily_2023_2025.csv).
- Handle missing values using SimpleImputer.
- Extract temporal features from the Date column — such as **day of the week** and **month**.
- Scale numerical features using StandardScaler.

### 🔹 2. Feature Definition
Independent variables (X):
- TV_Spend`
- SocialMedia_Spend`
- GoogleAds_Spend`
- Influencer_Spend`
- Email_Spend`

Dependent variable (y):
- `Total_Sales`

### 🔹 3. Model Training
Trains and compares multiple regression algorithms:
- **Linear Regression**
- **Ridge Regression (sag solver)**
- **Lasso Regression**
- **ElasticNet Regression**
- **Stochastic Gradient Descent (SGDRegressor)**
- **Random Forest Regressor**

Each model is evaluated using:
- **R² Score** (goodness of fit)
- **Mean Squared Error (MSE)** (accuracy)
- **Cross-validation scores** for stability

### 🔹 4. Optimization
Uses **SciPy’s minimize()** function to:
- Optimize ad spend under a fixed total budget.
- Identify **optimal budget allocation per channel** that maximizes predicted sales.
  
Example output:

Optimal ad spend allocation:
TV_Spend: ₹20,000
SocialMedia_Spend: ₹15,000
GoogleAds_Spend: ₹40,000
Influencer_Spend: ₹10,000
Email_Spend: ₹15,000
Predicted Total Sales: ₹385,000



---

## 📊 Dataset Description

| Column | Description |
|---------|-------------|
| **Date** | Transaction or campaign date |
| **TV_Spend** | Amount spent on TV advertisements |
| **SocialMedia_Spend** | Budget allocated to social media marketing |
| **GoogleAds_Spend** | Spending on Google Ads campaigns |
| **Influencer_Spend** | Amount paid to influencers |
| **Email_Spend** | Budget for email marketing |
| **Total_Sales** | Recorded sales revenue for that day |

---

## 🧩 Project Structure


📁 Ad-Spend-Optimization
├── Ads_Spend_Optimization_forcasting.ipynb   # Main notebook
├── marketing_spend_daily_2023_2025.csv       # Input dataset
├── models/                                   # (Optional) Saved model files
└── README.md                                 # Project documentation


## 🧠 Technologies Used

| Category              | Tools & Libraries   |
| --------------------- | ------------------- |
| **Language**          | Python 3.x          |
| **Data Analysis**     | pandas, numpy       |
| **Machine Learning**  | scikit-learn        |
| **Optimization**      | scipy.optimize      |
| **Visualization**     | matplotlib, seaborn |
| **Model Persistence** | joblib              |

---

## 📈 Results Summary

* Built multiple regression models to predict sales from ad spend data.
* Identified **Google Ads** and **Social Media** as strongest contributors to sales growth.
* Used optimization to suggest **ideal ad spend distribution** under given constraints.
* Achieved high **R² (>0.9)** with Random Forest and ElasticNet regressors.
* Provided actionable insights for **marketing ROI improvement**.

---

## 💡 Future Enhancements

* 🧠 Implement **Bayesian Optimization** for more robust budget allocation.
* 📈 Add **time-series forecasting (ARIMA / Prophet)** for future sales prediction.
* 🧮 Include **ROI-based weighting** for each marketing channel.
* 🧰 Build a **Streamlit dashboard** for real-time ad optimization simulation.

---

## 👨‍💻 Author

**Nitin Jangra**
📧 [nitinjangra0981@gmail.com](mailto:nitinjangra0981@gmail.com)



## ⭐ Acknowledgements

* Inspired by real-world **marketing analytics and media mix modeling (MMM)** frameworks.
* Uses regression-based optimization for practical **sales uplift prediction**.
