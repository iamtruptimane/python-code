#global variable
num=100

#global func
#outer func
def func1():
    print("inside func1")
    
    #local avriable
    salary=10.3
    
    #ineer fun
    #local func
    def inner_func():
        print("inside inner_func")
        print(f"inner_func={inner_func}, type= {type(inner_func)}")
        
    inner_func()
    
#func1() 
#inner_func() # we cannot call ineer_func outside the outer func
#print(f"inner_func={inner_func}, type= {type(inner_func)}")

def func2():
    outer_variable=10 
    print("inside outer variable")
    print(f"outer variable={outer_variable}")
    
    def inner_func1():
        ineer_vari1=20
        print("inside inner variable 1")
        print(f"inner variable={ineer_vari1}")
        print(f"outer variable={outer_variable}")
        
        
    inner_func1()
    
    def inner_func2():
        inner_vari2=30
        print("inside inner variable 2")
        #print(f"inner variable={ineer_vari1}")
        print(f"inner variable 2={inner_vari2}")
        
    inner_func2()
    
func2()
#print(f"inner variable={ineer_vari1}")

# inner function can access all the members of outer function
# outer function can not access any of the inner function members
    
        
        
        
        
        
            
       
    