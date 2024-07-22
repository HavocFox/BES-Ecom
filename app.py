from flask import Flask
from database import db
from models.schemas import ma
from limiter import limiter
from caching import cache

from models.customer import Customer
from models.product import Product
from models.order import Order
from models.orderproduct import order_product

from routes.customerBP import customer_blueprint
from routes.productBP import product_blueprint
from routes.orderBP import order_blueprint


def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)
    cache.init_app(app)
    limiter.init_app(app)
    
    
    return app

def blueprint_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')
    app.register_blueprint(product_blueprint, url_prefix='/products')
    app.register_blueprint(order_blueprint, url_prefix='/orders')

def rate_limit_config(app):
    limiter.limit("200 per day, 3 per second")(customer_blueprint)
    limiter.limit("200 per day, 3 per second")(product_blueprint)
    limiter.limit("200 per day, 3 per second")(order_blueprint)


if __name__ == '__main__':
    app = create_app('DevelopmentConfig')

    blueprint_config(app)

    rate_limit_config(app)

    with app.app_context():
        #db.drop_all()
        db.create_all()

    app.run()


    # irrelevant to app but putting notes here because then I'll look at them so much
    # I'll never forget them.

    # Left join - shows data from left table and matching from right.
