#decorator
def log(function):
    
    def inner(*args, **kwargs):
        
        #open the log file in append mode
        file=open('demo4.log', 'a')
        
        #write the logs
        file.write("*" * 40)
        file.write("\n")
        file.write(f"inside inner")
        file.write("\n")
        file.write(f"function name={function.__name__}")
        file.write("\n")
        file.write(f"args={args}")
        file.write("\n")
        file.write(f"kwargs={kwargs}")
        file.write("\n")
        file.write("*" * 40)
        
        #close the file
        file.close()
        
        function(*args, **kwargs)
        
    return inner
@log
def mul(p1,p2):
    print(f"multiplication={p1} * {p2}={p1 * p2}")

mul(23,34)

@log
def add(s1,s2):
    print(f"addition={s1} +{s2}={s1+s2}")
    
add(45,78)            
        