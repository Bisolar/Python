import tkinter as tk

root = tk.Tk()
root.title("My App")
label = tk.Label(root, text= "My first python app")
label.pack()
button = tk.Button(root, text= "Click me")
input = tk.Entry()
input.pack() 

button.pack()
root.mainloop() 