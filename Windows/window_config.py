from emptyWindow import *

window=EmptyWindow.CreateWindow("My window config", "400x300")

def change_window_bg(bgColor):
    window.config(bg=bgColor)
def get_color():
    color=txb_color.get()    
    change_window_bg(color)

lbl_msg=Label(window, text="please input color").grid(row=0)
txb_color=Entry(window)
txb_color.grid(row=0, column=1)

btn_exit=Button(window, text="Exit", command=window.destroy)
btn_change=Button(window, text="Change background color", command=get_color)
#btn_green=Button(window, text="To green", command=lambda:change_window_bg("lightgreen"))

btn_exit.grid(row=1, column=0)
btn_change.grid(row=1, column=1)
#btn_green.grid(row=1, column=2)

window.mainloop()