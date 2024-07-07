from mongodb.collections import CreateGetDropCollection
from bson.objectid import ObjectId


class Insert(CreateGetDropCollection):
    def __init__(self, conn):
        super().__init__(conn)
    def insert_one(self, db, collection_name:str, doc:dict):
        try:
            collection = self.get_collection(db, collection_name)
            doc = collection.insert_one(doc)
        except Exception as e:
            raise Exception("The following error occurred: ", e)
        else:
            return doc.inserted_id
        
    def insert_many(self, db:str , collection_name:str, docs:list):
        try:
            collection = self.get_collection(db, collection_name)
            for task in docs:
                typ = type(task)
                if typ != dict:
                    raise ValueError( f'collection has to be a list of dictionaries: {task}')
            data = collection.insert_many(docs)
        except Exception as e:
            raise Exception("The following error occurred: ", e)
        else:
            return data.inserted_ids
