from flask import Flask, render_template
import database

app = Flask(__name__)

@app.route("/")
def suppliers():
    suppliers = database.get_all_suppliers()
    return render_template('index.html', suppliers=suppliers)

@app.route("/suppliers/<int:supplier_id>")
def products(supplier_id):
    products = database.get_supplier_products(supplier_id)
    return render_template('products.html', products=products)


@app.route("/category")
def category():
    products = database.get_all_categories()
    return render_template('category.html', products=products)


app.run(debug=True)