#file handling
def write_file():
    #open the file
    file=open('myfile.txt', 'w') #w mode=overwrite the file
    
    #perform the operation on file
    file.write("you are my sunshine.")
    
    #close the file
    file.close()
    
write_file()

def append_file():
    #open the file
    file=open('myfile.txt', 'a')
    
    file.write("my only sunshine.")
    
    file.close()
    
append_file() 

def read_file():
    file=open('myfile.txt', 'r')
    
    data=file.read()
    print(f"data={data}")
    
    file.close()
    
read_file()           