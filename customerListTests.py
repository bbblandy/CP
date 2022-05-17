from customerList import *

def testConstructor():
    cList = CustomerList()
    print(f"Testing constructor.  Expect empty list. {cList}")
    print(f"Expect count property to be 0. {cList.count}")
    print(f"Expect len function to be 0. {len(cList)}")


def testAppend():
    cList = CustomerList()
    c1 = Customer(101, "p101", "test description 101")
    c2 = Customer(102, "p102", "test description 102")
    cList.append(c1)
    cList.append(c2)
    print(f"Testing append.  Expect list with 2 customers. {cList}")
    print(f"Expect count property to be 2. {cList.count}")
    print(f"Expect len function to be 2. {len(cList)}")


def createList():
    cList = CustomerList()
    c1 = Customer(101, "p101", "test description 101")
    c2 = Customer(102, "p102", "test description 102")
    c3 = Customer(103, "p103", "test description 103")
    cList.append(c1)
    cList.append(c2)
    cList.append(c3)
    return cList


def testPop():
    cList = createList()
    print(f"Testing pop.  Before pop expect list with 3 products. {cList}")
    print(f"Expect count property to be 3. {cList.count}")
    print(f"Expect len function to be 3. {len(cList)}")
    c3 = cList.pop()
    print(f"After pop with no parameter.  Expect first 2 products. {cList}")
    print(f"Expect popped product to be p103. {c3}")
    print(f"Expect count property to be 2. {cList.count}")
    print(f"Expect len function to be 2. {len(cList)}")
    c1 = cList.pop(0)
    print(f"After pop with 0 parameter.  Expect just p102. {cList}")
    print(f"Expect popped product to be p101. {c1}")
    print(f"Expect count property to be 1. {cList.count}")
    print(f"Expect len function to be 1. {len(cList)}")


def testFind():
    cList = createList()
    print(f"Testing find.  Current list with 3 products. {cList}")
    index = cList.find("p102")
    print(f"Called find with p102 as parameter.  Expect index to be 1. {index}")
    c2 = Customer(102, "p102", "test description 102")
    # this will return -1 if __eq__ is not defined on the product class
    index = cList.find(c2)
    print(f"Called find with Product object p102 as parameter.  Expect index to be 1. {index}")
    index = cList.find("p104")
    print(f"Called find with p104 as parameter.  Expect index to be -1. {index}")
    c4 = Customer(104, "p104", "test description 104")
    index = cList.find(c4)
    print(f"Called find with Product object p104 as parameter.  Expect index to be -1. {index}")


def testRemove():
    cList = createList()
    c2 = Customer(102, "p102", "test description 102")
    print(f"Testing find.  Current list with 3 products. {cList}")
    cList.remove(c2)
    print(f"Called remove with Product object p102 as parameter.  Expect list to now have 2 products. {cList}")
    c4 = Customer(104, "p104", "test description 104")
    try:
        pList.remove(p4)
        print(f"Called remove with Product object p104 as parameter.  An exception should have been thrown but was not.")
    except ValueError:
        print(f"Called remove with Product object p104 as parameter.  An exception was expected and was thrown")
        print(f"Expect list to still have 2 products. {cList}")


def testClear():
    cList = createList()
    print(f"Testing clear.  Current list with 3 products. {cList}")
    cList.clear()
    print(f"After the call to clear.  Expect list to be empty. {cList}")


def testGetItem():
    cList = createList()
    print(f"Testing list access by index.  Current list with 3 products. {cList}")
    c = cList[1]
    print(f"Element at index 1.  Expect p102. {c}")
    c = cList["p103"]
    print(f"Element with key of p103.  Expect p103. {c}")
    try:
        c = cList[2.5]
    except TypeError:
        print(f"Used [] with float as index.  An exception was expected and was thrown")


def testSetItem():
    cList = createList()
    print(f"Testing changing a list element by index.  Current list with 3 products. {cList}")
    c4 = Customer(104, "p104", "test description 104", 20, 4)
    cList[2] = c4
    print(f"Set element at index 2 to p104.  p104 should be at the end of the list. {cList}")
    try:
        cList["p104"] = c4
    except TypeError:
        print(f"Used [] with string as index.  An exception was expected and was thrown")
    try:
        cList[1] = "cat"
    except TypeError:
        print(f"Used [] with string element rather than a product.  An exception was expected and was thrown")


def testIn():
    cList = createList()
    print(f"Testing in.  Current list with 3 products. {cList}")
    c2 = Customer(102, "p102", "test description 102", 20, 4)
    c4 = Customer(104, "p104", "test description 104", 20, 4)
    print(f"Is p102 in the list?  Expect true  {c2 in cList}")
    print(f"Is p104 in the list?  Expect false  {c4 in cList}")


def testForLoop():
    cList = createList()
    print(f"Testing for loop.  Current list with 3 products. {cList}")
    print(f"Iterating through the list with for in.  Expect 3 individual products")
    for c in cList:
        print(c)


def testAdd():
    cList = createList()
    cList2 = createList()
    cListCombined = cList + cList2
    print(f"Testing adding 2 product lists.  Expect list with 6 products. {cListCombined}")