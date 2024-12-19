from models import Property, Tenant, Lease, Payment
from datetime import datetime

def add_property_data():
    name = input("Property Name: ")
    location = input("Location: ")
    rent_cost = float(input("Rent Cost: "))
    Property.create(name, location, rent_cost)

def add_tenant_data():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    phone = input("Phone Number: ")
    email = input("Email Address: ")
    Tenant.create(first_name, last_name, phone, email)

def add_lease_data():
    tenant_id = int(input("Tenant ID: "))
    property_id = int(input("Property ID: "))
    start_date = input("Start Date (YYYY-MM-DD): ")
    end_date = input("End Date (YYYY-MM-DD): ")
    Lease.create(tenant_id, property_id, start_date, end_date)

def add_payment_data():
    lease_id = int(input("Lease ID: "))
    amount = float(input("Amount: "))
    payment_date = input("Payment Date (YYYY-MM-DD): ")
    Payment.create(lease_id, amount, payment_date)
