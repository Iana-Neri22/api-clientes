from pymongo import MongoClient
from dotenv import load_dotenv
import os




import os

# Load .env file
load_dotenv()

# Access variables
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
secret_key = os.getenv("SECRET_KEY")

print(f"Database Host: {db_host}")
print(f"Secret Key: {secret_key}")

load_dotenv()

HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
DB_NAME = os.environ.get("DB_NAME")
COLLECTION_NAME = os.environ.get("COLLECTION_NAME")



class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = 'mongodb+srv://{}:{}@cluster0.fzen2.mongodb.net'.format(
            USERNAME,
            PASSWORD
        )
        self.__database_name = DB_NAME
        self.__client = None
        self.__db_connection = None
        self.__db_collection = None
        self.__db_collection_name = COLLECTION_NAME

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
