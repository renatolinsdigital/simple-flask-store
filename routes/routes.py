from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError  # Import IntegrityError
from db_models.models import db, Product, CartItem, Cart, User

# Create a Blueprint instance for routes
bp = Blueprint('routes', __name__)

# Define your routes using the Blueprint


@bp.route('/')
def index():
    # Check if a user exists in the database
    user = User.query.first()
    if not user:
        # If no user is found, create a new user
        new_user = User(
            user_name='admin',
            email='user@admin.com',
            name='John Doe The Admin'
        )
        db.session.add(new_user)
        db.session.commit()
        # Reload the user object to ensure it's properly loaded
        user = User.query.first()

    # Retrieve all products from the database
    products = Product.query.all()
    # Render the index.html template with the products data
    return render_template('index.html', products=products, user=user)

# Route to add a product to the cart


@bp.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    # Get the product object based on the product_id
    product = Product.query.get_or_404(product_id)
    # Retrieve the quantity of the product from the form data
    quantity = int(request.form['quantity'])

    # Get the current user
    user = User.query.first()  # TODO: Must retrieve the logged-in user

    # Check if the user has a cart, create one if not
    if not user.cart:
        cart = Cart(total_price=0.0, user=user)
        db.session.add(cart)
        db.session.commit()

    # Check if the product is already in the cart
    cart_item = CartItem.query.filter_by(
        product_id=product_id, cart_id=user.cart.id).first()
    if cart_item:
        # Update the quantity and total price of the existing cart item
        cart_item.quantity += quantity
        cart_item.total_price = cart_item.quantity * product.price
    else:
        # Calculate the total price for the new cart item
        total_price = product.price * quantity
        # Create a new cart item in the database
        cart_item = CartItem(product_id=product_id, quantity=quantity,
                             total_price=total_price, cart_id=user.cart.id)
        db.session.add(cart_item)

    # Commit the changes to the database
    db.session.commit()
    # Flash a success message
    flash('Product added to cart successfully!', 'success')
    # Redirect to the home page
    return redirect(url_for('routes.index'))

# Route to create a new product


@bp.route('/create_product', methods=['GET', 'POST'])
def create_product():
    # Check if the request method is POST and the user is 'admin'
    if request.method == 'POST' and User.query.filter_by(user_name='admin').first():
        # Retrieve product code, name, and price from the form data
        code = request.form['code']
        name = request.form['name']
        price = float(request.form['price'])

        # Create a new product in the database
        product = Product(name=name, price=price, code=code)
        db.session.add(product)

        try:
            db.session.commit()  # Try committing the changes
            # Flash a success message
            flash('Product created successfully!', 'success')
        except IntegrityError:
            db.session.rollback()  # Rollback the transaction
            # Flash a message indicating the code already exists
            flash('Product code already exists. Please choose a different code.', 'error')

        # Reloads as the proper way is having the function returning something
        return render_template('create_product.html')

    # Render the create_product.html template for GET requests or unauthorized POST requests
    return render_template('create_product.html')

# Route for the shopping cart


@bp.route('/cart')
def cart():
    # TODO: Retrieve the logged-in user's cart
    user_cart = User.query.first().cart

    if user_cart:
        # Retrieve all cart items associated with the user's cart
        cart_items = CartItem.query.filter_by(cart_id=user_cart.id).all()
        # Calculate the total cart price
        total_cart_price = sum(item.total_price for item in cart_items)

        # Ensure each CartItem object has a reference to its corresponding Product
        for item in cart_items:
            item.product = Product.query.get(item.product_id)

        # Render the cart.html template with the cart items and total cart price
        return render_template('cart.html', cart_items=cart_items, total_cart_price=total_cart_price)
    else:
        # Render the cart.html template with an empty cart message
        return render_template('cart.html', cart_items=[], total_cart_price=0)


# Return the Blueprint object for registration in app.py

def create_routes_blueprint():
    return bp
