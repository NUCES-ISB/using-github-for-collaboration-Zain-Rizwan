from app import add,mul,sub,div

def tester():
    assert add(2,4) == 6
    assert mul(2,3) ==6
    assert div(6,2) == 3
    assert sub(10,3) == 7
    
tester()