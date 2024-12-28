from flask import Blueprint, request, jsonify
from models.connection_options.connection import DBConnectionHandler
from models.repository.ClienteInfo_repository import clienteInfoRepository
from models.repository.ClienteInfo_repository import clienteInfoRepository
from models.connection_options.connection import DBConnectionHandler


db_handle = DBConnectionHandler()
db_handle.connect_to_db()

db_actions = clienteInfoRepository()

clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route("/", methods=["GET", "POST"])
def clientes():
    if request.method == "GET":
        try:
            filter_data = request.args.to_dict()
            result = db_actions.selecionar_clientes(db_handle, filter_data)
            return jsonify(result), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    elif request.method == "POST":
        try:
            data = request.json
            result = db_actions.inserir_cliente(db_handle, data)
            return jsonify(result), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@clientes_bp.route("/<cpf>", methods=["GET", "PUT", "DELETE"])
def cliente(cpf):
    try:
        if request.method == "GET":
            # Fetch a single client by CPF
            result = db_actions.selecionar_cliente(db_handle, {"cpf": cpf})
            if result:
                return jsonify(result), 200
            else:
                return jsonify({"message": "Cliente não encontrado"}), 404

        elif request.method == "PUT":
            update_data = request.json
            db_actions.edit_muitos_clientes(db_handle, {"CPF": cpf}, update_data)
            return jsonify({"message": "Cliente atualizado com sucesso"}), 200

        elif request.method == "DELETE":
            result = db_actions.selecionar_cliente(db_handle, {"CPF": cpf})
            if result:
                db_actions.deletar_cliente(db_handle, cpf)
                return jsonify({"message": "Cliente deletado com sucesso"}), 200
            else:
                return jsonify({"error": "Cliente não encontrado"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


clientes_bp = Blueprint('cliente', __name__)
        
clientes_bp.add_url_rule("/", view_func=clientes, methods=["GET", "POST"])
clientes_bp.add_url_rule("/<cpf>", view_func=cliente, methods=["GET", "PUT", "DELETE"])

