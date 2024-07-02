SELECT 
  o.product_id,
  p.product_name,
  SUM(o.quantity * o.price) AS total_sales,
  ROW_NUMBER() OVER (ORDER BY SUM(o.quantity * o.price) DESC) AS sales_rank
FROM ecommerce_data.orders o
INNER JOIN ecommerce_data.products p ON o.product_id = p.product_id
GROUP BY o.product_id, p.product_name
ORDER BY sales_rank;
