def can_vote(person):
    if person["age"] >=18:
        print("yes")
    else:
        print("no")
        
        
def person_info(person):
    print(f"name: {person['name']}")
    print(f"age:{person['age']}")


person1={"name": "Rahul", "age" : 23}
car={"model" : "iphone", "company": "apple"}

can_vote(person1)
person_info(person1)
#person_info(car)

                      
