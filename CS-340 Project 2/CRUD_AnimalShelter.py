from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, userName, password):
        # Initializing the MongoClient.
        # Replace these connection variables with your own MongoDB details.
        # USER = 'aacuser'
        # PASS = 'password1'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30091
        DB = 'AAC'
        COL = 'animals'

        # Initialize Connection
        # self.USER = userName
        # self.PASS = password
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (userName, password, HOST, PORT))
        self.database = self.client[DB]
        self.collection = self.database[COL]
        print("initialized")

    def create(self, data):
        if data is not None:
            # Insert the data into the 'animals' collection
            result = self.database.animals.insert_one(data)
            if result.inserted_id:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save because the data parameter is empty")
    
    def read(self, query):
        # Query for documents based on the provided query
        result = self.collection.find(query)
        
        # Convert the result to a list of dictionaries
        documents = [doc for doc in result]
        
        return documents
    
    def update(self, query, data):
        # Find documents matching the query
        result = self.collection.find(query)
        
        # Get the count of matching documents
        count = result.count()
        
        # If there was nothing return 0
        if count == 0:
            return 0
        
        # If there was 1 use the update_one function and return 1
        elif count == 1:
            self.collection.update_one(query, {"$set" : data})
            return 1
        
        # If there is more than 1 use the update_many functon and 
        # return the count
        else:
            self.collection.update_many(query, {"$set" : data})
            return count
        
        
    def delete(self, query):
        # Find documents matching the query
        result = self.collection.find(query)

        # Get the count of matching documents
        count = result.count()

        # Delete the documents
        self.collection.delete_many(query)

        # Return the count of deleted documents
        return count




