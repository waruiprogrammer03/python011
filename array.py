courses = ["MIT","Cybersecurity","Datascience"]

print(courses)

# Accesing an element in an array
print(courses[2])

# Looping through an Array
for course in courses:
    print(course)

# Adding a new elements in an array
courses.append("Android programming")
print(courses)

# Deleting an element from an array
courses.remove("Datascience")
print(courses)
