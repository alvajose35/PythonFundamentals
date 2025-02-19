from tkinter import Tk, Button

def handle_button_press(event):
    print("Button pressed!")

# Create the main window
window = Tk()
window.title("My TKinter App")

# Create a button
button = Button(window, text="Click Me")
button.pack()

# Bind the button click event
button.bind("<Button-1>", handle_button_press) 

# Start the GUI event loop
window.mainloop() 