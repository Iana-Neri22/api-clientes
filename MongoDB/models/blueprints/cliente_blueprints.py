from flask import Blueprint, request, jsonify
from models.repository.ClienteInfo_repository import clienteInfoRepository


class ClienteBlueprint:
    def __init__(self) -> None:
        # Store the database connection and initialize the repository
        # self.__db_connection = db_connection
        self.__db_actions = clienteInfoRepository
        
        # Initialize the Blueprint
        self.clientes_bp = Blueprint("clientes", __name__)
        
        # Define routes and associate them with class methods
        self.clientes_bp.add_url_rule("/", view_func=self.clientes, methods=["GET", "POST"])
        self.clientes_bp.add_url_rule("/<cpf>", view_func=self.cliente, methods=["GET", "PUT", "DELETE"])

    # Handle the '/' endpoint for GET and POST
    def clientes(self):
        if request.method == "GET":
            # Fetch multiple clients
            return jsonify(self.__db_actions.select_many())
        elif request.method == "POST":
            # Insert a new client
            data = request.json
            return jsonify(self.__db_actions.insert_document(data))
        else:
            return "Method not allowed", 405

    # Handle the '/<cpf>' endpoint for GET, PUT, and DELETE
    def cliente(self, cpf):
        if request.method == "GET":
            # Fetch a single client by CPF
            return jsonify(self.__db_actions.select_one({"CPF": cpf}))
        # elif request.method == "PUT":
        #     # Update a client by CPF
        #     data = request.json
        #     return jsonify(self.__db_actions.update_one({"CPF": cpf}, data))
        # elif request.method == "DELETE":
        #     # Delete a client by CPF
        #     return jsonify(self.__db_actions.delete_one({"CPF": cpf}))
        else:
            return "Method not allowed", 405
