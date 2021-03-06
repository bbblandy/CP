from customer import *

class CustomerList:
    """This class represents a list of customer objects """

    # region constructor
    def __init__(self):
        self.__customers = []

    # endregion

    # region properties
    @property
    def count(self):
        return len(self.__customers)

    # endregion

    # region methods that provide functionality similar to the built in list
    def append(self, item):
        if isinstance(item, Customer):
            self.__customers.append(item)
        else:
            raise TypeError(f"Object must be a valid customer object {type(item)}  {item}")

    def pop(self, index=None):
        if index is None:
            return self.__customers.pop()
        else:
            return self.__customers.pop(index)

    def find(self, item):
        if isinstance(item, Customer):
            index = 0
            for customer in self.__customers:
                if customer == item:
                    return index
                index += 1
            return -1
        elif isinstance(item, str):
            index = 0
            for customer in self.__customers:
                if customer.email == item:
                    return index
                index += 1
            return -1
        else:
            return -1

    def remove(self, item):
        index = self.find(item)
        if index == -1:
            raise ValueError(f"{item} is not in the customer list")
        else:
            self.pop(index)

    def clear(self):
        self.__customers = []

    # endregion

    # region magic or dunder methods
    def __str__(self):
        output = f"CustomerList["
        for customer in self.__customers:
            output += customer.__str__() + " "
        output += "]"
        return output

    def __len__(self):
        """Allows a programmer to use the len function to get the length of a customer list"""
        return len(self.__customers)

    def __getitem__(self, item):
        """Allows a programmer to [] to get an element in a customer list"""
        if isinstance(item, int):
            return self.__customers[item]
        elif isinstance(item, str):
            return self.__customers[self.find(item)]
        else:
            raise TypeError(f"Index must an int or a 4 character string {type(item)}  {item}")

    def __setitem__(self, key, value):
        """Allows a programmer to [] to mutate an element in a customer list"""
        if isinstance(key, int) and isinstance(value, Customer):
            self.__customers[key] = value
        elif not isinstance(key, int):
            raise TypeError(f"Index must an int {type(key)}  {key}")
        elif not isinstance(value, Customer):
            raise TypeError(f"Item must a customer object {type(value)}  {value}")

    def __delitem__(self, key):
        """Allows a programmer to use del to delete an element from a customer list"""
        if isinstance(key, int):
            del self.__customers[key]
        else:
            raise TypeError(f"Index must an int {type(key)}  {key}")

    def __add__(self, other):
        """Allows concatenation of customer lists.  Does not make a copy of the individual customers"""
        if isinstance(other, CustomerList):
            newList = CustomerList()
            for p in self.__customers:
                newList.append(p)
            for p in other.__customers:
                newList.append(p)
            return newList
        else:
            raise TypeError(f"Other must a customer list {type(other)}  {other}")

        ''' documentation suggests these are necessary to use in operator and for loop but testing indicates they are NOT necessary.
        I assume that's because we have written __eq__ in thee Product class and __getItem__ in ProductList
        def __contains__(self, item):
            if isinstance(item, Product):
                return self.find(item) != -1
            else:
                return False

        def __iter__(self):
            return self.__products.__iter__()

        def __next__(self):
            return self.__products.__next__()
        '''

    # endregion

