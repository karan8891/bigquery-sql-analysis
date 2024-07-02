import csv
from faker import Faker
from datetime import datetime, timedelta
import random

# Function to generate fake data for orders
def generate_orders(num_records, customer_ids, product_ids):
    fake = Faker()
    orders = []
    for _ in range(num_records):
        order_id = fake.uuid4()
        customer_id = random.choice(customer_ids)
        product_id = random.choice(product_ids)
        order_date = fake.date_between(start_date='-2y', end_date='today')
        quantity = random.randint(1, 10)
        price = round(random.uniform(10, 1000), 2)
        
        order_date_str = order_date.strftime('%Y-%m-%d')
        
        orders.append([order_id, customer_id, product_id, order_date_str, quantity, price])
    
    return orders

# Function to generate fake data for customers
def generate_customers(num_records):
    fake = Faker()
    customers = []
    for _ in range(num_records):
        customer_id = fake.uuid4()
        customer_name = fake.name()
        customer_email = fake.email()
        signup_date = fake.date_between(start_date='-5y', end_date='today')
        
        signup_date_str = signup_date.strftime('%Y-%m-%d')
        
        customers.append([customer_id, customer_name, customer_email, signup_date_str])
    
    return customers

# Function to generate fake data for products
def generate_products(num_records):
    fake = Faker()
    categories = ['Electronics', 'Clothing', 'Books', 'Home', 'Toys']
    products = []
    for _ in range(num_records):
        product_id = fake.uuid4()
        product_name = fake.word() + ' ' + fake.word()
        category = random.choice(categories)
        price = round(random.uniform(10, 1000), 2)
        
        products.append([product_id, product_name, category, price])
    
    return products

# Function to write data to CSV file
def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

if __name__ == '__main__':
    num_customers = 1000000  # Number of customers
    num_products = 100000  # Number of products
    num_orders = 3000000  # Number of orders
    
    # Generate customers
    customers_data = generate_customers(num_customers)
    write_to_csv('customers.csv', customers_data)
    print(f'{num_customers} customers generated and saved to customers.csv')
    
    # Generate products
    products_data = generate_products(num_products)
    write_to_csv('products.csv', products_data)
    print(f'{num_products} products generated and saved to products.csv')
    
    # Generate orders (requires customer and product IDs)
    customer_ids = [customer[0] for customer in customers_data]
    product_ids = [product[0] for product in products_data]
    orders_data = generate_orders(num_orders, customer_ids, product_ids)
    write_to_csv('orders.csv', orders_data)
    print(f'{num_orders} orders generated and saved to orders.csv')
