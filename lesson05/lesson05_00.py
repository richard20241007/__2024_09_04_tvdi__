from ttkthemes import ThemedTk
from tkinter import ttk

class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('Lesson 4 ')
        style = ttk.Style(self)
        style.configure('button.TButton',font=('Helvetica',30))
        self.show_lb = ttk.Label(self,text="")
        self.show_lb.pack()
        #=============Start of topframe===================
        topFrame = ttk.Frame(self,borderwidth=1,relief="groove")
        
        btn1 = ttk.Button(topFrame,text='botton 01',command=self.click1)
        btn1.pack(side='left',expand=True,fill='x',padx=10)
        btn2 = ttk.Button(topFrame,text='botton 02',command=self.click2)
        btn2.pack(side='left',expand=True,fill='x',padx=10)
        btn3 = ttk.Button(topFrame,text='botton 03',command=self.click3)
        btn3.pack(side='left',expand=True,fill='x',padx=10)
        topFrame.pack(padx=10,pady=(10,0),ipadx=10,ipady=10,expand=True,fill='x')
        #=============end of topframe===================

        #=============start of bottomeframe=============
        bottomFrame = ttk.Frame(self,borderwidth=1,relief="groove",width=500,height=300)
        
        #==========start of bottmeframe1 ==================
        bottomFrame1 = ttk.Frame(bottomFrame,borderwidth=1,relief="groove",width=500,height=300)
        btn4 = ttk.Button(bottomFrame1,text='botton 04',style='button.TButton')
        btn4.bind('<Motion>',self.click456)
        btn4.pack(side='top',expand=True,fill='x',padx=10)

        btn5 = ttk.Button(bottomFrame1,text='botton 05')
        btn5.bind('<Enter>',self.click456)
        btn5.pack(side='top',expand=True,fill='x',padx=10,pady=15)

        btn6 = ttk.Button(bottomFrame1,text='botton 06')
        btn6.bind('<ButtonRelease>',self.click456)
        btn6.pack(side='top',expand=True,fill='x',padx=10,pady=15)
        bottomFrame1.pack(padx=10,pady=10,ipadx=10,ipady=10,expand=True,fill='x',side='left')
        #<Motion> 跟 <Enter> 差異是 Motion 一直動 就會一直執行 ，Enter 只會執行一次

         #========== end of bottmeframe1 ==================


         #==========start of bottmeframe2 ==================
        bottomFrame2 = ttk.Frame(bottomFrame,borderwidth=1,relief="groove",width=500,height=300)

        btn7 = ttk.Button(bottomFrame2,text='botton 07',style='button.TButton')
        btn7.pack(side='top',expand=True,fill='x',padx=10)
        btn8 = ttk.Button(bottomFrame2,text='botton 08')
        btn8.pack(side='top',expand=True,fill='x',padx=10,pady=15)
        btn9 = ttk.Button(bottomFrame2,text='botton 09',style='button.TButton')
        btn9.pack(side='top',expand=True,fill='x',padx=10)
        bottomFrame2.pack(padx=10,pady=10,ipadx=10,ipady=10,expand=True,fill='x',side='left')
        #========== end of bottmeframe2 ==================


        #==========start of bottmeframe3 ==================
        bottomFrame3 = ttk.Frame(bottomFrame,borderwidth=1,relief="groove",width=500,height=300)
        btn10 = ttk.Button(bottomFrame3,text='botton 10',style='button.TButton')
        btn10.pack(side='top',expand=True,fill='x',padx=10)
        btn11 = ttk.Button(bottomFrame3,text='botton 11',style='button.TButton')
        btn11.pack(side='top',expand=True,fill='x',padx=10)
        btn12 = ttk.Button(bottomFrame3,text='botton 12',style='button.TButton')
        btn12.pack(side='top',expand=True,fill='x',padx=10)
        bottomFrame3.pack(padx=10,pady=10,ipadx=10,ipady=10,expand=True,fill='x',side='left')
        #========== end of bottmeframe3 ==================

        bottomFrame.pack(padx=10,pady=10,ipadx=10,ipady=10,expand=True,fill='x')
        
        #=============enf of bottomeframe=============

    def click1(self):
        self.show_lb.config(text='You click btn1 !')
    def click2(self):
        self.show_lb.config(text='You click btn2 !')
    def click3(self):
        self.show_lb.config(text='You click btn3 !')
    def click456(self,event):
        self.show_lb.config(text='You click btn4 !')
        print(event)
        print(type(event))
        print(event.x)
        print(event.y)
        print(event.width)
        print(event.widget)   #widget 就是告訴你 這個button 在哪，也等於 這個btn
        print(event.widget.configure(text =' Wrong !')) #既然是這個btn 表示可以修改
        #event 表示按我的按鈕
        #本案例指 btn4 btn5 btn6 
        #然後 這按鈕回傳到 widget 裡面
        #因此 這種event 的寫法 並不需要寫 self 


def main():
    window=Window(theme='scidpurple')
    window.mainloop()

if __name__=='__main__':
    main()


    """
    放在文件的是全域變數  (任何地方都可以存取)
    放在funciton 裡面的變數稱為區域變數，就是專門給function使用的
    
    在實體裡面只有
    attribute, property 以及 method
    並沒有function

    文件裡面的才叫做function (屬於全域的 任何地方都可以呼叫)
    放在class 裡面的叫做 method

    儘管開頭都是 def  但還是有區別
    使用英文來區分比較不會搞混

    

    在class 裡面的實體方法 都要一個self
    attribute 整個 class 都可以使用
    self.topframe (有self. 開頭的 就是attribute ，整個class都可以用)


    放在class 底下 有一個
    def abc(self):
            pass
    這個abc 叫做 實體方法(method)
    裡面都要有一個self
    

    在類別（class）裡，使用 self.show_lb 是為了讓 show_lb 成為類別的實例屬性，這樣它在類別的其他方法中都能被存取和修改。如果只寫 show_lb，那麼變數的作用範圍（scope）將只限於 __init__ 方法內，無法在其他方法中使用。

    詳細說明：
    self.show_lb：這是實例屬性。當使用 self.show_lb 時，它會將 show_lb 變數與這個類的實例關聯起來，並能在這個實例的所有方法中被訪問和修改。

    show_lb（不加 self）：如果不使用 self，這個變數就只是 __init__ 方法內的區域變數。一旦方法執行完畢，這個變數就會被銷毀，無法在其他方法中使用。


    btn1 = ttk.Button(topFrame,text='botton 01',command=self.click1)
    在command 裡面 的 這個方法 最後沒有括號
    self.click1() 如果這樣寫 表示馬上執行 而不是binding
    binding 是按下去才會執行

    """