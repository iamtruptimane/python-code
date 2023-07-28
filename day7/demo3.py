def func1():
    #single dimensional list
    list_1=[10,20,30,40,50]
    
    #multidomensional list
    list_2=[
        [10,20],
        [30,40],
        [50,60]
    ]
    
    print(f"list_2[0]= {list_2[0]}")
    print(f"list_2[1]= {list_2[1]}")
    print(f"list_2[2]= {list_2[2]}")
    
    print("*" * 30)
    
    print(f"list_2[0][0]= {list_2[0][0]}")
    print(f"list_2[0][1]= {list_2[0][1]}")
    print(f"list_2[1][0]= {list_2[1][0]}")
    print(f"list_2[1][1]= {list_2[1][1]}")
    print(f"list_2[2][0]= {list_2[2][0]}")
    print(f"list_2[2][1]= {list_2[2][1]}")
    
#func1()

def func2():
    list_1=[
        [10,20],
        [30,40,50],
        [60,70,80,90]
    ] 
    for row in list_1:
         for col in row:
             print(f"value = {col}") 
    print("*" * 30)
    print({range(len(list_1))}) 
    
    for row in range(len(list_1)):
        print(f"row at position= {row}= {list_1[row]} ") 
        tmp_list = list_1[row]
        for col in range(len(tmp_list)):
            print(f"value at [{row}][{col}] = {list_1[row][col]}")       
             
#func2()

def func3():
    #list of tuples
    p1=[
        ("raj", 20, "pune"),
        ("sam", 24, "mumbai"),
        ("jon", 30, "sangli")
    ]
    
    for row in p1:
        print(f"name= {row[0]}")
        print(f"age= {row[1]}")
        print(f"add= {row[2]}")
        
        print("*" * 30)
        
    for row in p1:
        name,age,add=row
        #name,age,add=raj,20,pune
        print(f"name={name}")
        print(f"age={age}")    
        print(f"add={add}") 
        
        print("*" * 30) 
        
    for name,age,add in p1:
        print(f"name={name}")
        print(f"age={age}")      
        print(f"add={add}")      
              
        print("*" * 30)    
#func3()

def func4():
    #tuple
    t1=10,20,30,40
    
    print(t1[0])
    print(t1[1])
    print(t1[2])
    print(t1[3])
    
    print("*" * 30)
    
    n1,n2,n3,n4=10,20,30,40
    print(f"n1= {n1}")
    print(f"n2= {n2}")
    print(f"n3= {n3}")
    print(f"n4= {n4}")
    
#func4()

def func5():
    p1="raj", 20, "pune"
    
    print(f"name={p1[0]}")
    print(f"age={p1[1]}")
    print(f"add={p1[2]}")
    
    print("*" * 30)
    
    name,age,add="raj",20, "pune"
    print(f"name={name}")
    print(f"age={age}")
    print(f"add={add}")
    
#func5()    
    
    

def func6():
    #n1=10
    #n2=20
    
    n1,n2=10,20
    print(f"n1={n1}")
    print(f"n2={n2}")
    
    #swap
    n2,n1=n1,n2
    print(f"n1={n1}")
    print(f"n2={n2}")
    
#func6()

def func7():
    #list of dictionaries
    person1= [
        {"name": "raj", "age": 20, "colour": "red"},
        {"name": "sam", "age": 30, "colour": "yellow"},
        {"name": "jon", "age": 40, "colour": "black"},
        {"name": "tom", "age": 50, "colour": "green"}
        
    ]
    
    for value in person1:
        print(f"name={value['name']}")
        print(f"age={value['age']}")
        print(f"colour={value['colour']}")
        
#func7()        
        
        
        
    
            
               
    
