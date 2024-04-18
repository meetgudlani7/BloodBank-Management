import mysql.connector as connector

con = connector.connect(host='localhost',
                        port='3306',
                        user='root',
                        password='HARSHsql@1234',
                        database='PROJECT')
cursor = con.cursor()

def Login_check(username,password):
    Qstr = "SELECT name,pass from userdata where name=\"" + str(username) + "\"" "and pass=\"" + str(password) + "\""
    cursor.execute(Qstr)
    rows = cursor.fetchall()
    if len(rows)==0:
        return False
    else:
        return True
    
def signup_check(username,email,Password):
    Qstr = "SELECT * from userdata where email=\"" + str(email) + "\""
    cursor.execute(Qstr)
    rows = cursor.fetchall()
    if len(rows)==0:
        Qstr = "insert into userdata values(\"{}\",\"{}\",\"{}\")".format(email,username,Password)
        cursor.execute(Qstr)
        con.commit()
        return True
    return False