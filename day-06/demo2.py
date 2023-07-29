#tuple
def func1():
    
    
    list_1=[10,20,30,40,50,60]
    print(f"list_1={list_1}, type={type(list_1)}")

    tuple_1=(10,20,30,40,50,60)
    print(f"tuple_1={tuple_1}, type={type(tuple_1)}")

#func1()

def func2():
    #empty list way 1
    list_1=[]
    print(f"list_1={list_1}, type={type(list_1)}")
    
    #empty list way 2
    list_2=list()
    print(f"list_2={list_2}, type={type(list_2)}")
    
    #list with one value
    list_3=[10]
    print(f"list_3={list_3}, type={type(list_3)}")
    
    #empty tuple way 1
    tuple_1=()
    print(f"tuple_1={tuple_1}, type={type(tuple_1)}")
    
    #empty tuple way 2
    tuple_2=tuple()
    print(f"tuple_2={tuple_2}, type={type(tuple_2)}")
    
    print("-*_" * 30)
    
    #tuple with one value (consider as int)
    tuple_3=(10)
    print(f"tuple_3={tuple_3}, type={type(tuple_3)}")
    
    #consider as str    
    tuple_4=("red")
    print(f"tuple_4={tuple_4}, type={type(tuple_4)}")
    
    tuple_5=(10,)
    print(f"tuple_5={tuple_5}, type={type(tuple_5)}")
    
    tuple_6=("red",)
    print(f"tuple_6={tuple_6}, type={type(tuple_6)}")
    
#func2()

def func3(p1,p2):
    add=p1+p2
    sub=p1-p2
    mul=p1*p2
    div=p1/p2
    return add,sub,mul,div

#ans=func3(10,20)
#print(ans)
#print(f"add 10 + 20= {ans[0]}")
#print(f"sub 10 - 20= {ans[1]}")
#print(f"mul 10 * 20= {ans[2]}")
#print(f"div 10 / 20= {ans[3]}")
        
def func4():
    num=(10,20,30,30,40,30)
    print(num)
    
    count=num.count(30)
    print(f"30 repeated {count} times")
    
    pos=0
    for i in range(count):
        pos_30=num.index(30,pos)
        print(f"30 appears at {pos_30} position")
        pos=pos_30+1
    
    
func4()    


    
    
    
    
    
        
    