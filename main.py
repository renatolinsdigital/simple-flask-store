from flask import Flask, render_template, request, redirect, url_for, flash
from db_models.models import db, Product, Order

app = Flask(__name__)
app.secret_key = 'secreto'  # Chave secreta para sessões
# Caminho para o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
db.init_app(app)

# Rota para a página inicial


@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

# Rota para adicionar um produto ao carrinho


@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)
    quantity = int(request.form['quantity'])

    # Verifica se o produto já está no carrinho
    existing_order = Order.query.filter_by(product_id=product_id).first()
    if existing_order:
        existing_order.quantity += quantity
        existing_order.total_price = existing_order.quantity * product.price
    else:
        total_price = product.price * quantity
        order = Order(product_id=product_id, quantity=quantity,
                      total_price=total_price, user_email='example@email.com')
        db.session.add(order)

    db.session.commit()
    flash('Produto adicionado ao carrinho com sucesso!', 'success')
    return redirect(url_for('index'))

# Rota para criar um novo produto


@app.route('/create_product', methods=['GET', 'POST'])
def create_product():
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        product = Product(name=name, price=price)
        db.session.add(product)
        db.session.commit()
        flash('Produto criado com sucesso!', 'success')
        return redirect(url_for('index'))
    return render_template('create_product.html')

# Rota para o carrinho de compras


@app.route('/cart')
def cart():
    cart_items = Order.query.all()
    total_cart_price = sum(item.total_price for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total_cart_price=total_cart_price)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados se não existirem
    app.run(debug=True, port=3000)
