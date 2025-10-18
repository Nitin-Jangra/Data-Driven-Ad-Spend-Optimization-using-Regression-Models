import streamlit as st
import pandas as pd
import numpy as np
import joblib
from scipy.optimize import minimize

st.title("📈 Ad Budget → Sales Predictor & Optimizer")

# Load model and scaler
model = joblib.load("best_ads_model1.joblib")
scaler = joblib.load("scaler1.joblib")

# Features your model expects
channel_names = ["TV_Spend", "SocialMedia_Spend", "GoogleAds_Spend",
                 "Influencer_Spend", "Email_Spend"]

st.sidebar.header("Enter Your Budget Constraints")


# Total budget input
total_budget = st.sidebar.number_input("Total Budget (₹)", min_value=0.0, value=100000.0)

# Minimum = 10% of total budget
min_budget_default = total_budget * 0.10
# Maximum = 10% of total budget
max_budget_default = total_budget * 0.90

# Optional min/max per channel
min_budget = st.sidebar.number_input(
    "Minimum per Channel (₹)",
    min_value=0.0,
    value=min_budget_default,
    step=100.0,
    format="%.2f"
)

max_budget = st.sidebar.number_input(
    "Maximum per Channel (₹)",
    min_value=0.0,
    value=max_budget_default,
    step=100.0,
    format="%.2f"
)

# ---------------- Optimization ----------------
def predict_sales(budgets):
    """Predict sales for a given budget array using model + scaler"""
    x = pd.DataFrame([dict(zip(channel_names, budgets))])
    scaled = scaler.transform(x)
    pred = model.predict(scaled)[0]
    return pred

def objective(budgets):
    """Negative sales for minimization (we maximize sales)"""
    return -predict_sales(budgets)

# Bounds for each channel
bounds = [(min_budget, max_budget) for _ in channel_names]

# Constraint: sum of budgets = total_budget
constraints = ({
    'type': 'eq',
    'fun': lambda x: total_budget - np.sum(x)
})

if st.sidebar.button("Optimize Budget Allocation"):
    # Initial guess: equally distribute
    initial_guess = [total_budget / len(channel_names)] * len(channel_names)

    result = minimize(objective, initial_guess, method='SLSQP', bounds=bounds, constraints=constraints)

    if result.success:
        optimized_budgets = result.x
        predicted_sales = -result.fun

        st.subheader("✅ Optimal Budget Allocation")
        for ch, val in zip(channel_names, optimized_budgets):
            st.write(f"{ch}: ₹{val:,.2f}")

        st.success(f"💰 Predicted Maximum Sales: ₹{predicted_sales:,.2f}")
    else:
        st.error("Optimization failed. Try adjusting constraints or total budget.")

# ---------------- Optional: Predict for manual input ----------------
st.sidebar.header("Or Predict Sales for Custom Budget")
user_input = {}
for ch in channel_names:
    user_input[ch] = st.sidebar.number_input(f"Budget for {ch}", min_value=0.0, value=1000.0, key=ch+"_manual")

if st.sidebar.button("Predict Sales"):
    x = pd.DataFrame([user_input])
    scaled = scaler.transform(x)
    pred = model.predict(scaled)[0]
    st.success(f"Predicted Sales: ₹{pred:,.2f}")
