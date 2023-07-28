#class
#empty class
class Person:
    pass

#instantiation:creating an object of class
#refrence = object
person=Person()

#object=collection of key value pair
#key=attribute
print(person.__dict__)

#add new attributes in object
setattr(person, "name", "Rahul")
setattr(person, "age", 25)
print(person.__dict__)

#getting value of an attribute
print(f"name : {getattr(person,'name')}")
print(f"age: {getattr(person, 'age')}")

#creating a another object
person2=Person()

setattr(person2,"name","Radha")
setattr(person2,"age",30)
print(person2.__dict__)

print(f"name: {getattr(person2,'name')}")
print(f"age:{getattr(person2,'age')}")

