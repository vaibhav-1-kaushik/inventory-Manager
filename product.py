from tkinter import *
from tkinter import ttk,font,messagebox
import pymysql


pr = Tk()
pr.title("products_databse")
pr.state("zoomed")

fnt = font.Font(family="Poppins",size=16,weight="bold")
_fnt = font.Font(family="Poppins",size=11)
sty =ttk.Style()
sty.configure("TButton",font=("Poppins",10))

b=[]

def Details(term) :
          # print(len(b))
          # print(b)
          db = pymysql.connect(host="localhost",user="root",password="Vaibhav123@",database="inventries")
          sql = "select * from product where p_id = %s"
          value = [t.get()]
          cur = db.cursor()
          def destroyer() :
                      for f in b :
                                 f[0].destroy()


          if  cur.execute(sql,value) :
                    destroyer()
                    for f in cur.fetchall() :
                              t.delete(0,END)
                              u.delete(0,END)
                              v.delete(0,END)
                              w.delete(0,END)

                              t.insert(0,f[0])
                              u.insert(0,f[1])
                              v.insert(0,f[2])
                              w.insert(0,f[3])
                    if term=="update" :
                           if x.get()!="":
                                value = f[3] - int(x.get())
                                value=[value,f[0]]
                                sql ="update product set qty = %s where p_id = %s"
                                cur = db.cursor()
                                cur.execute(sql,value)
                                db.commit()
                                der=ttk.Label(text=f"{int(x.get())*f[2]}", font=_fnt)
                                der.place(x=600, y=330, width=150, height=30)
                                c =[der]
                                b.append(c)
                                t.delete(0, END)
                                u.delete(0, END)
                                v.delete(0, END)
                                w.delete(0, END)
                                x.delete(0, END)
                                messagebox.showinfo(title="Success",message="updated and saved successfuly")
                           else:
                               messagebox.showinfo(title="Empty",message="getting empty selling field ..fill some thing")
          else:
              t.delete(0, END)
              u.delete(0, END)
              v.delete(0, END)
              w.delete(0, END)
              messagebox.showinfo(title="information",message="Data not available for the enterd product id plzz check the id twice and re_enter")


ttk.Label(text="product's database interaction",font=fnt).place(x=500,y=100,width=350,height=40)

ttk.Label(text="Product_id",font=_fnt).place(x=470,y=170,width=100,height=30)
ttk.Label(text=":",font=_fnt).place(x=580,y=170,width=10,height=30)
t=ttk.Entry(font=_fnt)
t.place(x=600,y=170,width=150,height=30)

ttk.Label(text="Product_name",font=_fnt).place(x=470,y=202,width=100,height=30)
ttk.Label(text=":",font=_fnt).place(x=580,y=202,width=10,height=30)
u=ttk.Entry(font=_fnt)
u.place(x=600,y=202,width=150,height=30)

ttk.Label(text="Amount",font=_fnt).place(x=470,y=234,width=100,height=30)
ttk.Label(text=":",font=_fnt).place(x=580,y=234,width=10,height=30)
v=ttk.Entry(font=_fnt)
v.place(x=600,y=234,width=150,height=30)

ttk.Label(text="Quantity",font=_fnt).place(x=470,y=266,width=100,height=30)
ttk.Label(text=":",font=_fnt).place(x=580,y=266,width=10,height=30)
w=ttk.Entry(font=_fnt)
w.place(x=600,y=266,width=150,height=30)

ttk.Label(text="Selling",font=_fnt).place(x=470,y=298,width=100,height=30)
ttk.Label(text=":",font=_fnt).place(x=580,y=298,width=10,height=30)
x=ttk.Entry(font=_fnt)
x.place(x=600,y=298,width=150,height=30)

ttk.Label(text="Total Amount",font=_fnt).place(x=470,y=330,width=100,height=30)
ttk.Label(text=":",font=_fnt).place(x=580,y=330,width=10,height=30)



ttk.Button(text="Details",command=lambda:Details("Details")).place(x=755,y=170,width=150,height=30)
ttk.Button(text="Sell Now",command=lambda :Details("update")).place(x=550,y=370,width=150,height=30)


pr.mainloop()