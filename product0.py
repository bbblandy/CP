class Product:
    """ this class represents a product.  This version has public attributes and getters and setters. """
    
    # self refers to the calling object.  It is passed as the first parameter in each method definition
    def __init__(self, id=0, code="na", description="na", unitPrice=0, quantity=0):
        """ init is a "magic method" that is used to construct or instantiate a product.  
            p = Product() will create a product with default attribute values 
            p = Product(1, "p001", "this is the description", 24.99, 10) will create a product for which each attribute has an explicit value"""
        self.id = id        # creates a PUBLIC instance variable called id.  Each object will have this attribute
        self.code = code
        self.description = description
        self.unitPrice = unitPrice
        self.quantity = quantity

    # getters or accessors provide access to each attribute
    def getId(self):
        return self.id

    def getCode(self):
        return self.code

    def getDescription(self):
        return self.description

    def getUnitPrice(self):
        return self.unitPrice

    def getQuantity(self):
        return self.quantity

    # setters or mutators allow a programmer to change attribute value 
    def setId(self, id):
        self.id = id

    def setCode(self, code):
        self.code = code

    def setDescription(self, description):
        self.description = description

    def setUnitPrice(self, unitPrice):
        self.unitPrice = unitPrice

    def setQuantity(self, quantity):
        self.quantity = quantity

    def __str__(self):
    """ another "magic method" that converts a product object into a string.
        When you call print(p) or print(str(p)) this method is called "under the covers" on your behalf"""
        return f'Product(id: {self.id}, code: {self.code}, description: {self.description}, ' \
               f'unit price: {self.unitPrice}, quantity: {self.quantity})'



