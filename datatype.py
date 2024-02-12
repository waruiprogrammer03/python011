# Data Type

numbers = 67 # int
num = 78.98 # float
greeting = "Hello there" #str
IsPythonInteresting = True #bool

# A variable storing mutiple values
languages = ["Python","PHP","Java"] #list
fruits = ("banana","apple","pineapple") #tuple
countries = {"Kenya","China","London"} #Set

#Dictionary
details = {
    "firstname":"Brian",
    "age" : 17,
    "course": "MIT",
    "nationality": "USA"
}
print(details)
print(details["course"])
print(details["nationality"])
print(numbers)
print(IsPythonInteresting)
print(countries)

# Determining the data type
print(type(details))
print(type(countries))
print((type(languages)))

# Typecasting - Converting one data type to another
print(float(numbers))
print(int(num))



