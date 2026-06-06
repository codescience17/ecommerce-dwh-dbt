SELECT
    order_id,
    customer_id,
    product_id,
    order_date,
    quantity,
    amount
FROM {{ ref('bronze_orders') }}
WHERE amount > 0