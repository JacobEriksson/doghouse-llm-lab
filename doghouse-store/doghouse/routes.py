from flask import render_template, request, redirect, url_for
from .models import products
from .chatbot import chat_handler


def init_routes(app):
    """
    Initialize all routes for the Flask application.
    """

    # Home Page
    @app.route('/')
    def home():
        return render_template('home.html')
    
    # Product List Page
    @app.route('/products')
    def product_list():
        return render_template('products.html', products=products)
    
    # Product Detail Page
    @app.route('/product/<int:id>')
    def product_detail(id):
        product = next((item for item in products if item['id'] == id), None)
        return render_template('product.html', product=product)
    
    # Purchase Route
    @app.route('/purchase/<int:id>', methods=['POST'])
    def purchase(id):
        product = next((item for item in products if item['id'] == id), None)
        if product:
            return redirect(url_for('checkout', product_name=product['name']))
        return redirect(url_for('product_list'))
    
    # Checkout Page
    @app.route('/checkout')
    def checkout():
        product_name = request.args.get('product_name')
        return render_template('checkout.html', product_name=product_name)
    
    # About Page
    @app.route('/about')
    def about():
        return render_template('about.html')
    
    # Chatbot Page
    @app.route('/chatbot')
    def chatbot():
        return render_template('chatbot.html')
    
    # API Chat Endpoint
    @app.route('/api/chat', methods=['POST'])
    def chat():
        return chat_handler(request)
