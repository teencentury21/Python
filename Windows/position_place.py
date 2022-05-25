from emptyWindow import *

window=EmptyWindow.CreateWindow("Place function", "200x150")

# 設定背景色
lbl_MCU=Label(window, text="銘傳大學.", bg="lightyellow", width=15) 
lbl_NCU=Label(window, text="中央大學.", bg="lightblue", width=15) 
lbl_YZU=Label(window, text="元智大學.", bg="lightgreen", width=15) 
 
lbl_NCU.place(x=0, y=0)
lbl_MCU.place(x=30, y=50)
lbl_YZU.place(x=60, y=100)


window.mainloop()