from config.database import db


class Product(db.Model):
    # Product model representing a product in the store
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    code = db.Column(db.String(50), unique=True, nullable=False)

    # Define a one-to-many relationship with CartItem model
    cart_items = db.relationship('CartItem', backref='product', lazy=True)

    def __repr__(self):
        return f'<Product {self.name}>'


class CartItem(db.Model):
    # CartItem model representing an item in a shopping cart
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)

    # Define foreign key relationships with Product and Cart models
    product_id = db.Column(db.Integer, db.ForeignKey(
        'product.id'), nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=False)

    def __repr__(self):
        return f'<CartItem {self.quantity} of {self.product.name}>'


class Cart(db.Model):
    # Cart model representing a user's shopping cart
    id = db.Column(db.Integer, primary_key=True)
    total_price = db.Column(db.Float, nullable=False)

    # Define a foreign key relationship to the User model
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id'), unique=True, nullable=False)

    # Define a one-to-many relationship with CartItem model
    items = db.relationship('CartItem', backref='cart', lazy=True)

    def __repr__(self):
        return f'<Cart {self.id}>'


class User(db.Model):
    # User model representing a registered user
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)

    # Define a one-to-one relationship with the Cart model
    cart = db.relationship('Cart', backref='user', uselist=False, lazy=True)

    def __repr__(self):
        return f'<User {self.id}>'
