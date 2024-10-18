from ttkthemes import ThemedTk
from tkinter import ttk



class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('Lesson 4')
        style = ttk.Style(self)
        topFrame = ttk.Frame(self,borderwidth=1,relief='groove')
        topFrame.pack(padx=10,pady=10,ipadx=10,ipady=10,fill='x',expand=True)
        bottomFrame= ttk.Frame(self,width=500,height=300,relief='sunken')
        bottomFrame.pack(padx=10,pady=10,ipadx=10,ipady=10)
        my_btn1 = ttk.Button(topFrame,text='Click me1')
        my_btn1.pack(side='left',expand=True,)
        
        #frame 有放東西 就沒有寬高，是依照內容物決定寬高
        my_btn2 = ttk.Button(topFrame,text='Click me2')
        my_btn2.pack(side='right',expand=True,fill='x',padx=10)
        my_btn3 = ttk.Button(topFrame,text='Click me3')
        my_btn3.pack()

        

def main():
    window = Window(theme='alt')
    window.mainloop()


if __name__ =='__main__':
    main()