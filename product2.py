class Product:
    """ This class representa a product.  This uses properties rather than getters and setters.  
        The attributes are PRIVATE and properties enforce encapsulation 
        BUT the syntax in the calling code is more intuitive. p.id rather than p.getId()."""

    def __init__(self, id=0, code="na", description="na", unitPrice=0, quantity=0):
        self.__id = id
        self.__code = code
        self.__description = description
        self.__unitPrice = unitPrice
        self.__quantity = quantity

    @property # the @property decorator signifies that this method is a property getter
    def id(self):
        return self.__id

    @property
    def code(self):
        return self.__code

    @property
    def description(self):
        return self.__description

    @property
    def unitPrice(self):
        return self.__unitPrice

    @property
    def quantity(self):
        return self.__quantity

    @id.setter # the @id.setter decorator signifies that this method is the setter for the id property
    def id(self, id):
        self.__id = id

    @code.setter
    def code(self, code):
        self.__code = code

    @description.setter
    def description(self, description):
        self.__description = description

    @unitPrice.setter
    def unitPrice(self, unitPrice):
        self.__unitPrice = unitPrice

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    def __str__(self):
        return f'Product(id: {self.__id}, code: {self.__code}, description: {self.__description}, ' \
               f'unit price: {self.__unitPrice}, quantity: {self.__quantity})'



