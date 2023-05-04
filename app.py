from flask import Flask, request, jsonify
import db_controller

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "hello world"


@app.route("/products", methods=["GET"])
def get_products():
    products = db_controller.get_products()
    return jsonify(products)


@app.route("/product", methods=["POST"])
def insert_product():
    product_details = request.get_json()
    id = product_details["id"]
    name = product_details["name"]
    description = product_details["description"]
    price = product_details["price"]
    vendor_id = product_details["vendor_id"]
    result = db_controller.insert_product(id, name, description, price, vendor_id)
    return jsonify(result)


@app.route("/product<int:id>", methods=["GET"])
def get_product_by_id(id):
    product = db_controller.get_product_by_id(id)
    return jsonify(product)


@app.route("/product", methods=["PUT"])
def update_product():
    product_details = request.get_json()
    id = product_details["id"]
    name = product_details["name"]
    description = product_details["description"]
    price = product_details["price"]
    vendor_id = product_details["vendor_id"]

    result = db_controller.update_product(id, name, description, price, vendor_id)
    return jsonify(result)


@app.route("/product/<int:id>", methods=["DELETE"])
def delete_product(id):
    result = db_controller.delete_product(id)
    return jsonify(result)


@app.route("/order/<int:vendor_id>", methods=["GET"])
def get_orders_by_vendor(vendor_id):
    result = get_orders_by_vendor(vendor_id)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)