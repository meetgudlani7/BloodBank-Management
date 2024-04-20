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

def getDocs():
    cursor.execute("Select Doc_id,Doc_name from doctor")
    rows = cursor.fetchall()
    return rows

def getHosp():
    cursor.execute("Select H_id,H_name from hospital")
    rows = cursor.fetchall()
    return rows

def getBBank():
    cursor.execute("Select Bank_id,Bank_name from BloodBank")
    rows = cursor.fetchall()
    return rows

def adddonor(name, gender, address, pno, weight, dob, docid):
    query = """
    INSERT INTO donor (Do_name, Do_gender, Do_address, Do_Phno, Do_weight, Do_DOB, Doc_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (name, gender, address, pno, weight, dob, docid))
    con.commit()
    print("Successful Insertion in Donor")

def addBloodBank(name, address):
    query = """
    INSERT INTO bloodbank (Bank_name, Bank_add)
    VALUES (%s, %s)
    """
    cursor.execute(query, (name, address))
    con.commit()
    print("Successful Insertion in Blood Bank")

def addhospital(name, address, mode):
    query = """
    INSERT INTO hospital (H_name, H_add, mode)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (name, address, mode))
    con.commit()
    print("Successful insertion in Hospital")

def addPatient(name, bloodgroup, hospital_id, bloodbank_id):
    query = """
    INSERT INTO patient (P_name, P_bloodgroup, H_id, Bank_id)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (name, bloodgroup, hospital_id, bloodbank_id))
    con.commit()
    print("Successful insertion in Patient")




