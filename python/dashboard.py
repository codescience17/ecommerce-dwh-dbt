import streamlit as st
import pandas as pd
from pathlib import Path

st.title("📊 Ecommerce Analytics Dashboard")

# project root = ecommerce_dwh
BASE_DIR = Path(__file__).resolve().parent

# go up one level from python/ → ecommerce_dwh/
PROJECT_ROOT = BASE_DIR.parent

data_dir = PROJECT_ROOT / "data" / "raw"

orders = pd.read_csv(data_dir / "orders.csv")
customers = pd.read_csv(data_dir / "customers.csv")

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