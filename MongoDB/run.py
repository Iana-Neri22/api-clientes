from flask import Flask
from models.blueprints.cliente_blueprints import clientes_bp


app = Flask(__name__)


app.register_blueprint(clientes_bp, url_prefix="/cliente")


app.run(port=5000)

