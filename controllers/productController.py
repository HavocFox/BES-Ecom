from flask import request, jsonify
from models.schemas.productSchema import product_schema, products_schema
from services import productService
from marshmallow import ValidationError
from caching import cache


def save(): #name the controller the same as the service function

    try:
        #try to validate the incoming data, and deserialize
        product_data = product_schema.load(request.json)

    except ValidationError as e:
        return jsonify(e.messages), 400
    
    product_saved = productService.save(product_data)
    return product_schema.jsonify(product_data), 201

@cache.cached(timeout=60)
def find_all():
    all_products = productService.find_all()
    return products_schema.jsonify(all_products), 201
