#square of number
def square(number):
    return number ** 2

print(f"square of 5 = {square(5)}")

#inline func (lambda)

square= lambda number : number ** 2
print(f"square of 5 = {square(5)}")
print(f"square ={square}")
print(f"type= {type(square)}")

#cube of number
def cube(num):
    return num ** 3

print(f"cube = {cube}")
print(f"cube of 4 = {cube(4)}")
print(f"type = {type(cube)}")

#inline func of cube

cube=lambda num: num ** 3
print(f"cube of 3 = {cube(3)}")
print(f"cube = {cube}")
print(f"type = {type(cube)}")

# addition
def add(n1,n2):
    return n1 + n2

addition = add(30,40)
print(f"30 + 40 = {addition}")

#inline add
add= lambda n1,n2:n1+n2
print(f"30+40 = {add(30,40)}")
print(f"add = {add}")

#multiplication
def multi(p1,p2):
    return p1 * p2

multiplication=multi(2,3)
print(f"2 * 3 = {multiplication}") 

#inline multi
multi = lambda p1,p2: p1 * p2
print(f"4 * 5 = {multi(4,5)}")

#division
def div(s1,s2):
    return s1//s2

division=div(10,2)
print(f"10/2 = {division}") 

#inline division
div= lambda s1,s2 : s1//s2
print(f"30/15 = {div(30,15)}")


