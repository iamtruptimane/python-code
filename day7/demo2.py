def func1():
    #empty list
    l1=[]
    print(f"l1={l1}, type={type(l1)}")
    
    l2=list()
    print(f"l2={l2}, type={type(l2)}")
    
    #empty tuple
    t1=()
    print(f"t1={t1}, type={type(t1)}")
    
    t2=tuple()
    print(f"t2={t2}, type={type(t2)}")
    
    #empty set(only one way)
    s1=set()
    print(f"s1={s1}, type={type(s1)}")
    
    #frozonset (only one way)
    f1=frozenset()
    print(f"f1={f1}, type={type(f1)}")
    
    #empty dictionary
    d1={}
    print(f"d1={d1}, type={type(d1)}")
    
    d2=dict()
    print(f"d2={d2}, type={type(d2)}")
    
#func1()

def func2():
    
    #name1="person1"
    #add1="pune"
    #age1=30
    
    #name2="person2"
    #add2="mumbai"
    #age2=20
    
    #list
    #person1=["person1", "pune", 30]
    #person2=["person2", "mumbai", 20]
    
    #tuple
    person1=("person1", "pune", 30)
    person2=("person2", "mumbai", 20)
    
    #set
    #person1={"person1", "pune", 30}
    #person2={"person2", "mumbai", 20}
    
    print(f"name1={person1[0]}")
    print(f"add1={person1[1]}")
    print(f"age1={person1[2]}")
    
    print("-" * 20)
    print(f"name2={person2[0]}")
    print(f"add2={person2[1]}")
    print(f"age2={person2[2]}")
    
#func2()

def func3():
    #dictionary
    #it is collection of key-value pair
    
    p1={"name": "raj", "add": "pune", "age": 30}
    print(f"p1={p1}, type={type(p1)}")
    
    p2={"name": "sam", "add": "mumbai", "age": 20}
    print(f"p2={p2}, type={type(p2)}")
    
    print(f"name1={p1['name']}")
    print(f"add1={p1['add']}")
    print(f"age1={p1['age']}")
    
    print("-" * 20)
    
    print(f"name2={p2['name']}")
    print(f"add2={p2['add']}")
    print(f"age2={p2['age']}")
    
    print("-" * 20)
    
    print(f"key={p1.keys()}")
    print(f"value={p1.values()}")
#func3()

def func4():
    p1={
        "name": "raj",
        "age": 20,
        "add":{
            "city": "pune",
            "country":"India",
            "state": "MH"
        },
        "colour":[
            "red",
            "blue",
            "pink"
        ]      
    } 
    
    print(f"name= {p1['name']}")
    print(f"age= {p1['age']}")
    #print(f"add= {p1['add']}")
    #print(f"colour= {p1['colour']}")
    print(f"address= {p1['add']['city']},{p1['add']['country']}, {p1['add']['state']} ")
    print(f"colour= {p1['colour'][0]}, {p1['colour'][1]}, {p1['colour'][2]}")
    
    print("*" * 30)
    
    values=p1.values()
    for value in values:
        print(f"value= {value}")
        
    print("*" * 30)
    
    keys=p1.keys()
    for key in keys:
        print(f"{key}= {p1[key]}")    
    
#func4()

def func5():
    d1={}
    
    print("enter name")
    d1['name']=input()
    
    print("enetr age")
    d1['age']=input()
    
    print(d1)
    
func5()        
       
    
    
        
    
    
    
    
    
    
    
    
    
    
       
    
    
    
    
    

    