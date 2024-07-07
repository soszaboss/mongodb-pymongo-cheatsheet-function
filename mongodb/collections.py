class CreateGetDropCollection:
    def __init__(self, conn):
        self.client = conn
    def get_collection(self, db:str, collection_name:str):
            db = self.client.get_database(db)
            collection = db.get_collection(collection_name)
            return collection
    def get_collections(self, db:str):
            db = self.client.get_database(db)
            collections = db.list_collections()
            for collection in collections:
                  print(collection)

    def create_collection(self, db:str, collection_name:str):
            try:
                db = self.client.get_database(db)
                db.create_collection(collection_name)
            except Exception as e:
                raise Exception("The following error occurred: ", e)
    def drop_collection(self, db:str, collection_name:str):
            try:
                db = self.client.get_database(db)
                db.drop_collection(collection_name)
            except Exception as e:
                raise Exception("The following error occurred: ", e)