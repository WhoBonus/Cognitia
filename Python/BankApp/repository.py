#This layer talks to the data (fake database)

# Simulated Database: Nested dictionary that contains a list of dictionaries. This simulates JSON 
    # Outer shell is a Dictionary. 
        #Key value pairs (Key = Customer, Value inside [] is a list)
            #Inside list is a nested dictionary: a customer has 3 keys
                #Value for accounts list is a another list of bank accounts/


class BankRepository:
    #connect to DB
    def __init__(self):
            self.dataSet = {
    "customers": [
        {"id": 1, "name": "Alice", "accounts": [
            {"id": 101, "account_type": "Savings", "balance": 15000.0}
        ]},
        {"id": 2, "name": "Bob", "accounts": [
            {"id": 102, "account_type": "Checking", "balance": 500.0}
        ]},
        {"id": 3, "name": "Charlie", "accounts": [
            {"id": 103, "account_type": "Checking", "balance": 20000.0}
        ]}

    ]
}
    #Return all Customers
    def getCustomers(self):
        return self.dataSet["customers"]
        
    #Return customer by ID
    def getCustomerByID(self, customer_id: int):
        return next((c for c in self.dataSet["customers"] if c["id"] == customer_id), None)
    
    #Create Customer
    def createCustomer (self, customerData: dict):
         self.dataSet["customers"].append(customerData)
         return customerData
    
    #delete Customer: rebuilds list from scratch
    def deleteCustomer (self, customerID: int):
         self.dataSet["customers"] = [c for c in self.dataSet["customers"] if c["id"] != customerID]