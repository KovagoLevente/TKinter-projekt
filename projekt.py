from tkinter import *
import math


# nevjegy
def nevjegy():
    abl2=Toplevel(foablak)
    uz2=Message(abl2,text='készitete:\nKővágó Levente\nUtasi Balázs\nAuer Zoltán', )
    gomb2=Button(abl2, text='Kilépés' , command=abl2.destroy)
    uz2.pack()
    gomb2.pack()
    abl2.pack()
def derekszog_terulet():
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
    abl3.title('Felszin')
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
def derekszog_kerulet():
def egyenloszaru_terulet():
def egyenloszaru_kerulet():
def egyenlooldalu_terulet():
def egyenlooldalu_kerulet():

foablak=Tk()

foablak.title("IKT projekt")
foablak.minsize(width=300, height=300)
# adatok menűpont
menusor=Frame(foablak)
menusor.pack(side=TOP , fill=X)

menu1=Menubutton(menusor, text='Adat', )
menu1.pack(side=LEFT)
fajl=Menu(menu1)
fajl.add_command(label='Nevjegy' ,command= nevjegy, )
fajl.add_command(label='Kilépés' ,command= foablak.destroy, )
menu1.config(menu=fajl)
# háromszög menüpont
menu2=Menubutton(menusor, text='Háromszögek', )
menu2.pack(side=LEFT)
haromszog=Menu(menu2)
haromszog.add_command(label='Derékszögü' , command=derekszog_terulet,  )
haromszog.add_command(label='Derékszögü' , command=derekszog_kerulet,  )
haromszog.add_command(label='Egyenlő oldalu' , command=egyenloszaru_terulet,  )
haromszog.add_command(label='Egyenlő oldalu' , command=egyenloszaru_kerulet,  )
haromszog.add_command(label='Egyelő szárú' , command=,egyenlooldalu_terulet  )
haromszog.add_command(label='Egyelő szárú' , command=, egyenlooldalu_kerulet )
menu2.config(menu=haromszog)

foablak.mainloop()
