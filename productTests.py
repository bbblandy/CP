from productBest import *


def testConstructor():
    p1 = Product()
    print(f"Testing constructor with default values.  Expect default values. {p1}")
    p2 = Product(101, "p101", "test description", 12.50, 2)
    print(f"Testing constructor with parameters.  Expect product 101. {p2}")


def testGetters():
    p = Product(101, "p101", "test description", 12.50, 2)
    print(f"Testing getters.  Expect individual attributes for product 101.")
    print(f"id: {p.getId()}, code: {p.getCode()}, description: {p.getDescription()}, unit price: {p.getUnitPrice()}, quantity: {p.getQuantity()}")


def testPropertyGetters():
    p = Product(101, "p101", "test description", 12.50, 2)
    print(f"Testing property getters.  Expect individual attributes for product 101.")
    print(f"id: {p.id}, code: {p.code}, description: {p.description}, unit price: {p.unitPrice}, quantity: {p.quantity}")


def testSetters():
    p = Product(101, "p101", "test description", 12.50, 2)
    p.setId(102)
    p.setCode("p102")
    p.setDescription("Edited test product")
    p.setUnitPrice(15.25)
    p.setQuantity(45)
    print(f"Testing setters.  Expect individual attributes for product 101 to change to 102. {p}")


def testPropertySetters():
    p = Product(101, "p101", "test description", 12.50, 2)
    p.id = 102
    p.code = "p102"
    p.description = "Edited test product"
    p.unitPrice = 15.25
    p.quantity = 45
    print(f"Testing property setters.  Expect individual attributes for product 101 to change to 102. {p}")

def testPropertySettersWithValidation():
    p = Product(101, "p101", "test description", 12.50, 2)
    try:
        p.id = "102"
    except ValueError as vErr:
        print ("An exception was thrown setting id to a string")
        print(vErr)
    try:
        p.id = -1
    except ValueError as vErr:
        print ("An exception was thrown setting id to a negative number")
        print(vErr)
    try:
        p.code = 102
    except ValueError as vErr:
        print("An exception was thrown setting code to an int")
        print(vErr)
    try:
        p.code = "p10"
    except ValueError as vErr:
        print("An exception was thrown setting code to a 3 character string")
        print(vErr)
    try:
        p.description = 102
    except ValueError as vErr:
        print("An exception was thrown setting description to an int")
        print(vErr)
    try:
        p.description = "    "
    except ValueError as vErr:
        print("An exception was thrown setting description to an empty string")
        print(vErr)
    try:
        p.unitPrice = "102.50"
    except ValueError as vErr:
        print ("An exception was thrown setting unit price to a string")
        print(vErr)
    try:
        p.unitPrice = -1
    except ValueError as vErr:
        print ("An exception was thrown setting unit price to a negative number")
        print(vErr)
    try:
        p.quantity = 102.50
    except ValueError as vErr:
        print ("An exception was thrown setting quantity to a float")
        print(vErr)
    try:
        p.quantity = -1
    except ValueError as vErr:
        print ("An exception was thrown setting quantity to a negative number")
        print(vErr)


def testEncapsulation():
    p = Product(101, "p101", "test description", 12.50, 2)
    try:
        print(p.id)
        p.id = 103
        print(p.id)
        #print (p.__id)
        #p.__id = 103
        #print (p.__id)
    except AttributeError as attErr:
        print("An attribute error was throws in testEncapsultion")
        print(attErr)




