#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Person:
    def __init__(self, FirstName, LastName, Age, Address, ContactNumber):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Age = Age
        self.Address = Address
        self.ContactNumber = ContactNumber

class Employee(Person):
    def __init__(self, FirstName, LastName, Age, Address, ContactNumber, EmployeeID, OrganizationName, Position):
        super().__init__(FirstName, LastName, Age, Address, ContactNumber)
        self.EmployeeID = EmployeeID
        self.OrganizationName = OrganizationName
        self.Position = Position

class CommissionEmployee(Employee):
    def __init__(self, FirstName, LastName, Age, Address, ContactNumber, EmployeeID, OrganizationName, Position, commissionRate):
        super().__init__(FirstName, LastName, Age, Address, ContactNumber, EmployeeID, OrganizationName, Position)
        self.commissionRate = commissionRate

    def calculateCommission(self, gross_sale):
        self.totalEarning = gross_sale * self.commissionRate

    def displayData(self):
        print("First Name:", self.FirstName)
        print("Last Name:", self.LastName)
        print("Age:", self.Age)
        print("Address:", self.Address)
        print("Contact Number:", self.ContactNumber)
        print("Employee ID:", self.EmployeeID)
        print("Organization Name:", self.OrganizationName)
        print("Position:", self.Position)
        print("Commission Rate:", self.commissionRate)
        print("Total Earning:", self.totalEarning)

class SalariedEmployee(Employee):
    def __init__(self, FirstName, LastName, Age, Address, ContactNumber, EmployeeID, OrganizationName, Position, baseSalary):
        super().__init__(FirstName, LastName, Age, Address, ContactNumber, EmployeeID, OrganizationName, Position)
        self.baseSalary = baseSalary

    def calculateNetSalary(self):
        provisional_tax = 0.13 * self.baseSalary
        insurance = 0.01 * self.baseSalary
        fed_tax = 0.03 * self.baseSalary
        self.NetSalary = self.baseSalary - provisional_tax - insurance - fed_tax

    def displayData(self):
        print("First Name:", self.FirstName)
        print("Last Name:", self.LastName)
        print("Age:", self.Age)
        print("Address:", self.Address)
        print("Contact Number:", self.ContactNumber)
        print("Employee ID:", self.EmployeeID)
        print("Organization Name:", self.OrganizationName)
        print("Position:", self.Position)
        print("Base Salary:", self.baseSalary)
        print("Net Salary:", self.NetSalary)

class BasePlusCommissionEmployee(CommissionEmployee):
    def __init__(self, FirstName, LastName, Age, Address, ContactNumber, EmployeeID, OrganizationName, Position, commissionRate, baseSalary):
        super().__init__(FirstName, LastName, Age, Address, ContactNumber, EmployeeID, OrganizationName, Position, commissionRate)
        self.baseSalary = baseSalary

    def calculateTotalEarning(self, gross_sale):
        super().calculateCommission(gross_sale)
        self.totalEarning += self.baseSalary

    def displayData(self):
        print("First Name:", self.FirstName)
        print("Last Name:", self.LastName)
        print("Age:", self.Age)
        print("Address:", self.Address)
        print("Contact Number:", self.ContactNumber)
        print("Employee ID:", self.EmployeeID)
        print("Organization Name:", self.OrganizationName)
        print("Position:", self.Position)
        print("Total Earning:", self.totalEarning)

# Testing the classes
if __name__ == "__main__":
    commission_employee = CommissionEmployee("John", "Doe", 30, "123 Main St", "555-1234", "E123", "ABC Inc", "Manager", 0.05)
    commission_employee.calculateCommission(10000)
    commission_employee.displayData()

    print()

    salaried_employee = SalariedEmployee("Jane", "Doe", 25, "456 Elm St", "555-5678", "E456", "XYZ Corp", "Developer", 50000)
    salaried_employee.calculateNetSalary()
    salaried_employee.displayData()

    print()

    base_plus_commission_employee = BasePlusCommissionEmployee("Mike", "Smith", 35, "789 Oak St", "555-9012", "E789", "123 Corp", "Salesperson", 0.07, 60000)
    base_plus_commission_employee.calculateTotalEarning(20000)
    base_plus_commission_employee.displayData()

