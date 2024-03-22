import mysql.connector
dbb= input("enter the data: ")
item=(dbb,)
column= 'quantity'
goal = 'item_name'
constrain = 'jeans stock'
db = mysql.connector.connect(
host="localhost",  
user="root", 
password="",  
database="retail_store"  
)

cursor = db.cursor()

#print (item)
query = "SELECT quantity FROM `stock` WHERE item_name=%s"


#cursor.execute("SELECT 'quantity' FROM `stock` WHERE 'item_name'= %s", (item,))
cursor.execute(query, item)

# Fetch the result
rows = cursor.fetchall()
#result = cursor.fetchone()

for row in rows:
    print(row)

# Print the result
# return (f"The items in stock: {result[0]}")

# Don't forget to close the connection
db.close()