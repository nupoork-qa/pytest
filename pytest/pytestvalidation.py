#fixtures : provides set of reusable set of code


import pytest

@pytest.fixture(scope="module") #scope can be function,module,class,session

def preWork():
    print("browser instance")

def test_initialCheck(): #to test use test keyword it will be test function
    print("first test")

def test_secondCheck(preWork): #fixture name as parameter
    print("second test")