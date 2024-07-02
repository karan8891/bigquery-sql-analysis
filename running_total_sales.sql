WITH daily_saless AS (
    SELECT 
        order_date,
        SUM(price * quantity) AS daily_sales
    FROM 
        ecommerce_data.orders
    GROUP BY 
        order_date
    ORDER BY 
        order_date
)

SELECT 
    order_date,
    daily_sales,
    SUM(daily_sales) OVER (ORDER BY order_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total_sales
FROM 
    daily_saless
ORDER BY 
    order_date;
