import psycopg2
conn = psycopg2.connect(host="localhost",port="5432",user="postgres",password="Alabaalaba0!",dbname="myduka_db")


cur=conn.cursor()

cur.execute("select * from products")
products = cur.fetchall()
print(products)
# print(type(products))

cur.execute("insert into products(name,buying_price,selling_price)values('shoes',500,1000)")
conn.commit()
print(products)

def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
products=get_products
print(products)   


def insert_products(values):
    cur.execute(f"insert into products(name,buying_price,selling_price) values{values}")
    conn.commit()

producta=insert_products(('milk',40,70))
productb=insert_products(('bread',40,65))

print(products)


# insert sales
def insert_sales(values):
    cur.execute(f"insert into sales(pid, quantity)values{values}")
    conn.commit()

my_sale = (1, 7000)
my_sale2 = (2, 4500)
insert_sales(my_sale)
insert_sales(my_sale2)


def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales

sales = get_sales()
print(sales)