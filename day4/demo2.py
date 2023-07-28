num=50
print(f"num={num}, type={type(num)}")

num2=num
print(f"num2={num2}, type={type(num2)}")

num=200
print(f"num={num}, type={type(num)}")
print(f"num2={num2}, type={type(num2)}")

num=300
print(f"num={num}, type={type(num)}")
print(f"num2={num2}, type={type(num2)}")

def func1():
    print("inside func1")

func1()

#func aliase
myFunc=func1
print(f"muFunc={myFunc}, type={type(myFunc)}")
print(f"func1={func1}, type={type(func1)}")

func1()
myFunc()
