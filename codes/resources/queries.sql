CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    order_date DATE NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    price_per_unit DECIMAL(10, 2) NOT NULL CHECK (price_per_unit > 0),
    total_amount DECIMAL(10, 2) GENERATED ALWAYS AS (quantity * price_per_unit) STORED,
    status VARCHAR(50) CHECK (status IN ('Pending', 'Shipped', 'Delivered', 'Cancelled'))
);


INSERT INTO orders (customer_name, product_name, order_date, quantity, price_per_unit, status)
VALUES
    ('Alice Johnson', 'Laptop', '2024-11-01', 1, 1200.00, 'Shipped'),
    ('Bob Smith', 'Smartphone', '2024-11-02', 2, 699.99, 'Delivered'),
    ('Charlie Brown', 'Tablet', '2024-11-03', 1, 350.00, 'Pending'),
    ('Diana Prince', 'Monitor', '2024-11-04', 2, 200.00, 'Shipped'),
    ('Eve Adams', 'Keyboard', '2024-11-05', 3, 30.00, 'Cancelled'),
    ('Frank Castle', 'Mouse', '2024-11-06', 5, 15.00, 'Pending'),
    ('Grace Hopper', 'Headphones', '2024-11-07', 2, 80.00, 'Delivered'),
    ('Henry Ford', 'Webcam', '2024-11-08', 1, 100.00, 'Shipped'),
    ('Ivy Carter', 'Printer', '2024-11-09', 1, 150.00, 'Delivered'),
    ('Jack Daniels', 'Router', '2024-11-10', 1, 75.00, 'Pending'),
    ('Karen Walker', 'External Hard Drive', '2024-11-11', 1, 120.00, 'Cancelled'),
    ('Liam Neeson', 'Flash Drive', '2024-11-12', 10, 10.00, 'Delivered'),
    ('Mary Jane', 'Speakers', '2024-11-13', 1, 60.00, 'Shipped'),
    ('Nathan Drake', 'Gaming Console', '2024-11-14', 1, 400.00, 'Pending'),
    ('Olivia Wilde', 'Smartwatch', '2024-11-15', 2, 250.00, 'Delivered'),
    ('Paul Atreides', 'Projector', '2024-11-16', 1, 500.00, 'Shipped'),
    ('Quinn Fabray', 'Fitness Tracker', '2024-11-17', 2, 75.00, 'Cancelled'),
    ('Ryan Reynolds', 'Drone', '2024-11-18', 1, 800.00, 'Pending'),
    ('Sophia Loren', 'Camera', '2024-11-19', 1, 1200.00, 'Delivered'),
    ('Tom Holland', 'Tripod', '2024-11-20', 2, 50.00, 'Shipped');