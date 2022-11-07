import persons

def main():

    name = input('Enter the name of the customer: ')
    address = input("Enter the address of the customer: ")
    telephone_number = int(input("Enter the customers telephone number:" ))
    mailing = input("Enter y if you want to be on the mailing list: ")
    print()

    obj = persons.Customer(name, address, telephone_number, mailing)

    print(f'the name of the customer is {obj.get_name()}')

    print(f'The address of the person is {obj.get_address()}')

    print(f'the telephone number of the customer is {obj.get_telephone()}')

    print(f'the status of the customer agreeing to be on the mailing list is {obj.get_status(mailing)}')


main()