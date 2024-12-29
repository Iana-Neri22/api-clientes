from pymongo import MongoClient
import os

class DBConnectionHandler:

    def __init__(self):
        # Use the variables for your database connection
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        #self.__db_host = os.getenv("DB_HOST")
        self.__database_name = os.getenv("DB_NAME")
        self.__connection_string = 'mongodb+srv://{}:{}@cluster0.fzen2.mongodb.net'.format(
            db_user, db_password)
        self.__client = None
        self.__db_connection = None
        self.__db_collection_name = os.getenv("COLLECTION_NAME")
    
    def connect_to_db(self):
        self.__client = MongoClient(self.__connection_string)
        self.__db_connection = self.__client[self.__database_name]
        self.__db_collection = self.__db_connection[self.__db_collection_name]

    def get_db_connection(self):
        return self.__db_connection

    def get_db_client(self):
        return self.__client
    
    def get_collection(self):
        if self.__db_collection is None:
            if self.__db_connection is None or self.__client is None:
                self.connect_to_db()
        return self.__db_collection
