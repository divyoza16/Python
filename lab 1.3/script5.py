# To print their id and checks if they are the same.  
# Modifies one of the variables and checks the id again.  
a = 10
b = 10 
print(f"Id1 = {id(a)}") 
print(f"Id2 = {id(b)}") 
print(f"Check Id1 == Id2 is {id(a)==id(b)}") 
c = 12
print(f"New value of Id1 = {id(c)}")  
print(f"Id2 = {id(b)}") 
print(f"Check Id1 == Id2 is {id(c)==id(b)}") 