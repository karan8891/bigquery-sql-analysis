SELECT
  EXTRACT(YEAR FROM signup_date) AS signup_year,
  COUNT(*) AS customer_count
FROM ecommerce_data.customers
GROUP BY signup_year
ORDER BY signup_year;
