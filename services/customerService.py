from database import db
from models.customer import Customer
from sqlalchemy import select

def save(customer_data):
    new_customer = Customer(name=customer_data['name'], email=customer_data['email'], password=customer_data['password'], phone=customer_data['phone'], username=customer_data['username'])
    db.session.add(new_customer)
    db.session.commit()

    db.session.refresh(new_customer)
    return new_customer

def find_all():

    query = select(Customer)
    all_customers = db.session.execute(query).scalars().all()
    return all_customers