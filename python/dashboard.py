import streamlit as st
import pandas as pd

st.title("📊 Ecommerce Analytics Dashboard")

# Load data directly from repo
orders = pd.read_csv("ecommerce_dwh/data/raw/orders.csv")
customers = pd.read_csv("ecommerce_dwh/data/raw/customers.csv")

# KPIs
st.metric("Total Orders", len(orders))
st.metric("Total Customers", customers["customer_id"].nunique())
st.metric("Total Revenue", orders["amount"].sum())

# Merge for analytics
merged = orders.merge(customers, on="customer_id", how="left")

st.subheader("Revenue by Customer")
revenue = merged.groupby("customer_name")["amount"].sum().reset_index()

st.bar_chart(revenue.set_index("customer_name"))

st.dataframe(orders)