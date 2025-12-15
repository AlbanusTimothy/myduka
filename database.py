import psycopg2
conn = psycopg2.connect(host="localhost",port="5432",user="postgres",password="Alabaalaba0!",dbname="myduka_db")

# get connection
def get_connection():
    return psycopg2.connect(
        host="localhost",
        port="5432",
        user="postgres",
        password="Alabaalaba0!",
        dbname="myduka_db"
    )



cur=conn.cursor()





def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products
products=get_products()
print(products)   


def insert_products(values):
    cur.execute(f"insert into products(name,buying_price,selling_price) values{values}")
    conn.commit()



# insert sales
def insert_sales(values):
    cur.execute(f"insert into sales(pid, quantity)values{values}")
    conn.commit()




def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales

# sales = get_sales()
# print(sales)


def available_stock(pid):
    cur.execute(f'select sum(stock_quantity) from stock where pid = {pid} ')
    total_stock = cur.fetchone()[0] or 0

    cur.execute(f'select sum(quantity) from sales where pid = {pid}')
    total_sales = cur.fetchone()[0] or 0

    return total_stock - total_sales

# stock
def get_stock():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM stock")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

# insert stock
def insert_stock(stock):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO stock (pid,stock_quantity) VALUES (%s, %s)",
        stock
    )
    conn.commit()
    cur.close()
    conn.close()

# inserting users
def insert_user(username, email, password_hash, profile_image=None):
    """
    Inserts a new user into the users table.

    Args:
        username (str): Username of the user.
        email (str): Email of the user.
        password_hash (str): Hashed password.
        profile_image (str, optional): Path or URL to profile image. Defaults to None.
    """
    try:
        query = """
        INSERT INTO users (username, email, password_hash, profile_image)
        VALUES (%s, %s, %s, %s)
        """
        cur.execute(query, (username, email, password_hash, profile_image))
        conn.commit()  # commits using your existing connection
        print("User inserted successfully!")
    except Exception as e:
        conn.rollback()
        print("Error inserting user:", e)





# sales per product
def sales_per_product():
    """
    Fetch total sales amount per product.
    Returns a list of tuples: (product_name, total_sales)
    """
    try:
        query = """
        SELECT p.name, SUM(s.selling_price * s.quantity) AS total_sales
        FROM sales s
        JOIN products p ON s.product_id = p.id
        GROUP BY p.name
        ORDER BY total_sales DESC
        """
        cur.execute(query)
        results = cur.fetchall()
        return results
    except Exception as e:
        print("Error fetching sales per product:", e)
        return []



# sales per day
def sales_per_day():
    """
    Fetch total sales amount per day.
    Returns a list of tuples: (sale_date, total_sales)
    """
    try:
        query = """
        SELECT sale_date, SUM(selling_price * quantity) AS total_sales
        FROM sales
        GROUP BY sale_date
        ORDER BY sale_date
        """
        cur.execute(query)
        results = cur.fetchall()
        return results
    except Exception as e:
        print("Error fetching sales per day:", e)
        return []


# profit per product
def profit_per_product():
    """
    Fetch total profit per product.
    Returns a list of tuples: (product_name, total_profit)
    """
    try:
        query = """
        SELECT p.name, SUM((s.selling_price - s.buying_price) * s.quantity) AS total_profit
        FROM sales s
        JOIN products p ON s.product_id = p.id
        GROUP BY p.name
        ORDER BY total_profit DESC
        """
        cur.execute(query)
        results = cur.fetchall()
        return results
    except Exception as e:
        print("Error fetching profit per product:", e)
        return []


# profit per day
def profit_per_day():
    """
    Fetch total profit per day.
    Returns a list of tuples: (sale_date, total_profit)
    """
    try:
        query = """
        SELECT sale_date, SUM((selling_price - buying_price) * quantity) AS total_profit
        FROM sales
        GROUP BY sale_date
        ORDER BY sale_date
        """
        cur.execute(query)
        results = cur.fetchall()
        return results
    except Exception as e:
        print("Error fetching profit per day:", e)
        return []


