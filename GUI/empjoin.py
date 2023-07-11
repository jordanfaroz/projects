import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="empdpt"
)
cur=mydb.cursor()
#sql= "select empname ,deptname from emptable, dept where emptable.deptno = dept.deptno"
#sql= "select emptable.empname as emp,dept.deptname as dept from emptable RIGHT JOIN  DEPT on  empTABLE.deptno = dept.deptno"
sql= "select emptable.empname as emp,dept.deptname as dept from emptable LEFT JOIN  DEPT on  empTABLE.deptno = dept.deptno"

cur.execute(sql)
result= cur.fetchall()\\

for x in result:
    print(x)