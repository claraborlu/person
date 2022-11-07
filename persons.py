# A program to create a class person with a sub class customer.

class Person:
    def __init__(self, name, address, telephone ):
        self.__name = name
        self.__address = address
        self.__telephone = telephone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_telephone(self, telephone):
        self.__telephone = telephone

    def get_name(self):
        return self.__name
        
    def get_address(self):
        return self.__address

    def get_telephone(self):
        return self.__telephone

class Customer(Person):
    def __init__(self,name, address, telephone, customer_number):
        Person.__init__(self, name, address, telephone)
        self.__customer_number = customer_number 
        self.__status = 'True'

    def set_(self, customer_number):
        self.__customer_number = customer_number

    

    def get_customer_number(self):
        return self.__customer_number

    def get_status(self,mailing):
        if mailing == "y":
            return self.__status
        else:
            return 'False'

