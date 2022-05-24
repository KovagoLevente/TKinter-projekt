from tkinter import *
from PIL import Image,ImageTk
import math

# nevjegy
def nevjegy():
    abl2=Toplevel(foablak)
    uz2=Message(abl2,text='készitete:\nKővágó Levente\nUtasi Balázs\nAuer Zoltán', )
    gomb2=Button(abl2, text='Kilépés' , command=abl2.destroy)
    uz2.pack()
    gomb2.pack()
    abl2.mainloop()
def h_terulet():
    k='' 
    def szam():
        if not k :
            mezo4.delete(0, END)
            mezo4.insert(0, str()+'szamadatot kell megadni')
        a=float(mezo1.get())
        b=float(mezo2.get())
        c=float(mezo3.get())
        terulet=(a*b)/2
        if a<=0 or b<=0 or c<=0:
            mezo4.delete(0, END)
            mezo4. insert(0, str()+' 0 nem lehet ')
        else:
            mezo4.delete(0, END)
            mezo4. insert(0, str(terulet))
    abl3= Toplevel(foablak)
    abl3.title('Terület')
    szoveg1=Label(abl3, text='a oldal (cm):')
    szoveg2=Label(abl3, text='b oldal (cm):')
    szoveg3=Label(abl3, text='c oldal (cm):')
    szoveg4=Label(abl3, text='Eredmény:')
    gomb1=Button(abl3, text='Szamitás', command=szam)
    mezo1= Entry(abl3)
    mezo2= Entry(abl3)
    mezo3= Entry(abl3)
    mezo4= Entry(abl3)
    szoveg1.grid(row=1)
    szoveg2.grid(row=2)
    szoveg3.grid(row=3)
    szoveg4.grid(row=5)
    gomb1.grid(row=4 ,column= 2)
    mezo1.grid(row=1 ,column= 2)
    mezo2.grid(row=2 ,column= 2)
    mezo3.grid(row=3 ,column= 2)
    mezo4.grid(row=5 ,column= 2)
    gomb2=Button(abl3, text='Kilépés' , command=abl3.destroy)
    gomb2.grid(row=6 ,column= 2)
    abl3.mainloop()
def h_kerulet():
    k='' 
    def szam():
        if not k :
            mezo4.delete(0, END)
            mezo4.insert(0, str()+'Számadatot kell megadni')
        a=float(mezo1.get())
        b=float(mezo2.get())
        c=float(mezo3.get())
        kerület= a+b+c
        if a<=0 or b<=0 or c<=0:
            mezo4.delete(0, END)
            mezo4. insert(0, str()+' 0 nem lehet ')
        else:
            mezo4.delete(0, END)
            mezo4. insert(0, str(kerület))
    abl4= Toplevel(foablak)
    abl4.title('Kerület')
    szoveg1=Label(abl4, text='a oldal (cm):')
    szoveg2=Label(abl4, text='b oldal (cm):')
    szoveg3=Label(abl4, text='c oldal (cm):')
    szoveg4=Label(abl4, text='Eredmény:')
    gomb1=Button(abl4, text='Szamitás', command=szam)
    mezo1= Entry(abl4)
    mezo2= Entry(abl4)
    mezo3= Entry(abl4)
    mezo4= Entry(abl4)
    szoveg1.grid(row=1)
    szoveg2.grid(row=2)
    szoveg3.grid(row=3)
    szoveg4.grid(row=5)
    gomb1.grid(row=4 ,column= 2)
    mezo1.grid(row=1 ,column= 2)
    mezo2.grid(row=2 ,column= 2)
    mezo3.grid(row=3 ,column= 2)
    mezo4.grid(row=5 ,column= 2)
    gomb2=Button(abl4, text='Kilépés' , command=abl4.destroy)
    gomb2.grid(row=6 ,column= 2)
    abl4.mainloop()
def teglalap_kerulet():
    k=''
    def szam():
        if not k :
            mezo4.delete(0, END)
            mezo4.insert(0, str()+'Számadatot kell megadni')
        a=float(mezo1.get())
        b=float(mezo2.get())
        kerület= (a+b)*2
        if a<=0 or b<=0 or c<=0:
            mezo4.delete(0, END)
            mezo4. insert(0, str()+' 0 nem lehet ')
        else:
            mezo4.delete(0, END)
            mezo4. insert(0, str(kerület))
    #teglalap kerület oldal
    abl5= Toplevel(foablak)
    abl5.title('Kerület')
    szoveg1=Label(abl5, text='a oldal (cm):')
    szoveg2=Label(abl5, text='b oldal (cm):')
    szoveg4=Label(abl5, text='Eredmény:')
    gomb1=Button(abl5, text='Szamitás', command=szam)
    mezo1= Entry(abl5)
    mezo2= Entry(abl5)
    mezo4= Entry(abl5)
    szoveg1.grid(row=1)
    szoveg2.grid(row=2)
    szoveg4.grid(row=5)
    gomb1.grid(row=4 ,column= 2)
    mezo1.grid(row=1 ,column= 2)
    mezo2.grid(row=2 ,column= 2)
    mezo4.grid(row=5 ,column= 2)
    gomb2=Button(abl5, text='Kilépés' , command=abl5.destroy)
    gomb2.grid(row=6 ,column= 2)
    #teglalap rajzolás
    teglalapkeruletcanvas = Canvas(abl5, width = 200, height = 150, bg = "white")
    teglalapkeruletcanvas.create_rectangle(30, 30, 180, 120, outline="#000000",fill="#fb0")
    teglalapkeruletcanvas.grid(column = 4, row = 1, rowspan = 7)
    abl5.mainloop()
  
def teglalap_területe():
    t=''
    def szam():
        if not t:
            mezo4.delete(0, END)
            mezo4.insert(0, str()+'Számadatot kell megadni')
        a=float(mezo1.get())
        b=float(mezo2.get())
        terület= a*b
        if a<=0 or b<=0:
            mezo4.delete(0, END)
            mezo4. insert(0, str()+' 0 nem lehet ')
        else:
            mezo4.delete(0, END)
            mezo4. insert(0, str(kerület))
    #teglalap terület oldal
    abl5= Toplevel(foablak)
    abl5.title('Terület')
    szoveg1=Label(abl5, text='a oldal (cm):')
    szoveg2=Label(abl5, text='b oldal (cm):')
    szoveg4=Label(abl5, text='Eredmény:')
    gomb1=Button(abl5, text='Szamitás', command=szam)
    mezo1= Entry(abl5)
    mezo2= Entry(abl5)
    mezo4= Entry(abl5)
    szoveg1.grid(row=1)
    szoveg2.grid(row=2)
    szoveg4.grid(row=5)
    gomb1.grid(row=4 ,column= 2)
    mezo1.grid(row=1 ,column= 2)
    mezo2.grid(row=2 ,column= 2)
    mezo4.grid(row=5 ,column= 2)
    gomb2=Button(abl5, text='Kilépés' , command=abl5.destroy)
    gomb2.grid(row=6 ,column= 2)
    #teglalap rajzolás
    teglalapkeruletcanvas = Canvas(abl5, width = 200, height = 150, bg = "white")
    teglalapkeruletcanvas.create_rectangle(30, 30, 180, 120, outline="#000000",fill="#fb0")
    teglalapkeruletcanvas.grid(column = 4, row = 1, rowspan = 7)
    abl5.mainloop()
    
foablak=Tk()
foablak.title("IKT projekt")
menubar=Menu(foablak)  
foablak.title("IKT projekt")
foablak.minsize(width=500, height=500)

# adatok menűpont
menusor=Menu(foablak)

#fő oldal elrendezés
cim = Label(foablak,  text='Síkidomok kerülete területe számítás', font=("Arial", 25))
foablakkep = Image.open('foablakkep.png')
meretezes = foablakkep.resize((550, 500), Image.ANTIALIAS)
meretezett = ImageTk.PhotoImage(meretezes)
kephez = Label(image= meretezett)
kephez.pack(side= BOTTOM)
cim.pack()

# adatok menűpont
file = Menu(menubar, tearoff=0)

#első gomb

menubar.add_command(label="Névjegy", command = nevjegy)
menubar.add_command(label="Kilépés", command = foablak.destroy)
file.add_cascade(label='Névjegy', menu=menubar)
foablak.config(menu=menubar) 
#második gomb a menüsávon vége

#háromszög menü gomb kezdete
haromszög = Menu(file, tearoff=0)
haromszög.add_command(label="Kerület", command=h_kerulet)
haromszög.add_command(label="Terület" , command=h_terulet)
file.add_cascade(label='Háromszög', menu=haromszög)

#trapéz menü gomb kezdete
trapéz = Menu(file, tearoff=0)
trapéz.add_command(label="Kerület")
trapéz.add_command(label="Terület")
file.add_cascade(label='Trapéz', menu=trapéz)

#paralelogramma menü gomb kezdete
Paralelogramma = Menu(file, tearoff=0)
Paralelogramma.add_command(label="Kerület")
Paralelogramma.add_command(label="Terület")
file.add_cascade(label='Paralelogramma', menu=Paralelogramma)

#téglalap menü gomb kezdete
teglalap = Menu(file, tearoff=0)
teglalap.add_command(label="Kerület")
teglalap.add_command(label="Terület")
file.add_cascade(label='Téglalap', menu=teglalap)

#deltoid menü gomb kezdete
deltoid = Menu(file, tearoff=0)
deltoid.add_command(label="Kerület")
deltoid.add_command(label="Terület")
file.add_cascade(label='Deltoid', menu=deltoid)

#rombusz menü gomb kezdete
rombusz = Menu(file, tearoff=0)
rombusz.add_command(label="Kerület")
rombusz.add_command(label="Terület")
file.add_cascade(label='Rombusz', menu=rombusz)

#négyzet menü gomb kezdete
negyzet = Menu(file, tearoff=0)
negyzet.add_command(label="Kerület")
negyzet.add_command(label="Terület")
file.add_cascade(label='Négyzet', menu=negyzet)

#kör menü gomb kezdete
kor = Menu(file, tearoff=0)
kor.add_command(label="Kerület")
kor.add_command(label="Terület")
file.add_cascade(label='Kör', menu=kor)

foablak.config(menu=menubar) 

foablak.mainloop()
