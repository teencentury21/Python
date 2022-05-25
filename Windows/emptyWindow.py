from queue import Empty
from tkinter import *

class EmptyWindow():
    @staticmethod
    def CreateWindow(title, size):
        # init
        window=Tk()
        # 視窗標題
        window.title(title)
        # 視窗寬高
        window.geometry(size)
        return window
