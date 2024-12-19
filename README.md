# Real Estate Manager

## Project Description
The Real Estate Manager is a Python-based application for managing properties, tenants, leases, and payments. This application allows users to add, view, delete, and update property and tenant data, manage leases, and track payments for properties.

This application is ideal for small to medium-sized real estate portfolios or anyone needing an efficient tool to track rental properties and tenants.

## Features

The following features are available in the Real Estate Manager:

### **Add Property**
- Users can add a new property by specifying:
  - Property Name
  - Location
  - Rent Cost
  
### **Add Tenant**
- Users can add a new tenant by specifying:
  - First Name
  - Last Name
  - Phone Number
  - Email Address

### **Add Lease**
- Users can create lease agreements between tenants and properties, specifying:
  - Tenant ID
  - Property ID
  - Lease Start Date
  - Lease End Date

### **Add Payment**
- Users can log payments made against leases, with details such as:
  - Lease ID
  - Payment Amount
  - Payment Date

### **View All Properties, Tenants, and Leases**
- Users can view all records of properties, tenants, and leases currently stored in the system.

### **Delete Property/Tenant**
- Users can delete unwanted properties or tenants by specifying their unique IDs.

### **CLI Interaction**
- The application uses a simple text-based CLI to interact with the user.
- Prompts guide the user through various operations like adding, deleting, or viewing records.
  
## Technologies Used

The Real Estate Manager application is built using the following technologies:

### **[Python 3.8+](https://www.python.org/)**
- The programming language used for implementing the application. Python’s simplicity and readability make it an excellent choice for building CLI applications.

### **[SQLAlchemy](https://www.sqlalchemy.org/)**
- An Object-Relational Mapping (ORM) library used to simplify database interaction. SQLAlchemy provides a high-level abstraction layer for working with databases like SQLite.

### **[SQLite](https://www.sqlite.org/)**
- The database system used to store property, tenant, lease, and payment data. SQLite is lightweight, file-based, and works perfectly for small-scale applications like this one.

### **[Click](https://click.palletsprojects.com/)**
- A Python package used for creating the command-line interface (CLI). Click makes it easy to handle input and commands, ensuring a user-friendly experience when interacting with the application.

### **[Virtualenv](https://virtualenv.pypa.io/en/latest/)**
- Virtualenv is used for creating isolated Python environments, allowing the project to maintain dependencies without affecting the global Python environment.

### **[Git](https://git-scm.com/)**
- Git is used for version control, tracking changes to the project and collaborating with other developers.

### **[SQLite3 (Python Library)](https://docs.python.org/3/library/sqlite3.html)**
- Used for database connections and managing SQL queries. The `sqlite3` library integrates seamlessly with SQLAlchemy for executing SQL queries.

## Installation

Follow these simple steps to get the application running locally:

1. **Clone the repository:**

```git clone https://github.com/your-username/real-estate-manager.git```

2. **Navigate into the project directory:**

 ```cd real-estate-manager``

 3. **Set up the virtual environment with Pipenv: If you don’t have Pipenv installed, install it first:**

 ```pip install pipenv```

Then, run the following command to install the dependencies and activate the virtual environment:
```pipenv install```
```pipenv shell```

4. **Run the application:** After the environment is set up and the dependencies are installed, you can start the application by running:
```python cli.py```

This will start the CLI, allowing you to manage properties, tenants, leases, and payments through the terminal.

### License
This project is licensed under the MIT License

## Notes:
The project can be extended with additional features, such as updating existing records or generating reports.
Currently, the system supports only basic CRUD operations for managing properties, tenants, leases, and payments.

---

### **By: [Fahmo Abdisalan Musa](https://github.com/fahma20)**
