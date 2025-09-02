# 1. Define the function
    # def name_of_function(param1, param2,...paramN):
    #     statement 1
    #     statement 2
    #     ...
    #     statement N
    
# 2. Invoke|call the function
    # name_of_function(value1,value2,...valueN)
    
def add():
    n1 = int(input('ENTER FIRST NUMBER - '))
    n2 = int(input('ENTER SECOND NUMBER - '))
    result = n1 + n2
    print(result)
    print('-------------------------')
    
def subtract(a,b):
    print(a - b)
    print('-------------------------')
    
def multiply():
    a = 70
    b = 5
    c = a * b
    return c

def divide(nr,dr):  
    return nr//dr

# add()

# n = int(input('ENTER A NUMBER - '))
# subtract(n,int(input('ENTER A NUMBER - ')))
x = multiply()
print(x)

print(divide(125,5))
print(divide(x,5))
print(divide(x,divide(25,5)))

# Function has four types:
    # 1. No parameter no return
    # 2. parameter and no return
    # 3. No parameter and return
    # 4. parameter and return both