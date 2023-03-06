# from hello import hello

# def test_hello():
#     # because there is no return value of the hello function
#     # just print output
#     assert hello("David") == "Hello, David"
#     assert hello() == "Hello, world"

from hello import hello

def test_hello():
    # because there is no return value of the hello function
    # just print output
    assert hello("David") == "Hello, David"

def test_hello_():
    assert hello() == "Hello, world"
