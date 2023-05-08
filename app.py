import os.path

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "db.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# init db
db = SQLAlchemy(app)

# init ma
ma = Marshmallow(app)


@app.errorhandler(404)
def pageNotFound(error):
    error_message = {"error": str(error)}
    return jsonify(error_message), 404


@app.errorhandler(400)
def handle_bad_request(error):
    error_message = {"error": str(error)}
    return jsonify(error_message), 400


@app.errorhandler(500)
def internal_error(error):
    error_message = {"error": str(error)}
    return jsonify(error_message), 500


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


# product schema
class CustomerSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "email", "password")


# init schema
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)


# Product Class
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    price = db.Column(db.Float)
    vendor_id = db.Column(db.Integer)

    def __init__(self, name, description, price, vendor_id):
        self.name = name
        self.description = description
        self.price = price
        self.vendor_id = vendor_id


# product schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description", "price", "vendor_id")


# init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    total = db.Column(db.Float)
    vendor_id = db.Column(db.Integer)
    status = db.Column(db.String(100))

    def __init__(self, customer_id, product_id, quantity, total, vendor_id, status):
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.total = total
        self.vendor_id = vendor_id
        self.status = status


# product schema
class OrderSchema(ma.Schema):
    class Meta:
        fields = ("id", "customer_id", "product_id", "quantity", "total", "vendor_id", "status")


# init schema
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)


# Create routes
@app.route('/product', methods=["POST"])
def create_product():
    product_details = request.get_json()
    name = product_details["name"]
    description = product_details["description"]
    price = product_details["price"]
    vendor_id = product_details["vendor_id"]

    new_product = Product(name, description, price, vendor_id)

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product), 201


@app.route('/products', methods=["GET"])
def get_all_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)

    return jsonify(result), 200


@app.route('/product/<int:id>', methods=["GET"])
def get_product_by_id(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product), 200


@app.route('/product/<int:id>', methods=["PUT"])
def update_product(id):
    product = Product.query.get(id)

    product_details = request.get_json()

    name = product_details["name"]
    description = product_details["description"]
    price = product_details["price"]
    vendor_id = product_details["vendor_id"]

    product.name = name
    product.description = description
    product.price = price
    product.vendor_id = vendor_id

    db.session.commit()

    return product_schema.jsonify(product), 200


@app.route('/product/<int:id>', methods=["DELETE"])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return product_schema.jsonify(product), 200


@app.route('/vendor/<int:vendor_id>/orders', methods=["GET"])
def get_vendor_orders(vendor_id):
    orders = Order.query.filter_by(vendor_id=vendor_id).all()
    result = orders_schema.dump(orders)

    return jsonify(result), 200


@app.route('/order/<int:id>', methods=["GET"])
def get_order_by_id(id):
    order = Order.query.get(id)

    return order_schema.jsonify(order), 200


@app.route('/order', methods=["POST"])
def create_order():
    order_details = request.get_json()
    customer_id = order_details['customer_id']
    product_id = order_details['product_id']
    quantity = order_details['quantity']
    total = order_details['total']
    vendor_id = order_details['vendor_id']
    status = order_details['status']

    new_order = Order(customer_id, product_id, quantity, total, vendor_id, status)

    db.session.add(new_order)
    db.session.commit()

    return product_schema.jsonify(new_order), 201


@app.route('/order/<int:id>/status', methods=["PUT"])
def update_order_status(id):
    order = Order.query.get(id)
    status = request.json.get('status')
    order.status = status
    db.session.commit()

    return order_schema.jsonify(order), 200


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
