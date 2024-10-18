import tkinter as tk
"""
class Window(tk.Tk):
    def __init__(screenName=None, baseName=None, className='Tk',useTk=True, sync=False, use=None):
        super().__init__(
            screenName=screenName,
            baseName=baseName,
            className=className,
            useTk=useTk,
            sync=sync,
            use=use)  #執行父類別的init 不用放self

      選取TK 按右鍵 移至定義 可以查詢TK 這個class 的原始碼
      那TK 有很多引數全寫很麻煩因此
      多個引數名稱 可以改成 **kwargs 如下
      **kwargs 不限數量 (包含0個)      
"""       
class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)  #執行父類別的init 不用放self



def main():
    root = Window()
    print(type(root))       #type 為 window
    root.title("Lesson04")
    root.geometry("500x500+25+25")

    lb1 = tk.Label(root,text='Account')
    lb1.pack()

    text = tk.StringVar()
    ent1 = tk.Entry(root,textvariable=text,bg='yellow')
    ent1.pack(fill='x',expand=True)

    def click():
        pass
    btn1 = tk.Button(root,text='Click me',command=click)
    btn1.pack()
    root.mainloop()     #有個Tk實體方法叫做 mainloop()


if __name__ =='__main__':
    main()