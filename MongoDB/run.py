from models.connection_options.connection import DBConnectionHandler
from models.repository.ClienteInfo_repository import clienteInfoRepository
from datetime import datetime, timedelta
from flask import Flask, request, jsonify
from models.blueprints.cliente_blueprints import ClienteBlueprint

app = Flask(__name__)
#app.register_blueprint(clientes_bp, url_prefix="/clientes")

# Initialize the ClienteBlueprint with a database connection
db_connection = DBConnectionHandler().get_db_connection()
cliente_blueprint = ClienteBlueprint()

# Register the Blueprint with a URL prefix
app.register_blueprint(cliente_blueprint.clientes_bp, url_prefix="/clientes")

# @app.route("/")
# def homepage():
#     return "App is running"

# @app.route("/clientes", methods=["GET", "POST"])
# def clientes():
#     if request.method == "GET":
#         return jsonify(cadastro_cliente_repository.select_many({}))
#     elif request.method == "POST":
#         data = request.json
#         return jsonify(cadastro_cliente_repository.insert_document(data))
#     else:
#         return "Method not allowed", 405
    
# @app.route("/clientes/<cpf>", methods=["GET", "PUT", "DELETE"])
# def cliente(cpf):
#     if request.method == "GET":
#         return jsonify(cadastro_cliente_repository.select_one({ "CPF": cpf }))
#     elif request.method == "PUT":
#         data = request.json
#         return jsonify(cadastro_cliente_repository.update_one({ "CPF": cpf }, data))
#     elif request.method == "DELETE":
#         return jsonify(cadastro_cliente_repository.delete_one({ "CPF": cpf }))
#     else:
#         return "Method not allowed", 405

db_handle = DBConnectionHandler()
db_handle.connect_to_db()
db_connection = db_handle.get_db_connection()

app.run(port=5000)