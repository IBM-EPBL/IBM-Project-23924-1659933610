import ibm_db

dsn_hostname="ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud"
dsn_uid="bjb88982"
dsn_pwd="LE5WROahhuRottl5"

dsn_driver= "{IBM DB2 ODBC DRIVER}"
dsn_database="BLUDB"
dsn_port="31321"
dsn_protocol="TCPIP"
dsn_security="SSL"

dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,dsn_security)

conn=None
def setupConnection():
    
    try:
        conn = ibm_db.connect(dsn, "", "")
        print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)
        return conn

    except:
        print ("Unable to connect: ", ibm_db.conn_errormsg())

    return conn

def createTable(conn):
    createQuery="create Table IF NOT EXISTS UserDB(Id INT NOT NULL PRIMARY KEY,username VARCHAR(50),password VARCHAR(50));"
    createTable=ibm_db.exec_immediate(conn,createQuery)

