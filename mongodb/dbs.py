class CreateDropDbs:
    def __init__(self, conn):
        self.client = conn
    def create_dbs(self, db_name:str):
        try:
            db = self.client[db_name]
        except Exception as e:
                raise Exception("The following error occurred: ", e)
        else:
            return db
    def drop_dbs(self, db_name:str):
        try:
            self.client.drop_database(db_name)
        except Exception as e:
                raise Exception("The following error occurred: ", e)
        
    def get_databases(self):
         try:
            databases = self.client.list_database_names()
         except Exception as e:
                raise Exception("The following error occurred: ", e)
         else:
              for database in databases:
                  print(database)

