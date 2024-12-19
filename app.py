from flask import Flask, render_template

app = Flask(__name__)

# Sample product data
# Sample product data with images
products = [
    {'id': 1, 'name': 'Product 1', 'price': 10.00, 'image': 'images/product1.jpeg'},
    {'id': 2, 'name': 'Product 2', 'price': 20.00, 'image': 'images/product2.jpeg'},
    {'id': 3, 'name': 'Product 3', 'price': 30.00, 'image': 'images/product3.jpeg'},
]
@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    return render_template('product.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)