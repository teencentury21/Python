import emptyWindow
from tkinter import *

window=emptyWindow.CreateWindow("Grid function","400x200")

# 設定背景色
lbl_MCU=Label(window, text="銘傳大學.", bg="lightyellow", width=15) 
lbl_NCU=Label(window, text="中央大學.", bg="lightblue", width=15) 
lbl_YZU=Label(window, text="元智大學.", bg="lightgreen", width=15) 
 
lbl_NCU.grid(row=0, column=0)
lbl_MCU.grid(row=1, column=2)
lbl_YZU.grid(row=2, column=1)

# columnspan, rowspan
# 版面會因為上面而跑掉
lbl_1=Label(window, text="標籤1.", relief="raised") 
lbl_2=Label(window, text="標籤2.", relief="raised") 
lbl_4=Label(window, text="標籤4.", relief="raised") 
lbl_5=Label(window, text="標籤5.", relief="raised") 
lbl_6=Label(window, text="標籤6.", relief="raised") 
lbl_7=Label(window, text="標籤7.", relief="raised") 

lbl_1.grid(row=4, column=0)
lbl_2.grid(row=4, column=1, columnspan=2)
lbl_4.grid(row=4, column=3, rowspan=2)
lbl_5.grid(row=5, column=0)
lbl_6.grid(row=5, column=1)
lbl_7.grid(row=5, column=2)

window.mainloop()