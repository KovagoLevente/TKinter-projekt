from re import L
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
def teglalap_terület():

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
def trapez_kerulet():
    k=''
    def szam():
        if not k :
            mezo4.delete(0, END)
            mezo4.insert(0, str()+'Számadatot kell megadni')
        a=float(mezo1.get())
        b=float(mezo2.get())
        c=float(mezo3.get())
        d=float(mezo5.get())
        kerület= a+b+c+d
        if a<=0 or b<=0 or c<=0 or d<=0:
            mezo4.delete(0, END)
            mezo4. insert(0, str()+' 0 nem lehet ')
        else:
            mezo4.delete(0, END)
            mezo4. insert(0, str(kerület))
    #teglalap kerület oldal
    abl6= Toplevel(foablak)
    abl6.title('Kerület')
    szoveg1=Label(abl6, text='a oldal (cm):')
    szoveg2=Label(abl6, text='b oldal (cm):')
    szoveg3=Label(abl6, text='c oldal (cm):')
    szoveg5=Label(abl6, text='d oldal (cm):')
    szoveg4=Label(abl6, text='Eredmény:')
    gomb1=Button(abl6, text='Szamitás', command=szam)
    mezo1= Entry(abl6)
    mezo2= Entry(abl6)
    mezo3= Entry(abl6)
    mezo5= Entry(abl6)
    mezo4= Entry(abl6)
    szoveg1.grid(row=1)
    szoveg2.grid(row=2)
    szoveg3.grid(row=3)
    szoveg5.grid(row=4)
    szoveg4.grid(row=5)
    gomb1.grid(row=5 ,column= 2)
    mezo1.grid(row=1 ,column= 2)
    mezo2.grid(row=2 ,column= 2)
    mezo3.grid(row=3 ,column= 2)
    mezo5.grid(row=4 ,column= 2)
    mezo4.grid(row=6 ,column= 2)
    gomb2=Button(abl6, text='Kilépés' , command=abl6.destroy)
    gomb2.grid(row=7 ,column= 2)
    #teglalap rajzolás
    trapezrajz = Canvas(abl6, width = 200, height = 150 )
    trapezrajz.create_line(15, 125, 185, 125, fill="black", width = 4)
    trapezrajz.create_line(140, 50, 60, 50, fill = "black", width = 4)
    trapezrajz.create_line(15, 125, 60, 50, fill = "black", width = 4)
    trapezrajz.create_line(185, 125, 140, 50, fill = "black", width = 4)
    trapezrajz.grid(column = 4, row = 1, rowspan = 7)
    abl6.mainloop()
def trapez_terulet():
    k=''
    def szam():
        if not k :
            mezo4.delete(0, END)
            mezo4.insert(0, str()+'Számadatot kell megadni')
        a=float(mezo1.get())
        b=float(mezo2.get())
        m=float(mezo3.get())
        kerület= ((a+c)*m)/2
        if a<=0 or b<=0 or m<=0  :
            mezo4.delete(0, END)
            mezo4. insert(0, str()+' 0 nem lehet ')
        else:
            mezo4.delete(0, END)
            mezo4. insert(0, str(kerület))
    #teglalap kerület oldal
    abl6= Toplevel(foablak)
    abl6.title('Kerület')
    szoveg1=Label(abl6, text='a oldal (cm):')
    szoveg2=Label(abl6, text='b oldal (cm):')
    szoveg3=Label(abl6, text='m oldal (cm):')
    szoveg4=Label(abl6, text='Eredmény:')
    gomb1=Button(abl6, text='Szamitás', command=szam)
    mezo1= Entry(abl6)
    mezo2= Entry(abl6)
    mezo3= Entry(abl6)
    mezo5= Entry(abl6)
    mezo4= Entry(abl6)
    szoveg1.grid(row=1)
    szoveg2.grid(row=2)
    szoveg3.grid(row=3)
    szoveg4.grid(row=5)
    gomb1.grid(row=5 ,column= 2)
    mezo1.grid(row=1 ,column= 2)
    mezo2.grid(row=2 ,column= 2)
    mezo3.grid(row=3 ,column= 2)
    mezo4.grid(row=6 ,column= 2)
    gomb2=Button(abl6, text='Kilépés' , command=abl6.destroy)
    gomb2.grid(row=7 ,column= 2)
    #teglalap rajzolás
    trapezrajz = Canvas(abl6, width = 200, height = 150 )
    trapezrajz.create_line(15, 125, 185, 125, fill="black", width = 4)
    trapezrajz.create_line(140, 50, 60, 50, fill = "black", width = 4)
    trapezrajz.create_line(15, 125, 60, 50, fill = "black", width = 4)
    trapezrajz.create_line(185, 125, 140, 50, fill = "black", width = 4)
    trapezrajz.grid(column = 4, row = 1, rowspan = 7)
foablak=Tk()
foablak.title("IKT projekt")
menubar=Menu(foablak)  
foablak.title("IKT projekt")
foablak.minsize(width=500, height=500)
cim = Label(foablak,  text='Síkidomok kerülete területe számítás', font=("Arial", 25))
foablakkep = Image.open('foablakkep.png')
meretezes = foablakkep.resize((550, 500), Image.ANTIALIAS)
meretezett = ImageTk.PhotoImage(meretezes)
kephez = Label(image= meretezett)
kephez.pack(side= BOTTOM)
cim.pack()

menubar=Menu(foablak)
foablak.config(menu=menubar)

leiras_menu=Menu(menubar ,tearoff=0 )
leiras_menu.add_command(label='Névjegy',  command=nevjegy)
leiras_menu.add_command(label='Kilépés', command= foablak.destroy)
leiras_menu.add_separator()
menubar.add_cascade( label="Leírás", menu = leiras_menu , underline=0)


#háromszög
haromszog_menu = Menu( menubar, tearoff=0 )
haromszog_menu.add_command(label='Terület' , command=h_terulet)
haromszog_menu.add_command(label='Kerület' , command= h_kerulet)
haromszog_menu.add_separator()
menubar.add_cascade( label="Háromszög", menu=haromszog_menu, underline=0)
#négyzet
negyszog_menu = Menu( menubar, tearoff=0 )

trapez_menu = Menu(negyszog_menu, tearoff=0)
trapez_menu.add_command(label='Terület', command=trapez_terulet)
trapez_menu.add_command(label='Kerület', command=trapez_kerulet)

paralelogramma_menu = Menu(negyszog_menu, tearoff=0)
paralelogramma_menu.add_command(label='Terület',)
paralelogramma_menu.add_command(label='Kerület',)

teglalap_menu = Menu(negyszog_menu, tearoff=0)
teglalap_menu.add_command(label='Terület', command=teglalap_terület )
teglalap_menu.add_command(label='Kerület', command=teglalap_kerulet )

deltoid_menu = Menu(negyszog_menu, tearoff=0)
deltoid_menu.add_command(label='Terület', )
deltoid_menu.add_command(label='Kerület', )

negyzet_menu = Menu(negyszog_menu, tearoff=0)
negyzet_menu.add_command(label='Terület', )
negyzet_menu.add_command(label='Kerület', )

rombusz_menu = Menu(negyszog_menu, tearoff=0)
rombusz_menu.add_command(label='Terület', )
rombusz_menu.add_command(label='Kerület', )

negyszog_menu.add_cascade(label='Trapéz' , menu=trapez_menu )
negyszog_menu.add_cascade(label='Paralelogramma' , menu= paralelogramma_menu )
negyszog_menu.add_cascade(label='Téglalap' , menu=teglalap_menu  )
negyszog_menu.add_cascade(label='Deltoid' , menu=deltoid_menu  )
negyszog_menu.add_cascade(label='Négyzet' , menu=negyzet_menu  )
negyszog_menu.add_cascade(label='Rombusz' , menu=rombusz_menu )
negyszog_menu.add_separator()
menubar.add_cascade( label="Négyszögek", menu=negyszog_menu, underline=0)

#kör
kor_menu = Menu( menubar, tearoff=0 )
kor_menu.add_command(label='Terület' , )
kor_menu.add_command(label='Kerület' , )
kor_menu.add_separator()
menubar.add_cascade( label="Kör", menu=kor_menu, underline=0)


foablak.mainloop()
