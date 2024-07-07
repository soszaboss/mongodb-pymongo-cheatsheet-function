from mongodb.collections import CreateGetDropCollection
from bson.objectid import ObjectId

class Update(CreateGetDropCollection):
    
    def __init__(self, conn):
        super().__init__(conn)
        
    def update_one(self, db, collection_name:str, query_filter:dict, update_operation:dict, upsert=False):
        try:
            collection = self.get_collection(db, collection_name)
            if not query_filter and not update_operation:
                raise ValueError('query filter and update operation cannot be empty')
            updated_data = collection.update_one(query_filter, update_operation, upsert=upsert)
        except Exception as e:
            raise Exception("The following error occurred: ", e)
        else:
            if not upsert:
                return updated_data.raw_result
            else:
                return updated_data.upserted_id
    def update_many(self, db, collection_name:str, query_filter:dict, update_operation:dict, upsert=False):
        try:
            collection = self.get_collection(db, collection_name)
            if not query_filter and not update_operation:
                raise ValueError('query filter and update operation cannot be empty')
            updated_data = collection.update_many(query_filter, update_operation, upsert=upsert)
        except Exception as e:
            raise Exception("The following error occurred: ", e)
        else:
            if not upsert:
                return updated_data.raw_result
            else:
                return updated_data.upserted_id
