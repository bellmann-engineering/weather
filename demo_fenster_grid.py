from tkinter import *

def change_label():
    message = "Tschüss"
    hidden_label.configure(text=message)

fenster = Tk()

fenster.geometry("300x300")
fenster.title("Testfenster")

# Use grid instead of pack
hello_label = Label(fenster, text="Hallo", font=("Arial", 22))
hello_label.grid(row=0, column=0, columnspan=2, pady=10)

hidden_label = Label(fenster, text="")
hidden_label.grid(row=1, column=0, columnspan=2, pady=10)

click_button = Button(fenster, text="Klick mich", command=change_label)
click_button.grid(row=2, column=0, padx=10, pady=10)

close_button = Button(fenster, text="Close", command=fenster.quit, fg="red")
close_button.grid(row=2, column=1, padx=10, pady=10)

fenster.mainloop()
