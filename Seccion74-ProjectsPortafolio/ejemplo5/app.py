from tkinter import *



window = Tk()
window.config(padx=200, pady=200)
i = 3
def to_do():
    global i
    i += 1
    text = input.get()
    input.delete(0, END)


    butt = Checkbutton(text=text)
    butt.grid(row=i, column=1)







label = Label(text="Enter your task here")
label.grid(row=1, column=1)
input = Entry()
input.grid(row =2, column=1)
for i in range(100):
    button = Button(text="save", command=to_do)
    button.grid(row=3, column=1)



window.mainloop()