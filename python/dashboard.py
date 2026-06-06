import streamlit as st
import pandas as pd
from pathlib import Path

st.title("📊 Ecommerce Analytics Dashboard")

# get correct base path
BASE_DIR = Path(__file__).resolve().parent.parent

orders_path = BASE_DIR / "ecommerce_dwh" / "data" / "raw" / "orders.csv"
customers_path = BASE_DIR / "ecommerce_dwh" / "data" / "raw" / "customers.csv"

orders = pd.read_csv(orders_path)
customers = pd.read_csv(customers_path)

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