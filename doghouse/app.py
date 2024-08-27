from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

# Sample data
products = [
    {'id': 1, 'name': 'Doghouse Classic', 'price': 49.99, 'description': 'A cozy place for your dog to rest.'},
    {'id': 2, 'name': 'Deluxe Doghouse', 'price': 89.99, 'description': 'A luxurious doghouse with extra space.'},
    {'id': 3, 'name': 'Portable Doghouse', 'price': 39.99, 'description': 'A lightweight doghouse perfect for travel.'},
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def product_list():
    return render_template('products.html', products=products)

@app.route('/product/<int:id>')
def product_detail(id):
    product = next((item for item in products if item['id'] == id), None)
    return render_template('product.html', product=product)

@app.route('/purchase/<int:id>', methods=['POST'])
def purchase(id):
    product = next((item for item in products if item['id'] == id), None)
    if product:
        return redirect(url_for('checkout', product_name=product['name']))
    return redirect(url_for('product_list'))

@app.route('/checkout')
def checkout():
    product_name = request.args.get('product_name')
    return render_template('checkout.html', product_name=product_name)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
