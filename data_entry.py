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

def get_all_properties():
    properties = Property.get_all()
    for property in properties:
        print(f"{property.id}: {property.name} located at {property.location} with rent cost {property.rent_cost}")

def get_all_tenants():
    tenants = Tenant.get_all()
    for tenant in tenants:
        print(f"{tenant.id}: {tenant.first_name} {tenant.last_name}, {tenant.phone}, {tenant.email}")

def delete_property():
    property_id = int(input("Enter property ID to delete: "))
    Property.delete(property_id)

def delete_tenant():
    tenant_id = int(input("Enter tenant ID to delete: "))
    Tenant.delete(tenant_id)
