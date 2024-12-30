from bson.objectid import ObjectId
from typing import Dict, List
from datetime import timedelta
from models.connection_options.connection import DBConnectionHandler

class clienteInfoRepository:

    def inserir_cliente(self, db: DBConnectionHandler, document: Dict) -> Dict:
        collection = db.get_collection()
        document['_id'] = str(ObjectId())
        collection.insert_one(document)
        return document
    
    def inserir_lista_de_clientes(self, db: DBConnectionHandler, list_of_documents: List[Dict]) -> List[Dict]:
        collection = db.get_collection()
        collection.insert_many(list_of_documents)
        return list_of_documents


    def selecionar_clientes(self, db: DBConnectionHandler, filter) -> List[Dict]:
        collection = db.get_collection()
        data = collection.find(
            filter, # Filtro
            { "endereco": 0, "_id": 0 } # Opcoes de retorno
        )

        response = []
        for elem in data: response.append(elem)

        return response

    def selecionar_cliente(self, db: DBConnectionHandler, filter) -> Dict:
        collection = db.get_collection()
        response = collection.find_one(filter)
        return response

    def editar_cliente(self, db: DBConnectionHandler, filtro, propriedades) -> None:
        collection = db.get_collection()
        data = collection.update_one(
            filtro, 
            { "$set": propriedades }
        )
        print(data.modified_count)

    
    def deletar_cliente(self, db: DBConnectionHandler, cpf: str) -> None:
        collection = db.get_collection()
        data = collection.delete_one({ "CPF": cpf })
        print(data.deleted_count)

