import os
from db_models.models import db, Product, Order
from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create a Flask application instance
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY') 

# Handling Database URL
db_path = os.getenv('DATABASE_PATH') 
if not db_path:
    raise RuntimeError("DATABASE_PATH is not set")
os.makedirs(db_path, exist_ok=True)

app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}/store.db"

# Initialize the Flask application with the database
db.init_app(app)

# Route for the home page
@app.route('/')
def index():
    # Retrieve all products from the database
    products = Product.query.all()
    # Render the index.html template with the products data
    return render_template('index.html', products=products)

# Route to add a product to the cart
@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    # Get the product object based on the product_id
    product = Product.query.get_or_404(product_id)
    # Retrieve the quantity of the product from the form data
    quantity = int(request.form['quantity'])

    # Check if the product is already in the cart
    existing_order = Order.query.filter_by(product_id=product_id).first()
    if existing_order:
        # Update the quantity and total price of the existing order
        existing_order.quantity += quantity
        existing_order.total_price = existing_order.quantity * product.price
    else:
        # Calculate the total price for the new order
        total_price = product.price * quantity
        # Create a new order in the database
        order = Order(product_id=product_id, quantity=quantity,
                      total_price=total_price, user_email='example@email.com')
        db.session.add(order)

    # Commit the changes to the database
    db.session.commit()
    # Flash a success message
    flash('Product added to cart successfully!', 'success')
    # Redirect to the home page
    return redirect(url_for('index'))

# Route to create a new product
@app.route('/create_product', methods=['GET', 'POST'])
def create_product():
    if request.method == 'POST':
        # Retrieve product name and price from the form data
        name = request.form['name']
        price = float(request.form['price'])
        # Create a new product in the database
        product = Product(name=name, price=price)
        db.session.add(product)
        db.session.commit()
        # Flash a success message
        flash('Product created successfully!', 'success')
        # Redirect to the home page
        return redirect(url_for('index'))
    # Render the create_product.html template for GET requests
    return render_template('create_product.html')

# Route for the shopping cart
@app.route('/cart')
def cart():
    # Retrieve all items in the cart from the database
    cart_items = Order.query.all()
    # Calculate the total cart price
    total_cart_price = sum(item.total_price for item in cart_items)
    # Render the cart.html template with the cart items and total cart price
    return render_template('cart.html', cart_items=cart_items, total_cart_price=total_cart_price)

# Entry point for running the Flask application
if __name__ == '__main__':
    with app.app_context():
        # Create tables in the database if they don't exist
        db.create_all()
    # Run the Flask application with debugging enabled on the specified port
    app.run(debug=True, port=os.getenv('PORT') )
