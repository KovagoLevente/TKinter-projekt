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
    abl2.pack()
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


foablak=Tk()

foablak.title("IKT projekt")
foablak.minsize(width=500, height=500)
# adatok menűpont
menusor=Frame(foablak)
menusor.pack(side=TOP , fill=X)

menu1=Menubutton(menusor, text='Adat', )
menu1.pack(side=LEFT)
fajl=Menu(menu1)
fajl.add_command(label='Nevjegy' ,command= nevjegy, )
fajl.add_command(label='Kilépés' ,command= foablak.destroy, )
menu1.config(menu=fajl)
#fő oldal elrendezés
cim = Label(foablak,  text='Síkidomok kerülete területe számítás', font=("Arial", 25))
foablakkep = Image.open('foablakkep.png')
meretezes = foablakkep.resize((550, 500), Image.ANTIALIAS)
meretezett = ImageTk.PhotoImage(meretezes)
kephez = Label(image= meretezett)
kephez.pack(side= BOTTOM)
cim.pack()


#menü
nevjegy0=tk.Menu(menusor, tearoff=0, )
haromszog0=tk.Menu(menusor, tearoff=0 )
negyszogek0=tk.Menu(menusor, tearoff=0 )
kor0=tk.Menu(menusor, tearoff=0 )
#________________________________________________________________________
#menüsor
menusor.add_cascade(label='Névjegy', menu=nevjegy0)
menusor.add_cascade(label='Háromszög' , menu=haromszog0) # elsö sor 
menusor.add_cascade(label='Négyszögek', menu=negyszogek0)
menusor.add_cascade(label='Kör', menu=kor0)
#________________________________________________________________________
#Névjegy
nevjegy0.add_command(label='Nevjegy' ,command= nevjegy, )
nevjegy0.add_command(label='Kilépés' ,command= foablak.destroy, )
#________________________________________________________________________
#Háromszög
haromszog0.add_command(label='terület' , command=h_terulet,  )
haromszog0.add_command(label='kerület' , command=h_kerulet,  )

foablak.mainloop()
