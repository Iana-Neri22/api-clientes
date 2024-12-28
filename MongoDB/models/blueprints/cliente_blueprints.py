from flask import Blueprint, request, jsonify
from models.repository.ClienteInfo_repository import clienteInfoRepository
#from clienterepository import get_all_clients, get_client_by_id, add_client
from models.connection_options.connection import DBConnectionHandler


db_actions = clienteInfoRepository()

# Handle the '/' endpoint for GET and POST
def clientes():
    if request.method == "GET":
        # Fetch multiple clients
        return jsonify(db_actions.select_many())
    elif request.method == "POST":
        # Insert a new client
        data = request.json
        return jsonify(db_actions.insert_document(data))
    else:
        return "Method not allowed", 405

# Handle the '/<cpf>' endpoint for GET, PUT, and DELETE
def cliente(self, cpf):
    if request.method == "GET":
        # Fetch a single client by CPF
        return jsonify(db_actions.select_one({"CPF": cpf}))
    # elif request.method == "PUT":
    #     # Update a client by CPF
    #     data = request.json
    #     return jsonify(self.__db_actions.update_one({"CPF": cpf}, data))
    # elif request.method == "DELETE":
    #     # Delete a client by CPF
    #     return jsonify(self.__db_actions.delete_one({"CPF": cpf}))
    else:
        return "Method not allowed", 405


# Create a Blueprint for the Cliente API
clientes_bp = Blueprint('cliente', __name__)
        
clientes_bp.add_url_rule("/", view_func=clientes, methods=["GET", "POST"])
clientes_bp.add_url_rule("/<cpf>", view_func=cliente, methods=["GET", "PUT", "DELETE"])