WITH purchase_counts AS (
  SELECT
    customer_id,
    COUNT(*) AS purchase_count
  FROM `ecommerce_data.orders`
  GROUP BY customer_id
)
SELECT
  pc.customer_id,
  pc.purchase_count,
  NTILE(4) OVER (ORDER BY pc.purchase_count DESC) AS purchase_quartile
FROM purchase_counts AS pc
ORDER BY purchase_quartile DESC, purchase_count DESC;
