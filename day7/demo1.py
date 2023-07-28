def func1():
    #mutable set
    s1={10,20,30,40,50}
    print(f"s1={s1}, type={type(s1)}")
    
    s1.add(70)
    s1.add(70)
    s1.add(70)
    
    print(s1)
#func1()    

def func2():
    #immutable set
    s1=frozenset([10,20,30,10,20,30,10,20,30])
    print(f"s1={s1}, type={type(s1)}")
    
    #cannot add coz it is immutable
    #s1.add(80)
    #print(s1)
    
func2()    