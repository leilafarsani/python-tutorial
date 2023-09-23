print("Hello World")
print("*" * 3)
students_count = 30
rating = 4.99
is_published = True
course_name = "Python Programming"
message = """

Hi people, 
My name is Leila,

blah blah blah 

"""

print(message)
print(len(message))
print(len(course_name))

print(message[1])
print(course_name[0])
print(course_name[-1])
print(course_name[11])

print(course_name[0:3])
print(course_name[0:])
print(course_name[:3])
print(course_name[:])

# scape sequences
# \"
# \'
# \\
# \n

course = "Python Programming  \n for \"beginners\""
print(course)

first_name = "Leila"
last_name = "Farsani"
full_name = first_name + " " + last_name
print(full_name)

# Formatted Strings
full = f"{first_name} {last_name}"
username = F"{first_name}{len(last_name)+3}"
print(full)
print(username)

# Strings Methods
print(course_name.upper())
print(course_name)
print(course_name.lower())
print(course_name.islower())
print(message.strip())
print(len(message.strip()))
print(message.find("leila"))
print(message.find("Leila"))
print(course.find("P"))
print(course.find("Pr"))
print(course.replace("P", "J"))
