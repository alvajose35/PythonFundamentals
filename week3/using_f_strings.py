# Usage of f-strings
name = "Alice"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)

# Using expressions inside f-strings
number = 5
square = f"The square of {number} is {number ** 2}."
print(square)

# Combining f-strings with string methods
my_string = "hello world"
formatted_string = f"{my_string.upper()} has {len(my_string)} characters."
print(formatted_string)

# Formatting numbers with f-strings
pi = 3.14159265359
formatted_pi = f"Pi to three decimal places is {pi:.3f}"
print(formatted_pi)

# Combining f-strings with multiline strings
multiline_fstring = f"""
Name: {name}
Age: {age}
Greeting: {greeting}
"""
print(multiline_fstring)