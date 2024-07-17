from flask import Flask, render_template
from sqlalchemy import create_engine
from dotenv import load_dotenv
from flask_restful import Api
from db import db
import os
from models.producto import Productos
from models.heladeria import Heladeria
from views.heladeria_controller import Heladeria_Controller

load_dotenv()

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_database = os.getenv('DB_DATABASE')

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_database}"
db.init_app(app)
api = Api(app)

api.add_resource(Heladeria_Controller, '/vender/<int:id_producto>')

heladeria = Heladeria()

@app.route("/")
def home():
    productos = heladeria.listar_productos()
    return render_template("index.html", productos = productos)

if __name__ == "__main__":
    app.run(debug=True)


