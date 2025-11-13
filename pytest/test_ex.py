# Pytest Naming Rules (very important!)

# ✅ File names should start with test_
# ✅ Function names should start with test_
# ✅ Don’t use classes unless needed
# ✅ Don’t print — Pytest handles output reporting



# def test_initialCheck():
#     print("this is first test")

# def add(a,b):
#     return a + b

# def test_addition():
#     result = add(3,2)
#     assert result == 5

# def test_sub():
#     a = 10
#     b = 5
#     assert a - b == 4


def test_uppercase():
    word = "hello"
    assert word.upper() == "HELLO"

def test_isdigit():
    number = "123"
    assert number.isdigit()