---

# Real-time E-commerce Data Analysis Project Overview

## Objective
Perform comprehensive data analysis on a test e-commerce dataset to extract meaningful insights and drive business decisions.

## Steps Involved

### 1. Setup

- **Create BigQuery Environment:**
  Set up a BigQuery environment to store and analyze the dataset.
  
- **Dataset Creation:**
  Create a dataset named `ecommerce_data` in BigQuery.

### 2. Data Loading

- **Create Tables:**
  Define tables for orders, customers, and products within the `ecommerce_data` dataset.
  
- **Load Data:**
  Load CSV files (orders.csv, customers.csv, products.csv) into respective BigQuery tables using Google Cloud Storage.

### 3. Data Analysis

#### Basic Analysis

- **Total Sales by Product:**
  Calculate total sales for each product and rank them in descending order.
  
- **Customer Signup Analysis:**
  Extract signup year from `signup_date` and count new customer signups each year.

#### Advanced Analysis Using SQL

- **Rank Products by Sales:**
  Use SQL window functions to rank products based on total sales.

- **Calculate Running Total of Sales:**
  Determine daily sales and compute the cumulative total over time.

- **Customer Purchase Frequency Quartiles:**
  Divide customers into quartiles based on their purchase frequency using SQL's analytical functions.

### 4. Future Steps
- **Visualization:**
  Create visualizations (charts, graphs) to present key findings and insights from the analysis.

- **Report Generation:**
  Generate a detailed report summarizing findings and recommendations for stakeholders.
  
- **Automation and Scaling:**
  Explore opportunities for automating data loading and analysis processes.
  
- **Advanced Analytics:**
  Consider implementing machine learning models for predictive analytics or segmentation.

---

This project overview provides a structured approach to performing real-time data analysis on an e-commerce dataset, ensuring clarity and direction throughout the process.
