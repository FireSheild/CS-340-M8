from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
    
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31580
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary            
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            self.database.animals.find_one(data)
        else:
            raise Exception("Nothing to read, because data parameter is empty")

# Create method to implement the U in CRUD

    def update(self, data):
        if data is not None:
            self.database.animals.update_one(data)
        else:
            raise Exception("Nothing to change, because data parameter is empty")
            
# Create method to implement the D in CRUD

    def delete(self, data):
        if data is not None:
            self.database.animals.delete_one(data)
        else:
            raise Exception("Nothing to delete, because data parameter is empty")
