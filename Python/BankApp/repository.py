#This layer talks to the data (fake database)
"""
When you initialized your repository, you created a self.client using AsyncIOMotorClient. This client provides the tools needed to interact with your cloud "filing cabinet".

    find_one(): This is a method provided by the Motor Collection object. It is used to search the cloud drawer for a single document that matches your criteria (like a specific id).

    inserted_id: This is a property of the Result Object returned by the insert_one() function. When you save a new customer, MongoDB automatically creates a unique binary identifier; inserted_id allows you to grab that value so you can convert it to a string for the user.

    to_list(): While find() creates a "pointer" (cursor) to your data, to_list() is the Motor function that actually pulls that data down from the cloud and converts it into a standard Python list.

"""
# Simulated Database: Nested dictionary that contains a list of dictionaries. This simulates JSON 
    # Outer shell is a Dictionary. 
        #Key value pairs (Ke
        # y = Customer, Value inside [] is a list)
            #Inside list is a nested dictionary: a customer has 3 keys
                #Value for accounts list is a another list of bank accounts/

#Await tells python to not free app while waiting for cloud to answer
import urllib.parse
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId # MongoDB uses unique 'ObjectIds'

class BankRepository:
    
    #connect to DB
    def __init__(self):
       
        safe_password = urllib.parse.quote_plus(rawPassword)

        self.uri = f"mongodb+srv://dbUser:{safe_password}@bankapp-cluster.wdb1f8c.mongodb.net/?appName=BankApp-Cluster"
        self.client = AsyncIOMotorClient(self.uri)
        self.db = self.client.bankDataBase
        self.collection = self.db.customers

    #Helper method to convert MongodDB objectid to string
    def formatID(self, data):
        if not data:
            return None
        if isinstance(data, dict):
            if "_id" in data:
                data ["_id"] = str(data["_id"])
        elif isinstance(data, list):
            for item in data:
                if "_id" in item:
                    item ["_id"] = str(item["_id"])
        return data


    #Return all Customers
    async def getCustomers(self):
        #fastAPI cannot turn that binary _id into json string so i must convert each _id to a string
        pointer = self.collection.find()
        allCustomers = await pointer.to_list(length = 100)
        return self.formatID(allCustomers)
        
    #Return customer by ID
    async def getCustomerByID(self, customerID: int):
        customer = await self.collection.find_one({"id": customerID})
        return self.formatID(customer)
    
    #Create Customer
    async def createCustomer (self, customerData: dict):
        # 1. Save to the cloud
        result = await self.collection.insert_one(customerData)
        customerData["_id"] = str(result.inserted_id)
        return customerData
    
    #delete Customer: rebuilds list from scratch
    async def deleteCustomer (self, customerID: int):
         customer = await self.collection.delete_one({"id": customerID})
         return customer.deleted_count > 0