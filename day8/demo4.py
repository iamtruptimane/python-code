def func1():
    #1st way to do square of num using for in loop
    num=[1,2,3,4,5,6,7]
    square=[]
    for n in num:
        square.append(n ** 2)
    print(num)    
    print(square)
#func1()

def func2():
    #2nd way to make square of num using map
    num=[1,2,3,4,5,6,7]
    square=lambda x : x ** 2
    num1=list(map(square,num))
    print(num)
    print(num1)
#func2()

def func3():
    num=[1,2,3,4,5,6,7]
    
    #list comprheation
    num1=[n for n in num]
    print(f"num={num1}")
    
    square=[s ** 2 for s in num]
    print(f"square= {square}")
    
    cube=[c ** 3 for c in num]
    print(f"cube= {cube}")
    
#func3()

def func4():
    #find out even num using filter
    num=[1,2,3,4,5,6,7,8]
    even=lambda x : x %2 ==0
    num1=list(filter(even,num))
    print(num)
    print(num1)
    
    print("*" * 30)
    
    #find out even num using list comprheation
    num2=[x for x in num if x %2 ==0]
    print(num)
    print(num2)
#func4()

def func5():
    cars = [
        {"model": "i20", "company": "hyundai", "price": 7.5},
        {"model": "i10", "company": "hyundai", "price": 5.5},
        {"model": "nano", "company": "tata", "price": 2.5},
        {"model": "X5", "company": "BMW", "price": 35.5},
        {"model": "Inova", "company": "Toyota", "price": 20.5},
    ]
    
    expensive_car=[car for car in cars if car['price'] >20.00]
    print(expensive_car)
    
func5()
            
    
    
    
            
        