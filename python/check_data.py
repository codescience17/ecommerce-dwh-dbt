import duckdb

# connect to warehouse
con = duckdb.connect('../ecommerce_dwh/dev.duckdb')

# show tables
tables = con.execute("SHOW TABLES").fetchall()

print("===== TABLES =====")
print(tables)

# dimension table
print("\n===== DIM CUSTOMER =====")
dim_customer = con.execute(
    "SELECT * FROM dim_customer"
).fetchdf()

print(dim_customer)

# fact table
print("\n===== FACT ORDERS =====")
fact_orders = con.execute(
    "SELECT * FROM fact_orders"
).fetchdf()

print(fact_orders)