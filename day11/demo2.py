#closure
def log(function):
    
    def inner(*args, **kwargs):
        print("*" * 30)
        print(f"inside inner")
        print(f"function name ={function.__name__}")
        print(f"args={args}")
        print(f"kwargs={kwargs}")
        function(*args,**kwargs)
        print("*" * 30)
    return inner

@log
def square(no):
    print(f"square of {no}={no ** 2}")


#square(3)
@log
def divide(p1,p2):
    if p2==0:
        print(f"number cannot be divide by zero")
    else:
        print(f"{p1}/{p2}={p1/p2}")
        
divide(40,20)            
        
                