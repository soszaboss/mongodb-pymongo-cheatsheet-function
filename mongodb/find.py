from .collections import CreateGetDropCollection
from bson.objectid import ObjectId
from .decorators import find_many_decorator, list_find_decorator_items

class Find(CreateGetDropCollection):

    def __init__(self, conn, param=None):
        self.param = param
        super().__init__(conn)

    @list_find_decorator_items
    @find_many_decorator() #(param=parameter)
    def find(db, collection_name):
        pass
 
    def find_one(self, db, collection_name, filter:tuple):
        try:
            collection = self.get_collection( db, collection_name)
        except Exception as e:
            raise Exception("The following error occurred: ", e)
        else:
            if not filter:
                raise ValueError('filter is empty')
            return list(collection.find(*filter))

    def find_one_by_id(self, db, collection_name, id:str):
        object_id = ObjectId(id)
        filter = ({'_id': object_id},)
        return self.find_one(db, collection_name, filter)
    
    def find_and_sort(self, data:dict, db:str, collection_name:str):
        try:
            items = self.find(db=db, collection_name=collection_name).sort(data)
        except Exception as e:
            raise Exception("The following error occurred: ", e)
        else:
            return list(items)
        
    def find_and_limit(self, limit:int, db:str, collection_name:str):
        try:
            items = self.find(db=db, collection_name=collection_name).limit(limit)
        except Exception as e:
            raise Exception("The following error occurred: ", e)
        else:
            return list(items)
        
    def limit_and_sort(self, limit:int, data:dict, db:str, collection_name:str):
        try:
            items = self.find(db=db, collection_name=collection_name).sort(data).limit(limit)
        except Exception as e:
            raise Exception("The following error occurred: ", e)
        else:
            return list(items)