import psycopg2

# 连接数据库
conn = psycopg2.connect(
    host="192.168.198.128",
    port="26000",
    database="xuezymis05",
    user="zjutuser",
    password="Bigdata@123"
)

def getCursor():
    return conn.cursor()