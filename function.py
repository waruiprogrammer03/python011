 # Inbuilt functions
number = max(34, 78, 90, 123, 45)
print(number)

y = min(45, 78, 34, 23)
print(y)

z = pow(2, 3)
print(z)

# User defined
def name():
    print("Me")
name() # Calling a function

def details():
    name = "Aziz"
    age = 18
    course = "MIT"
    print(name,age,course)
details()

# Parameter/variables and arguments/values
def patient(name,gender,age,marriagestatus):
    print(name,gender,age,marriagestatus)

patient("Joe","Male",43,"Single")
patient("Lucy","Female",31,"Married")

def multiply(x,y):
    print(x * y)

multiply(2,3)
multiply(29,12)
multiply(20,16)
multiply(23,23)

# Create a user-defined function
# called employees. Display details of five employees using the following parameters
# fullname,age,position,salary


