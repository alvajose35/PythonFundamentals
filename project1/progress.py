import time

'''for i in range(10):
    print(f"Progress: {i*10}%", end='\r') 
    time.sleep(0.5) 

print("Progress: 100%")  # Print a final message on a new line
'''
'''import os

def clear_line():
    print("\033[2K\033[G", end="")  # ANSI escape sequences for clearing line and moving to beginning

print("Line 1")
print("Line 2")
print("Line 3")
time.sleep(3) 


clear_line()  # Attempt to clear the last line
print("New Line 1") 
'''
import os

def clear_console():
  """Clears the console screen."""
  if os.name == 'nt':
    os.system('cls')  # For Windows
  else:
    os.system('clear')  # For macOS and Linux

# Example usage:
print("Line 1")
print("Line 2")
print("Line 3")
time.sleep(3) 

clear_console()
print("This line will be printed on a cleared screen.")
print("\033[31mHello, World!\033[0m")
print("\033[32mHello, World!\033[0m")
print("\033[42mHello, World!\033[0m")
input()