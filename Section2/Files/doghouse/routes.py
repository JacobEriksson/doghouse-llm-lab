from flask import render_template, request, redirect, url_for
from .models import products
from .designer import generate_doghouse_suggestion, get_user_ip
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
    
    # Designer Form Page
    @app.route('/designer', methods=['GET', 'POST'])
    def designer():
        if request.method == 'POST':
            style = request.form['style']
            size = request.form['size']
            color = request.form['color']
            # location = request.form['location']
            return redirect(url_for('confirm', style=style, size=size, color=color))
        return render_template('designer.html')
    
    # Design Confirmation Page
    @app.route('/confirm', methods=['GET', 'POST'])
    def confirm():
        if request.method == 'POST':
            suggestion, image_url = generate_doghouse_suggestion(request)
            return redirect(url_for('result', suggestion=suggestion, image_url=image_url))

        # Retrieve query parameters if GET method is used
        style = request.args.get('style')
        size = request.args.get('size')
        color = request.args.get('color')
        # location = request.args.get('location')
        return render_template('confirm.html', style=style, size=size, color=color)
    
    # Result Page
    @app.route('/result')
    def result():
        suggestion = request.args.get('suggestion')
        image_url = request.args.get('image_url')    
        return render_template('result.html', suggestion=suggestion, image_url=image_url)
