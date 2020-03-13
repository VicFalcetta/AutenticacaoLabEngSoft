from flask import Flask
import pyodbc
app = Flask(__name__)

server = 'dbserver-vf.database.windows.net'
database = 'database.VF'
username = 'VFNascimento'
password = 'DataFals0'
driver = '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect(DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)

@app.route("/")
def hello():
    return "Hello World!"
