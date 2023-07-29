num=100 #global variable
print(f"value of num before calling function={num}")

def func1():
    print(f"inside func1")
    
    #local variable
    #it cannot modify global variable value
    num=300
    print(f"value of num inside func={num}")
    
#func1()

#print(f"value of func after calling func1={num}") 

def func2():
    print("inside func2")
    
    #to modify global variable value inside func
    #and to stop creating copy of local variable num
    global num
    num=300
    print(f"value of num inside func2={num}")
    
func2()
print(f"value of func after calling func2={num}") 

       