import tkinter as tk
root = tk.Tk()   #他是一個Tk的實體
# print(type(root))

def main():
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