# CustomerViewer.py
# Nagaru Okawa
# ISQA 3900 - Web Application Development
# Nov 17th. 2024
# This file reads customer data, allows user interaction, and displays customer information based on user input.

import csv
from Customer import Customer

def read_customers(filename):
    customers = []
    try:
        file = open(filename, 'r')
        data = list(csv.reader(file, delimiter=","))
        file.close()

        # Skip the header row and process each customer row
        for row in data[1:]:
            cust_ID, fName, lName, company, street, city, state, zipcode = row
            customers.append(Customer(cust_ID, fName, lName, company, street, city, state, zipcode))
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    return customers


def display_customer_ids(customers):
    print("ALL CUSTOMERS")
    print("--------------------------")
    for customer in customers:
        print(f"{customer.cust_ID()} : {customer.cust_name()}")


def find_customer(customers, cust_ID):
    for customer in customers:
        if customer.cust_ID() == cust_ID:
            return customer
    return None


def main():
    filename = input("Enter the customer data file name (e.g., 'customers-1.csv'): ")
    customers = read_customers(filename)
    if customers is None:
        return

    display_customer_ids(customers)

    while True:
        cust_ID = input("\nEnter Customer ID: ")
        if not cust_ID.isdigit():
            print(f"Customer {cust_ID} does not exist")
        else:
            customer = find_customer(customers, cust_ID)
            if customer:
                print(customer)
            else:
                print(f"Customer {cust_ID} does not exist")

        cont = input("\nWould you like to continue? y/n: ")
        if cont.lower() != 'y':
            break


if __name__ == "__main__":
    main()
