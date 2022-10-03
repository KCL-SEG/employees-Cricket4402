"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from mimetypes import common_types


class Employee:
    def __init__(self, name, contract, contractamt, wagehrs, commission, commissionamt, commno):
        self.name = name
        self.contract = contract
        self.commission = commission
        self.contractamt = contractamt
        self.commissionamt = commissionamt
        self.wagehrs = wagehrs
        self.commno = commno

    def get_pay(self):
        x = 0
        y = 0
        if self.contract == "Salary":
            x = self.contractamt
        elif self.contract == "Wage":
            x = self.contractamt * self.wagehrs
        
        if self.commission == "Fixed":
            y = self.commissionamt
        elif self.commission == "Bonus":
            y = self.commissionamt * self.commno
            
        return x + y
            
        pass

    def __str__(self):
        returnstr = ""
        returnstr = returnstr + self.name + " "
        if self.contract == "Salary":
            returnstr = returnstr + "works on a monthly salary of " + str(self.contractamt)
        elif self.contract == "Wage":
            returnstr = returnstr + "works on a contract of " + str(self.wagehrs) + " hours at " + str(self.contractamt) + "/hour"
        
        if self.commission == "Fixed":
            returnstr = returnstr + " and receives a bonus commission of " + str(self.commissionamt)
        elif self.commission == "Bonus":
            returnstr = returnstr + " and receives a commission for " + str(self.commno) + " contract(s) at " + str(self.commissionamt) + "/contract"
        returnstr = returnstr + ".  Their total pay is " + str(Employee.get_pay(self)) + "."
        return returnstr
    
        


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "Salary", 4000, 0, "None", 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "Wage", 25, 100, "None", 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "Salary", 3000, 0, "Bonus", 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',"Wage", 25, 150, "Bonus", 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "Salary", 2000, 0, "Fixed", 1500, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "Wage", 30, 120, "Fixed", 600, 0)
