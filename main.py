from flask import Flask, render_template, request, url_for, redirect, flash, session
from database import get_products, get_sales, insert_products, insert_sales, available_stock, get_connection, insert_stock, get_stock, check_user_exists, insert_user, sales_per_product, sales_per_day, profit_per_product, profit_per_day
from flask_bcrypt import Bcrypt
from functools import wraps

# Flask instance
app = Flask(__name__)

# creating the bcrypt object
bcrypt = Bcrypt(app)

# secret key--signs session data
app.secret_key = "17yajhsgihsfrwysmmkkihs89076$$3hhgdtshjus"


@app.route("/")
def home():
    return render_template("index.html")


def login_required(f):
    @wraps(f)
    def protected(*args, **kwargs):
        if 'email' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return protected


@app.route("/products")
@login_required
def fetch_products():
    products = get_products(session['user_id'])
    return render_template("products.html", products=products)


@app.route("/add_products", methods=['GET', 'POST'])
@login_required
def add_products():
    product_name = request.form["product_name"]
    buying_price = request.form["buying_price"]
    selling_price = request.form["selling_price"]
    new_product = (product_name, buying_price, selling_price, session['user_id'])
    insert_products(new_product)
    flash("product added successfully", 'success')
    return redirect(url_for('fetch_products'))


@app.route('/sales')
@login_required
def fetch_sales():
    sales = get_sales(session['user_id'])
    products = get_products(session['user_id'])
    return render_template("sales.html", sales=sales, products=products)


# posting sales
@app.route('/add_sale', methods=['GET', 'POST'])
@login_required
def add_sale():
    pid = request.form["pid"]
    quantity = request.form["quantity"]
    new_sale = (pid, quantity, session['user_id'])
    check_stock = available_stock(pid, session['user_id'])
    if check_stock < float(quantity):
        flash("Failed to make sale. Please try again.", "danger")
        return redirect(url_for('fetch_sales'))
    insert_sales(new_sale)
    flash("sale made successfully", 'success')
    return redirect(url_for('fetch_sales'))


# stock
@app.route('/stock')
@login_required
def fetch_stock():
    stock = get_stock(session['user_id'])
    return render_template('stock.html', stock=stock, products=get_products(session['user_id']))


@app.route('/add_stock', methods=['POST'])
@login_required
def add_stock():
    pid = request.form["pid"]
    quantity = request.form["quantity"]
    new_stock = (pid, quantity, session['user_id'])
    insert_stock(new_stock)
    flash("stock added successfully", 'success')
    return redirect(url_for('fetch_stock'))


# dashboard register login
@app.route("/dashboard")
@login_required
def dashboard():
    sales_by_product = sales_per_product(session['user_id'])
    sales_by_day = sales_per_day(session['user_id'])
    profit_by_product = profit_per_product(session['user_id'])
    profit_by_day = profit_per_day(session['user_id'])

    return render_template(
        "dashboard.html",
        sales_by_product=sales_by_product,
        sales_by_day=sales_by_day,
        profit_by_product=profit_by_product,
        profit_by_day=profit_by_day
    )


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['name']
        email = request.form['email']
        phone_number = request.form['phone']
        password = request.form['password']

        existing_user = check_user_exists(email)
        if not existing_user:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = (full_name, email, phone_number, hashed_password)
            insert_user(new_user)
            flash("user registered successfully", 'success')
            return redirect(url_for('login'))
        else:
            flash("user with this email alredy exists", 'danger')

    return render_template("register.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        registered_user = check_user_exists(email)
        if not registered_user:
            flash("User with this email doesnt exist, register", 'danger')
        else:
            if bcrypt.check_password_hash(registered_user[-1], password):
                session['email'] = email
                session['full_name'] = registered_user[1]
                session['user_id'] = registered_user[0]  # NEW: store the user's id for data scoping
                return redirect(url_for('dashboard'))
            else:
                flash("Password incorrect", 'danger')
    return render_template("login.html")


@app.route('/logout')
def logout():
    session.pop('email', None)
    session.pop('full_name', None)
    session.pop('user_id', None)
    flash("Logged out successfully", 'success')
    return redirect(url_for('login'))


app.run(debug=True)