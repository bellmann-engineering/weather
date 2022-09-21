from tkinter import *

def change_label():
    message = ""
    if auswahl.get() == option_celcius_to_fahrenheit:
        message = "C->F"
    elif auswahl.get() == option_fahrenheit_to_celcius:
        message = "F->C"
    else:
        message = "ungültig"
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

option_fahrenheit_to_celcius = "Fahrenheit -> Celcius"
option_celcius_to_fahrenheit = "Celcius -> Fahrenheit"
auswahl = StringVar(fenster)
auswahl.set(option_celcius_to_fahrenheit)
menu = OptionMenu(fenster, auswahl, option_fahrenheit_to_celcius, option_celcius_to_fahrenheit)
menu.pack()


fenster.mainloop()
