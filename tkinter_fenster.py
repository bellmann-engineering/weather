from tkinter import *

def write_slogan():
    message = "Hallo Wolfsburg!"
    label.configure(text=message)

frame = Tk()
frame.title("Test")

label = Label(frame, 
            justify = LEFT, 
            font=("Helvetica", 16), 
            text="")
label.pack()

button = Button(frame, 
          text="QUIT", fg="red",
          command=frame.quit)
button.pack(side=LEFT)

slogan = Button(frame,
          text="Hello",
          command=write_slogan)
slogan.pack(side=LEFT)

frame.mainloop()
