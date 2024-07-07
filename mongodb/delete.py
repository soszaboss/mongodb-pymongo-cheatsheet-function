from .collections import CreateGetDropCollection
from bson.objectid import ObjectId


#class for deleting document(s) in your database
class Delete(CreateGetDropCollection):

    def __init__(self, conn):
        super().__init__(conn)
        
    def delete_one(self, db, collection_name:str, query_filter:dict):
        try:
            collection = self.get_collection(db, collection_name)
            if not query_filter:
                raise ValueError('query filter operation cannot be empty')
            deleted_data = collection.delete_one(query_filter)
        except Exception as e:
            raise Exception("The following error occurred: ", e)
        else:
            return deleted_data.raw_result
        
    def delete_one_by_id(self, db, collection_name:str, id:str):
        try:
            collection = self.get_collection(db, collection_name)
            if not id:
                raise ValueError('query filter operation cannot be empty')
            object_id = ObjectId(id)
            filter = {'_id': object_id}
            deleted_data = collection.delete_one(filter)
        except Exception as e:
            raise Exception("The following error occurred: ", e)
        else:
            return deleted_data.raw_result
    
    def delete_many(self, db, collection_name:str, query_filter:dict):
        try:
            collection = self.get_collection(db, collection_name)
            # if not query_filter:
            #     raise ValueError('query filter operation cannot be empty')
            deleted_data = collection.delete_many(query_filter)
        except Exception as e:
            raise Exception("The following error occurred: ", e)
        else:
            return deleted_data.raw_result
        
    

