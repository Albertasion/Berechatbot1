#server connection
import pymysql
mydb = pymysql.connect(
  host="localhost",
  user="root",
  database="strument_str_test",
  passwd=""
)
mycursor = mydb.cursor()