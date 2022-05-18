class Customer:
    """ This class representa a customer.  It uses private attributes and property getters and setters.
        Setters have appropriate validation that raise an exception when invalid data is used."""
    
    def __init__(self, email='na', firstName='firstTest', lastName='lastTest'):
        self.__email = email
        self.__firstName = firstName
        self.__lastName = lastName

    @property
    def email(self):
        return self.__email

    @property
    def firstName(self):
        return self.__firstName

    @property
    def lastName(self):
        return self.__lastName

    @email.setter
    def email(self, email):
        if isinstance(email, str): #and id > 0 it's valid for a programmer to call p.id = 10
            self.__email = email
        else: # but invalid to use a non-integer value or a value that's < 0
            raise ValueError(f"Id must be a non-zero positive integer. {type(email)}  {email}") # this error cannot be ignored in the calling code

    @firstName.setter
    def firstName(self, firstName):
        if isinstance(firstName, str): #and len(code) == 4:
            self.__firstName = firstName
        else:
            raise ValueError(f"Code must a 4 character string {type(firstName)}  {firstName}")

    @lastName.setter
    def lastName(self, lastName):
        if isinstance(lastName, str):  #and len(description.strip()) > 0:
            self.__lastName = lastName #.strip()
        else:
            raise ValueError(f"Description must a non-empty character string {type(lastName)}  {lastName}")


    def __str__(self):
        return f'Customer(email: {self.__email}, FIRST: {self.__firstName}, LAST: {self.__lastName})'


    def __eq__(self, other):
        """ This "magic method" is called when you check the equality of 2 products.  I had to add this to the product class
        in order for find and __contains__ to work"""
        if isinstance(other, Customer):
            return (self.email == other.email and self.firstName == other.firstName and
                    self.lastName == other.lastName)
        else:
            return False