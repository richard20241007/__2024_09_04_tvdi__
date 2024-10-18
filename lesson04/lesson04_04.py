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
        #label
        # style.configure('TLabel',font=('Helvetica',36))  #修改現有的
        # style.configure('Title.TLabel',font=('Helvetica',20),background="yellow",foreground='blue') #自訂的style
        # message = ttk.Label(self,text="Hello Tkinter ! ~~") #建立區域變數
        # message.pack()
        # message2 = ttk.Label(self,text="使用自訂style",style='Title.TLabel') #使用自訂style
        # message2.pack()
        # print(message.winfo_class()) # 出現 TLabel 就是其中一個theme
        
        #button
        style.configure('TButton',font=('Helvetica',15))
        def click_me():
            pass
        my_btn = ttk.Button(self,text='Click me ~ ',command=click_me)
        my_btn.pack()

        style.configure('Main.TButton',font=('Helvetica',30),foreground='purple')
        my_btn1 = ttk.Button(self,text='Click me ~ ',command=click_me,style='Main.TButton')
        my_btn1.pack(padx=10,pady=10, ipadx=20,ipady=20)
        """
        padx pady 等於 margin 概念
        ipadx ipady 等於padding 概念

        """
        


        

def main():
    window = Window()
    window.mainloop()


if __name__ =='__main__':
    main()