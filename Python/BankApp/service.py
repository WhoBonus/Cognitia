#This is the brain. Handles logic such as identifying if premium account.
from repository import BankRepository

class BankService:
    #Connect Service to Database/Repo
    def __init__(self):
        self.repo = BankRepository()

    #Add customer
    async def addCustomer (self, customer):
        #Implement automatic ID inncr
        allCustomers = await self.repo.getCustomers()
        validIDs = [c['id'] for c in allCustomers if c.get('id') is not None]
        #if list empty
        if not allCustomers:
            newID = 1
        else:
            #add one to the highest existing ID
            newID = max(validIDs) + 1
            
        customerData = customer.model_dump()
        customerData['id'] = newID

        return await self.repo.createCustomer(customerData)
    
    #get customer 
    async def getCustomer (self, customerID: int):
        return await self.repo.getCustomerByID(customerID)
    
    #Get customer accounts
    async def getAllCustomerAccounts (self, customerID : int):
        #get all customers then a seperate list for the accounts
        allCustomers = await self.repo.getCustomers()
        allAccounts = []
        for customer in allCustomers:
            for account in customer['accounts']:
                allAccounts.append(account)
        return allAccounts
    
    #Get accounts
    def getAllAccounts(self):
        #First get all customers then loop through all of their accounts
        allCustomers = self.repo.getCustomers()
        allAccounts = []

        for customer in allCustomers:
            for account in customer['accounts']:
                allAccounts.append(account)
        return allAccounts
    
    #Get Premiums
    async def getPremiumAccounts(self):
        #First get all customers
        allCustomers = self.repo.getCustomers()

        #Make new list of premium accounts to return
        premiumAccounts = []
        
        for customer in allCustomers:
            for account in customer['accounts']:
                # Balance > 10,000 is PREMIUM
                if account['balance'] > 10000:
                    premiumAccounts.append(account)
        return premiumAccounts
    