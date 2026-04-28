import pymysql

def connect_db():
  conn = pymysql.connect(
      host="192.168.0.49",
      port=3306,
      user="firstcommit",
      password="1111",
      database="cust_analysis"
  )

  print("연결 성공")



def test_select(conn):
  cursor = conn.cursor()
  cursor.execute("SHOW TABLES")
  result = cursor.fetchall()
  print(result)
  

  cursor.execute("SELECT * FROM menu")
  result = cursor.fetchall()
  print(result)


  cursor.execute("SELECT * FROM menu")
  rows = cursor.fetchall()
  for row in rows:
    print(row)