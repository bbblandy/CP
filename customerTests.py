from customer import *

def testConstructor():
    c1 = Customer()
    print(f"Testing constructor with default values.  Expect default values. {c1}")
    c2 = Customer('@', 'Brendan', 'Blandy')
    print(f"Testing constructor with parameters.  Expect customer Brendan. {c2}")


# def testPropertyGetters():

def testPropertyGetters():
    c = Customer('@', 'Brendan', 'Blandy')
    print(f"Testing property getters.  Expect individual attributes for Customer c.")
    print(f"email: {c.email}, FIRST: {c.firstName}, LAST: {c.lastName}")

# def testPropertySetters():
def testPropertySetters():
    c = Customer('@', "FIRST", 'LAST')
    c.email = 'test@test.com'
    c.firstName = 'Brendan'
    c.lastName = 'Blandy'
    print(f"Testing property setters.  Expect individual attributes for Customer FIRST to change to Brendan. {c}")
# def testPropertySettersWithValidation():

def testPropertySettersWithValidation():
    c = Customer('@', "Brendan", "Blandy")
    try:
        c.email = 102
    except ValueError as vErr:
        print("An exception was thrown setting code to an int")
        print(vErr)
    try:
        c.firstName = 102
    except ValueError as vErr:
        print("An exception was thrown setting First Name to an int")
        print(vErr)
    try:
        c.lastName = 100
    except ValueError as vErr:
        print ("An exception was thrown setting Last Name to an int")
        print(vErr)


# def testEncapsulation():

def testEncapsulation():
    c = Customer('@', "Brendan", "Blandy")
    try:
        print(c.email)
        c.email = 'test@test.com'
        print(c.email)
        print (c.__email)
        c.__id = 'test2@test2.com'
        print (c.__email)
    except AttributeError as attErr:
        print("An attribute error was throws in test Encapsulation")
        print(attErr)



