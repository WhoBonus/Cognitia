#Pydantic validates the data coming in and makes sure a balance is a number instead of a text
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum
from abc import ABC, abstractmethod
from typing import Optional

#Models Define the shape of our data

#practice inheritance or abstraction or interface for the checking account
#add crud operations

#enum for allowed account types
class AccountType(str, Enum):
    SAVINGS = "Savings"
    Checking = "Checking"
    Business = "Business"
    Investment = "Investment"

#Create a blueprint fot the accounts with an abstract class 
class Account(BaseModel, ABC):
    id: Optional [int] = None #Set to optional because added automatic id increment
    accountType: AccountType #enum
    balance: float

    #@abstractmethod


class SavingsAccount(Account):
    interestRate: float = 0.02
class CheckingAccount(Account):
    overDraftLimit: float = 100


class Customer (BaseModel):
    id: Optional [int] = None #Set to optional because added automatic userID increment
    name: str
    accounts: List[Account] = [] 