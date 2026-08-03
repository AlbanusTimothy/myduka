import psycopg2
conn = psycopg2.connect(host="localhost",port="5432",user="postgres",password="Alabaalaba0!",dbname="myduka_db")

def get_connection():
    return psycopg2.connect(
        host="localhost",
        port="5432",
        user="postgres",
        password="Alabaalaba0!",
        dbname="myduka_db"
    )

cur = conn.cursor()


def get_products(user_id):
    cur.execute("SELECT * FROM products WHERE user_id = %s ORDER BY id", (user_id,))
    return cur.fetchall()


def insert_products(values):
    # values = (product_name, buying_price, selling_price, user_id)
    cur.execute(
        "INSERT INTO products (name, buying_price, selling_price, user_id) VALUES (%s, %s, %s, %s)",
        values
    )
    conn.commit()


def insert_sales(values):
    # values = (pid, quantity, user_id)
    cur.execute(
        "INSERT INTO sales (pid, quantity, user_id) VALUES (%s, %s, %s)",
        values
    )
    conn.commit()


def get_sales(user_id):
    cur.execute("""
        SELECT s.id, s.pid, p.name, s.quantity, s.created_at
        FROM sales s
        JOIN products p ON s.pid = p.id
        WHERE s.user_id = %s
        ORDER BY s.id
    """, (user_id,))
    return cur.fetchall()


def available_stock(pid, user_id):
    cur.execute(
        "SELECT SUM(stock_quantity) FROM stock WHERE pid = %s AND user_id = %s",
        (pid, user_id)
    )
    total_stock = cur.fetchone()[0] or 0

    cur.execute(
        "SELECT SUM(quantity) FROM sales WHERE pid = %s AND user_id = %s",
        (pid, user_id)
    )
    total_sales = cur.fetchone()[0] or 0

    return total_stock - total_sales


def get_stock(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT s.id, s.pid, p.name, s.stock_quantity, s.created_at
        FROM stock s
        JOIN products p ON s.pid = p.id
        WHERE s.user_id = %s
        ORDER BY s.id
    """, (user_id,))
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data


def insert_stock(stock):
    # stock = (pid, quantity, user_id)
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO stock (pid, stock_quantity, user_id) VALUES (%s, %s, %s)",
        stock
    )
    conn.commit()
    cur.close()
    conn.close()


def insert_user(values):
    cur.execute(
        "INSERT INTO users (full_name, email, phone_number, password) VALUES (%s, %s, %s, %s)",
        values
    )
    conn.commit()


def sales_per_product(user_id):
    try:
        query = """
        SELECT p.name,
               SUM(s.quantity) AS total_quantity,
               SUM(s.quantity * p.selling_price) AS total_sales
        FROM sales s
        JOIN products p ON s.pid = p.id
        WHERE s.user_id = %s
        GROUP BY p.name
        ORDER BY total_sales DESC
        """
        cur.execute(query, (user_id,))
        return cur.fetchall()
    except Exception as e:
        print("Error fetching sales per product:", e)
        return []


def sales_per_day(user_id):
    try:
        query = """
        SELECT DATE(s.created_at) AS sale_date,
               SUM(s.quantity * p.selling_price) AS total_sales
        FROM sales s
        JOIN products p ON s.pid = p.id
        WHERE s.user_id = %s
        GROUP BY DATE(s.created_at)
        ORDER BY sale_date
        """
        cur.execute(query, (user_id,))
        return cur.fetchall()
    except Exception as e:
        print("Error fetching sales per day:", e)
        return []


def profit_per_product(user_id):
    try:
        query = """
        SELECT p.name,
               SUM((p.selling_price - p.buying_price) * s.quantity) AS total_profit
        FROM sales s
        JOIN products p ON s.pid = p.id
        WHERE s.user_id = %s
        GROUP BY p.name
        ORDER BY total_profit DESC
        """
        cur.execute(query, (user_id,))
        return cur.fetchall()
    except Exception as e:
        print("Error fetching profit per product:", e)
        return []


def profit_per_day(user_id):
    try:
        query = """
        SELECT DATE(s.created_at) AS sale_date,
               SUM((p.selling_price - p.buying_price) * s.quantity) AS total_profit
        FROM sales s
        JOIN products p ON s.pid = p.id
        WHERE s.user_id = %s
        GROUP BY DATE(s.created_at)
        ORDER BY sale_date
        """
        cur.execute(query, (user_id,))
        return cur.fetchall()
    except Exception as e:
        print("Error fetching profit per day:", e)
        return []


def check_user_exists(email):
    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
    return cur.fetchone()