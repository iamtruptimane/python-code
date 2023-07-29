def func1():
    list_1=[10,20,30,40]

    print(f"before appending list will be = {list_1}")
    #append
    list_1.append(50)
    print(f"after appending list will be = {list_1}")

    print("enter value:")

    value=input()
    #typcasting str to int
    v=int(value)
    list_1.append(v)

    print(list_1)

    list_2=["india", "japan", "china"]
    print(list_2)

    list_2.append("uk")
    print(list_2)

    print("enter country name :")

    country=input()
    list_2.append(country)
    print(list_2)

    list_3=[10.2, 13.4, 12.4, 20.0 ]
    print(list_3)

    list_3.append(12.5)
    print(list_3)

    print("enter float value :")
    value=input()
    v=float(value)
    list_3.append(v)
    print(list_3)


#func1() 

def func2():
    #insert
    list_1=[10,20,30,40,50]
    print(list_1)

    list_1.insert(2,60)
    print(list_1)

    print("enter value 1st between 0-4 :")
    num1=input()
    n=int(num1)

    print("enter value 2nd between 10-100 :")
    num2=input()
    m=int(num2)
    list_1.insert(n,m)
    print(list_1) 

    #str
    list_2=["india", "japan", "china"]
    print(list_2)
    print(f"length of list={len(list_2)}")

    list_2.insert(1,"uk")
    print(list_2)
    print(f"length of list={len(list_2)}")

    print("enter value between 0-2:")
    s=input()
    s1=int(s)

    print("enter any country name:")
    p=input()

    list_2.insert(s1,p)
    print(list_2)

    #float
    list_3=[10.0, 23.5, 34.8, 24.9]
    print(list_3)

    list_3.insert(3,34.5)
    print(list_3)

    print("enter neumber between 0-3")
    q=input()
    q1=int(q)

    print("enter any float value :")
    w=input()
    w1=float(w)

    list_3.insert(q1,w1)
    print(list_3)


    

#func2()

def func3():
    #pop
    list_1=[10,20,30,40,50]
    print(list_1)

    #list_1.pop()
    #print(list_1)

   # list_1.pop(3)
   # print(list_1)
   
    print("enter value between 0-4:")
    q=input()
    q1=int(q)

    list_1.pop(q1)
    print(list_1)

#func3() 

def func4():
    list_1=[10,20,30,40,30,50,60]
    print(list_1)

    #remove
    list_1.remove(30)
    print(list_1)
    #it removes only one occurence of 30

    print("enter number from above list :")
    value=input()
    v=int(value)
    list_1.remove(v)
    print(list_1)

#func4() 

def func5():
    list_1=[10,20,30,40,30,50,60,30]
    print(list_1)

    count_30=list_1.count(30)
    print(f"30 repeated {count_30} times")
    print(f"range ={range(count_30)}")

    for i in list_1:
        print(i)

    for i in range(count_30):
        print(i)
        list_1.remove(30)

    print(list_1)    

#func5()

def func6():
    colour=["black", "white", "red", "green", "red", "red"]
    print(colour)

    print(f"red repeated {colour.count('red')} times")

    colour_count=colour.count("red")

    for i in range(colour_count):
        colour.remove("red")

    print(colour)

    fruits=["mango", "banana", "mango", "mango", "mango"]
    print(fruits)

    print(f"mango repeated {fruits.count('mango')} times ")

    fruit_count=fruits.count("mango")
    for i in range(fruit_count):
        fruits.remove("mango")

    print(fruits) 

    fruits=["mango", "banana", "mango", "mango", "mango","banana", "apple"]
    print(fruits)

    print("enter fruit name you want to remove:")
    f=input()
    print(f"{f} repeated {fruits.count(f)} times")

    fruit_count=fruits.count(f)
    for i in range(fruit_count):
        fruits.remove(f)

    print(fruits)

#func6()

def func7():
    list_1=[10,20,50,40,50,60,50,80]
    print(f"50 repeated {list_1.count(50)} times")
    
    #position_50=list_1.index(50)
    #print(f"50 appears at positon {position_50}")
    
    #position_50=list_1.index(50,3)
    #print(f"50 appears at postion {position_50} ")
    
    #position_50=list_1.index(50,5)
    #print(f"50 appears at {position_50}")
    
    count=list_1.count(50)
    position=0
    for i in range(count):
        position_50=list_1.index(50,position)
        print(f"50 appears at {position_50}")
        
        position=position_50+1
    print("-" * 20)    
        
    list_2=[30,20,30,40,30,50]
    print(f"30 repeated at {list_2.count(30)} times")
    
    position=0
    count=list_2.count(30)
    for i in range(count):
        position_30=list_2.index(30,position)
        print(f"30 appears at {position_30}")
        
        position=position_30+1
    print("-" * 20)    
        
    fruits=["apple", "grapes", "apple", "mango", "apple"]
    print(f"apple repeated {fruits.count('apple')} times")
    
    position=0
    count=fruits.count('apple')
    for i in range(count):
        position_apple=fruits.index('apple', position)
        print(f"apple appears at {position_apple}")
        position=position_apple+1        
    
#func7()

def func8():
    list_1=[20,10,40,30,60,40,70]
    print(list_1)
    
    list_1.sort()
    print(f"ascending list= {list_1}")
    list_1.reverse()
    print(f"decending list={list_1}")
    
    list_1.sort(reverse=True)
    print(f"descending list={list_1}")
    
    print("-" * 30)
    
    list_2=[30,20,10,40,60,50]
    print(f"original list={list_2}")
    
    list_2_copy=list_2.copy()
    print(f"copy of list={list_2_copy}")
    
    list_2_copy.sort()
    print(f"ascending list={list_2_copy}")
        
#func8() 

def func9():
    list_1=[10,30,50,60,20]
    print(list_1)
    
    list_1.reverse()
    print(f"reverse of list={list_1}")
    
#func9()

def func10():
    list_1=[10,30,20,40,50]
    print(list_1)
    
    list_1.clear()
    print(f"clear list={list_1}")
    
#func10()

def func11():
    list_1=[10,20,30,40,50]
    list_2=[60,70,80,90,100]
    
    print(list_1)
    print(len(list_1))
    
    #to add list_2 in list_1
    list_1.extend(list_2)
    print(list_1)
    print(len(list_1))
    
func11()                            


