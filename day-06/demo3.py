#set
def func1():
    #list
    num1=[10,20,30,40,50,60,70]
    print(f"num1={num1}, type={type(num1)}")
    
    #tuple
    num2=(10,20,30,40,50,60,70)
    print(f"num2={num2}, type={type(num2)}")
    
    #set
    num3={10,20,30,40,50,60,70}
    print(f"num3={num3}, type={type(num3)}")
    
    #list
    num4=[10,20,30,40,50,60,70]
    set_1=set(num4)
    print(f"num4={num4}, type= {type(num4)}")
    print(f"set_1={set_1}, type={type(set_1)}")
    
#func1()    
    
def func2():
    set1={10,20,30,40}
    set2={30,40,50,60}
    
    print(f"s1 union s2 ={set1.union(set2)}")
    print(f"s2 union s1 ={set2.union(set1)}")
    
    print(f"set1 intersection set2= {set1.intersection(set2)}")
    print(f"set2 intersection set1= {set2.intersection(set1)}")
    
    print(f"set1 - set2 = {set1.difference(set2)}")
    print(f"set2 - set1 = {set2.difference(set1)}")
    
#func2()    

def func3():
    s1={10,20,30,40,50}
    print(s1)
    
    s1.add(60)
    s1.add(60)
    s1.add(60)
    s1.add(60)
    
    print(s1)
    
#func3()

def func4():
    s1={10,20,30,40,50}
    print(s1)
    
    s1.remove(20)
    print(s1)
    
    #raise and error if we are trying to remove value which is not in set
    #s1.remove(60)
    #print(s1)
    
    s1.discard(30)
    print(s1)
    
    # does not raise and error if we are trying to remove value which is not in set
    s1.discard(100)
    print(s1)
    
func4()    
    
        
    