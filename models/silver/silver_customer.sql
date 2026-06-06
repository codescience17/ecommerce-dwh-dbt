SELECT
    customer_id,
    TRIM(customer_name) AS customer_name,
    LOWER(email) AS email,
    city,
    country
FROM {{ ref('bronze_customers') }}
WHERE customer_id IS NOT NULL