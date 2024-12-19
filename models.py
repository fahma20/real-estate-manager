from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the base class for all models
Base = declarative_base()

# Database setup
DATABASE_URL = "sqlite:///real_estate.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)
session = Session()

# Property model
class Property(Base):
    __tablename__ = 'properties'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    rent_cost = Column(Float, nullable=False)

    # Relationship to Lease
    leases = relationship("Lease", back_populates="property")

    @staticmethod
    def create(name, location, rent_cost):
        property = Property(name=name, location=location, rent_cost=rent_cost)
        session.add(property)
        session.commit()

    @staticmethod
    def delete(property_id):
        property = session.query(Property).filter(Property.id == property_id).first()
        if property:
            session.delete(property)
            session.commit()

    @staticmethod
    def get_all():
        return session.query(Property).all()

    @staticmethod
    def find_by_id(property_id):
        return session.query(Property).filter(Property.id == property_id).first()

    @staticmethod
    def find_by_name(name):
        return session.query(Property).filter(Property.name.ilike(f'%{name}%')).all()


# Tenant model
class Tenant(Base):
    __tablename__ = 'tenants'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)

    # Relationship to Lease
    leases = relationship("Lease", back_populates="tenant")

    @staticmethod
    def create(first_name, last_name, phone, email):
        tenant = Tenant(first_name=first_name, last_name=last_name, phone=phone, email=email)
        session.add(tenant)
        session.commit()

    @staticmethod
    def delete(tenant_id):
        tenant = session.query(Tenant).filter(Tenant.id == tenant_id).first()
        if tenant:
            session.delete(tenant)
            session.commit()

    @staticmethod
    def get_all():
        return session.query(Tenant).all()

    @staticmethod
    def find_by_id(tenant_id):
        return session.query(Tenant).filter(Tenant.id == tenant_id).first()

    @staticmethod
    def find_by_email(email):
        return session.query(Tenant).filter(Tenant.email == email).first()


# Lease model
class Lease(Base):
    __tablename__ = 'leases'

    id = Column(Integer, primary_key=True)
    tenant_id = Column(Integer, ForeignKey('tenants.id'), nullable=False)
    property_id = Column(Integer, ForeignKey('properties.id'), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    tenant = relationship("Tenant", back_populates="leases")
    property = relationship("Property", back_populates="leases")

    @staticmethod
    def create(tenant_id, property_id, start_date, end_date):
        lease = Lease(tenant_id=tenant_id, property_id=property_id, start_date=start_date, end_date=end_date)
        session.add(lease)
        session.commit()

    @staticmethod
    def get_all():
        return session.query(Lease).all()

    @staticmethod
    def find_by_id(lease_id):
        return session.query(Lease).filter(Lease.id == lease_id).first()

    @staticmethod
    def find_by_tenant(tenant_id):
        return session.query(Lease).filter(Lease.tenant_id == tenant_id).all()

    @staticmethod
    def find_by_property(property_id):
        return session.query(Lease).filter(Lease.property_id == property_id).all()


# Payment model
class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    lease_id = Column(Integer, ForeignKey('leases.id'), nullable=False)
    amount = Column(Float, nullable=False)
    payment_date = Column(Date, nullable=False)

    lease = relationship("Lease")

    @staticmethod
    def create(lease_id, amount, payment_date):
        payment = Payment(lease_id=lease_id, amount=amount, payment_date=payment_date)
        session.add(payment)
        session.commit()

    @staticmethod
    def get_all():
        return session.query(Payment).all()

    @staticmethod
    def find_by_lease(lease_id):
        return session.query(Payment).filter(Payment.lease_id == lease_id).all()


# Create tables if they don't exist
Base.metadata.create_all(engine)
