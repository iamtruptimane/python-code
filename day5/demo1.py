def func1():
    #empty list(1st way)
    list_1=[]
    print(list_1)
    print(f"type of list= {type(list_1)}")

    #empty list(2nd way)
    list_2=list()
    print(list_2)
    print(f"type of list= {type(list_2)}")

    #list with one value(1st way)
    list_3=[20]
    print(list_3)

    #list with one value(2nd way)
    list_4=list([20])
    print(list_4)

#func1()

def func2():
    list_1=[10,20,30,40,50]
    #using for in loop
    for number in list_1:
        print(f"number = {number}")
    print(f"length of list= {len(list_1)}")

    #using traditional for loop
    #index_pos=list(range(len(list_1)))
    index_pos=[0,1,2,3,4]
    for i in index_pos:
        print(f"value at {i}= {list_1[i]}")

#func2()

def func3():
    list_1=["india", "china", "japan", "uk", "usa"]

    for country in list_1:
        print(f"country = {country}")

    print(f"total number of countries = {len(list_1)}")

    index_pos=list(range(len(list_1)))

    for i in index_pos:
        print(f"country at {i} = {list_1[i]}")

#func3()

def func4():
    fruits=["mango", "orange", "apple", "banana"]

    for value in fruits:
        print(f"fruit = {value}")

    print(f" number of fruits = {len(fruits)}")

    index_pos=list(range(len(fruits)))
    for i in index_pos:
        print(f"fruit at {i} = {fruits[i]}")

func4()            
        




