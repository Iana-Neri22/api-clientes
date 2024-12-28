from models.connection_options.connection import DBConnectionHandler
from models.repository.ClienteInfo_repository import clienteInfoRepository
from datetime import datetime, timedelta
from flask import Flask, request, jsonify
from models.blueprints.cliente_blueprints import clientes_bp

app = Flask(__name__)

#app.register_blueprint(clientes_bp, url_prefix="/clientes")

# Initialize the ClienteBlueprint with a database connection
db_connection = DBConnectionHandler().get_db_connection()

# Register the Blueprint with a URL prefixi
app.register_blueprint(clientes_bp, url_prefix="/clientes")
#app.register_blueprint(clientes_bp)

db_handle = DBConnectionHandler()
db_handle.connect_to_db()
db_connection = db_handle.get_db_connection()

app.run(port=5000)