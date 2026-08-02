import streamlit as st
import pandas as pd
import joblib

# ============================================
# Page Configuration
# ============================================

st.set_page_config(
    page_title="Customer Lifetime Value Prediction",
    page_icon="🛍️",
    layout="centered"
)

# ============================================
# Title
# ============================================

st.title("🛍️ Customer Lifetime Value Prediction & Segmentation")

st.write(
    """
Predict a customer's **Customer Lifetime Value (CLV)** and identify
their **customer segment** using Machine Learning.
"""
)

st.divider()

# ============================================
# Load Models
# ============================================

clv_model = joblib.load("../models/clv_model.pkl")
kmeans_model = joblib.load("../models/kmeans_model.pkl")
scaler = joblib.load("../models/scaler.pkl")

# ============================================
# Sidebar
# ============================================

st.sidebar.header("Enter Customer Details")

recency = st.sidebar.number_input(
    "Recency (Days)",
    min_value=1,
    value=30
)

frequency = st.sidebar.number_input(
    "Frequency",
    min_value=1,
    value=5
)

monetary = st.sidebar.number_input(
    "Total Amount Spent (Monetary)",
    min_value=0.0,
    value=1000.0,
    step=100.0
)

tenure = st.sidebar.number_input(
    "Customer Tenure (Days)",
    min_value=0,
    value=100
)

purchase_frequency = st.sidebar.number_input(
    "Purchase Frequency",
    min_value=0.0,
    value=0.050,
    format="%.3f"
)

# ============================================
# Prediction
# ============================================

if st.sidebar.button("Predict"):

    # Prepare input for Linear Regression model
    input_df = pd.DataFrame({
        "Recency": [recency],
        "Frequency": [frequency],
        "CustomerTenure": [tenure],
        "PurchaseFrequency": [purchase_frequency]
    })

    # Predict CLV
    predicted_clv = clv_model.predict(input_df)[0]

    # Prepare input for KMeans
    cluster_input = pd.DataFrame({
        "Recency": [recency],
        "Frequency": [frequency],
        "Monetary": [monetary]
    })

    # Scale features
    cluster_scaled = scaler.transform(cluster_input)

    # Predict cluster
    cluster = kmeans_model.predict(cluster_scaled)[0]

    # Customer segment names
    cluster_names = {
        0: "Regular Customers",
        1: "At-Risk Customers",
        2: "VIP Customers",
        3: "Premium Customers",
        4: "Loyal Customers"
    }

    # ============================================
    # Results
    # ============================================

    st.success("Prediction completed successfully!")

    st.divider()

    st.subheader("Customer Summary")

    st.dataframe(input_df, use_container_width=True)

    st.divider()

    st.subheader("Prediction Results")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Predicted CLV",
            value=f"₹ {predicted_clv:,.2f}"
        )

    with col2:
        st.metric(
            label="Customer Segment",
            value=cluster_names[cluster]
        )

    st.divider()

    st.subheader("Business Insight")

    if predicted_clv >= 10000:
        st.success(
            "💎 This customer has a **high predicted lifetime value**. "
            "Consider offering premium memberships, exclusive rewards, and personalized recommendations."
        )

    elif predicted_clv >= 3000:
        st.info(
            "⭐ This customer has a **moderate lifetime value**. "
            "Target them with loyalty programs and personalized offers to increase retention."
        )

    else:
        st.warning(
            "⚠️ This customer has a **relatively low predicted lifetime value**. "
            "Consider promotional discounts and engagement campaigns to encourage repeat purchases."
        )

st.markdown("---")
st.caption(
    "Developed using Streamlit, Scikit-learn, and the Online Retail II Dataset "
    "as part of the IIT Jammu Data Science Internship Capstone Project."
)