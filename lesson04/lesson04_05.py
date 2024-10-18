from ttkthemes import ThemedTk
from tkinter import ttk



class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
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

        style.configure('Main.TButton',font=('Helvetica',15),foreground='purple')
        my_btn1 = ttk.Button(self,text='Click me ~ ',command=click_me,style='Main.TButton')
        my_btn1.pack(pady=10)
        


        

def main():
    window = Window(theme='radiance')
    window.mainloop()


if __name__ =='__main__':
    main()