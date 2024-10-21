from ttkthemes import ThemedTk
import tkinter as tk
from tkinter import ttk


class Window(ThemedTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.title('表單')
        #==========style============
        style = ttk.Style(self)
        style.configure('lb.TLabel',font=("Helvetica",25))
        #==========style============

        #===start of topframe=====
        topframe = ttk.Frame(self)
        lb1 = ttk.Label(self,text="個人資料",style='lb.TLabel')
        lb1.pack(pady=20)
        topframe.pack(padx=20,pady=10)
        #===end of topframe=======

        #===start of bottomframe=====
        bottomframe = ttk.Frame(self)
        
        lb_name = ttk.Label(bottomframe,text="姓名: ")
        lb_name.grid(row=0,column=0,pady=5,padx=5)
        self.name = tk.StringVar()
        ent_name = ttk.Entry(bottomframe,textvariable=self.name)
        ent_name.grid(row=0,column=1,pady=5,padx=5)
        

        lb_sex = ttk.Label(bottomframe,text='性別: ')
        lb_sex.grid(row=1,column=0,pady=5,padx=5)
        self.sex = tk.StringVar()
        ent_sex = ttk.Entry(bottomframe,textvariable=self.sex)
        ent_sex.grid(row=1,column=1,pady=5,padx=5)

        lb_age = ttk.Label(bottomframe,text='年齡: ')
        lb_age.grid(row=2,column=0,pady=5,padx=5)
        self.age = tk.StringVar()
        ent_age = ttk.Entry(bottomframe,textvariable=self.age)
        ent_age.grid(row=2,column=1,pady=5,padx=5)

        lb_note = ttk.Label(bottomframe,text='說明: ')
        lb_note.grid(row=3,column=0,pady=5,padx=5)
        self.note = tk.StringVar()
        ent_note = ttk.Entry(bottomframe,textvariable=self.note)
        ent_note.grid(row=3,column=1,rowspan=2,pady=5,padx=5)
        bottomframe.columnconfigure(index=0,weight=1)
        bottomframe.columnconfigure(index=1,weight=3)
        bottomframe.rowconfigure(index=3,weight=1)
        bottomframe.rowconfigure(index=4,weight=1)

        btn_cancel = ttk.Button(bottomframe,text='Submit')
        btn_cancel.grid(row=5,column=0,pady=(5,10),padx=15)

        btn_submit = ttk.Button(bottomframe,text='Submit')
        btn_submit.grid(row=5,column=1,pady=(5,10),padx=5,sticky='e')

        

        bottomframe.pack(expand=True,fill='x',padx=20,pady=(0,20),ipadx=10,ipady=10)

        #===end of bottomeframe=======


        
        


def main():
    window = Window(theme='scidpurple')
    window.name.set('姓名')
    window.sex.set('性別')
    window.age.set('年齡')
    window.age.set('備註')
    window.mainloop()

if __name__=='__main__':
    main()





"""
bottomframe.columnconfigure(index=0,weight=1)
bottomframe.columnconfigure(index=1,weight=3)
表示在bottomframe的框架裡面
column 0 權重佔1等分
column 1 權重佔3等分
(總共4等分)

"""