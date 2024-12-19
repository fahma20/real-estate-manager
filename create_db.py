
from models import Property, Tenant, Lease, Payment

# Create necessary tables (if not already created)
Property.create('Property Name', 'Location', 1200.50)
Tenant.create('John', 'Doe', '555-1234', 'john@example.com')
Lease.create(1, 1, '2024-01-01', '2025-01-01')
Payment.create(1, 1200.50, '2024-01-05')
