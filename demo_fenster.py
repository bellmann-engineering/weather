from tkinter import *

def change_label():
    message = "Tschüss"
    hidden_label.configure(text=message)

fenster = Tk()

fenster.geometry("300x300")
fenster.title("Testfenster")

hidden_label = Label(fenster, text="")
hidden_label.pack()

hello_label = Label(fenster, text="Hallo", font=("Arial", 22))
hello_label.pack()

click_button = Button(fenster, text="Klick mich", command=change_label)
click_button.pack()

close_button = Button(fenster, text="Close", command=fenster.quit, fg="red")
close_button.pack(side=LEFT)


fenster.mainloop()
