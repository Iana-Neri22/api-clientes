from bson.objectid import ObjectId
from typing import Dict, List
from datetime import timedelta
from models.connection_options.connection import DBConnectionHandler

class clienteInfoRepository:
    def __init__(self) -> None:
        self.__collection_name = "clienteInfo"

        #self.__db_connection = DBConnectionHandler.get_db_connection(self)

        #self.teste = DBConnectionHandler.get_db_connection()

    def insert_document(self, db: DBConnectionHandler, document: Dict) -> Dict:
        collection = db.__get_collection(self.__collection_name)
        document['_id'] = str(ObjectId())
        collection.insert_one(document)
        return document
    
    def insert_list_of_documents(self, db: DBConnectionHandler, list_of_documents: List[Dict]) -> List[Dict]:
        collection = db.__get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)
        return list_of_documents


    def select_many(self, db: DBConnectionHandler, filter) -> List[Dict]:
        collection = db.get_collection(self.__collection_name)
        data = collection.find(
            filter, # Filtro
            { "endereco": 0, "_id": 0 } # Opcoes de retorno
        )

        response = []
        for elem in data: response.append(elem)

        return response

    def select_one(self, db: DBConnectionHandler, filter) -> Dict:
        collection = db.__get_collection(self.__collection_name)
        response = collection.find_one(filter, { "_id": 0 })
        return response

    def select_if_property_exists(self, db: DBConnectionHandler) -> None:
        collection = db.__get_collection(self.__collection_name)
        data = collection.find({ "cpf": { "$exists": True } })
        for elem in data: print(elem)

    def select_many_order(self, db: DBConnectionHandler) -> None:
        collection = db.__get_collection(self.__collection_name)
        data = collection.find(
            { "name": "Lhama" }, # Filtro
            { "endereco": 0, "_id": 0 } # Opcoes de retorno
        ).sort([("pedidos.pizza", 1)])

        for elem in data: print(elem)

    def select_or(self, db: DBConnectionHandler) -> None:
        collection = db.__get_collection(self.__collection_name)
        data = collection.find({ "$or": [{ "name": "Lhama" }, { "ola": { "$exists": True } }] })
        for elem in data:
            print(elem)
            print()

    def select_by_object_id(self, db: DBConnectionHandler) -> None:
        collection = db.__get_collection(self.__collection_name)
        data = collection.find({ "_id": ObjectId("642c9643dac681ba1fc5a8e7") })
        for elem in data: print(elem)

    def edit_registry(self, db:DBConnectionHandler, name) -> None:
        collection = db.__get_collection(self.__collection_name)
        data = collection.update_one(
            { "_id": ObjectId("645585c1ddbce431b3c82d9e") }, #Filtro
            { "$set": { "name": name } } # Campo de edição
        )
        print(data.modified_count)

    def edit_many_registries(self, db: DBConnectionHandler, filtro, propriedades) -> None:
        collection = db.__get_collection(self.__collection_name)
        data = collection.update_many(
            filtro, #Filtro
            { "$set": propriedades }
        )
        print(data.modified_count)

    def edit_many_increment(self, db: DBConnectionHandler, num) -> None:
        collection = db.__get_collection(self.__collection_name)
        data = collection.update_many(
            { "_id": ObjectId("645585c1ddbce431b3c82d9e") }, #Filtro
            { "$inc": { "idade": num } }
        )
        print(data.modified_count)

    def delete_many_registries(self, db: DBConnectionHandler) -> None:
        collection = db.__get_collection(self.__collection_name)
        data = collection.delete_many({ "profissao": "Programador" })
        print(data.deleted_count)
    
    def delete_registry(self, db: DBConnectionHandler) -> None:
        collection = db.__get_collection(self.__collection_name)
        data = collection.delete_one({ "_id": ObjectId("645585c1ddbce431b3c82d9e") })
        print(data.deleted_count)

    def create_index_ttl(self, db: DBConnectionHandler) -> None:
        collection = db.__get_collection(self.__collection_name)
        tempo_de_vida = timedelta(seconds=10)
        collection.create_index("data_de_criacao", expireAfterSeconds=tempo_de_vida.seconds)
