from emptyWindow import *

window=EmptyWindow.CreateWindow("My button window", "400x300")

def msgShow():
    label["text"]="I love python"
    label["bg"]="lightyellow"
    label["fg"]="blue"

label=Label(window)
btn=Button(window, text="Message", command=msgShow)
btn_exit=Button(window, text="Exit", command=window.destroy)

label.pack()
btn.pack(side=LEFT)
btn_exit.pack(side=RIGHT)

window.mainloop()