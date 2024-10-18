from ttkthemes import ThemedTk
from tkinter import ttk



class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title('Lesson 4')
        style = ttk.Style(self)
        topFrame = ttk.Frame(self,borderwidth=1,relief='groove')
        topFrame.pack(padx=10,pady=10,fill='x')
        bottomFrame= ttk.Frame(self,width=500,height=300,relief='sunken')
        bottomFrame.pack(padx=10,pady=10,ipadx=10,ipady=10)
        my_btn1 = ttk.Button(topFrame,text='Click me')
        my_btn1.pack()
        
        #frame 有放東西 就沒有寬高，是依照內容物決定寬高
        my_btn2 = ttk.Button(topFrame,text='Click me')
        my_btn2.pack(side='right')
        my_btn3 = ttk.Button(topFrame,text='Click me')
        my_btn3.pack(side='left')

        

def main():
    window = Window(theme='radiance')
    window.mainloop()


if __name__ =='__main__':
    main()