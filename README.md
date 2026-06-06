# Ecommerce Data Warehouse Project

## Live dashboard https://ecommerce-dwh-dbt-eisfmmhi2aegpbgsljbbds.streamlit.app/
 

## Overview

This project demonstrates a modern analytics engineering workflow using dbt and DuckDB following Medallion Architecture principles.

The pipeline ingests raw ecommerce CSV data, transforms it through Bronze, Silver, and Gold layers, and creates analytics-ready dimensional models.

---

## Architecture

### Bronze Layer

* Raw ingestion of source CSV files
* Minimal transformations
* Preserves source data

### Silver Layer

* Data cleansing and standardization
* Validation rules applied
* Trusted intermediate layer

### Gold Layer

* Kimball dimensional modeling
* Fact and dimension tables
* Analytics-ready datasets

---

## Technologies Used

* dbt
* DuckDB
* SQL
* Python
* YAML

---

## Data Models

### Dimension Tables

* dim_customer

### Fact Tables

* fact_orders

---

## Data Quality Tests

Implemented dbt tests for:

* uniqueness
* not null validation

---

## Project Structure

ecommerce-dwh-project/
│
├── data/
├── ecommerce_dwh/
├── python/
├── docs/
└── README.md

---

## Key Concepts Demonstrated

* Medallion Architecture
* dbt transformations
* Data lineage
* Kimball dimensional modeling
* Data quality testing
* Warehouse layering
