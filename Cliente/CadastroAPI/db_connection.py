import pymongo

url = 'mongodb+srv://iananeri:Scot3232@cluster0.fzen2.mongodb.net/tech-challenge1?authSource=admin'
client = pymongo.MongoClient(url)

db = client['cadastro-cliente']