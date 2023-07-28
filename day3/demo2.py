#function
#defining function (empty func)

def function1():
    pass

#parameterless func

def function2():
    print("this is the func body")

#func call
function2()

#parametrized func

def function3(param):
    print(f"(param) = {param}, type={type(param)}")

function3(10) #int
function3(10.2) #float
function3("jane") #str

#docstring

def function4(n1,n2):
    """
     this function will add two parameters
    :param p1: integer first argument
    :param p2: integer second parameter
    :return: nothing

    """
    add=(n1+n2)
    print(f"{n1} + {n2} = {add}")

print(function4.__doc__)
function4(10,20)

#return statement

def multiply(p1,p2):
    """
     multiply two parameters
    :param p1: int
    :param p2: int
    :return: multiplication of two parameters

    """
    multi = (p1 * p2)
    return(multi)

print(multiply.__doc__)
answer=multiply(30,2)
print(f"(answer) = {answer}")    


