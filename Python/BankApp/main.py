from fastapi import FastAPI
from pydantic import BaseModel, Field
from service import BankService
from models import*
app = FastAPI(title = "BankApp API") #Also implements Swagger. FastAPI self documents
service = BankService()

#Routes / Controllers deliver data to user.

#Route: Homepage [Verified in postman]
@app.get("/")
def home():
    return "Hello World"

#Route: Return all customers
@app.get("/customers")
async def getAllCustomers():
    #Access service layer, connect to repository, then call specfici function
    customers = await service.repo.getCustomers()
    return customers

#Route: Call the service layer abd calculate premium
@app.get("/accounts/premium")
async def getPremium():
    return await service.getPremiumAccounts()

#Route: Get all Accounts
@app.get("/accounts")
def getAllAcounts():
    return service.getAllAccounts()

#Route: get aall counts with specific customer id
@app.get("/customers/{customerId}/accounts")
def getAllCustomerAccounts(customerID: int):
    accounts = service.getAccountsByCustomerID(customerID)
    if not accounts:
        return {"Error" : " No accounts found for this customer"}
    return accounts

#***Routes: CRUD***
#POST / ADD CUSTOMER
@app.post("/customers")
async def addCustomer(customer: Customer):
    return await service.addCustomer(customer)

#GET / Get Customer by ID
@app.get("/customers/{id}")
async def getCustomerByID(id :int):
    customer = await service.getCustomer(id)
    if not customer:
        return {"error": "Customer not found"}
    return customer

#PUT / Update Customer
@app.put("/customers/{id}")

#DELETE / Delete Customer
@app.delete("/customers/{id}")
async def deleteCustomer(id : int):
    await service.repo.deleteCustomer(id)
    return {"message" : f"Customer {id} deleted"}

