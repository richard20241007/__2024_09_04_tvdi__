"""
self.zzz() 叫做方法
self.zzz= abc 叫做 屬性

"""





import tkinter as tk
from tkinter import ttk



class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title('Lesson 4')
        self.geometry('500x500')
        style = ttk.Style(self)
        style.configure('TLabel',font=('Helvetica',36))
        message = ttk.Label(self,text="Hello Tkinter ! ~~") #建立區域變數
        message.pack()
        print(message.winfo_class()) # 出現 TLabel 就是其中一個theme

        


        

def main():
    window = Window()
    window.mainloop()


if __name__ =='__main__':
    main()