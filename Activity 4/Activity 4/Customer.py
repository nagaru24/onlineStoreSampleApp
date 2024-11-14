# Customer.py
# Nagaru Okawa
# ISQA 3900 - Web Application Development
# Nov 17th. 2024
# This file defines a Customer class to store customer data and manage related properties.

class Customer:
    def __init__(self, cust_ID, fName, lName, company, street, city, state, zipcode):
        self.__cust_ID = cust_ID
        self.__fName = fName
        self.__lName = lName
        self.__company = company
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zipcode = zipcode

    def __str__(self):
        return f"{self.cust_name()}\n{self.cust_fullAddress()}"

    def cust_name(self):
        return f"{self.__fName} {self.__lName}"

    def cust_fullAddress(self):
        address = f"{self.__street}\n{self.__city}, {self.__state} {self.__zipcode}"
        if self.__company:
            address = f"{self.__company}\n" + address
        return address

    def cust_ID(self):
        return self.__cust_ID

    def cust_company(self):
        return self.__company
