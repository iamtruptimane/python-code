def add(p1,p2):
    return p1+p2

def sub(p1,p2):
    return p1-p2

def execute(func):
    print(f"function={func}")
    
    print("*_*" * 20)
    print(F"result={func(10,20)}")
    print("*_*" * 20)
    
execute(add)
execute(sub)

mul=lambda x,y : x * y
print(f"multiply={mul}")
execute(mul)    
    
