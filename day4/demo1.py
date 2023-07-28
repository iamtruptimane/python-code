def func1():
    print("inside the func1")


func1()

def func2(p1,p2):
    print(f"p1={p1}, type={type(func2)}")
    print(f"p2={p2}, type={type(func2)}")

func2(10,20)
func2(p1=10,p2=20)
func2(p2=20,p1=10)
func2(10,p2=20)

num=100
print(f"num={num}, type={type(num)}")

num=300
print(f"num={num}, type={type(num)}")

print(f"func1={func1}, type={type(func1)}")
print(f"func2={func2}, type={type(func2)}")
