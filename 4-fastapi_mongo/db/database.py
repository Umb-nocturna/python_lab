from pymongo import MongoClient

class Database:
    def __init__(self):
        self.client = MongoClient(
            "mongodb+srv://dbumb:12345@cluster0.84xqg.mongodb.net/",
            tlsAllowInvalidCertificates=True  # Desactiva verificación de SSL
        )
        self.db = self.client["umb-practice"]

    def get_collection(self, collection_name):
        return self.db[collection_name]

# Instancia única de la base de datos
database = Database()
