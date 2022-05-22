import emptyWindow
from tkinter import *

window=emptyWindow.CreateWindow("Peak function","400x200")

# 設定背景色
lbl_MCU=Label(window, text="銘傳大學.", bg="lightyellow", width=15) 
lbl_NCU=Label(window, text="中央大學.", bg="lightblue", width=15) 
lbl_CYCU=Label(window, text="中原大學.", bg="lightgray", width=15) 
lbl_YZU=Label(window, text="元智大學.", bg="lightgreen", width=15) 

# lbl_NCU.pack()
# lbl_MCU.pack()
# lbl_CYCU.pack()
# lbl_YZU.pack()
 
# padx -> 左右間隔 pady -> 上下間隔
# 順序 FIFO
lbl_NCU.pack(side=TOP)
lbl_CYCU.pack(side=BOTTOM)
lbl_MCU.pack(side=BOTTOM, pady=5)
lbl_YZU.pack(side=BOTTOM)

lbl_L=Label(window, text="左.", bg="lightyellow", width=15) 
lbl_M=Label(window, text="中.", bg="lightblue", width=15) 
lbl_R=Label(window, text="右.", bg="lightgray", width=15) 

lbl_L.pack(side=LEFT)
lbl_M.pack(side=LEFT, padx=5)
lbl_R.pack(side=LEFT)


window.mainloop()