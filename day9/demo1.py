#global scope
num=100

def func1():
    print(f"num ={num}")
    
    #local variable
    colour="red"
    print(f"colour={colour}")
func1()

#if trying to call local variable ouside function it doesnt work
#print(f"colour={colour}")

def func2():
    print(f"num ={num}") #global variable
    
    #if im trying to call local variable in other function it will give me error
    #print(f"colour={colour}")
    
func2()    
    
    
    

    