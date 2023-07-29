#slicing
def func1():
    num=[10,20,30,40,50,60,70,80]
    print(num)
    
    num_1=[]
    pos=range(1,5)
    for i in pos:
        num_1.append(num[i])
    print(num_1)
    
    colour=["red", "yellow", "black", "orange"]
    print(colour)
    
    colour_slice=[]
    #position=[0,1,2]
    pos=range(0,2)
    for i in pos:
        colour_slice.append(colour[i])
    print(colour_slice)    
    
#func1()

def func2():
    num=[10,20,30,40,50,60,70,80]
    print(num)
    
    print(num[1:4])
    
    print(num[0:5])
    print(num[:5])
    
    print(num[1:8])
    print(num[1:])
    
    print(num[0:8])
    print(num[:])
    print(num)
     
    
#func2()

def func3():
    #find out even position value
    num=[10,20,30,40,50,60,70,80]
    print(num)
    num_even=[]
    pos=range(len(num))
    for i in pos:
        if i % 2 ==0:
            num_even.append(num[i])
    print(f"num_even = {num_even}")
    
    num2=[10,20,30,40,50,60,70,80]
    num_odd=[]
    pos=range(len(num2))
    for i in pos:
        if i % 2 != 0:
            num_odd.append(num[i])
    print(f"num_odd={num_odd}")
            
#func3()

def func4():
    num=[10,20,30,40,50,60,70,80]
    
    print(F"even_num={num[::2]}")
    print(f"num_odd={num[1::2]}")
    
func4()                
    
    
        