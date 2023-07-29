def func1():
    
    num=[1,2,3,4,5,6,7,8]
    
    #find out even num
    even_num=lambda x : x %2 == 0
    #square of even num
    square=lambda x : x ** 2
    num1=list(filter(even_num,num))
    num2=list(map(square,num1))
    
    print(num)
    print(num1)
    print(num2)
#func1()

def func2():
    num=[1,2,3,4,5,6,7,8]
    
    #find out odd num
    odd_num=lambda x : x %2 !=0
    #cube of odd num
    cube_num=lambda x : x ** 3
    
    num1=list(filter(odd_num,num))
    num2=list(map(cube_num,num1))
    
    print(num)
    print(num1)
    print(num2)
#func2()    
    
        