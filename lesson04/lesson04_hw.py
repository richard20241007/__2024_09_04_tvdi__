from ttkthemes import ThemedTk
from tkinter import ttk

class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('使用ttk的套件')
        style = ttk.Style(self)  
        style.configure('Main.TButton',font=('Helvetica',20))      
        topFrame = ttk.Frame(self,borderwidth=1,relief='groove')
        btn1 = ttk.Button(topFrame,text="按鈕1")
        btn1.pack(side='left')
        btn1.pack(side='left',expand=True,fill='x',padx=10)
        btn2 = ttk.Button(topFrame,text="按鈕2")
        btn2.pack(side='left')
        btn2.pack(side='left',expand=True,fill='x')
        btn3 = ttk.Button(topFrame,text="按鈕3")
        btn3.pack(side='left')
        topFrame.pack(padx=10,pady=(10,0),expand=True,fill='x')
        btn3.pack(side='left')
        topFrame.pack(padx=10,pady=(10,0),ipadx=10,ipady=10,expand=True,fill='x')
        bottomFrame = ttk.Frame(self,width=600,height=300,borderwidth=1,relief='groove')
        bottomFrame.pack(padx=10,pady=10)

        bottomFrame1 = ttk.Frame(bottomFrame,width=200,height=300,borderwidth=1,relief='groove')
        bottomFrame1.pack(side='left',expand=True,fill='x')
        bottomFrame2 = ttk.Frame(bottomFrame,width=200,height=300,borderwidth=1,relief='groove')
        bottomFrame2.pack(side='left')
        bottomFrame3 = ttk.Frame(bottomFrame,width=200,height=300,borderwidth=1,relief='groove')
        bottomFrame3.pack(side='left')

        btn4 = ttk.Button(bottomFrame1,text='Button04',style='Main.TButton')
        btn4.pack(side='top')
        btn5 = ttk.Button(bottomFrame1,text='Button04')
        btn5.pack(side='top')
        btn6 = ttk.Button(bottomFrame1,text='Button04')
        btn6.pack(side='top')


        btn7 = ttk.Button(bottomFrame2,text='Button07',style='Main.TButton')
        btn7.pack(side='top')
        btn8 = ttk.Button(bottomFrame2,text='Button08')
        btn8.pack(side='top')
        btn9 = ttk.Button(bottomFrame2,text='Button09',style='Main.TButton')
        btn9.pack(side='top')


        btn10 = ttk.Button(bottomFrame3,text='Button10',style='Main.TButton')
        btn10.pack(side='top')
        btn11 = ttk.Button(bottomFrame3,text='Button11',style='Main.TButton')
        btn11.pack(side='top')
        btn12 = ttk.Button(bottomFrame3,text='Button12',style='Main.TButton')
        btn12.pack(side='top')







def main():
    window = Window(theme='alt')
    window.mainloop()


if __name__ =='__main__':
    main()