from flask import Blueprint, render_template, request, redirect, url_for, flash
from db_models.models import db, Product, Order

# Create a Blueprint instance for routes
bp = Blueprint('routes', __name__)

# Define your routes using the Blueprint


@bp.route('/')
def index():
    # Retrieve all products from the database
    products = Product.query.all()
    # Render the index.html template with the products data
    return render_template('index.html', products=products)

# Route to add a product to the cart


@bp.route('/add_to_cart/<int:product_id>', methods=['POST'])
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
    return redirect(url_for('routes.index'))

# Route to create a new product


@bp.route('/create_product', methods=['GET', 'POST'])
def create_product():
    if request.method == 'POST':
        # Retrieve product name and price from the form data
        name = request.form['name']
        price = float(request.form['price'])
        # Create a new product in the database
        product = Product(name=name, price=price)
        db.session.add(product)
        db.session.commit()
        # Redirect to the home page
        return redirect(url_for('routes.index'))
    # Render the create_product.html template for GET requests
    return render_template('create_product.html')

# Route for the shopping cart


@bp.route('/cart')
def cart():
    # Retrieve all items in the cart from the database
    cart_items = Order.query.all()
    # Calculate the total cart price
    total_cart_price = sum(item.total_price for item in cart_items)

    # Ensure each Order object has a reference to its corresponding Product
    for item in cart_items:
        item.product = Product.query.get(item.product_id)

    # Render the cart.html template with the cart items and total cart price
    return render_template('cart.html', cart_items=cart_items, total_cart_price=total_cart_price)

# Return the Blueprint object for registration in app.py


def create_routes_blueprint():
    return bp
