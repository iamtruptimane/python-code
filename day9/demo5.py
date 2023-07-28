def add(p1,p2):
    print(f"addition={p1+p2}")
    
def sub(p1,p2):
    print(f"subtraction={p1-p2}")
    
def mul(p1,p2):
    print(f"multiplication={p1*p2}")
    
def div(p1,p2):
    print(f"division={p1/p2}")
    
def execute(function):
    print(f"function={function}")
    function(10,20)
    function(30,40)
    function(20,30)
    function(30,20)
    function(10,30)

execute(add)
execute(sub)            
execute(mul)            
execute(div)            
           
            
        
        