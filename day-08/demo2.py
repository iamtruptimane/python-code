def func1():
    num=[1,2,3,4,5,6,7]
    for n in num:
        if n % 2 == 0:
            print(n)
#func1()

def func2():
    num=[1,2,3,4,5,6,7]
    even_num=[]
    
    for n in num:
        if n % 2 == 0:
            even_num.append(n)
            
    print(num)
    print(even_num)
    print("*" * 30)
    
    for i in range(len(num)):
        if i % 2==0:
            print(i)
            
#func2()

def func3():
    num=[1,2,3,4,5,6,7]
    even=lambda x : x % 2 ==0
    
    num1=list(map(even,num))
    num2=list(filter(even,num))
    
    print(num)
    print(num1)
    print(num2)
    
#func3()

def func4():
    num=[1,2,3,4,5,6,7]
    odd=lambda x : x %2 != 0
    
    num1=list(filter(odd,num))
    print(num)
    print(num1)
#func4()

def func5():
    cars = [
        {"model": "i20", "company": "hyundai", "price": 7.5},
        {"model": "i10", "company": "hyundai", "price": 5.5},
        {"model": "nano", "company": "tata", "price": 2.5},
        {"model": "X5", "company": "BMW", "price": 35.5},
        {"model": "Inova", "company": "Toyota", "price": 20.5},
    ]
    
    cars_affordable=lambda car : car['price'] < 10.0
    cars_expensive=lambda car : car['price'] > 10.0
    car1=list(filter(cars_affordable,cars))
    car2=list(filter(cars_expensive,cars))
    
    
    print(car1)
    print("*" * 30)
    print(car2)
#func5()

def func6():
    persons = [
        {"name": "person1", "address": "pune", "age": 40, "email": "person1@test.com"},
        {"name": "person2", "address": "mumbai", "age": 20, "email": "person2@test.com"},
        {"name": "person3", "address": "nashik", "age": 30, "email": "person3@test.com"},
        {"name": "person4", "address": "satara", "age": 10, "email": "person4@test.com"}
    ]
    
    old_person=lambda age : age['age'] >=30 and age['age'] <=40
    young_person=lambda age : age['age'] >=10 and age['age']<=20
    
    p1=list(filter(old_person,persons))
    p2=list(filter(young_person,persons))
    
    print(p1)
    print("*" * 30)
    print(p2)
#func6()            
            
        
                
                    
        