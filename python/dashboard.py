import os
import subprocess
import streamlit as st
import duckdb
import pandas as pd

# build warehouse if not exists

# connect to dbt warehouse
con = duckdb.connect("ecommerce_dwh/dev.duckdb")

st.title("📊 Ecommerce Analytics Dashboard")

# Load data
orders = con.execute("SELECT * FROM fact_orders").fetchdf()
customers = con.execute("SELECT * FROM dim_customer").fetchdf()

# KPIs
total_orders = len(orders)
total_customers = len(customers)
total_revenue = orders["amount"].sum()

st.metric("Total Orders", total_orders)
st.metric("Total Customers", total_customers)
st.metric("Total Revenue", total_revenue)

st.divider()

# Revenue by customer
merged = orders.merge(customers, on="customer_id", how="left")
revenue_by_customer = merged.groupby("customer_name")["amount"].sum().reset_index()

st.subheader("Revenue by Customer")
st.bar_chart(revenue_by_customer.set_index("customer_name"))

# Orders table
st.subheader("Orders Data")
st.dataframe(orders)