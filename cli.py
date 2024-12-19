# cli.py
import sys
from models import Property, Tenant, Lease, Payment
from datetime import datetime

def validate_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None

def validate_id(id_str):
    try:
        return int(id_str)
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return None

def main():
    while True:
        print("\nReal Estate Manager CLI")
        print("1. Add Property")
        print("2. View All Properties")
        print("3. Delete Property")
        print("4. Find Property by Name")
        print("5. Add Tenant")
        print("6. View All Tenants")
        print("7. Delete Tenant")
        print("8. Find Tenant by Email")
        print("9. Add Lease")
        print("10. View All Leases")
        print("11. Find Leases by Tenant")
        print("12. Add Payment")
        print("13. View All Payments")
        print("14. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Property Name: ")
            location = input("Location: ")
            rent_cost = input("Rent Cost: ")
            Property.create(name, location, float(rent_cost))
            print("Property added successfully.")
        elif choice == '2':
            properties = Property.get_all()
            for property in properties:
                print(property)
        elif choice == '3':
            property_id = validate_id(input("Enter Property ID to delete: "))
            if property_id:
                Property.delete(property_id)
                print(f"Property {property_id} deleted.")
        elif choice == '4':
            name = input("Enter Property Name to search: ")
            properties = Property.find_by_name(name)
            for property in properties:
                print(property)
        elif choice == '5':
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            Tenant.create(first_name, last_name, phone, email)
            print("Tenant added successfully.")
        elif choice == '6':
            tenants = Tenant.get_all()
            for tenant in tenants:
                print(tenant)
        elif choice == '7':
            tenant_id = validate_id(input("Enter Tenant ID to delete: "))
            if tenant_id:
                Tenant.delete(tenant_id)
                print(f"Tenant {tenant_id} deleted.")
        elif choice == '8':
            email = input("Enter Tenant Email to search: ")
            tenant = Tenant.find_by_email(email)
            if tenant:
                print(tenant)
        elif choice == '9':
            tenant_id = validate_id(input("Enter Tenant ID: "))
            property_id = validate_id(input("Enter Property ID: "))
            start_date = input("Lease Start Date (YYYY-MM-DD): ")
            start_date = validate_date(start_date)
            end_date = input("Lease End Date (YYYY-MM-DD): ")
            end_date = validate_date(end_date)
            if start_date and end_date:
                Lease.create(tenant_id, property_id, start_date, end_date)
                print("Lease added successfully.")
        elif choice == '10':
            leases = Lease.get_all()
            for lease in leases:
                print(lease)
        elif choice == '11':
            tenant_id = validate_id(input("Enter Tenant ID to find leases: "))
            if tenant_id:
                leases = Lease.find_by_tenant(tenant_id)
                for lease in leases:
                    print(lease)
        elif choice == '12':
            lease_id = validate_id(input("Enter Lease ID: "))
            amount = float(input("Amount: "))
            payment_date = input("Payment Date (YYYY-MM-DD): ")
            payment_date = validate_date(payment_date)
            if payment_date:
                Payment.create(lease_id, amount, payment_date)
                print("Payment added successfully.")
        elif choice == '13':
            payments = Payment.get_all()
            for payment in payments:
                print(payment)
        elif choice == '14':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
