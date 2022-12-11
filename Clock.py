from time import strftime
from tkinter import Label, Tk, CENTER

window = Tk()
window.title("Digital Clock")
window.geometry("335x80")
window.configure(bg="black")
window.resizable(False, False)

clock_label = Label(
    window,
    anchor=CENTER,
    bg="black",
    fg="cyan",
    font=("Times", 30, "bold", "italic"),
    relief="raised",
)
clock_label.place(x=20, y=20)


def update_label():
    current_time = strftime("%H:%M:%S  %b-%d-%Y")
    clock_label.configure(text=current_time)
    clock_label.after(80, update_label)


update_label()
window.mainloop()
