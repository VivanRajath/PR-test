import uuid
import time
import random

class Order:
    def __init__(self, customer, products):
        self.id = str(uuid.uuid4())
        self.customer = customer
        self.products = products
        self.status = "Pending"

    def calculate_total(self):
        return sum(item["price"] * item["qty"] for item in self.products)

class OrderProcessor:
    STATUSES = ["Pending", "Packed", "Shipped", "Out for Delivery", "Delivered"]

    def __init__(self):
        self.orders = []

    def create_order(self, customer, products):
        order = Order(customer, products)
        self.orders.append(order)
        print(f"Order created with ID {order.id}")
        return order

    def update_status(self, order):
        index = self.STATUSES.index(order.status)
        if index < len(self.STATUSES) - 1:
            order.status = self.STATUSES[index + 1]

    def process_orders(self):
        for order in self.orders:
            print(f"\nProcessing Order ID: {order.id}")
            while order.status != "Delivered":
                self.update_status(order)
                print(f"Status: {order.status}")
                time.sleep(random.uniform(0.5, 1.5))

def main():
    processor = OrderProcessor()

    products1 = [
        {"name": "Shoes", "price": 1200, "qty": 1},
        {"name": "T Shirt", "price": 500, "qty": 2}
    ]

    products2 = [
        {"name": "Laptop", "price": 55000, "qty": 1},
        {"name": "Mouse", "price": 700, "qty": 1}
    ]

    order1 = processor.create_order("Rahul", products1)
    order2 = processor.create_order("Priya", products2)

    print("\nTotal for Order 1:", order1.calculate_total())
    print("Total for Order 2:", order2.calculate_total())

    processor.process_orders()

if __name__ == "__main__":
    main()
