from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'TarasKorneev.mysql.pythonanywhere-services.com'
app.config['MYSQL_DATABASE_USER'] = 'TarasKorneev'
app.config['MYSQL_DATABASE_PASSWORD'] = '1qazxsw2'
app.config['MYSQL_DATABASE_DB'] = 'TarasKorneev$hrdep_db'

mysql = MySQL()
mysql.init_app(app)
