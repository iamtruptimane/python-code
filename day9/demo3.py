def add1(p1,p2):
    addition=p1+p2
    print(f"addition={addition}")
    
#add1(10,20)
#add1(p1=10,p2=20)

def add2(p1,p2,p3):
    addition=p1+p2+p3
    print(f"addition={addition}")
#add2(10,20,30)
#add2(p1=10,p2=20,p3=30)

#variable lenghth argument function
def add(*args):
    print(f"args={args}, type={type(args)}")
    
    addition=0
    for value in args:
        addition=addition+value
    print(f"addition={addition}")
    
#add(10,20,30,40) 

def mul1(*args):
    multiplication=1
    for value in args:
        multiplication=multiplication * value
    print(f"multipliaction={multiplication}")
    
#mul1(2,3,4,5) #here you can pass as many as parameters you want

#or
def mul2(p1,p2,p3):
    multi=p1*p2*p3
    print(f"multiplication={multi}")
    
#mul2(2,3,4) #but here you can pass only 3 parameteres 

def draw_circle(*args, **kwargs):
    radius,colour,border=10, "green", 20
    print(f"args={args},type={type(args)}")
    print(f"kwargs={kwargs},type={type(kwargs)}")
    
    
    print(f"radius={kwargs.get('radius')}")
    print(f"colour={kwargs.get('colour')}")                 
    print(f"border={kwargs.get('border')}")
    
    #check if key radius exist
    if kwargs.get('radius'):
        radius=kwargs.get('radius')
    
    if kwargs.get('colour'):
        colour=kwargs.get('colour')
    
    if kwargs.get('border'):
        border=kwargs.get('border')
        
    print(f"radius={radius}")
    print(f"colour={colour}")                 
    print(f"border={border}")

#draw_circle()    
#draw_circle(colour="red")
draw_circle(radius=30,colour="green",border=10) 
   
    
        
        
        
        
        
        
        
                         
                     
    
        