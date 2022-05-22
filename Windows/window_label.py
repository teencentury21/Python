import emptyWindow
from tkinter import *

window=emptyWindow.CreateWindow("My Label window","400x300")
label=Label(window, text="I Like tkinter.")
# 包裝與定位元件
label.pack()

# 設定背景色
lbl_backgrund=Label(window, text="I Like tkinter.",
                            bg="#00FF00", 
                            width=15,
                            font="Helvetica 16 bold italic") 
#RRGGBB
#font(字體 fontsize 粗體 斜體)
lbl_backgrund.pack()

window.mainloop()