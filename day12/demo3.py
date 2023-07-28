class Person():
    pass

def can_vote(person):
    if getattr(person,'age') >= 18:
        print(f"{getattr(person,'name')} is eligible for voting")
    else:
        print(f"{getattr(person,'name')} is not eligible for voting")
        
def print_info(person):
    print(f"name: {getattr(person,'name')}")
    print(f"age:{getattr(person, 'age')}")
    
p1=Person()

setattr(p1,"name", "Trupti")
setattr(p1, "age", 23)
setattr(p1,"print_info", print_info)  #function alias
setattr(p1,"can_vote", can_vote)

can_vote(p1)
print_info(p1) 
print(p1.__dict__)

#one way to access attr in object
print(f"name: {getattr(p1,'name')}")
print(f"age:{getattr(p1,'age')}")
#print(f"print_info:{getattr(p1,print_info)}")
function=getattr(p1,'can_vote') #function=can_vote (function aliase)
function(p1)

#another way to access attr in object
print(f"name: {p1.name}")
print(f"age:{p1.age}")
p1.print_info(p1)
p1.can_vote(p1)

p2=Person()
setattr(p2,"name","sam")
setattr(p2,"age", 10)
setattr(p2,"print_info",print_info)
setattr(p2,"can_vote",can_vote)

print(p2.__dict__)

can_vote(p2)
print_info(p2)

print(f"name: {p2.name}")
print(f"age: {p2.age}")

p3=Person()
p3.name="Radha"
p3.age=17
p3.print_info=print_info

print(p3.__dict__)

print(f"name:{p3.name}")
print(f"age:{p3.age}")

can_vote(p3)





   
    
                