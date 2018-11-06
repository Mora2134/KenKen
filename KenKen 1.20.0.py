#Vara KenKen Con Jocxan

import tkinter
from tkinter import * 
from tkinter import messagebox
import math
import time
import random
import os 

#Variables globales que se utilizan para varias funciones y comrpobacioles a la hora de validar
proceso=0
iraresta="SI"
procesodecrono= "Si"
dificultad= "F"
OpcionReloj="N"
OpcionSonido="N"
partidaActual= 0
nombre= "Jocxan"
multiTAMANO= "N"
tamano= 3
jugadas=[]
rehacer=[]


#Son listas que se crearon para guardar lo que el jugador fuera seleccionando en la cuadricula 6x6
Primer=[0,0,0,0,0,0,0,0,0]
segundo=[0,0,0,0,0,0,0,0,0]
tercero=[0,0,0,0,0,0,0,0,0]
cuarto=[0,0,0,0,0,0,0,0,0]
quinto=[0,0,0,0,0,0,0,0,0]
sexto=[0,0,0,0,0,0,0,0,0]
septimo=[0,0,0,0,0,0,0,0,0]
octavo=[0,0,0,0,0,0,0,0,0]
noveno=[0,0,0,0,0,0,0,0,0]
#Son variables que se le otorgan a los labels que no estan en la cuadricula, los que se utilizan para saber que es lo que el jugador debe hacer por cada color
texto1=texto2= texto3= texto4= texto5= texto6= texto7= texto8= texto9= texto10= texto11= texto12= texto13= texto14= texto15= texto16= texto17= texto18= texto19= "   "
texto20=texto21=texto22=texto23=texto24=texto25=texto26=texto27=texto28=texto29=texto30=texto31=texto32=texto33=texto34=texto35=texto36="   "

#Son las variables para los colores de cada label
A1=A2=A3=A4=A5=A6=A7=A8=A9=A10=A11=A12=A13=A14=A15=A16=A17=A18=A19=A20=A21=A22=A23=A24=A25=A26=A27=A28=A29=A30=A31=A32=A33=A34=A35=A36=A37=A38=A39=A40=A41=A42=A43="green"
A44=A45=A46=A47=A48=A49=A50=A61=A62=A63=A64=A65=A66=A67=A68=A69=A70=A71=A72=A73=A74=A75=A76=A77=A78=A79=A80=A81= "green"
A51=A52=A53=A54=A55=A56=A57=A58=A59=A60= "green"
#--------------------------------------------------------------------------------------------------------
#Clase para guardar los tiempos del pronostico y también del cronómetro para cuando los necesite como cuando uso la de
# la funcion continuar. Es parte del cronómetro
class cronoguardador:
    def __init__(self):
        self.__hora= 0
        self.__minutos= 0
        self.__segundos= 0
        self.__deci= 0

        self.__d= 0
        self.__s= 0
        self.__m= 0
        self.__h= 0

        self.__cd= 0
        self.__cs= 0
        self.__cm= 0
        self.__ch= 0

    def comprobador(self):
        if guardador.geth()>= guardador.getho():
            if guardador.getm()>= guardador.getmi():
                if guardador.gets()>= guardador.getse():
                    if guardador.getd()>= guardador.getde():
                        return True
                    return False
                return False
            return False
        return False
                
            
    def setguardar(self,d,s,m,h):
        self.__hora= h
        self.__minutos= m
        self.__segundos= s
        self.__deci= d

    def setguardar1(self):
        self.__d= 0
        self.__s= 0
        self.__m= 0
        self.__h= 0
        self.__cd= 0
        self.__cs= 0
        self.__cm= 0
        self.__ch= 0

    def getd(self):
        return self.__deci
    def gets(self):
        return self.__segundos
    def getm(self):
        return self.__minutos
    def geth(self):
        return self.__hora
    #Estos son los get y set de el pronostico

    def setde(self,d):
        self.__d= d

    def setse(self,s):
        self.__s= s

    def setmi(self,m):
        self.__m= m

    def setho(self,h):
        self.__h= h

    def getde(self):
        return self.__d
    
    def getse(self):
        return self.__s
    
    def getmi(self):
        return self.__m
    
    def getho(self):
        return self.__h
    #---------------------------------------------------------
    def setdec(self,d):
        self.__cd= d

    def setsec(self,s):
        self.__cs= s

    def setmic(self,m):
        self.__cm= m

    def sethoc(self,h):
        self.__ch= h

    def getdec(self):
        return self.__cd
    
    def getsec(self):
        return self.__cs
    
    def getmic(self):
        return self.__cm
    
    def gethoc(self):
        return self.__ch
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------

#Es la primera ventana al ejecutar el programa, donde vienen las diferentes opciones para configuar, acerca de, iniciar juego y ayuda
def inicioD():
    
    principal= Tk()
    principal.title("Bienvenido")
    principal.geometry("450x300")
    principal.tit=Label(principal,text="Bienvenido",font="Arial 22 italic")
    principal.tit.place(x=150,y=20)
    
    def kenken1():
        principal.destroy()
        menu()
        
    def ayuda1():
        os.startfile("ManualDeKenKen.pdf")

    def acercade1():
        messagebox.showinfo("Acerca De", "Autor: Jocxan Sandí Batista y Sebastian Mora \nFecha: 15/10/2018 \nVersión: 5.8")

    def configuraciondejuego():
        principal.destroy()
        config()

    kenken=Button(principal,text="Jugar KenKen", font="Arial 18 bold", bg="SteelBlue1",command=kenken1)
    kenken.place(x=10,y=100)
    configuracion=Button(principal,text="Configuracion", font="Arial 18 bold", bg="lime green",command=configuraciondejuego)
    configuracion.place(x=250,y=100)
    ayuda=Button(principal,text="Ayuda", font="Arial 18 bold", bg="yellow",command=ayuda1)
    ayuda.place(x=10,y=200)
    acerca=Button(principal,text="Acerca De", font="Arial 18 bold",bg="red", command=acercade1)
    acerca.place(x=250,y=200)
    
#Ventana del juego de 6x6 donde A con su sigueinte número se utilizan para el color que se le va a dar a cada cuadricula por eso son 36
def kenken_juego_Abierto(A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16,A17,A18,A19,A20,A21,A22,A23,A24,A25,A26,A27,A28,A29,A30,A31,A32,A33,A34,A35,A36,A37,A38, A39,A40,A41,A42,A43,A44,A45,A46,A47,A48,A49,A50,A51,A52,A53,A54,A55,A56,A57,A58,A59,A60,A61,A62,A63,A64,A65,A66,A67,A68,A69,A70,A71,A72,A73,A74,A75,A76,A77,A78,A79,A80,A81,op1):
    global defaultbg,Laf1,Laf2,Laf3,Laf4,Laf5,Laf6,Laf7,Laf8,Laf9,Laf10,Laf11,Laf12,Laf13,Laf14,Laf15,Laf16,Laf17,Laf18,Laf19,Laf20,Laf21,Laf22,Laf23,Laf24,Laf25,Laf26,Laf27,Laf28,Laf29,Laf30,Laf31,Laf32,Laf33,Laf34,Laf35,Laf36
    global texto1,texto2,texto3,texto4,texto5,texto6,texto7,texto8,texto9,texto10,texto11,texto12,texto13,texto14,texto15,texto16,texto17,texto18,texto19,texto20,texto21,texto22,texto23,texto24,texto25,texto26,texto27,texto28,texto29,texto30,texto31,texto32,texto33,texto34,texto35,texto36
    global tamano
    menu= Tk()
    menu.title("KenKen juego")
    menu.geometry("1200x850")
    tit=Label(menu,text="KenKen")
    tit.config(font=("serif 34 bold italic"),fg="green")
    tit.place(x=350,y=20)
    

    ###Funciones que van de la mano con el cronómetro
    #Cronómetro con pronostico(timer)

    def pararcronometro2():
        global proceso,procesodecrono, iraresta
        time.after_cancel(proceso)
        iraresta="NO"
        btnContinuar=Button(menu,width=8, fg='blue', text='Continuar', command=continuar)
        btnContinuar.place(x=3000,y=100)

    def resta():
        if guardador.getdec()==0:
            if  guardador.getsec()==0:
                if guardador.getmic()==0:
                    if guardador.gethoc()==0:
                        pararcronometro2()
                        terminarya1()
                    else:
                        h=guardador.gethoc() -1
                        hora['text'] = h
                        guardador.sethoc(h)
                        guardador.setdec(900)
                        guardador.setsec(59)
                        guardador.setmic(59)

                        d['text'] = 90
                        minn['text'] =  59
                        time['text'] = 59
                    
                else:
                    h=guardador.getmic() -1
                    minn['text'] = h
                    guardador.setmic(h)
                    guardador.setdec(900)
                    guardador.setsec(59)

                    d['text'] = 90
                    time['text'] = 59
                    
            else:
                h=guardador.getsec() -1
                time['text'] = h
                guardador.setsec(h)
                guardador.setdec(900)
                d['text'] = 90
        else:
            h= guardador.getdec() -1
            d['text'] = h//10
            guardador.setdec(h)

    def iniciarcrono2(decimales=0,segundos=0,minutos=0,horas=0):
        global proceso, iraresta
        guardador.setguardar(decimales,segundos,minutos,horas)
        if iraresta=="SI":
            resta()
     
        # hacemos un llamamient a la funcion mostrarContador pasando el
        # contador mas uno
        if decimales==900:
            if segundos == 59:
                if minutos==59:
                    proceso=time.after(1, iniciarcrono2, (0),(0),(0),(horas+1))

                else:
                    proceso=time.after(1, iniciarcrono2, (0),(0),(minutos+1),(horas))

            else:
                proceso=time.after(1, iniciarcrono2, (0),(segundos+1),(minutos),(horas))
        else:
            
            proceso=time.after(1, iniciarcrono2,(decimales+1), (segundos),(minutos),(horas))


    #Funciones que van con el cronómetro pero el normal     
    def continuar():
        h= guardador.geth()
        m= guardador.getm()
        s= guardador.gets()
        d= guardador.getd()
        btnParar=Button(menu, width=8,fg='blue', text='Pausar', command=pararcronometro)
        btnParar.place(x=1035,y=100)
        proceso=time.after(1, iniciarcrono, (d),(s),(m),h)

    def botones():
        btnParar=Button(menu,width=8, fg='blue', text='Pausar', command=pararcronometro)
        btnParar.place(x=1035,y=100)
    def cero():
        global proceso
        time['text'] = 0
        minn['text']=0
        hora['text']=0
        d['text']=0

        btnIniciar=Button(root,width=8, fg='blue', text='Iniciar', command=iniciarcrono)
        btnIniciar.place(x=350,y=1)
        time.after_cancel(proceso)
    def pararcronometro():
        global proceso,procesodecrono
        
        procesodecrono= "N"
        time.after_cancel(proceso)
        
        btnContinuar=Button(menu,width=8, fg='blue', text='Continuar', command=continuar)
        btnContinuar.place(x=1035,y=100)
    def iniciarcrono(decimales=0,segundos=0,minutos=0,horas=0):
        global proceso, procesodecrono
        procesodecrono= "Si"

        guardador.setguardar(decimales,segundos,minutos,horas)
        
        time['text'] = segundos
        minn['text']=minutos
        hora['text']=horas
        d['text']=decimales//10

        if decimales==900:
            if segundos == 59:
                if minutos==59:
                    proceso=time.after(1, iniciarcrono, (0),(0),(0),(horas+1))

                else:
                    proceso=time.after(1, iniciarcrono, (0),(0),(minutos+1),(horas))

            else:
                proceso=time.after(1, iniciarcrono, (0),(segundos+1),(minutos),(horas))
        else:
            
            proceso=time.after(1, iniciarcrono,(decimales+1), (segundos),(minutos),(horas))
    #Labels que se utilizan para el cronómetro
    time = Label(menu, fg='red', width=2, font=("","18"),bg="white")
    time.place(x=1070,y=61)

    cronometroLa = Label(menu,text="Cronómetro", fg='black', width=10,height=2, font=("","18"))
    cronometroLa.place(x=990,y=1)

    hora = Label(menu, fg='red', width=2, font=("","18"),bg="white")
    hora.place(x=1000,y=60)

    minn = Label(menu, fg='red', width=2, font=("","18"),bg="white")
    minn.place(x=1035,y=60)

    
    d = Label(menu, fg='red', width=2, font=("","18"),bg="white")
    d.place(x=1105,y=70)
    #-----------------------------------------------------------------------------------------------------------------------------
    if op1=="S1":
        botones()
        iniciarcrono()
    if op1=="S2":
        iniciarcrono2()

    if op1=="N":
        time.destroy()
        minn.destroy()
        cronometroLa.destroy()
        hora.destroy()
        d.destroy()
    #---------------------------------------------------------------------------------------------------------------------------------
    #Labels que se usan para los cuadros con las formulas
    if tamano >=3:
        la1=Button(menu,text=texto1,height=3,width=3,bd=2,relief="solid",command=lambda:posib(texto1,1),activebackground="SteelBlue1",bg=Laf1)
        la1.place(x=20,y=5)
        la2=Button(menu,text=texto2,height=3,width=3,bd=2,command=lambda:posib(texto2,2),relief="solid",activebackground="SteelBlue1",bg=Laf2)
        la2.place(x=45,y=5)
        la3=Button(menu,text=texto3,height=3,command=lambda:posib(texto3,3),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf3)
        la3.place(x="70",y=5)
        la4=Button(menu,text=texto4,height=3,command=lambda:posib(texto4,4),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf4)
        la4.place(x="95",y=5)

    if tamano>= 4:
        la5=Button(menu,text=texto5,height=3,command=lambda:posib(texto5,5),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf5)
        la5.place(x="120",y=5)
        la6=Button(menu,text=texto6,height=3,command=lambda:posib(texto6,6),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf6)
        la6.place(x="145",y=5)
        la7=Button(menu,text=texto7,height=3,command=lambda:posib(texto7,7),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf7)
        la7.place(x=20,y=55)
        la8=Button(menu,text=texto8,height=3,command=lambda:posib(texto8,8),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf8)
        la8.place(x=45,y=55)
        la9=Button(menu,text=texto9,height=3,command=lambda:posib(texto9,9),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf9)
        la9.place(x=70,y=55)
        la10=Button(menu,text=texto10,height=3,command=lambda:posib(texto10,10),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf10)
        la10.place(x=95,y=55)
    if tamano>= 5:
        la11=Button(menu,text=texto11,height=3,command=lambda:posib(texto11,11),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf11)
        la11.place(x=120,y=55)
        la12=Button(menu,text=texto12,height=3,command=lambda:posib(texto12,12),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf12)
        la12.place(x=145,y=55)
    if tamano>=6:
        la13=Button(menu,text=texto13,height=3,command=lambda:posib(texto13,13),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf13)
        la13.place(x=20,y=105)
        la14=Button(menu,text=texto14,height=3,command=lambda:posib(texto14,14),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf14)
        la14.place(x=45,y=105)
        la15=Button(menu,text=texto15,height=3,command=lambda:posib(texto15,15),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf15)
        la15.place(x=70,y=105)
        la16=Button(menu,text=texto16,height=3,command=lambda:posib(texto16,16),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf16)
        la16.place(x=95,y=105)
        la17=Button(menu,text=texto17,height=3,command=lambda:posib(texto17,17),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf17)
        la17.place(x=120,y=105)
    if tamano>=7:
        la18=Button(menu,text=texto18,height=3,command=lambda:posib(texto18,18),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf18)
        la18.place(x=145,y=105)
        la19=Button(menu,text=texto19,height=3,command=lambda:posib(texto19,19),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf19)
        la19.place(x=20,y=160)
        la20=Button(menu,text=texto20,height=3,command=lambda:posib(texto20,20),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf20)
        la20.place(x=45,y=160)
        la21=Button(menu,text=texto21,height=3,command=lambda:posib(texto21,21),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf21)
        la21.place(x=70,y=160)
        la22=Button(menu,text=texto22,height=3,command=lambda:posib(texto22,22),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf22)
        la22.place(x=95,y=160)
        la23=Button(menu,text=texto23,height=3,command=lambda:posib(texto23,23),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf23)
        la23.place(x=120,y=160)
        la24=Button(menu,text=texto24,height=3,command=lambda:posib(texto24,24),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf24)
        la24.place(x=145,y=160)
        la25=Button(menu,text=texto25,height=3,command=lambda:posib(texto25,25),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf25)
        la25.place(x=20,y=210)
        la26=Button(menu,text=texto26,height=3,command=lambda:posib(texto26,26),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf26)
        la26.place(x=45,y=210)
        la27=Button(menu,text=texto27,height=3,command=lambda:posib(texto27,27),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf27)
        la27.place(x=70,y=210)
    if tamano>=8:
        la28=Button(menu,text=texto28,height=3,command=lambda:posib(texto28,28),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf28)
        la28.place(x=95,y=210)
        la29=Button(menu,text=texto29,height=3,command=lambda:posib(texto29,29),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf29)
        la29.place(x=120,y=210)
        la30=Button(menu,text=texto30,height=3,command=lambda:posib(texto30,30),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf30)
        la30.place(x=145,y=210)
        la31=Button(menu,text=texto31,height=3,command=lambda:posib(texto31,31),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf31)
        la31.place(x=20,y=265)
        la32=Button(menu,text=texto32,height=3,command=lambda:posib(texto32,32),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf32)
        la32.place(x=45,y=265)
    if tamano>=9:
        la33=Button(menu,text=texto33,height=3,command=lambda:posib(texto33,33),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf33)
        la33.place(x=70,y=265)
        la34=Button(menu,text=texto34,height=3,command=lambda:posib(texto34,34),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf34)
        la34.place(x=95,y=265)
        la35=Button(menu,text=texto35,height=3,command=lambda:posib(texto35,35),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf35)
        la35.place(x=120,y=265)
        la36=Button(menu,text=texto36,height=3,command=lambda:posib(texto36,36),width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf36)
        la36.place(x=145,y=265)


    def volvertextos():
        global texto1,texto2,texto3,texto4,texto5,texto6,texto7,texto8,texto9,texto10,texto11,texto12,texto13,texto14,texto15,texto16,texto17,texto18,texto19,texto20,texto21,texto22,texto23,texto24,texto25,texto26,texto27,texto28,texto29,texto30,texto31,texto32,texto33,texto34,texto35,texto36
        texto1=texto2= texto3= texto4= texto5= texto6= texto7= texto8= texto9= texto10= texto11= texto12= texto13= texto14= texto15= texto16= texto17= texto18= texto19= "   "
        texto20=texto21=texto22=texto23=texto24=texto25=texto26=texto27=texto28=texto29=texto30=texto31=texto32=texto33=texto34=texto35=texto36="   "



    #funciones con el juego kenken
    def partinaAiniciar():
        global partidaActual, OpcionReloj
        if OpcionReloj=="S1" or OpcionReloj=="N":
            menu.destroy()
            abrirjuegos()
            motrar()
        else:
            h= guardador.getho()
            m= guardador.getmi()
            s= guardador.getse()
    
            guardador.sethoc(h)
            guardador.setmic(m)
            guardador.setsec(s)
            menu.destroy()
            abrirjuegos()
            motrar()

        

    def salir2():
        global nombre
        nombre= "N"
        menu.destroy()
        
        inicioD()

    def reiniciajuego():

        global partidaActual, OpcionReloj
        if OpcionReloj=="S1" or OpcionReloj=="N":
            menu.destroy()
            partida_juego(partidaActual)
            motrar()
            
            
        else:
            h= guardador.getho()
            m= guardador.getmi()
            s= guardador.getse()
    
            guardador.sethoc(h)
            guardador.setmic(m)
            guardador.setsec(s)
            menu.destroy()
            partida_juego(partidaActual)
            motrar()
    def terminarya():
        global OpcionReloj,iraresta
        menuA= Tk()
        menuA.title("Aviso")
        menuA.geometry("700x150")
        tit=Label(menuA,text="¿Desea terminar el juego?")
        tit.config(font=("serif 34 bold italic"),fg="green")
        tit.place(x=10,y=20)
        if OpcionReloj=="S1":
            pararcronometro()
        if OpcionReloj=="S2":
            pararcronometro2()
            

        def quehacer1():
            menu.destroy()
            menuA.destroy()
            volvertextos()
            inicioD()
        def quehacer2():
            global OpcionReloj,iraresta
            menuA.destroy()
            if OpcionReloj=="S1":
                continuar()
            if OpcionReloj=="S2":
                iraresta="SI"
                h= guardador.gethoc()
                m= guardador.getmic()
                s= guardador.getsec()
                d= guardador.getdec()
                
                iniciarcrono2(d,s,m,h)

        si= Button(menuA,text="SÍ",height=3,width=7,bg="blue",fg="black",command=quehacer1)
        si.place(x=150,y=90)
        no= Button(menuA,text="No",height=3,width=7,bg="blue",fg="black",command=quehacer2)
        no.place(x=300,y=90)

    def terminarya1():
        menuA= Tk()
        menuA.title("Aviso")
        menuA.geometry("700x150")
        tit=Label(menuA,text="¿Desea continuar el juego?")
        tit.config(font=("serif 34 bold italic"),fg="green")
        tit.place(x=10,y=20)

        def quehacer1():
            deci= guardador.getde()
            segundos= guardador.getse()
            mi= guardador.getmi()
            horass= guardador.getho()
            
            
            menuA.destroy()
            iniciarcrono(deci,segundos,mi,horass)
        def quehacer2():
            guardador.setguardar1()
            menu.destroy()
            menuA.destroy()
        si= Button(menuA,text="SÍ",height=3,width=7,bg="blue",fg="black",command=quehacer1)
        si.place(x=150,y=90)
        no= Button(menuA,text="No",height=3,width=7,bg="blue",fg="black",command=quehacer2)
        no.place(x=300,y=90)
        
    def escribir():
        global nombre, dificultad, OpcionReloj
        h= guardador.geth()
        m= guardador.getm()
        s= guardador.gets()
        
        f = open("kenken_jugadores.dat","a")

        if OpcionReloj== "S1" or OpcionReloj== "S2":
            variable= dificultad + "                          " + nombre + "                          " + str(h)+":"+str(m)+":"+str(s) + "\n"
            f.write(variable)

        f.close()
    ##
    ##
    ##
    def  Guardar_Partida():
        global partidaActual, Primer,segundo,tercero,cuarto,quinto,sexto,septimo,octavo,noveno, tamano, dificultad, nombre, OpcionReloj
        h= guardador.geth()
        m= guardador.getm()
        s= guardador.gets()
        f = open("Partida_Guardada.dat","w")

        if tamano==3:
            if OpcionReloj== "S1" or OpcionReloj== "S2":
                Variable3= "Segundos " + str(s) + "\n" + "Minutos " + str(m) + "\n" + "Horas " + str(h) + "\n" + "Tiempo " + str(h)+":"+str(m)+":"+str(s) + "\n"
                variable="Nombre "+ nombre + "\n"+ "Dificultad " + dificultad+ str(tamano) + "\n" + "Partida " + str(partidaActual) + "\n" + "Primeros " + str(Primer)+ "\n" + "Segundos " + str(segundo)+"\n"+"Terceros " + str(tercero)+ "\n"
                final= Variable3 + variable
                f.write(final)
            else:
                variable="Nombre "+ nombre + "\n"+ "Dificultad " + dificultad+ str(tamano) + "\n" + "Partida " + str(partidaActual) + "\n" + "Primeros " + str(Primer)+ "\n" + "Segundos " + str(segundo)+"\n"+"Terceros " + str(tercero)+ "\n"
                f.write(variable)
        
        elif tamano==4:
            if OpcionReloj== "S1" or OpcionReloj== "S2":
                Variable3= "Segundos " + str(s) + "\n" + "Minutos " + str(m) + "\n" + "Horas " + str(h) + "\n" + "Tiempo " + str(h)+":"+str(m)+":"+str(s) + "\n"
                variable="Nombre "+ nombre + "\n"+ "Dificultad " + dificultad+ str(tamano) + "\n" + "Partida " + str(partidaActual) + "\n" + "Primeros " + str(Primer)+ "\n" + "Segundos " + str(segundo)+"\n"+"Terceros " + str(tercero)+ "\n"
                variable1= "Cuartos " + str(cuarto) + "\n"
                final= Variable3+ variable + variable1
                f.write(final)
            else:
                
                variable="Nombre "+ nombre + "\n"+ "Dificultad " + dificultad+ str(tamano) + "\n" + "Partida " + str(partidaActual) + "\n" + "Primeros " + str(Primer)+ "\n" + "Segundos " + str(segundo)+"\n"+"Terceros " + str(tercero)+ "\n"
                variable1= "Cuartos " + str(cuarto) + "\n"
                final= variable + variable1
                f.write(final)
        elif tamano==5:
            if OpcionReloj== "S1" or  OpcionReloj=="S2":
                Variable3= "Segundos " + str(s) + "\n" + "Minutos " + str(m) + "\n" + "Horas " + str(h) + "\n" + "Tiempo " +  str(h)+":"+str(m)+":"+str(s) + "\n"
                variable="Nombre "+ nombre + "\n"+ "Dificultad " + dificultad+ str(tamano) + "\n" + "Partida " + str(partidaActual) + "\n" + "Primeros " + str(Primer)+ "\n" + "Segundos " + str(segundo)+"\n"+"Terceros " + str(tercero)+ "\n"
                variable1= "Cuartos " + str(cuarto) + "\n" + "Quintos " + str(quinto) + "\n" 
                final= Variable3+ variable + variable1
                f.write(final)
            else:
                variable="Nombre "+ nombre + "\n"+ "Dificultad " + dificultad+ str(tamano) + "\n" + "Partida " + str(partidaActual) + "\n" + "Primeros " + str(Primer)+ "\n" + "Segundos " + str(segundo)+"\n"+"Terceros " + str(tercero)+ "\n"
                variable1= "Cuartos " + str(cuarto) + "\n" + "Quintos " + str(quinto) + "\n" 
                final= variable + variable1
                f.write(final)
        elif tamano==6:
            if OpcionReloj== "S1" or OpcionReloj=="S2":
                Variable3= "Segundos " + str(s) + "\n" + "Minutos " + str(m) + "\n" + "Horas " + str(h) + "\n" + "Tiempo " + str(h)+":"+str(m)+":"+str(s) + "\n"
                variable="Nombre "+ nombre + "\n"+ "Dificultad " + dificultad+ str(tamano) + "\n" + "Partida " + str(partidaActual) + "\n" + "Primeros " + str(Primer)+ "\n" + "Segundos " + str(segundo)+"\n"+"Terceros " + str(tercero)+ "\n"
                variable1= "Cuartos " + str(cuarto) + "\n" + "Quintos " + str(quinto) + "\n" + "Sextos " + str(sexto) + "\n"
                final= Variable3+ variable + variable1
                f.write(final)
            else:
                
                variable="Nombre "+ nombre + "\n"+ "Dificultad " + dificultad+ str(tamano) + "\n" + "Partida " + str(partidaActual) + "\n" + "Primeros " + str(Primer)+ "\n" + "Segundos " + str(segundo)+"\n"+"Terceros " + str(tercero)+ "\n"
                variable1= "Cuartos " + str(cuarto) + "\n" + "Quintos " + str(quinto) + "\n" + "Sextos " + str(sexto) + "\n"
                final= variable + variable1
                f.write(final)
        elif tamano==7:
            if OpcionReloj== "S1" or OpcionReloj=="S2":
                Variable3= "Segundos " + str(s) + "\n" + "Minutos " + str(m) + "\n" + "Horas " + str(h) + "\n" + "Tiempo " +  str(h)+":"+str(m)+":"+str(s) + "\n"
                variable="Nombre "+ nombre + "\n"+ "Dificultad " + dificultad+ str(tamano) + "\n" + "Partida " + str(partidaActual) + "\n" + "Primeros " + str(Primer)+ "\n" + "Segundos " + str(segundo)+"\n"+"Terceros " + str(tercero)+ "\n"
                variable1= "Cuartos " + str(cuarto) + "\n" + "Quintos " + str(quinto) + "\n" + "Sextos " + str(sexto) + "\n"+ "Setimos " + str(septimo) + "\n"
                final= Variable3+ variable + variable1
                f.write(final)
            else:
                variable="Nombre "+ nombre + "\n"+ "Dificultad " + dificultad+ str(tamano) + "\n" + "Partida " + str(partidaActual) + "\n" + "Primeros " + str(Primer)+ "\n" + "Segundos " + str(segundo)+"\n"+"Terceros " + str(tercero)+ "\n"
                variable1= "Cuartos " + str(cuarto) + "\n" + "Quintos " + str(quinto) + "\n" + "Sextos " + str(sexto) + "\n"+ "Setimos " + str(septimo) + "\n"
                final= variable + variable1
                f.write(final)
        elif tamano==8:
            if OpcionReloj== "S1" or OpcionReloj=="S2":
                Variable3= "Segundos " + str(s) + "\n" + "Minutos " + str(m) + "\n" + "Horas " + str(h) + "\n" + "Tiempo " +  str(h)+":"+str(m)+":"+str(s) + "\n"
                variable= "Nombre "+ nombre + "\n"+"Dificultad " + dificultad+ str(tamano) + "\n" + "Partida " + str(partidaActual) + "\n" + "Primeros " + str(Primer)+ "\n" + "Segundos " + str(segundo)+"\n"+"Terceros " + str(tercero)+ "\n"
                variable1= "Cuartos " + str(cuarto) + "\n" + "Quintos " + str(quinto) + "\n" + "Sextos " + str(sexto) + "\n"+ "Setimos " + str(septimo) + "\n"
                variable2= "Octavos " + str(octavo) + "\n"
                final=Variable3 + variable + variable1 + variable2
                f.write(final)
            else:
                
                variable= "Nombre "+ nombre + "\n"+"Dificultad " + dificultad+ str(tamano) + "\n" + "Partida " + str(partidaActual) + "\n" + "Primeros " + str(Primer)+ "\n" + "Segundos " + str(segundo)+"\n"+"Terceros " + str(tercero)+ "\n"
                variable1= "Cuartos " + str(cuarto) + "\n" + "Quintos " + str(quinto) + "\n" + "Sextos " + str(sexto) + "\n"+ "Setimos " + str(septimo) + "\n"
                variable2= "Octavos " + str(octavo) + "\n"
                final= variable + variable1 + variable2
                f.write(final)
        else:
            if OpcionReloj== "S1" or OpcionReloj=="S2":
                Variable3= "Segundos " + str(s) + "\n" + "Minutos " + str(m) + "\n" + "Horas " + str(h) + "\n" + "Tiempo " +  str(h)+":"+str(m)+":"+str(s) + "\n"
                variable= "Nombre "+ nombre + "\n"+"Dificultad " + dificultad+ str(tamano) + "\n" + "Partida " + str(partidaActual) + "\n" + "Primeros " + str(Primer)+ "\n" + "Segundos " + str(segundo)+"\n"+"Terceros " + str(tercero)+ "\n"
                variable1= "Cuartos " + str(cuarto) + "\n" + "Quintos " + str(quinto) + "\n" + "Sextos " + str(sexto) + "\n"+ "Setimos " + str(septimo) + "\n"
                variable2= "Octavos " + str(octavo) + "\n" + "Novenos " + str(noveno) + "\n"
                final= Variable3 + variable + variable1 + variable2
                f.write(final)
            else:
                
                variable= "Nombre "+ nombre + "\n"+"Dificultad " + dificultad+ str(tamano) + "\n" + "Partida " + str(partidaActual) + "\n" + "Primeros " + str(Primer)+ "\n" + "Segundos " + str(segundo)+"\n"+"Terceros " + str(tercero)+ "\n"
                variable1= "Cuartos " + str(cuarto) + "\n" + "Quintos " + str(quinto) + "\n" + "Sextos " + str(sexto) + "\n"+ "Setimos " + str(septimo) + "\n"
                variable2= "Octavos " + str(octavo) + "\n" + "Novenos " + str(noveno) + "\n"
                final= variable + variable1 + variable2
                f.write(final)
            
            
            
            
        f.close
        
    #---------------------------------------------------------------------------------------------------------------------------------------------------
            
    #Validaciones para cuando el jugador termine
    def probarvacias():
        global time,Primer,segundo,tercero,cuarto,quinto,sexto,septimo,octavo,noveno, tamano
        
        if tamano== 3:
            if 0 in Primer[:3]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in segundo[:3]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in tercero[:3]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            else:
                return ("SIGA")
        elif tamano==4:
            if 0 in Primer[:4]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in segundo[:4]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in tercero[:4]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in cuarto[:4]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            else:
                return ("SIGA")
            
        elif tamano==5:
            if 0 in Primer[:5]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in segundo[:5]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in tercero[:5]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in cuarto[:5]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in quinto[:5]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            else:
                return ("SIGA")
            
        elif tamano==6:
            if 0 in Primer[:6]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in segundo[:6]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in tercero[:6]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in cuarto[:6]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in quinto[:6]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in sexto[:6]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            else:
                return ("SIGA")
        elif tamano==7:
            if 0 in Primer[:7]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in segundo[:7]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in tercero[:7]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in cuarto[:7]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in quinto[:7]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in sexto[:7]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in septimo[:7]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            else:
                return ("SIGA")
        elif tamano==8:
            if 0 in Primer[:8]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in segundo[:8]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in tercero[:8]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in cuarto[:8]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in quinto[:8]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in sexto[:8]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in septimo[:8]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in octavo[:8]:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            else:
                return ("SIGA")
        else:
            if 0 in Primer:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in segundo:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in tercero:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in cuarto:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in quinto:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in sexto:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in septimo:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in octavo:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            elif 0 in noveno:
                messagebox.showinfo("Error:", "No pueden haber casillas vacias")
            else:
                return ("SIGA")
            
            
            
        

    def probarfilas(lista):
        
        if lista[0]==lista[1] or lista[0]==lista[2] or lista[0]==lista[3] or lista[0]==lista[4] or lista[0]==lista[5]or lista[0]==lista[6]or lista[0]==lista[7]or lista[0]==lista[8]:
            messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
        elif lista[1]==lista[2] or lista[1]==lista[3] or lista[1]==lista[4] or lista[1]==lista[5]or lista[1]==lista[6]or lista[1]==lista[7]or lista[1]==lista[8]:
            messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
        elif lista[2]==lista[3] or lista[2]==lista[4] or lista[2]==lista[5]or lista[2]==lista[6]or lista[2]==lista[7]or lista[2]==lista[8]:
            messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
        elif lista[3]==lista[4] or lista[3]==lista[5] or lista[3]==lista[6]or lista[3]==lista[7]or lista[3]==lista[8]:
            messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
        elif lista[4]==lista[5] or lista[4]==lista[6] or lista[4]==lista[7]or lista[4]==lista[8]:
            messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
        elif lista[5]==lista[6] or lista[5]==lista[7] or lista[5]==lista[8]:
            messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
        elif lista[6]==lista[7] or lista[6]==lista[8]:
            messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
        elif lista[7]==lista[8]:
            messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
        else:
            return ("SIGA")
    def Hacer_VARIABLES_FILAS():
        global time,Primer,segundo,tercero,cuarto,quinto,sexto,septimo,octavo,noveno,OpcionReloj,iraresta
        if tamano==3:
            variable1= [Primer[0],segundo[0],tercero[0]]
            variable2= [Primer[1],segundo[1],tercero[1]]
            variable3= [Primer[2],segundo[2],tercero[2]]
            if BUSCADOR_NUMEROS_IGUALES(variable1)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable2)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable3)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            else:
                return "SIGA"
                
        elif tamano==4:
            variable1= [Primer[0],segundo[0],tercero[0],cuarto[0]]
            variable2= [Primer[1],segundo[1],tercero[1],cuarto[1]]
            variable3= [Primer[2],segundo[2],tercero[2],cuarto[2]]
            variable4= [Primer[3],segundo[3],tercero[3],cuarto[3]]
            if BUSCADOR_NUMEROS_IGUALES(variable1)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable2)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable3)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable4)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            else:

                return "SIGA"
        elif tamano==5:
            variable1= [Primer[0],segundo[0],tercero[0],cuarto[0],quinto[0]]
            variable2= [Primer[1],segundo[1],tercero[1],cuarto[1],quinto[1]]
            variable3= [Primer[2],segundo[2],tercero[2],cuarto[2],quinto[2]]
            variable4= [Primer[3],segundo[3],tercero[3],cuarto[3],quinto[3]]
            variable5= [Primer[4],segundo[4],tercero[4],cuarto[4],quinto[4]]
            if BUSCADOR_NUMEROS_IGUALES(variable1)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable2)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable3)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable4)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable5)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            else:

                return "SIGA"
        elif tamano==6:
            variable1= [Primer[0],segundo[0],tercero[0],cuarto[0],quinto[0],sexto[0]]
            variable2= [Primer[1],segundo[1],tercero[1],cuarto[1],quinto[1],sexto[1]]
            variable3= [Primer[2],segundo[2],tercero[2],cuarto[2],quinto[2],sexto[2]]
            variable4= [Primer[3],segundo[3],tercero[3],cuarto[3],quinto[3],sexto[3]]
            variable5= [Primer[4],segundo[4],tercero[4],cuarto[4],quinto[4],sexto[4]]
            variable6= [Primer[5],segundo[5],tercero[5],cuarto[5],quinto[5],sexto[5]]
            if BUSCADOR_NUMEROS_IGUALES(variable1)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable2)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable3)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable4)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable5)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable6)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            else:

                return "SIGA"
        elif tamano==7:
            variable1= [Primer[0],segundo[0],tercero[0],cuarto[0],quinto[0],sexto[0],septimo[0]]
            variable2= [Primer[1],segundo[1],tercero[1],cuarto[1],quinto[1],sexto[1],septimo[0]]
            variable3= [Primer[2],segundo[2],tercero[2],cuarto[2],quinto[2],sexto[2],septimo[0]]
            variable4= [Primer[3],segundo[3],tercero[3],cuarto[3],quinto[3],sexto[3],septimo[0]]
            variable5= [Primer[4],segundo[4],tercero[4],cuarto[4],quinto[4],sexto[4],septimo[0]]
            variable6= [Primer[5],segundo[5],tercero[5],cuarto[5],quinto[5],sexto[5],septimo[0]]
            variable7= [Primer[5],segundo[5],tercero[5],cuarto[5],quinto[5],sexto[5],septimo[0]]
            if BUSCADOR_NUMEROS_IGUALES(variable1)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable2)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable3)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable4)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable5)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable6)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable7)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            else:

                return "SIGA"
        elif tamano==8:
            variable1= [Primer[0],segundo[0],tercero[0],cuarto[0],quinto[0],sexto[0],septimo[0],octavo[0]]
            variable2= [Primer[1],segundo[1],tercero[1],cuarto[1],quinto[1],sexto[1],septimo[0],octavo[0]]
            variable3= [Primer[2],segundo[2],tercero[2],cuarto[2],quinto[2],sexto[2],septimo[0],octavo[0]]
            variable4= [Primer[3],segundo[3],tercero[3],cuarto[3],quinto[3],sexto[3],septimo[0],octavo[0]]
            variable5= [Primer[4],segundo[4],tercero[4],cuarto[4],quinto[4],sexto[4],septimo[0],octavo[0]]
            variable6= [Primer[5],segundo[5],tercero[5],cuarto[5],quinto[5],sexto[5],septimo[0],octavo[0]]
            variable7= [Primer[5],segundo[5],tercero[5],cuarto[5],quinto[5],sexto[5],septimo[0],octavo[0]]
            variable8= [Primer[5],segundo[5],tercero[5],cuarto[5],quinto[5],sexto[5],septimo[0],octavo[0]]
            if BUSCADOR_NUMEROS_IGUALES(variable1)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable2)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable3)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable4)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable5)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable6)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable7)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable8)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            else:

                return "SIGA"
        elif tamano==9:
            variable1= [Primer[0],segundo[0],tercero[0],cuarto[0],quinto[0],sexto[0],septimo[0],octavo[0],noveno[0]]
            variable2= [Primer[1],segundo[1],tercero[1],cuarto[1],quinto[1],sexto[1],septimo[0],octavo[0],noveno[0]]
            variable3= [Primer[2],segundo[2],tercero[2],cuarto[2],quinto[2],sexto[2],septimo[0],octavo[0],noveno[0]]
            variable4= [Primer[3],segundo[3],tercero[3],cuarto[3],quinto[3],sexto[3],septimo[0],octavo[0],noveno[0]]
            variable5= [Primer[4],segundo[4],tercero[4],cuarto[4],quinto[4],sexto[4],septimo[0],octavo[0],noveno[0]]
            variable6= [Primer[5],segundo[5],tercero[5],cuarto[5],quinto[5],sexto[5],septimo[0],octavo[0],noveno[0]]
            variable7= [Primer[5],segundo[5],tercero[5],cuarto[5],quinto[5],sexto[5],septimo[0],octavo[0],noveno[0]]
            variable8= [Primer[5],segundo[5],tercero[5],cuarto[5],quinto[5],sexto[5],septimo[0],octavo[0],noveno[0]]
            variable9= [Primer[5],segundo[5],tercero[5],cuarto[5],quinto[5],sexto[5],septimo[0],octavo[0],noveno[0]]
            if BUSCADOR_NUMEROS_IGUALES(variable1)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable2)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable3)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable4)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable5)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable6)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable7)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable8)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            elif BUSCADOR_NUMEROS_IGUALES(variable9)==True:
                messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
            else:

                return "SIGA"

    def BUSCADOR_NUMEROS_IGUALES(lista):
        while lista!=[]:
            n= 1
            while n< len(lista):
                if lista[0]== lista[1]:
                    return True
                else:
                    n= n + 1

            lista=lista[1:]
        return False
            
        

    def validarcasillas():
        global time,Primer,segundo,tercero,cuarto,quinto,sexto,septimo,octavo,noveno,OpcionReloj,iraresta,multiTAMANO,tamano
        if OpcionReloj=="S1":
            if probarvacias()!= "SIGA":
                continuar()

            elif Hacer_VARIABLES_FILAS()!=  "SIGA":
                continuar()


                
            elif comprobadorfinal()=="Correcto":
                if multiTAMANO== "S":
                    
                    tamano= tamano + 1
                    menu.destroy()
                    abrirjuegos()
                    motrar()
                    

                else:
                    escribir()
                    messagebox.showinfo("Felicidades:", "Usted ha ganado este juego")


        elif OpcionReloj=="S2":
            pararcronometro2()
            h= guardador.gethoc()
            m= guardador.getmic()
            s= guardador.getsec()
            d=guardador.getdec()

        
            if probarvacias()!= "SIGA":
                iraresta="SI"
                iniciarcrono2(d,s,m,h)
            elif Hacer_VARIABLES_FILAS()!=  "SIGA":
                iraresta="SI"
                iniciarcrono2(d,s,m,h)
                
            elif comprobadorfinal()=="Correcto":
                if multiTAMANO== "S":
                    
                    tamano= tamano + 1
                    menu.destroy()
                    abrirjuegos()
                    motrar()
                else:
                    iraresta="SI"
                    escribir()
                    messagebox.showinfo("Felicidades:", "Usted ha ganado este juego")
        else:
            if probarvacias()!= "SIGA":
                print("")

            elif Hacer_VARIABLES_FILAS()!=  "SIGA":
                print("")

           
            elif comprobadorfinal()=="Correcto":
                if multiTAMANO== "S":
                    
                    tamano= tamano + 1
                    menu.destroy()
                    abrirjuegos()
                    motrar()
                else:
                    messagebox.showinfo("Felicidades:", "Usted ha ganado este juego")
    #-----------------------------------------------------------------------------------------------------------------------------------
    #Funciones para escribir en cada label
    def B1(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=1

    def B2(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=2
    def B3(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=3
    def B4(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=4
    def B5(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=5
    def B6(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=6
    def B7(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=7
    def B8(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=8
    def B9(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=9
    def B10(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=10
    def B11(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=11
    def B12(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=12
    def B13(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=13
    def B14(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=14
    def B15(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=15
    def B16(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=16
    def B17(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=17
    def B18(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=18
    def B19(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=19
    def B20(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=20
    def B21(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=21
    def B22(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=22
    def B23(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=23
    def B24(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=24
    def B25(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=25
    def B26(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=26
    def B27(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=27
    def B28(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=28
    def B29(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=29
    def B30(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=30
    def B31(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=31
    def B32(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=32
    def B33(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=33
    def B34(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=34
    def B35(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=35
    def B36(event): #Selecciona el tiempo en horas, y con esto podemos darle un valor en horas al pronostico
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=36

    def B37(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=37
    def B38(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=38
    def B39(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=39
    def B40(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=40
    def B41(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=41
    def B42(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=42
    def B43(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=43
    def B44(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=44
    def B45(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=45
    def B46(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=46
    def B47(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=47
    def B48(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=48
    def B49(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=49
    def B50(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=50
    def B51(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=51
    def B52(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=52
    def B53(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=53
    def B54(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=54
    def B55(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=55
    def B56(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=56
    def B57(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=57
    def B58(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=58
    def B59(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=59
    def B60(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=60
    def B61(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=61
    def B62(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=62
    def B63(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=63
    def B64(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=64
    def B65(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=65
    def B66(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=66
    def B67(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=67
    def B68(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=68
    def B69(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=69
    def B70(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=70
    def B71(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=71
    def B72(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=72
    def B73(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=73
    def B74(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=74
    def B75(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=75
    def B76(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=76
    def B77(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=77
    def B78(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=78
    def B79(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=79
    def B80(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=80
    def B81(event): 
        global time, procesodecrono
        if procesodecrono== "N":
            messagebox.showinfo("Error:", "El cronómetro debe estar en funcionamiento")
        else:
            time=81

    #Con esta función escribe lo que el jugador seleccionando en las casillas y lo guarda en las variables que mencionamos al inicio del código 
            
    def valores(numero):
        global jugadas,time,Primer,segundo,tercero,cuarto,quinto,sexto,septimo,octavo,noveno
        if time ==1:
            b1['text']= numero
            Primer[0]=numero
            jugadas.insert(0,(["b1",numero]))
            print(jugadas)
        elif time==2:
            b2['text']= numero
            Primer[1]=numero
            jugadas.insert(0,(["b2",numero]))
            print(jugadas)
        elif time== 3:
            b3['text']= numero
            Primer[2]=numero
            jugadas.insert(0,(["b3",numero]))
            print(jugadas)
        elif time== 4:
            b4['text']= numero
            Primer[3]=numero
            jugadas.insert(0,(["b4",numero]))
            print(jugadas)
        elif time== 5:
            b5['text']= numero
            Primer[4]=numero
            jugadas.insert(0,(["b5",numero]))
            print(jugadas)
        elif time== 6:
            b6['text']= numero
            Primer[5]=numero
            jugadas.insert(0,(["b6",numero]))
            print(jugadas)
        elif time== 7:
            b7['text']= numero
            segundo[0]=numero
            jugadas.insert(0,(["b7",numero]))
            print(jugadas)
        elif time== 8:
            b8['text']= numero
            segundo[1]=numero
            jugadas.insert(0,(["b8",numero]))
            print(jugadas)
        elif time== 9:
            b9['text']= numero
            segundo[2]=numero
            jugadas.insert(0,(["b9",numero]))
            print(jugadas)
        elif time== 10:
            b10['text']= numero
            segundo[3]=numero
            jugadas.insert(0,(["b10",numero]))
            print(jugadas)
        elif time== 11:
            b11['text']= numero
            segundo[4]=numero
            jugadas.insert(0,(["b11",numero]))
            print(jugadas)
        elif time== 12:
            b12['text']= numero
            segundo[5]=numero
            jugadas.insert(0,(["b12",numero]))
            print(jugadas)
        elif time== 13:
            b13['text']= numero
            tercero[0]=numero
            jugadas.insert(0,(["b13",numero]))
            print(jugadas)
        elif time== 14:
            b14['text']= numero
            tercero[1]=numero
            jugadas.insert(0,(["b14",numero]))
            print(jugadas)
        elif time== 15:
            b15['text']= numero
            tercero[2]=numero
            jugadas.insert(0,(["b15",numero]))
            print(jugadas)
        elif time== 16:
            b16['text']= numero
            tercero[3]=numero
            jugadas.insert(0,(["b16",numero]))
            print(jugadas)
        elif time== 17:
            b17['text']= numero
            tercero[4]=numero
            jugadas.insert(0,(["b17",numero]))
            print(jugadas)
        elif time== 18:
            b18['text']= numero
            tercero[5]=numero
            jugadas.insert(0,(["b18",numero]))
        elif time== 19:
            b19['text']= numero
            cuarto[0]=numero
            jugadas.insert(0,(["b19",numero]))
        elif time== 20:
            b20['text']= numero
            cuarto[1]=numero
            jugadas.insert(0,(["b20",numero]))
        elif time== 21:
            b21['text']= numero
            cuarto[2]=numero
            jugadas.insert(0,(["b21",numero]))
        elif time== 22:
            b22['text']= numero
            cuarto[3]=numero
            jugadas.insert(0,(["b22",numero]))
        elif time== 23:
            b23['text']= numero
            cuarto[4]=numero
            jugadas.insert(0,(["b23",numero]))
        elif time== 24:
            b24['text']= numero
            cuarto[5]=numero
            jugadas.insert(0,(["b24",numero]))
        elif time== 25:
            b25['text']= numero
            quinto[0]=numero
            jugadas.insert(0,(["b25",numero]))
        elif time== 26:
            b26['text']= numero
            quinto[1]=numero
            jugadas.insert(0,(["b26",numero]))
        elif time== 27:
            b27['text']= numero
            quinto[2]=numero
            jugadas.insert(0,(["b27",numero]))
        elif time== 28:
            b28['text']= numero
            quinto[3]=numero
            jugadas.insert(0,(["b28",numero]))
        elif time== 29:
            b29['text']= numero
            quinto[4]=numero
            jugadas.insert(0,(["b29",numero]))
        elif time== 30:
            b30['text']= numero
            quinto[5]=numero
            jugadas.insert(0,(["b30",numero]))
        elif time== 31:
            b31['text']= numero
            sexto[0]=numero
            jugadas.insert(0,(["b31",numero]))
        elif time== 32:
            b32['text']= numero
            sexto[1]=numero
            jugadas.insert(0,(["b32",numero]))
        elif time== 33:
            b33['text']= numero
            sexto[2]=numero
            jugadas.insert(0,(["b33",numero]))
        elif time== 34:
            b34['text']= numero
            sexto[3]=numero
            jugadas.insert(0,(["b34",numero]))
        elif time== 35:
            b35['text']= numero
            sexto[4]=numero
            jugadas.insert(0,(["b35",numero]))
        elif time== 36:
            b36['text']= numero
            sexto[5]=numero
            jugadas.insert(0,(["b36",numero]))
        elif time== 37:
            b37['text']= numero
            Primer[6]= numero
            jugadas.insert(0,(["b37",numero]))
        elif time== 38:
            b38['text']= numero
            Primer[7]= numero
            jugadas.insert(0,(["b38",numero]))
        elif time== 39:
            b39['text']= numero
            Primer[8]= numero
            jugadas.insert(0,(["b39",numero]))
        elif time== 40:
            b40['text']= numero
            segundo[6]= numero
            jugadas.insert(0,(["b40",numero]))
        elif time== 41:
            b41['text']= numero
            segundo[7]= numero
            jugadas.insert(0,(["b41",numero]))
        elif time== 42:
            b42['text']= numero
            segundo[8]= numero
            jugadas.insert(0,(["b42",numero]))
        elif time== 43:
            b43['text']= numero
            tercero[6]=numero
            jugadas.insert(0,(["b43",numero]))
        elif time== 44:
            b44['text']= numero
            tercero[7]=numero
            jugadas.insert(0,(["b44",numero]))
        elif time== 45:
            b45['text']= numero
            tercero[8]=numero
            jugadas.insert(0,(["b45",numero]))
        elif time== 46:
            b46['text']= numero
            cuarto[6]=numero
            jugadas.insert(0,(["b46",numero]))
        elif time== 47:
            b47['text']= numero
            cuarto[7]=numero
            jugadas.insert(0,(["b47",numero]))
        elif time== 48:
            b48['text']= numero
            cuarto[8]=numero
            jugadas.insert(0,(["b48",numero]))
        elif time== 49:
            b49['text']= numero
            jugadas.insert(0,(["b49",numero]))
            quinto[6]=numero
        elif time== 50:
            b50['text']= numero
            quinto[7]=numero
            jugadas.insert(0,(["b50",numero]))
        elif time== 51:
            b51['text']= numero
            quinto[8]=numero
            jugadas.insert(0,(["b51",numero]))
        elif time== 52:
            b52['text']= numero
            sexto[6]=numero
            jugadas.insert(0,(["b52",numero]))
        elif time== 53:
            b53['text']= numero
            sexto[7]=numero
            jugadas.insert(0,(["b53",numero]))
        elif time== 54:
            b54['text']= numero
            sexto[7]=numero
            jugadas.insert(0,(["b54",numero]))

        elif time== 55:
            b55['text']= numero
            septimo[0]=numero
            jugadas.insert(0,(["b55",numero]))
        elif time== 56:
            b56['text']= numero
            septimo[1]=numero
            jugadas.insert(0,(["b56",numero]))
        elif time== 57:
            b57['text']= numero
            septimo[2]=numero
            jugadas.insert(0,(["b57",numero]))
        elif time== 58:
            b58['text']= numero
            septimo[3]=numero
            jugadas.insert(0,(["b58",numero]))
        elif time== 59:
            b59['text']= numero
            septimo[4]=numero
            jugadas.insert(0,(["b59",numero]))
        elif time== 60:
            b60['text']= numero
            septimo[5]=numero
            jugadas.insert(0,(["b60",numero]))
        elif time== 61:
            b61['text']= numero
            septimo[6]=numero
            jugadas.insert(0,(["b61",numero]))
        elif time== 62:
            b62['text']= numero
            septimo[7]=numero
            jugadas.insert(0,(["b62",numero]))
        elif time== 63:
            b63['text']= numero
            septimo[8]=numero
            jugadas.insert(0,(["b63",numero]))
            
        elif time== 64:
            b64['text']= numero
            octavo[0]=numero
            jugadas.insert(0,(["b64",numero]))
        elif time== 65:
            b65['text']= numero
            octavo[1]=numero
            jugadas.insert(0,(["b65",numero]))
        elif time== 66:
            b66['text']= numero
            octavo[2]=numero
            jugadas.insert(0,(["b66",numero]))
        elif time== 67:
            b67['text']= numero
            octavo[3]=numero
            jugadas.insert(0,(["b67",numero]))
        elif time== 68:
            b68['text']= numero
            octavo[4]=numero
            jugadas.insert(0,(["b68",numero]))
        elif time== 69:
            b69['text']= numero
            octavo[5]=numero
            jugadas.insert(0,(["b69",numero]))
        elif time== 70:
            b70['text']= numero
            octavo[6]=numero
            jugadas.insert(0,(["b70",numero]))
        elif time== 71:
            b71['text']= numero
            octavo[7]=numero
            jugadas.insert(0,(["b71",numero]))
        elif time== 72:
            b72['text']= numero
            octavo[8]=numero
            jugadas.insert(0,(["b72",numero]))
            
        elif time== 73:
            b73['text']= numero
            noveno[0]=numero
            jugadas.insert(0,(["b73",numero]))
        elif time== 74:
            b74['text']= numero
            noveno[1]=numero
            jugadas.insert(0,(["b74",numero]))
        elif time== 75:
            b75['text']= numero
            noveno[2]=numero
            jugadas.insert(0,(["b75",numero]))
        elif time== 76:
            b76['text']= numero
            noveno[3]=numero
            jugadas.insert(0,(["b76",numero]))
        elif time== 77:
            b77['text']= numero
            noveno[4]=numero
            jugadas.insert(0,(["b77",numero]))
        elif time== 78:
            b78['text']= numero
            noveno[5]=numero
            jugadas.insert(0,(["b78",numero]))
        elif time== 79:
            b79['text']= numero
            noveno[6]=numero
            jugadas.insert(0,(["b79",numero]))
        elif time== 80:
            b80['text']= numero
            noveno[7]=numero
            jugadas.insert(0,(["b80",numero]))
        elif time== 81:
            b81['text']= numero
            noveno[8]=numero
            jugadas.insert(0,(["b81",numero]))
            
    def deshacerf():
        global jugadas
        global rehacer
        if jugadas==[]:
            messagebox.showinfo("Error","No hay jugadas previas")
        elif jugadas[0][0]=="b1":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b1":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b1['text']=num
                    print(num)
                    return()
            b1['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
            
        elif jugadas[0][0]=="b2":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b2":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b2['text']=num
                    print(num)
                    return()
            b2['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b3":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b3":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b3['text']=num
                    print(num)
                    return()
            b3['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
            
        elif jugadas[0][0]=="b4":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b4":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b4['text']=num
                    print(num)
                    return()
            b4['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b5":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b5":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b5['text']=num
                    print(num)
                    return()
            b5['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b6":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b6":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b6['text']=num
                    print(num)
                    return()
            b6['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b7":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b7":
                    num=jugadas[vara][1]
                    rrehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b7['text']=num
                    print(num)
                    return()
            b7['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b8":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b8":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b8['text']=num
                    print(num)
                    return()
            b8['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b9":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b9":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b9['text']=num
                    print(num)
                    return()
            b9['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b10":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b10":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b10['text']=num
                    print(num)
                    return()
            b10['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b11":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b11":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b11['text']=num
                    print(num)
                    return()
            b11['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b12":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b12":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b12['text']=num
                    print(num)
                    return()
            b12['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b13":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b13":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b13['text']=num
                    print(num)
                    return()
            b13['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b14":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b14":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b14['text']=num
                    print(num)
                    return()
            b14['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b15":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b15":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b15['text']=num
                    print(num)
                    return()
            b15['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b16":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b16":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b16['text']=num
                    print(num)
                    return()
            b16['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b17":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b17":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b17['text']=num
                    print(num)
                    return()
            b17['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b18":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b18":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b18['text']=num
                    print(num)
                    return()
            b18['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b19":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b19":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b19['text']=num
                    print(num)
                    return()
            b19['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b20":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b20":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b20['text']=num
                    print(num)
                    return()
            b20['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b21":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b21":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b21['text']=num
                    print(num)
                    return()
            b21['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b22":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b22":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b22['text']=num
                    print(num)
                    return()
            b22['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b23":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b23":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b23['text']=num
                    print(num)
                    return()
            b23['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b24":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b24":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b24['text']=num
                    print(num)
                    return()
            b24['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b25":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b25":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b25['text']=num
                    print(num)
                    return()
            b25['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b26":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b26":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b26['text']=num
                    print(num)
                    return()
            b26['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b27":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b27":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b27['text']=num
                    print(num)
                    return()
            b27['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b28":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b28":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b28['text']=num
                    print(num)
                    return()
            b28['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b29":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b29":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b29['text']=num
                    print(num)
                    return()
            b29['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b30":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b30":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b30['text']=num
                    print(num)
                    return()
            b30['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b31":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b31":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b31['text']=num
                    print(num)
                    return()
            b31['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b32":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b32":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b32['text']=num
                    print(num)
                    return()
            b32['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b33":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b33":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b33['text']=num
                    print(num)
                    return()
            b33['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b34":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b34":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b34['text']=num
                    print(num)
                    return()
            b34['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b35":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b35":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b35['text']=num
                    print(num)
                    return()
            b35['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b36":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b36":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b36['text']=num
                    print(num)
                    return()
            b36['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b37":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b37":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b37['text']=num
                    print(num)
                    return()
            b37['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b38":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b38":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b38['text']=num
                    print(num)
                    return()
            b38['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b39":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b39":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b39['text']=num
                    print(num)
                    return()
            b39['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b40":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b40":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b40['text']=num
                    print(num)
                    return()
            b40['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b41":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b41":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b41['text']=num
                    print(num)
                    return()
            b41['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b42":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b42":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b42['text']=num
                    print(num)
                    return()
            b42['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b43":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b43":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b43['text']=num
                    print(num)
                    return()
            b43['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b44":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b44":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b44['text']=num
                    print(num)
                    return()
            b44['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b45":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b45":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b45['text']=num
                    print(num)
                    return()
            b45['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b46":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b46":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b46['text']=num
                    print(num)
                    return()
            b46['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b47":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b47":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b47['text']=num
                    print(num)
                    return()
            b47['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b48":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b48":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b48['text']=num
                    print(num)
                    return()
            b48['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b49":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b49":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b49['text']=num
                    print(num)
                    return()
            b49['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b50":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b50":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b50['text']=num
                    print(num)
                    return()
            b50['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b51":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b51":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b51['text']=num
                    print(num)
                    return()
            b51['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b52":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b52":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b52['text']=num
                    print(num)
                    return()
            b52['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b53":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b53":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b53['text']=num
                    print(num)
                    return()
            b53['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b54":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b54":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b54['text']=num
                    print(num)
                    return()
            b54['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b55":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b55":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b55['text']=num
                    print(num)
                    return()
            b55['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b56":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b56":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b56['text']=num
                    print(num)
                    return()
            b56['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b57":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b57":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b57['text']=num
                    print(num)
                    return()
            b57['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b58":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b58":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b58['text']=num
                    print(num)
                    return()
            b58['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b59":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b59":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b59['text']=num
                    print(num)
                    return()
            b59['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b60":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b60":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b60['text']=num
                    print(num)
                    return()
            b60['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b61":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b61":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b61['text']=num
                    print(num)
                    return()
            b61['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b62":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b62":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b62['text']=num
                    print(num)
                    return()
            b62['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b63":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b63":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b63['text']=num
                    print(num)
                    return()
            b63['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b64":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b64":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b64['text']=num
                    print(num)
                    return()
            b64['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b65":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b65":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b65['text']=num
                    print(num)
                    return()
            b65['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b66":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b66":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b66['text']=num
                    print(num)
                    return()
            b66['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b67":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b67":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b67['text']=num
                    print(num)
                    return()
            b67['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b68":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b68":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b68['text']=num
                    print(num)
                    return()
            b68['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b69":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b69":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b69['text']=num
                    print(num)
                    return()
            b69['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b70":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b70":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b70['text']=num
                    print(num)
                    return()
            b70['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b71":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b71":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b71['text']=num
                    print(num)
                    return()
            b71['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b72":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b72":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b72['text']=num
                    print(num)
                    return()
            b72['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b73":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b73":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b73['text']=num
                    print(num)
                    return()
            b73['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b74":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b74":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b74['text']=num
                    print(num)
                    return()
            b74['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b75":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b75":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b75['text']=num
                    print(num)
                    return()
            b75['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b76":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b76":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b76['text']=num
                    print(num)
                    return()
            b76['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b77":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b77":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b77['text']=num
                    print(num)
                    return()
            b77['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b78":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b78":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b78['text']=num
                    print(num)
                    return()
            b78['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b79":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b79":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b79['text']=num
                    print(num)
                    return()
            b79['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b80":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b80":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b80['text']=num
                    print(num)
                    return()
            b80['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
        elif jugadas[0][0]=="b81":
            for vara in range(1,len(jugadas[1:])+1):
                if jugadas[vara][0]=="b81":
                    num=jugadas[vara][1]
                    rehacer.insert(0,(jugadas[0]))
                    jugadas=(jugadas[1:])
                    b81['text']=num
                    print(num)
                    return()
            b81['text']=0
            rehacer.insert(0,(jugadas[0]))
            jugadas=jugadas[1:]
            
    def rehacerf():
        global jugadas
        global rehacer
        print(rehacer)
        if rehacer==[]:
            messagebox.showinfo("Error","No hay jugadas para rehacer")
        elif rehacer[0][0]=="b1":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b1['text']=num
        elif rehacer[0][0]=="b2":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b2['text']=num
        elif rehacer[0][0]=="b3":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b3['text']=num
        elif rehacer[0][0]=="b4":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b4['text']=num
        elif rehacer[0][0]=="b5":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b5['text']=num
        elif rehacer[0][0]=="b6":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b6['text']=num
        elif rehacer[0][0]=="b7":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b7['text']=num
        elif rehacer[0][0]=="b8":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b8['text']=num
        elif rehacer[0][0]=="b9":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b9['text']=num
        elif rehacer[0][0]=="b10":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b10['text']=num
        elif rehacer[0][0]=="b11":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b11['text']=num
        elif rehacer[0][0]=="b12":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b12['text']=num
        elif rehacer[0][0]=="b13":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b13['text']=num
        elif rehacer[0][0]=="b14":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b14['text']=num
        elif rehacer[0][0]=="b15":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b15['text']=num
        elif rehacer[0][0]=="b16":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b16['text']=num
        elif rehacer[0][0]=="b17":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b17['text']=num
        elif rehacer[0][0]=="b18":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b18['text']=num
        elif rehacer[0][0]=="b19":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b19['text']=num
        elif rehacer[0][0]=="b20":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b20['text']=num
        elif rehacer[0][0]=="b21":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b21['text']=num
        elif rehacer[0][0]=="b22":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b22['text']=num
        elif rehacer[0][0]=="b23":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b23['text']=num
        elif rehacer[0][0]=="b24":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b24['text']=num
        elif rehacer[0][0]=="b25":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b25['text']=num
        elif rehacer[0][0]=="b26":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b26['text']=num
        elif rehacer[0][0]=="b27":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b27['text']=num
        elif rehacer[0][0]=="b28":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b28['text']=num
        elif rehacer[0][0]=="b29":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b29['text']=num
        elif rehacer[0][0]=="b30":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b30['text']=num
        elif rehacer[0][0]=="b31":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b31['text']=num
        elif rehacer[0][0]=="b32":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b32['text']=num
        elif rehacer[0][0]=="b33":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b33['text']=num
        elif rehacer[0][0]=="b34":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b34['text']=num
        elif rehacer[0][0]=="b35":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b35['text']=num
        elif rehacer[0][0]=="b36":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b36['text']=num
        elif rehacer[0][0]=="b37":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b37['text']=num
        elif rehacer[0][0]=="b38":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b38['text']=num
        elif rehacer[0][0]=="b39":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b39['text']=num
        elif rehacer[0][0]=="b40":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b40['text']=num
        elif rehacer[0][0]=="b41":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b41['text']=num
        elif rehacer[0][0]=="b42":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b42['text']=num
        elif rehacer[0][0]=="b43":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b43['text']=num
        elif rehacer[0][0]=="b44":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b44['text']=num
        elif rehacer[0][0]=="b45":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b45['text']=num
        elif rehacer[0][0]=="b46":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b46['text']=num
        elif rehacer[0][0]=="b47":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b47['text']=num
        elif rehacer[0][0]=="b48":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b48['text']=num
        elif rehacer[0][0]=="b49":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b49['text']=num
        elif rehacer[0][0]=="b50":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b50['text']=num
        elif rehacer[0][0]=="b51":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b51['text']=num
        elif rehacer[0][0]=="b52":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b52['text']=num
        elif rehacer[0][0]=="b53":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b53['text']=num
        elif rehacer[0][0]=="b54":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b54['text']=num
        elif rehacer[0][0]=="b55":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b55['text']=num
        elif rehacer[0][0]=="b56":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b56['text']=num
        elif rehacer[0][0]=="b57":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b57['text']=num
        elif rehacer[0][0]=="b58":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b58['text']=num
        elif rehacer[0][0]=="b59":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b59['text']=num
        elif rehacer[0][0]=="b60":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b60['text']=num
        elif rehacer[0][0]=="b61":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b61['text']=num
        elif rehacer[0][0]=="b62":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b62['text']=num
        elif rehacer[0][0]=="b63":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b63['text']=num
        elif rehacer[0][0]=="b64":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b64['text']=num
        elif rehacer[0][0]=="b65":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b65['text']=num
        elif rehacer[0][0]=="b66":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b66['text']=num
        elif rehacer[0][0]=="b67":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b67['text']=num
        elif rehacer[0][0]=="b68":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b68['text']=num
        elif rehacer[0][0]=="b69":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b69['text']=num
        elif rehacer[0][0]=="b70":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b70['text']=num
        elif rehacer[0][0]=="b71":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b71['text']=num
        elif rehacer[0][0]=="b72":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b72['text']=num
        elif rehacer[0][0]=="b73":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b73['text']=num
        elif rehacer[0][0]=="b74":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b74['text']=num
        elif rehacer[0][0]=="b75":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b75['text']=num
        elif rehacer[0][0]=="b76":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b76['text']=num
        elif rehacer[0][0]=="b77":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b77['text']=num
        elif rehacer[0][0]=="b78":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b78['text']=num
        elif rehacer[0][0]=="b79":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b79['text']=num
        elif rehacer[0][0]=="b80":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b80['text']=num
        elif rehacer[0][0]=="b81":
            num=rehacer[0][1]
            jugadas.insert(1,(rehacer[0]))
            rehacer=rehacer[1:]
            b81['text']=num

    

    #Inician a aparacer los labels
    if tamano>=3:
        uno=Button(menu,text=1,command=lambda:valores(1),bg="lightgreen",font=("Helvetica",24))
        uno.place(x=750,y=50)       

        dos=Button(menu,text=2,command=lambda:valores(2),bg="lightgreen",font=("Helvetica",24))
        dos.place(x=750,y=105)

        tres=Button(menu,text=3,command=lambda:valores(3),bg="lightgreen",font=("Helvetica",24))
        tres.place(x=750,y=180)

        

        b1=Label(menu,height=3,width=7,relief="solid",activebackground="SteelBlue1",bg=A1)
        b1.bind("<1>",B1)
        b1.place(x=200,y=110)
        b2=Label(menu,height=3,width=7,relief="solid",activebackground="SteelBlue1",bg=A2)
        b2.bind("<1>",B2)
        b2.place(x= 255 ,y= 110 )
        b3=Label(menu,height=3,width=7,relief="solid",activebackground="SteelBlue1",bg=A3)
        b3.bind("<1>",B3)
        b3.place(x= 310 ,y= 110 )

        b7=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A7)
        b7.bind("<1>",B7)
        b7.place(x=200,y=161)

        b8=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A8)
        b8.bind("<1>",B8)
        b8.place(x=255,y=161)
        b9=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A9)
        b9.bind("<1>",B9)
        b9.place(x=310,y=161)

        b13=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A13)
        b13.bind("<1>",B13)
        b13.place(x=200,y=212)
        
        b14=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A14)
        b14.bind("<1>",B14)
        b14.place(x=255,y=212)
        b15=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A15)
        b15.bind("<1>",B15)
        b15.place(x=310,y=212)
    if tamano>=4:
        cuatro=Button(menu,text=4,command=lambda:valores(4),bg="lightgreen",font=("Helvetica",24))
        cuatro.place(x=750,y=240)

        
        b4=Label(menu,height=3,width=7,relief="solid",activebackground="SteelBlue1",bg=A4)
        b4.bind("<1>",B4)
        b4.place(x= 365 ,y= 110 )
        b10=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A10)
        b10.bind("<1>",B10)
        b10.place(x=365,y=161)
        b16=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A16)
        b16.bind("<1>",B16)
        b16.place(x=365,y=212)
        b19=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A19)
        b19.bind("<1>",B19)
        b19.place(x=200,y=263)

        b20=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A20)
        b20.bind("<1>",B20)
        b20.place(x=255,y=263)
        b21=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A21)
        b21.bind("<1>",B21)
        b21.place(x=310,y=263)
        b22=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A22)
        b22.bind("<1>",B22)
        b22.place(x=365,y=263)

    if tamano >=5:
        cinco=Button(menu,text=5,command=lambda:valores(5),bg="lightgreen",font=("Helvetica",24))
        cinco.place(x=750,y=310)

        
        b5=Label(menu,height=3,width=7,relief="solid",activebackground="SteelBlue1",bg=A5)
        b5.bind("<1>",B5)
        b5.place(x= 420 ,y= 110 )
        b11=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A11)
        b11.bind("<1>",B11)
        b11.place(x=420,y=161)
        b17=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A17)
        b17.bind("<1>",B17)
        b17.place(x=420,y=212)
        b23=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A23)
        b23.bind("<1>",B23)
        b23.place(x=420,y=263)
        b25=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A25)
        b25.bind("<1>",B25)
        b25.place(x=200,y=314)

        b26=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A26)
        b26.bind("<1>",B26)
        b26.place(x=255,y=314)
        b27=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A27)
        b27.bind("<1>",B27)
        b27.place(x=310,y=314)
        b28=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A28)
        b28.bind("<1>",B28)
        b28.place(x=365,y=314)
        b29=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A29)
        b29.bind("<1>",B29)
        b29.place(x=420,y=314)
    if tamano >=6:
        
        seis=Button(menu,text=6,command=lambda:valores(6),bg="lightgreen",font=("Helvetica",24))
        seis.place(x=750,y=375)
        b6=Label(menu,height=3,width=7,relief="solid",activebackground="SteelBlue1",bg=A6)
        b6.bind("<1>",B6)
        b6.place(x= 475 ,y= 110 )
        b12=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A12)
        b12.bind("<1>",B12)
        b12.place(x=475,y=161)
        b18=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A18)
        b18.bind("<1>",B18)
        b18.place(x=475,y=212)
        b24=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A24)
        b24.bind("<1>",B24)
        b24.place(x=475,y=263)
        b30=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A30)
        b30.bind("<1>",B30)
        b30.place(x=475,y=314)
        b31=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A31)
        b31.bind("<1>",B31)
        b31.place(x=200,y=365)
        b32=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A32)
        b32.bind("<1>",B32)
        b32.place(x=255,y=365)
        b33=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A33)
        b33.bind("<1>",B33)
        b33.place(x=310,y=365)
        b34=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A34)
        b34.bind("<1>",B34)
        b34.place(x=365,y=365)
        b35=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A35)
        b35.bind("<1>",B35)
        b35.place(x=420,y=365)
        b36=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A36)
        b36.bind("<1>",B36)
        b36.place(x=475,y=365)
    if tamano>=7:
        siete=Button(menu,text=7,command=lambda:valores(7),bg="lightgreen",font=("Helvetica",24))
        siete.place(x=750,y=430)
        b37=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A37)
        b37.bind("<1>",B37)
        b37.place(x=530,y=110)
        b38=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A40)
        b38.bind("<1>",B38)
        b38.place(x=530,y=161)
        b39=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A43)
        b39.bind("<1>",B39)
        b39.place(x=530,y=212)
        b40=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A46)
        b40.bind("<1>",B40)
        b40.place(x=530,y=263)
        b41=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A49)
        b41.bind("<1>",B41)
        b41.place(x=530,y=314)
        b42=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A52)
        b42.bind("<1>",B42)
        b42.place(x=530,y=365)

        b43=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A55)
        b43.bind("<1>",B43)
        b43.place(x=200,y=416)
        b44=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A56)
        b44.bind("<1>",B44)
        b44.place(x=255,y=416)
        b45=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A57)
        b45.bind("<1>",B45)
        b45.place(x=310,y=416)
        b46=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A58)
        b46.bind("<1>",B46)
        b46.place(x=365,y=416)
        b47=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A59)
        b47.bind("<1>",B47)
        b47.place(x=420,y=416)
        b48=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A60)
        b48.bind("<1>",B48)
        b48.place(x=475,y=416)
        b49=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A61)
        b49.bind("<1>",B49)
        b49.place(x=530,y=416)
    if tamano>=8:
        ocho=Button(menu,text=8,command=lambda:valores(8),bg="lightgreen",font=("Helvetica",24))
        ocho.place(x=750,y=485)
        b50=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A38)
        b50.bind("<1>",B50)
        b50.place(x=585,y=110)
        b51=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A41)
        b51.bind("<1>",B51)
        b51.place(x=585,y=161)
        b52=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A44)
        b52.bind("<1>",B52)
        b52.place(x=585,y=212)
        b53=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A47)
        b53.bind("<1>",B53)
        b53.place(x=585,y=263)
        b54=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A50)
        b54.bind("<1>",B54)
        b54.place(x=585,y=314)
        b55=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A53)
        b55.bind("<1>",B55)
        b55.place(x=585,y=365)
        b56=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A62)
        b56.bind("<1>",B56)
        b56.place(x=585,y=416)

        #ultima fila
        
        b57=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A64)
        b57.bind("<1>",B57)
        b57.place(x=200,y=467)
        b58=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A65)
        b58.bind("<1>",B58)
        b58.place(x=255,y=467)
        b59=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A66)
        b59.bind("<1>",B59)
        b59.place(x=310,y=467)
        b60=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A67)
        b60.bind("<1>",B60)
        b60.place(x=365,y=467)
        b61=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A68)
        b61.bind("<1>",B61)
        b61.place(x=420,y=467)
        b62=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A69)
        b62.bind("<1>",B62)
        b62.place(x=475,y=467)
        b63=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A70)
        b63.bind("<1>",B63)
        b63.place(x=530,y=467)
        b64=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A71)
        b64.bind("<1>",B64)
        b64.place(x=585,y=467)

    if tamano>=9:
        nueve=Button(menu,text=9,command=lambda:valores(9),bg="lightgreen",font=("Helvetica",24))
        nueve.place(x=750,y=540)

        b65=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A39)
        b65.bind("<1>",B65)
        b65.place(x=640,y=110)
        b66=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A42)
        b66.bind("<1>",B66)
        b66.place(x=640,y=161)
        b67=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A45)
        b67.bind("<1>",B67)
        b67.place(x=640,y=212)
        b68=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A48)
        b68.bind("<1>",B68)
        b68.place(x=640,y=263)
        b69=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A51)
        b69.bind("<1>",B69)
        b69.place(x=640,y=314)
        b70=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A54)
        b70.bind("<1>",B70)
        b70.place(x=640,y=365)
        b71=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A63)
        b71.bind("<1>",B71)
        b71.place(x=640,y=416)
        b72=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A72)
        b72.bind("<1>",B72)
        b72.place(x=640,y=467)

        #ultima fila

        b73=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A73)
        b73.bind("<1>",B73)
        b73.place(x=200,y=518)
        b74=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A74)
        b74.bind("<1>",B74)
        b74.place(x=255,y=518)
        b75=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A75)
        b75.bind("<1>",B75)
        b75.place(x=310,y=518)
        b76=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A76)
        b76.bind("<1>",B76)
        b76.place(x=365,y=518)
        b77=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A77)
        b77.bind("<1>",B77)
        b77.place(x=420,y=518)
        b78=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A78)
        b78.bind("<1>",B78)
        b78.place(x=475,y=518)
        b79=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A79)
        b79.bind("<1>",B79)
        b79.place(x=530,y=518)
        b80=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A80)
        b80.bind("<1>",B80)
        b80.place(x=585,y=518) 
        b81=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg=A81)
        b81.bind("<1>",B81)
        b81.place(x=640,y=518)

    validar=Button(menu, text="Validar Juego", font=("Arial 14"),bg="green",command=validarcasillas)
    validar.place(x=1,y=650)
    nuevo=Button(menu,text="Nuevo Juego", font=("Arial 14"),bg="SteelBlue1", command=partinaAiniciar)
    nuevo.place(x=150,y=650)
    restart=Button(menu, text="Reiniciar Juego", font=("Arial 14"),bg="orange",command=reiniciajuego)
    restart.place(x=300,y=650)
    terminar=Button(menu, text="Terminar Juego", font=("Arial 14"),bg="light coral",command=terminarya)
    terminar.place(x=450,y=650)
    terminar=Button(menu, text="Guardar Partida", font=("Arial 14"),bg="light coral",command=Guardar_Partida)
    terminar.place(x=600,y=650)
    deshacer=Button(menu,text="Deshacer jugada", font="Arial 14",bg="light coral",command=lambda:deshacerf())
    deshacer.place(x=750,y=650)
    rehacer=Button(menu,text="Rehacer jugada", font="Arial 14",bg="light coral", command=lambda:rehacerf())
    rehacer.place(x=900,y=650)
    nombred=Label(menu,text="Nombre del Jugador:",font="Arial 14")
    nombred.place(x=1,y=620)
    global nombre
    nombreya=Label(menu,text=nombre,font="Arial 14")
    nombreya.place(x=180,y=620)    
    mainloop()

#Primera ventana donde inica despue´s se ejecutar el botón incio de la primera parte
def menu():
    global defaultbg,Laf1,Laf2,Laf3,Laf4,Laf5,Laf6,Laf7,Laf8,Laf9,Laf10,Laf11,Laf12,Laf13,Laf14,Laf15,Laf16,Laf17,Laf18,Laf19,Laf20,Laf21,Laf22,Laf23,Laf24,Laf25,Laf26,Laf27,Laf28,Laf29,Laf30,Laf31,Laf32,Laf33,Laf34,Laf35,Laf36
    menu= Tk()
    menu.title("KenKen juego")
    menu.geometry("1200x850")
    menu.tit=Label(menu,text="KenKen")
    menu.tit.config(font=("serif 34 bold italic"),fg="green")
    menu.tit.place(x=350,y=20)
    defaultbg= menu.cget('bg')

    Laf1= defaultbg
    Laf2= defaultbg
    Laf3= defaultbg
    Laf4= defaultbg
    Laf5= defaultbg
    Laf6= defaultbg
    Laf7= defaultbg
    Laf8= defaultbg
    Laf9= defaultbg
    Laf10= defaultbg
    Laf11= defaultbg
    Laf12= defaultbg
    Laf13= defaultbg
    Laf14= defaultbg
    Laf15= defaultbg
    Laf16= defaultbg
    Laf17= defaultbg
    Laf18= defaultbg
    Laf19= defaultbg
    Laf20= defaultbg
    Laf21= defaultbg
    Laf22= defaultbg
    Laf23= defaultbg
    Laf24= defaultbg
    Laf25= defaultbg
    Laf26= defaultbg
    Laf27= defaultbg
    Laf28= defaultbg
    Laf29= defaultbg
    Laf30= defaultbg
    Laf31= defaultbg
    Laf32= defaultbg
    Laf33= defaultbg
    Laf34= defaultbg
    Laf35= defaultbg
    Laf36= defaultbg

    def partinaAiniciar():
        print("partidaA")
        global nombre
        if nombre == "N":
            messagebox.showinfo("Aviso importante","Primero debe indicar un nombre de jugador")
        else:
            print("iniciar")
            menu.destroy()
            abrirjuegos()
            motrar()

    def salir1():
        menu.destroy()
        inicioD()
    def avisos():
        messagebox.showinfo("Error","Primero debe iniciar la partida")
    #Funcion de leer el top de los jugadores

    def leer():
        f = open("kenken_jugadores.dat","r")
        numero_partida= {}
        numero_partidaI= {}
        numero_partidaD= {}
        cantidadF=1
        cantidadI=1
        cantidadD=1
        
        while True:
            l = f.readline()
            if l=="": break  
            
            n = l[0] 
            d = (l[2:-1]) 
            if l[0]== "F":
                numero_partida[cantidadF]= l
                cantidadF= cantidadF + 1

            elif l[0]=="I":
                 
                numero_partidaI [cantidadI]= l
                cantidadI= cantidadI + 1
            else:
                numero_partidaD[cantidadD]=l
                cantidadD= cantidadD + 1
        orden= ["Dificultad             Nombre             Tiempo" ]

        f.close()
        
        for h in numero_partida:
            orden= orden + [numero_partida[h] ]
        for m in numero_partidaI:
            orden=orden + [numero_partidaI[m]]
        for l in numero_partidaD:
            orden= orden+[numero_partidaD[l]]

        k="\n"
        k= k.join(orden)
        messagebox.showinfo("Error:", k)

    def funcionnombre():
        global nombre
        h= lpppp.get()
        if len(h)>=3:
            nombre= lpppp.get()
            
        else:
            messagebox.showinfo("Error:", "Introducir un nombre mayor o igual a 3 caractéres")
        


    #Funciones de los bonotes iniciales
    iniciar=Button(menu,command=lambda:partinaAiniciar(), text="Iniciar Juego", font=("Arial 18"),bg="red")
    iniciar.place(x=70,y=450)
    validar=Button(menu, text="Validar Juego", font=("Arial 18"),bg="green",command=avisos)
    validar.place(x=230,y=450)
    nuevo=Button(menu, text="Nuevo Juego", font=("Arial 18"),bg="SteelBlue1",command=avisos)
    nuevo.place(x=400,y=450)
    restart=Button(menu, text="Reiniciar Juego", font=("Arial 18"),bg="orange",command=avisos)
    restart.place(x=565,y=450)
    terminar=Button(menu, text="Volver al menu", font=("Arial 18"),bg="light coral",command=salir1)
    terminar.place(x=300,y=525)
    top=Button(menu, text="Top 10", font=("Arial 18"),bg="gold",command=leer)
    top.place(x=700,y=575)

    nombre=Label(menu,text="Nombre del Jugador:",font="Arial 14")
    nombre.place(x=30,y=545)
    lpppp = StringVar()
    nombreingres=Entry(menu,width=35,textvariable=lpppp)
    nombreingres.place(x=30,y=600)

    guardarnombre=Button(menu,text="Guardar",command=lambda:funcionnombre())
    guardarnombre.place(x=250,y=600)
        
#Ventana de configuracion del juego
def config():
      
    opciones= Tk()
    opciones.title("Configuracion de Juego")
    opciones.geometry("300x600")

    def salir():
        opciones.destroy()
        menu()

    def listo():
        global dificultad, OpcionReloj, OpcionSonido, tamano, labels,multiTAMANO
        if tam.get()==3:
            tamano=3
            labels= []
        if tam.get()==4:
            tamano=4
            labels= []
        if tam.get()==5:
            tamano=5
            labels= []
        if tam.get()==6:
            tamano=6
            labels= []
        if tam.get()==7:
            tamano=7
            labels= []
        if tam.get()==8:
            tamano=8
            labels= []
        if tam.get()==9:
            tamano=9
            labels= []
        if tam.get()==10:
            labels= []
            tamano= 3
            multiTAMANO= "S"
            
            
        if d.get()==1:
            dificultad= "F"
        if d.get()== 2:
            dificultad= "I"
        if d.get()==3:
            dificultad= "D"

        if timer.get()==1:
            OpcionReloj="S1"
        if timer.get()==0:
            OpcionReloj="N"
        if timer.get()==2:
            OpcionReloj="S2"
            opciones.destroy()
            ventana_pronosticar()
    d = IntVar()
    timer=IntVar()
    sonido=IntVar()
    tam= IntVar()
    r1=Radiobutton(opciones, text="facil", font="Arial 12", value=1, variable=d)
    r2= Radiobutton(opciones,text="intermedio",font="Arial 12", value=2, variable=d)
    r3=Radiobutton(opciones,text="dificil",font="Arial 12",value=3, variable=d)
    r1.place(x=10,y=80)
    r2.place(x=10,y=100)
    r3.place(x=10,y=120)

    r4=Radiobutton(opciones, text="Si", font="Arial 12", value=1, variable=timer)
    r5= Radiobutton(opciones,text="No",font="Arial 12", value=0, variable=timer)
    r6=Radiobutton(opciones,text="Timer",font="Arial 12",value=2, variable=timer)
    r4.place(x=10,y=170)
    r5.place(x=10,y=190)
    r6.place(x=10,y=210)

    r7=Radiobutton(opciones, text="Si", font="Arial 12", value=1, variable=sonido)
    r8= Radiobutton(opciones,text="No",font="Arial 12", value=0, variable=sonido)
    r7.place(x=10,y=260)
    r8.place(x=10,y=280)

    r9= Radiobutton(opciones, text="3x3", font="Arial 12", value=3, variable=tam)
    r9.place(x=10,y=330)
    r10= Radiobutton(opciones, text="4x4", font="Arial 12", value=4, variable=tam)
    r10.place(x=10,y=350)
    r11= Radiobutton(opciones, text="5x5", font="Arial 12", value=5, variable=tam)
    r11.place(x=10,y=370)
    r12= Radiobutton(opciones, text="6x6", font="Arial 12", value=6, variable=tam)
    r12.place(x=10,y=390)
    r13= Radiobutton(opciones, text="7x7", font="Arial 12", value=7, variable=tam)
    r13.place(x=10,y=410)
    r14= Radiobutton(opciones, text="8x8", font="Arial 12", value=8, variable=tam)
    r14.place(x=10,y=430)
    r15= Radiobutton(opciones, text="9x9", font="Arial 12", value=9, variable=tam)
    r15.place(x=10,y=450)
    r16= Radiobutton(opciones, text="Multi Tamaño", font="Arial 12", value=10, variable=tam)
    r16.place(x=10,y=470)
    
    

    l1=Label(opciones,text="DIFICULTAD",font="Arial 12 bold")
    l2=Label(opciones, text="Reloj?",font="Arial 12 bold")
    l3=Label(opciones,text="Sonido al terminar?",font="Arial 12 bold")
    l1.place(x=10,y=60)
    l2.place(x=10,y=150)
    l3.place(x=10,y=240)
    l4= Label(opciones,text="Tamaño",font="Arial 12 bold")
    l4.place(x=10,y=310)
    

    boton=Button(opciones,text="Listo",font="Arial 14 bold",command=listo,bg="green")
    boton.place(x=1,y=1)
    boton2=Button(opciones,text="Jugar",font="Arial 14 bold",command=salir,bg="Steelblue1")
    boton2.place(x=120,y=1)
    mainloop()


def ventana_pronosticar():
    #----------------------------------------------
    #funciones de para volver al menú y para abir el cronómetro con pronostico
    def crono_dos():
        global OpcionReloj
        deci= guardador.getde()
        segundos= guardador.getse()
        mi= guardador.getmi()
        horass= guardador.getho()


        guardador.sethoc(horass)
        guardador.setdec(deci)
        guardador.setsec(segundos)
        guardador.setmic(mi)
        OpcionReloj="S2"
        root.destroy()
        menu()
    #----------------------------------------------------------------------------
    root = Tk()
    root.title('Pronosticar')
    root.geometry("600x400")
    root.config(bg="SteelBlue1")

    andrey = StringVar()
    time = Entry(root,width=5,fg="black",textvariable=andrey).place(x=290,y=100)
    
    carlos = StringVar()
    hora = Entry(root,width=5,fg="black",textvariable=carlos).place(x=200,y=100)
    
    alex = StringVar()
    hola = Entry(root,width=5,fg="black",textvariable=alex).place(x=245,y=100)
    

    time = Label(root,text="S" ,fg='black')
    time.place(x=295,y=140)

    time = Label(root,text="M" ,fg='black')
    time.place(x=250,y=140)

    time = Label(root,text="H" ,fg='black')
    time.place(x=205,y=140)

    time = Label(root,text="Introducir el tiempo que desea")
    time.place(x=175,y=60)
    def verguardados():
        global OpcionReloj
        hor= carlos.get()
        mito= alex.get()
        
        segdos= andrey.get()
        ll= hor.isdigit()==True
        jj= mito.isdigit()==True
        mm=segdos.isdigit()== True
        if hor =="" and mito=="" and segdos=="" : 
            OpcionReloj="N"
            messagebox.showinfo("Error:", "Introducir algo en cada una de las casillas")
        elif  hor =="0" and mito=="0" and segdos=="0":
            OpcionReloj="N"
            messagebox.showinfo("Error:", "Introducir al menos un numero diferente de 0")

        
        
        elif ll==False:
            OpcionReloj="N"
            messagebox.showinfo("Error:", "Introducir numeros no letras")
        elif jj==False:
            messagebox.showinfo("Error:", "Introducir numeros no letras")
        elif mm==False:
            messagebox.showinfo("Error:", "Introducir numeros no letras")
        else:
            if int(hor)<0 or int(hor)>24:
                OpcionReloj="N"
                messagebox.showinfo("Error:", "Horas no pueden ser <0 o >24")
            elif int(mito)<0 or int(mito)>59:
                OpcionReloj="N"
                messagebox.showinfo("Error:", "Minutos no pueden ser <0 o >59")
            elif int(segdos)<0 or int(segdos)>59:
                OpcionReloj="N"
                messagebox.showinfo("Error:", "Segundos  no pueden ser <0 o >59")
            
            else:
                guardador.setse(int(segdos))
                guardador.setmi(int(mito))
                guardador.setho(int(hor))
                crono_dos()

    guardarbtn=Button(root,width=8, fg='blue', text='Guardar', command=verguardados)
    guardarbtn.place(x=350,y=100)
    root.mainloop()

#Funciones para abrir los juegos y los archivos
def abrirjuegos():
    global dificultad, partidaActual,tamano

    par= dificultad + str(tamano)
    
    f = open("kenken_juegos.dat")
    numero_partida= 0   # consecutivo para cada partida en el diccionario
    partidas = {}   # diccionario con todas las partidas
    while True:
        l = f.readline()
        if l=="": break  # EOF fin de archivo
        
        n = l[0] # nivel de la partida
        y= l[1]
        z= n + y
        d = eval(l[2:-1]) # diccionario de esta partida
        if z == par:
            numero_partida = numero_partida + 1
            partidas [ dificultad[0]+ str(numero_partida)]= d
    cantidadFinal=numero_partida
            
    f.close()
    juego= dificultad[0]+ str(random.randint(1,cantidadFinal))
    partidaActual=partidas[juego]

    partida_juego(partidas[juego])


#Colorea cada label como tiene que arbirse para la próxima                
def valorycolora():
    global labels,sobrelabel,colores
    global  Laf1,Laf2,Laf3,Laf4,Laf5,Laf6,Laf7,Laf8,Laf9,Laf10,Laf11,Laf12,Laf13,Laf14,Laf15,Laf16,Laf17,Laf18,Laf19,Laf20,Laf21,Laf22,Laf23,Laf24,Laf25,Laf26,Laf27,Laf28,Laf29,Laf30,Laf31,Laf32,Laf33,Laf34,Laf35,Laf36
    global texto1,texto2,texto3,texto4,texto5,texto6,texto7,texto8,texto9,texto10,texto11,texto12,texto13,texto14,texto15,texto16,texto17,texto18,texto19,texto20,texto21,texto22,texto23,texto24,texto25,texto26,texto27,texto28,texto29,texto30,texto31,texto32,texto33,texto34,texto35,texto36
    

    formula= labels
    lugar= sobrelabel
    colo= colores
    contador=1

    while len(formula)>0:
        if contador==1:
            contador=contador+1
            texto1=formula[0]
            Laf1=colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 2:
            contador=contador+1
            texto2=formula[0]
            Laf2=colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 3:
            contador=contador+1
            texto3=formula[0]
            Laf3=colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 4:
            contador=contador+1
            texto4=formula[0]
            Laf4=colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 5:
            contador=contador+1
            texto5=formula[0]
            Laf5=colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 6:
            contador=contador+1
            texto6=formula[0]
            Laf6=colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 7:
            contador=contador+1
            texto7=formula[0]
            Laf7=colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 8:
            contador=contador+1
            texto8=formula[0]
            Laf8=colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 9:
            contador=contador+1
            texto9=formula[0]
            Laf9=colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 10:
            contador=contador+1
            texto10=formula[0]
            Laf10=colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 11:
            contador=contador+1
            texto11=formula[0]
            Laf11=colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 12:
            contador=contador+1
            texto12=formula[0]
            Laf12=colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 13:
            contador=contador+1
            texto13=formula[0]
            Laf13=colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 14:
            contador=contador+1
            texto14=formula[0]
            Laf14=colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 15:
            contador=contador+1
            texto15=formula[0]
            Laf15=colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 16:
            contador=contador+1
            texto16=formula[0]
            Laf16=colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 17:
            contador=contador+1
            texto17=formula[0]
            Laf17=colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 18:
            contador=contador+1
            texto18=formula[0]
            Laf18=colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 19:
            contador=contador+1
            texto19=formula[0]
            Laf19=colo[0]
            formula=formula[1:]
            colo=colo[1:]

        elif contador== 20:
            contador= contador + 1
            texto20= formula[0]
            Laf20= colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 21:
            contador= contador + 1
            texto21= formula[0]
            Laf21= colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 22:
            contador= contador + 1
            texto22= formula[0]
            Laf22= colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 23:
            contador= contador + 1
            texto23= formula[0]
            Laf23= colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 24:
            contador= contador + 1
            texto24= formula[0]
            Laf24= colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 25:
            contador= contador + 1
            texto25= formula[0]
            Laf25= colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 26:
            contador= contador + 1
            texto26= formula[0]
            Laf26= colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 27:
            contador= contador + 1
            texto27= formula[0]
            Laf27= colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 28:
            contador= contador + 1
            texto28= formula[0]
            Laf28= colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 29:
            contador= contador + 1
            texto29= formula[0]
            Laf29= colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 30:
            contador= contador + 1
            texto30= formula[0]
            Laf30= colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 31:
            contador= contador + 1
            texto31= formula[0]
            Laf31= colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 32:
            contador= contador + 1
            texto32= formula[0]
            Laf32= colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 33:
            contador= contador + 1
            texto33= formula[0]
            Laf33= colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 34:
            contador= contador + 1
            texto34= formula[0]
            Laf34= colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 35:
            contador= contador + 1
            texto35= formula[0]
            Laf35= colo[0]
            formula=formula[1:]
            colo=colo[1:]
        elif contador== 36:
            contador= contador + 1
            texto36= formula[0]
            Laf36= colo[0]
            formula=formula[1:]
            colo=colo[1:]
    
        
            
#Comprueba las validaciones de las fórmulas        
def comprobadorfinal():
    global partidaActual

    for h in partidaActual:
        m= partidaActual[h]
        if compruebadic(m)==True:
            continue
        else:
            messagebox.showinfo("Error:", "Lo sentimos, mejor suerte para la próxima")
    
    return ("Correcto")
  

def compruebadic(lista):
    global Primer,segundo,tercero,cuarto,quinto,sexto,septimo,octavo,noveno
    LISTA= list(lista)
    FOR= LISTA[0]
    RESLISTA= LISTA[1:]
    

    nuevaLista=[]
    while RESLISTA!=[]:
        
        
        if RESLISTA[0] == (1,1):
            RESLISTA[0]=int(Primer[0])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (1,2):
            RESLISTA[0]=int(Primer[1])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (1,3):
            RESLISTA[0]=int(Primer[2])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (1,4):
            RESLISTA[0]=int(Primer[3])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (1,5):
            RESLISTA[0]=int(Primer[4])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (1,6):
            RESLISTA[0]=int(Primer[5])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (2,1):
            RESLISTA[0]=int(segundo[0])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (2,2):
            RESLISTA[0]=int(segundo[1])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (2,3):
            RESLISTA[0]=int(segundo[2])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (2,4):
            RESLISTA[0]=int(segundo[3])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (2,5):
            RESLISTA[0]=int(segundo[4])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (2,6):
            RESLISTA[0]=int(segundo[5])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (3,1):
            RESLISTA[0]=int(tercero[0])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (3,2):
            RESLISTA[0]=int(tercero[1])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (3,3):
            RESLISTA[0]=int(tercero[2])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (3,4):
            RESLISTA[0]=int(tercero[3])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (3,5):
            RESLISTA[0]=int(tercero[4])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (3,6):
            RESLISTA[0]=int(tercero[5])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (4,1):
            RESLISTA[0]=int(cuarto[0])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (4,2):
            RESLISTA[0]=int(cuarto[1])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (4,3):
            RESLISTA[0]=int(cuarto[2])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (4,4):
            RESLISTA[0]=int(cuarto[3])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (4,5):
            RESLISTA[0]=int(cuarto[4])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (4,6):
            RESLISTA[0]=int(cuarto[5])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (5,1):
            RESLISTA[0]=int(quinto[0])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (5,2):
            RESLISTA[0]=int(quinto[1])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (5,3):
            RESLISTA[0]=int(quinto[2])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (5,4):
            RESLISTA[0]=int(quinto[3])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (5,5):
            RESLISTA[0]=int(quinto[4])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (5,6):
            RESLISTA[0]=int(quinto[5])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (6,1):
            RESLISTA[0]=int(sexto[0])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (6,2):
            RESLISTA[0]=int(sexto[1])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (6,3):
            RESLISTA[0]=int(sexto[2])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (6,4):
            RESLISTA[0]=int(sexto[3])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (6,5):
            RESLISTA[0]=int(sexto[4])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (6,6):
            RESLISTA[0]=int(sexto[5])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]

        elif RESLISTA[0] == (1,7):
            RESLISTA[0]=int(Primer[6])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (1,8):
            RESLISTA[0]=int(Primer[7])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (1,9):
            RESLISTA[0]=int(Primer[8])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (2,7):
            RESLISTA[0]=int(segundo[6])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (2,8):
            RESLISTA[0]=int(segundo[7])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (2,9):
            RESLISTA[0]=int(segundo[8])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (3,7):
            RESLISTA[0]=int(tercero[6])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (3,8):
            RESLISTA[0]=int(tercero[7])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (3,9):
            RESLISTA[0]=int(tercero[8])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (4,7):
            RESLISTA[0]=int(cuarto[6])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (4,8):
            RESLISTA[0]=int(cuarto[7])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (4,9):
            RESLISTA[0]=int(cuarto[8])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (5,7):
            RESLISTA[0]=int(quinto[6])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (5,8):
            RESLISTA[0]=int(quinto[7])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (5,9):
            RESLISTA[0]=int(quinto[8])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (6,7):
            RESLISTA[0]=int(sexto[6])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (6,8):
            RESLISTA[0]=int(sexto[7])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (6,9):
            RESLISTA[0]=int(sexto[8])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]

        elif RESLISTA[0] == (7,1):
            RESLISTA[0]=int(septimo[0])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (7,2):
            RESLISTA[0]=int(septimo[1])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (7,3):
            RESLISTA[0]=int(septimo[2])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (7,4):
            RESLISTA[0]=int(septimo[3])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (7,5):
            RESLISTA[0]=int(septimo[4])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (7,6):
            RESLISTA[0]=int(septimo[5])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (7,7):
            RESLISTA[0]=int(septimo[6])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (7,8):
            RESLISTA[0]=int(septimo[7])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (7,9):
            RESLISTA[0]=int(septimo[8])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (8,1):
            RESLISTA[0]=int(octavo[0])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (8,2):
            RESLISTA[0]=int(octavo[1])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (8,3):
            RESLISTA[0]=int(octavo[2])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (8,4):
            RESLISTA[0]=int(octavo[3])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (8,5):
            RESLISTA[0]=int(octavo[4])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (8,6):
            RESLISTA[0]=int(octavo[5])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (8,7):
            RESLISTA[0]=int(octavo[6])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (8,8):
            RESLISTA[0]=int(octavo[7])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (8,9):
            RESLISTA[0]=int(octavo[8])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]

        elif RESLISTA[0] == (9,1):
            RESLISTA[0]=int(noveno[0])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (9,2):
            RESLISTA[0]=int(noveno[1])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (9,3):
            RESLISTA[0]=int(noveno[2])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (9,4):
            RESLISTA[0]=int(noveno[3])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (9,5):
            RESLISTA[0]=int(noveno[4])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (9,6):
            RESLISTA[0]=int(noveno[5])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (9,7):
            RESLISTA[0]=int(noveno[6])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (9,8):
            RESLISTA[0]=int(noveno[7])
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
        elif RESLISTA[0] == (9,9):
            RESLISTA[0]=int(noveno[8])
            
            nuevaLista.append(RESLISTA[0])
            RESLISTA= RESLISTA[1:]
       


    finalFORM= FOR[:-1]


    if len(FOR)==1:
        if nuevaLista[0]== int(finalFORM):
            return True
        else:
            return False

        
    elif FOR[-1]=="+":
        sumadores=nuevaLista
        suma=0
        while sumadores!=[]:
            suma=suma+sumadores[0]
            sumadores=sumadores[1:]
        if suma== int(finalFORM):
            return True
        else:
            return False
             
    elif FOR[-1]=="-":
        restadores= nuevaLista
        restadores.sort(reverse=True)
        resta= restadores[0]
        restadores=restadores[1:]

        while restadores!=[]:
            resta= resta - restadores[0]
            restadores= restadores[1:]

        if resta== int(finalFORM):
            return True
        else:
            return False
    elif FOR[-1]=="x":
        multiplicadores= nuevaLista
        multiplica= 1
        while multiplicadores!=[]:
            multiplica= multiplica * multiplicadores[0]
            multiplicadores= multiplicadores[1:]

        if multiplica== int(finalFORM):
            return True
        else:
            return False
    
    else:
        divisores= nuevaLista
        divisores.sort(reverse=True)
        divisor= divisores[0]
        divisores=divisores[1:]
        while divisores!=[]:
            divisor=divisor//divisores[0]
            divisores=divisores[1:]
        if divisor== int(finalFORM):
            return True
        else:
            return False
                
    
def partida_juego(partida):
    global labels,sobrelabel,colores
    Tamano= len(partida)
    labels= []
    sobrelabel=[]
    contador=1
    while contador<= Tamano:
        labels.append(partida[contador][0])
        sobrelabel.append(partida[contador][1])
        contador= contador + 1


    
    C1= "gainsboro"
    C2= "midnight blue"
    C3= "green"
    C4= "yellow"
    C5= "dim gray"
    C6= "rosy brown"
    C7= "gold"
    C8= "peach puff"
    C9= "purple"
    C10= "saddle brown"
    C11= "red"
    C12= "coral"
    C13= "indian red"
    C14= "turquoise1"
    C15= "SpringGreen2"
    C16= "khaki3"
    C17= "aquamarine4"
    C18= "gold4"
    C19= "DarkSeaGreen2"
    C20= "sienna3"
    C21= "purple3"
    C22= "MediumPurple1"
    C23= "lawn green"
    C24= "peru"
    C25= "AntiqueWhite3"
    C26= "chartreuse3"
    C27= "NavajoWhite2"
    C28= "HotPink1"
    C29= "SkyBlue4"
    C30= "sienna4"
    C31= "chocolate2"
    C32= "pale violet red"
    C33= "burlywood3"
    C34= "SeaGreen1"
    C35= "sky blue"
    C36= "orange red"

    colores=[C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,C14,C15,C16,C17,C18,C19,C20,C21,C22,C23,C24,C25,C26,C27,C28,C29,C30,C31,C32,C33,C34,C35,C36]
    valorycolora()

    nContador= 1
    while nContador<= Tamano:
        indiceContador=1
        while indiceContador<=len(partida[nContador])-1:
            
            
                  
            if nContador==1:
                colorear(C1,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==2:
                colorear(C2,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==3:
                colorear(C3,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==4:
                colorear(C4,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==5:
                colorear(C5,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==6:
                colorear(C6,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==7:
                colorear(C7,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==8:
                colorear(C8,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==9:
                colorear(C9,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==10:
                colorear(C10,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==11:
                colorear(C11,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==12:
                colorear(C12,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==13:
                colorear(C13,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==14:
                colorear(C14,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==15:
                colorear(C15,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==16:
                colorear(C16,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==17:
                colorear(C17,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==18:
                colorear(C18,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==19:
                colorear(C19,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==20:
                colorear(C20,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==21:
                colorear(C21,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==22:
                colorear(C22,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==23:
                colorear(C23,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==24:
                colorear(C24,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==25:
                colorear(C25,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==26:
                colorear(C26,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==27:
                colorear(C27,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==28:
                colorear(C28,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==29:
                colorear(C29,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==30:
                colorear(C30,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
                nContador= nContador + 1
            elif nContador==31:
                colorear(C31,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==32:
                colorear(C32,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==33:
                colorear(C33,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==34:
                colorear(C34,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==35:
                colorear(C35,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
            elif nContador==36:
                colorear(C36,partida[nContador][indiceContador],"a")
                indiceContador= indiceContador + 1
        nContador= nContador + 1


        

    
def motrar():
   
    global OpcionReoj

    if OpcionReloj=="N":
        
        kenken_juego_Abierto(A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16,A17,A18,A19,A20,A21,A22,A23,A24,A25,A26,A27,A28,A29,A30,A31,A32,A33,A34,A35,A36,A37,A38, A39,A40,A41,A42,A43,A44,A45,A46,A47,A48,A49,A50,A51,A52,A53,A54,A55,A56,A57,A58,A59,A60,A61,A62,A63,A64,A65,A66,A67,A68,A69,A70,A71,A72,A73,A74,A75,A76,A77,A78,A79,A80,A81,"N")
    else:
        
        kenken_juego_Abierto(A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16,A17,A18,A19,A20,A21,A22,A23,A24,A25,A26,A27,A28,A29,A30,A31,A32,A33,A34,A35,A36,A37,A38, A39,A40,A41,A42,A43,A44,A45,A46,A47,A48,A49,A50,A51,A52,A53,A54,A55,A56,A57,A58,A59,A60,A61,A62,A63,A64,A65,A66,A67,A68,A69,A70,A71,A72,A73,A74,A75,A76,A77,A78,A79,A80,A81,OpcionReloj)
def colorear(color,par,orden):
    global A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16,A17,A18,A19,A20,A21,A22,A23,A24,A25,A26,A27,A28,A29,A30,A31,A32,A33,A34,A35,A36,A37,A38
    global A39,A40,A41,A42,A43,A44,A45,A46,A47,A48,A49,A50,A51,A52,A53,A54,A55,A56,A57,A58,A59,A60,A61,A62,A63,A64,A65,A66,A67,A68,A69,A70,A71,A72,A73,A74,A75,A76,A77,A78,A79,A80,A81
    if par == (1,1):
        A1=color

    elif par == (1,2):
        A2=color
    elif par == (1,3):
        A3=color
    elif par == (1,4):
        A4=color
    elif par == (1,5):
        A5=color
    elif par == (1,6):
        A6=color
    elif par == (2,1):
        A7=color
    elif par == (2,2):
        A8=color
    elif par == (2,3):
        A9=color
    elif par == (2,4):
        A10=color
    elif par == (2,5):
        A11=color
    elif par == (2,6):
        A12=color
    elif par == (3,1):
        A13=color
    elif par == (3,2):
        A14=color
    elif par == (3,3):
        A15=color
    elif par == (3,4):
        A16=color
    elif par == (3,5):
        A17=color
    elif par == (3,6):
        A18=color
    elif par == (4,1):
        A19=color
    elif par == (4,2):
        A20=color
    elif par == (4,3):
        A21=color
    elif par == (4,4):
        A22=color
    elif par == (4,5):
        A23=color
    elif par == (4,6):
        A24=color
    elif par == (5,1):
        A25=color
    elif par == (5,2):
        A26=color
    elif par == (5,3):
        A27=color
    elif par == (5,4):
        A28=color
    elif par == (5,5):
        A29=color
    elif par == (5,6):
        A30=color
    elif par == (6,1):
        A31=color
    elif par == (6,2):
        A32=color
    elif par == (6,3):
        A33=color
    elif par == (6,4):
        A34=color
    elif par == (6,5):
        A35=color
    elif par == (6,6):
        A36=color

    elif par == (1,7):
        A37=color
    elif par == (2,7):
        A40=color
    elif par == (3,7):
        A43=color
    elif par == (4,7):
        A46=color
    elif par == (5,7):
        A49=color
    elif par == (6,7):
        A52=color
    elif par == (7,2):
        A56=color
    elif par == (7,3):
        A57=color
    elif par == (7,4):
        A58=color
    elif par == (7,5):
        A59=color
    elif par == (7,6):
        A60=color
    elif par == (7,7):
        A61=color
    elif par==(1,8):
        A38= color
    elif par==(2,8):
        A41= color 
    elif par==(3,8):
        A44= color 
    elif par==(4,8):
        A47= color 
    elif par==(5,8):
        A50= color 
    elif par==(6,8):
        A53= color
    elif par == (7,8):
        A62=color
    elif par==(8,1):
        A64= color
    elif par==(8,2):
        A65= color 
    elif par==(8,3):
        A66= color 
    elif par==(8,4):
        A67= color 
    elif par==(8,5):
        A68= color 
    elif par==(8,6):
        A69= color 
    elif par==(8,7):
        A70= color 
    elif par==(8,8):
        A71= color

    elif par==(1,9):
        A39= color
    elif par==(2,9):
        A42= color 
    elif par==(3,9):
        A45= color 
    elif par==(4,9):
        A48= color 
    elif par==(5,9):
        A51= color 
    elif par==(6,9):
        A54= color
    elif par==(7,9):
        A63= color
    elif par==(8,9):
        A72= color
    elif par==(9,1):
        A73= color 
    elif par==(9,2):
        A74= color 
    elif par==(9,3):
        A75= color 
    elif par==(9,4):
        A76= color 
    elif par==(9,5):
        A77= color 
    elif par==(9,6):
        A78= color 
    elif par==(9,7):
        A79= color 
    elif par==(9,8):
        A80= color 
    elif par==(9,9):
        A81= color
#posibles resultados
def posib(a,n):
    global partidaActual
    tam=tamano
    signo=a[-1]
    result=a[:-1]
    if len((partidaActual[n]))==4:    
        return(posibles3(tam,int(result),signo))
    elif len(partidaActual[n])==3:
        return(posibles2(tam,int(result),signo))
    else:
        messagebox.showinfo("Jugada",a)
def posibles3(tam,result,signo):#Esta es para las casillas de 3 numeros
    fin=[]
    for n1 in range(1,tam+1):
        for n2 in range(1,tam+1):
            for n3 in range(1,tam+1):
                if resultado3(n1,n2,n3,result,signo)==True:
                    fin.append((n1,n2,n3))
    
    return sults(fin)

def resultado3(n1,n2,n3,result,signo):#Esta solo tiene el de + y * porque los de 3 casillas solo usan + y *
    if n1==n2 or n1==n3 or n2==n3:
        return(False)
    elif signo=="+":
        if n1+n2+n3==result:
            return(True)
        else:
            return(False)
    elif signo=="x":
        if n1*n2*n3==result:
            return(True)
        else:
            return(False)

def resultado2(n1,n2,result,signo):
    if n1==n2:
        return False
    elif signo=="+":
        if n1+n2==result:
            return(True)
        else:
            return(False)
    elif signo=="x":
        if n1*n2==result:
            return(True)
        else:
            return(False)
    elif signo=="-":
        if n1>n2:
            if n1-n2==result:
                return(True)
            else:
                return(False)
        else:
            if n2-n1==result:
                return(True)
            else:
                return(False)
    else:
        if n1>n2:
            if n1//n2==result:
                return(True)
            else:
                return(False)
        else:
            if n2//n1==result:
                return(True)
            else:
                return(False)
        
    
def posibles2(tam,result,signo):#Se usa el tamaño porque ese es el numero maximo que puede ser utilizado en las casillas
    fin=[]
    for n1 in range(1,tam+1):
        for n2 in range(1,tam+1):
            if resultado2(n1,n2,result,signo)==True:
                fin.append((n1,n2))
    return sults(fin)


def sults(fin):
    messagebox.showinfo("Posibilidades","sus posibles jugadas son:  "+str(fin))
guardador = cronoguardador()
inicioD()
