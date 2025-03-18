from pymongo import MongoClient

class Database:
    def __init__(self):
        self.client = MongoClient(
            "{atlas-mongo-conexion}",
            tlsAllowInvalidCertificates=True  # Desactiva verificación de SSL
        )
        self.db = self.client["{my data base}"]

    def get_collection(self, collection_name):
        return self.db[collection_name]

# Instancia única de la base de datos
database = Database()
