from tkinter import *

timer = ""
text = ""


def count_down():
    global text, timer
    if text == t.get(1.0, END):
        if timer == 5:
            t.delete("1.0", "end")
            timer = 0
        window.after(1000, count_down)
        timer += 1
    else:
        window.after(1000, count_down)
        text = t.get(1.0, END)
        timer = 0


window = Tk()
window.title("Disappearing Text")
window.geometry("500x200")

t = Text(window, height=15, width=70)
t.grid(column=0, row=0)


window.after(1000, count_down)
window.mainloop()