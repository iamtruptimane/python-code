def func1():
    num=[1,2,3,4,5]
    square=[]
    
    for n in num:
        square.append(n ** 2)
    print(num)    
    print(square)
#func1()

def func2():
    num=[1,2,3,4,5]
    for n in num:
        print(f"square of {n}={n ** 2}")
        
#func2()

def get_qube(n):
    return n ** 3

def func3():
    num=[1,2,3,4,5]
    
    qube=[]
    
    for n in num:
        qube.append(get_qube(n))
        
    print(num)
    print(qube)
#func3()

def func4():
    num=[1,2,3,4,5]
    
    #using lambda func
    cube=lambda x: x ** 3
    cubes=[]
    
    for p in num:
        cubes.append(cube(p))
        
    print(num)
    print(cubes)
    
#func4()

def get_square(p):
    return p ** 2

def func5():
    num=[1,2,3,4,5,6]
    
    #list
    cubes=list(map(get_qube, num))
    
    print(num)
    print(cubes)
    print("*" * 30)
    
    square=tuple(map(get_square, num))
    print(num)
    print(square)
    
#func5()  

def func6():
    num=[1,2,3,4,5,6]
    
    square=lambda x : x ** 2
    cube=lambda p : p ** 3
    
    squares=list(map(square,num))
    cubes=tuple(map(cube,num))
    
    print(num)
    print(squares)
    print("*" * 30)
    
    print(num)
    print(cubes)
#func6()

def func7():
    kilometer=[1,2,3,4]
    
    meter=lambda x : x * 1000
    
    meters=list(map(meter,kilometer))
    
    print(kilometer)
    print(meters)
    
#func7()

def func8():
    cars = [
        {"model": "i20", "company": "hyundai", "price": 7.5},
        {"model": "i10", "company": "hyundai", "price": 5.5},
        {"model": "nano", "company": "tata", "price": 2.5},
        {"model": "X5", "company": "BMW", "price": 35.5},
        {"model": "Inova", "company": "Toyota", "price": 20.5},
    ]
    
    cars_new=list(map(lambda car : {"model": car['model'], "company" : car['company'], "price": car['price']},cars))
    print(cars)
    print(cars_new)
    
func8()    
       
      
        
            

        
        