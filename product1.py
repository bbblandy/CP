class Product:
    """ This class representa a product.  This version changes the attributes to PRIVATE.
        Most object oriented languages would use private attributes to implement encapsulation and data hiding."""
    def __init__(self, id=0, code="na", description="na", unitPrice=0, quantity=0):
        self.__id = id # __ denotes private in Python
        self.__code = code
        self.__description = description
        self.__unitPrice = unitPrice
        self.__quantity = quantity

    def getId(self):
        return self.__id

    def getCode(self):
        return self.__code

    def getDescription(self):
        return self.__description

    def getUnitPrice(self):
        return self.__unitPrice

    def getQuantity(self):
        return self.__quantity

    def setId(self, id):
        self.__id = id

    def setCode(self, code):
        self.__code = code

    def setDescription(self, description):
        self.__description = description

    def setUnitPrice(self, unitPrice):
        self.__unitPrice = unitPrice

    def setQuantity(self, quantity):
        self.__quantity = quantity

    def __str__(self):
        return f'Product(id: {self.__id}, code: {self.__code}, description: {self.__description}, ' \
               f'unit price: {self.__unitPrice}, quantity: {self.__quantity})'



