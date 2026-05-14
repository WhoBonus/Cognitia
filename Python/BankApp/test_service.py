import pytest
from service import BankService
from repository import BankRepository
from models import Customer
service = BankService()
repo = BankRepository()
def testGetPremiumAccountsLogic():
    #Connect to the service (which is connected to the DB)
    
    
    #Get actual data
    premiums = service.getPremiumAccounts()
    
    #ASSERT: Check if the results match what we expect
    #This assert verifies the amount of premium accounts
    assert len(premiums) == 2 

    #These asserts verify account balance in the premiums list returned
    assert premiums[0]['balance'] == 15000.0 #checks alice
    assert premiums[1]['balance'] == 20000.0 #checks charlie

def testGetAllCustomersLogic():
    #Get expected Data
    allCustomers = repo.getCustomers()

    #compare expectedData with actualData
    assert allCustomers == repo.dataSet["customers"]

def testIDAutoIncrement():
    newCustomerData = Customer(name = "Dan", accounts = []) 
    result = service.addCustomer(newCustomerData)
    assert result['id'] == 4

def testGetInvalidCustomer():
    result = service.getCustomer(9999)
    assert result is None