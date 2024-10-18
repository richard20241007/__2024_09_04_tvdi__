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
        style.configure('TLabel',font=('Helvetica',36))  #修改現有的
        style.configure('Title.TLabel',font=('Helvetica',20)) #自訂的style
        message = ttk.Label(self,text="Hello Tkinter ! ~~") #建立區域變數
        message.pack()
        message2 = ttk.Label(self,text="使用自訂style",style='Title.TLabel') #使用自訂style
        message2.pack()
        print(message.winfo_class()) # 出現 TLabel 就是其中一個theme

        


        

def main():
    window = Window()
    window.mainloop()


if __name__ =='__main__':
    main()