from flask import Flask, render_template,request,url_for,redirect
from database import get_products,get_sales,insert_products,insert_sales,available_stock,get_connection, insert_stock, get_stock

# Flask instance
app=Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/products")
def fetch_products():
    products= get_products()
    return render_template("products.html",products= products)

@app.route("/add_products",methods=['GET','POST'])
def add_products():
    product_name=request.form["product_name"]
    buying_price=request.form["buying_price"]
    selling_price=request.form["selling_price"]
    new_product=(product_name,buying_price,selling_price)
    insert_products(new_product)
    return redirect(url_for('fetch_products'))


@app.route('/sales')
def fetch_sales():
    sales = get_sales()
    products=get_products()
    return render_template("sales.html",sales=sales,products=products)

#posting sales
@app.route('/add_sale',methods=['GET','POST'])
def add_sale():
    pid = request.form["pid"]
    quantity = request.form["quantity"]
    new_sale = (pid,quantity)
    check_stock = available_stock(pid) 
    if check_stock < float(quantity):
        print("Insufficient stock")
        return redirect(url_for('fetch_sales'))
    insert_sales(new_sale)
    return redirect(url_for('fetch_sales'))


# stock
@app.route('/stock')
def fetch_stock():
    stock = get_stock()
    
    return render_template('stock.html', stock=stock, products=get_products())

@app.route('/add_stock', methods=['POST'])
def add_stock():
    pid = request.form["pid"]
    quantity = request.form["quantity"]
    new_stock = (pid, quantity)
    insert_stock(new_stock)
    return redirect(url_for('fetch_stock'))

    
# dashboard register login
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")



app.run(debug=True)

