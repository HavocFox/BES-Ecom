from marshmallow import fields
from . import ma

class OrderSchema(ma.Schema):
    id = fields.Integer(required=False)
    date = fields.Date(required=False)
    customer_id = fields.Integer(required=True)
    products = fields.Nested("ProductSchema", many=True)
    customer = fields.Nested("CustomerOrderSchema")
    
    class Meta:
        fields = ('id', 'date', 'customer_id', 'product_ids', 'products', 'customer')

# Create an instance of the OrderSchema
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)  # For handling multiple orders