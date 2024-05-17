#pytest practice

# def test_f1():
#     n = 25
#     assert n == 25 


def add():
    n1 = 10 
    n2 = 20
    return n1+n2

print(add())

def test_add():
    assert add() == 30