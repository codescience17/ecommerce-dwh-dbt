SELECT DISTINCT
    customer_id,
    customer_name,
    city,
    country
FROM {{ ref('silver_customer') }}