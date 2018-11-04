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
tamano= 6


#Son listas que se crearon para guardar lo que el jugador fuera seleccionando en la cuadricula 6x6
Primer=[0,0,0,0,0,0]
segundo=[0,0,0,0,0,0]
tercero=[0,0,0,0,0,0]
cuarto=[0,0,0,0,0,0]
quinto=[0,0,0,0,0,0]
sexto=[0,0,0,0,0,0]
#Son variables que se le otorgan a los labels que no estan en la cuadricula, los que se utilizan para saber que es lo que el jugador debe hacer por cada color
texto2= texto3= texto4= texto5= texto6= texto7= texto8= texto9= texto10= texto11= texto12= texto13= texto14= texto15= texto16= texto17= texto18= texto19= "   "

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

    #--------------------------------------
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
def kenken_juego_Abierto(A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16,A17,A18,A19,A20,A21,A22,A23,A24,A25,A26,A27,A28,A29,A30,A31,A32,A33,A34,A35,A36,op1):
    global defaultbg, Laf1,Laf2,Laf3,Laf4,Laf5,Laf6,Laf7,Laf8,Laf9,Laf10,Laf11,Laf12,Laf13,Laf14,Laf15,Laf16,Laf17,Laf18,Laf19, texto1,texto1,texto2,texto3,texto4,texto5,texto6,texto7,texto8,texto9,texto10,texto11,texto12,texto13,texto14,texto15,texto16,texto17,texto18,texto1
    
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
        

        

        # mostramos la variable contandor

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
    la1=Label(menu,text=texto1,height=3,width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf1)
    la1.place(x=20,y=5)

    la2=Label(menu,text=texto2,height=3,width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf2)
    la2.place(x=45,y=5)

    la3=Label(menu,text=texto3,height=3,width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf3)
    la3.place(x="70",y=5)
    la4=Label(menu,text=texto4,height=3,width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf4)
    la4.place(x="95",y=5)
    la5=Label(menu,text=texto5,height=3,width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf5)
    la5.place(x="120",y=5)
    la6=Label(menu,text=texto6,height=3,width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf6)
    la6.place(x="145",y=5)
    la7=Label(menu,text=texto7,height=3,width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf7)
    la7.place(x="170",y=5)
    la8=Label(menu,text=texto8,height=3,width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf8)
    la8.place(x="195",y=5)
    la9=Label(menu,text=texto9,height=3,width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf9)
    la9.place(x="220",y=5)
    la10=Label(menu,text=texto10,height=3,width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf10)
    la10.place(x="245",y=5)
    la11=Label(menu,text=texto11,height=3,width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf11)
    la11.place(x=20,y=55)
    la12=Label(menu,text=texto12,height=3,width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf12)
    la12.place(x=45,y=55)
    la13=Label(menu,text=texto13,height=3,width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf13)
    la13.place(x=70,y=55)
    la14=Label(menu,text=texto14,height=3,width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf14)
    la14.place(x=95,y=55)
    la15=Label(menu,text=texto15,height=3,width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf15)
    la15.place(x=120,y=55)
    la16=Label(menu,text=texto16,height=3,width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf16)
    la16.place(x=145,y=55)
    la17=Label(menu,text=texto17,height=3,width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf17)
    la17.place(x=170,y=55)
    la18=Label(menu,text=texto18,height=3,width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf18)
    la18.place(x=195,y=55)
    la19=Label(menu,text=texto19,height=3,width=3,bd=2,relief="solid",activebackground="SteelBlue1",bg=Laf19)
    la19.place(x="220",y=55)


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

        if OpcionReloj== "S1" or "S2":
            variable= dificultad + "                          " + nombre + "                          " + str(h)+":"+str(m)+":"+str(s) + "\n"
            f.write(variable)

        f.close()
    #---------------------------------------------------------------------------------------------------------------------------------------------------
            
    #Validaciones para cuando el jugador termine
    def probarvacias():
        global time,Primer,segundo,tercero,cuarto,quinto,sexto
        
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
        else:
            return ("SIGA")

    def probarfilas(lista):
        
        if lista[0]==lista[1] or lista[0]==lista[2] or lista[0]==lista[3] or lista[0]==lista[4] or lista[0]==lista[5]:
            messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
        elif lista[1]==lista[2] or lista[1]==lista[3] or lista[1]==lista[4] or lista[1]==lista[5]:
            messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
        elif lista[2]==lista[3] or lista[2]==lista[4] or lista[2]==lista[5]:
            messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
        elif lista[3]==lista[4] or lista[3]==lista[5] or lista[4]==lista[5]:
            messagebox.showinfo("Error:", "No pueden un mismo número repetido en una misma fila o columna")
        else:
            return ("SIGA")

    def validarcasillas():
        global time,Primer,segundo,tercero,cuarto,quinto,sexto,OpcionReloj,iraresta
        variable1= [Primer[0],segundo[0],tercero[0],cuarto[0],quinto[0],sexto[0]]
        variable2= [Primer[1],segundo[1],tercero[1],cuarto[1],quinto[1],sexto[1]]
        variable3= [Primer[2],segundo[2],tercero[2],cuarto[2],quinto[2],sexto[2]]
        variable4= [Primer[3],segundo[3],tercero[3],cuarto[3],quinto[3],sexto[3]]
        variable5= [Primer[4],segundo[4],tercero[4],cuarto[4],quinto[4],sexto[4]]
        variable6= [Primer[5],segundo[5],tercero[5],cuarto[5],quinto[5],sexto[5]]

        if OpcionReloj=="S1":
            if probarvacias()!= "SIGA":
                continuar()

            elif probarfilas(Primer)!="SIGA":
                continuar()
                
            elif probarfilas(segundo)!="SIGA":
                continuar()
            elif probarfilas(tercero)!="SIGA":
                continuar()
            
            elif probarfilas(cuarto)!="SIGA":
                continuar()
            elif probarfilas(quinto)!="SIGA":
                continuar()
            elif probarfilas(sexto)!="SIGA":
                continuar()

            elif probarfilas(variable1)!="SIGA":
                continuar()
            elif probarfilas(variable2)!="SIGA":
                continuar()
            
            elif probarfilas(variable3)!="SIGA":
                continuar() 
            elif probarfilas(variable4)!="SIGA":
                continuar()
            elif probarfilas(variable5)!="SIGA":
                continuar()
            elif probarfilas(variable6)!="SIGA":
                continuar()
            elif comprobadorfinal()=="Correcto":
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
                

            elif probarfilas(Primer)!="SIGA":
                iraresta="SI"
                iniciarcrono2(d,s,m,h)
                
            elif probarfilas(segundo)!="SIGA":
                iraresta="SI"
                iniciarcrono2(d,s,m,h)
            elif probarfilas(tercero)!="SIGA":
                iraresta="SI"
                iniciarcrono2(d,s,m,h)
            
            elif probarfilas(cuarto)!="SIGA":
                iraresta="SI"
                iniciarcrono2(d,s,m,h) 
            elif probarfilas(quinto)!="SIGA":
                iraresta="SI"
                iniciarcrono2(d,s,m,h)
            elif probarfilas(sexto)!="SIGA":
                iraresta="SI"
                iniciarcrono2(d,s,m,h)

            elif probarfilas(variable1)!="SIGA":
                iraresta="SI"
                iniciarcrono2(d,s,m,h) 
            elif probarfilas(variable2)!="SIGA":
                iraresta="SI"
                iniciarcrono2(d,s,m,h)
            
            elif probarfilas(variable3)!="SIGA":
                iraresta="SI"
                iniciarcrono2(d,s,m,h) 
            elif probarfilas(variable4)!="SIGA":
                iraresta="SI"
                iniciarcrono2(d,s,m,h) 
            elif probarfilas(variable5)!="SIGA":
                iraresta="SI"
                iniciarcrono2(d,s,m,h) 
            elif probarfilas(variable6)!="SIGA":
                iraresta="SI"
                iniciarcrono2(d,s,m,h)
            elif comprobadorfinal()=="Correcto":
                iraresta="SI"
                escribir()
                messagebox.showinfo("Felicidades:", "Usted ha ganado este juego")
        else:
            if probarvacias()!= "SIGA":
                print("")

            elif probarfilas(Primer)!="SIGA":
                print("")
                
            elif probarfilas(segundo)!="SIGA":
                print("")
            elif probarfilas(tercero)!="SIGA":
                print("")
            
            elif probarfilas(cuarto)!="SIGA":
                print("")
            elif probarfilas(quinto)!="SIGA":
                print("")
            elif probarfilas(sexto)!="SIGA":
                print("")

            elif probarfilas(variable1)!="SIGA":
                print("") 
            elif probarfilas(variable2)!="SIGA":
                print("")
            
            elif probarfilas(variable3)!="SIGA":
                print("") 
            elif probarfilas(variable4)!="SIGA":
                print("")
            elif probarfilas(variable5)!="SIGA":
                print("")
            elif probarfilas(variable6)!="SIGA":
                print("")
            elif comprobadorfinal()=="Correcto":
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
        global time
        time= 37
    def B38(event): 
        global time
        time= 38
    def B39(event): 
        global time
        time= 39
    def B40(event): 
        global time
        time= 40
    def B41(event): 
        global time
        time= 41
    def B42(event): 
        global time
        time= 42
    def B44(event): 
        global time
        time= 44
    def B43(event): 
        global time
        time= 43
    def B45(event): 
        global time
        time= 45
    def B46(event): 
        global time
        time= 46
    def B47(event): 
        global time
        time= 47
    def B48(event): 
        global time
        time= 48
    def B49(event): 
        global time
        time= 49
    def B50(event): 
        global time
        time= 50
    def B51(event): 
        global time
        time= 51
    def B52(event): 
        global time
        time= 52
    def B53(event): 
        global time
        time= 53
    def B54(event): 
        global time
        time= 54
    def B55(event): 
        global time
        time= 55
    def B56(event): 
        global time
        time= 56
    def B57(event): 
        global time
        time= 57
    def B58(event): 
        global time
        time= 58
    def B59(event): 
        global time
        time= 59
    def B60(event): 
        global time
        time= 60
    def B61(event): 
        global time
        time= 61
    def B62(event): 
        global time
        time= 62
    def B63(event): 
        global time
        time= 63
    def B64(event): 
        global time
        time= 64
    def B65(event): 
        global time
        time= 65
    def B66(event): 
        global time
        time= 66
    def B67(event): 
        global time
        time= 67
    def B68(event): 
        global time
        time= 68
    def B69(event): 
        global time
        time= 69
    def B70(event): 
        global time
        time= 70
    def B71(event): 
        global time
        time= 71
    def B72(event): 
        global time
        time= 72
    def B73(event): 
        global time
        time= 73
    def B74(event): 
        global time
        time= 74
    def B75(event): 
        global time
        time= 75
    def B76(event): 
        global time
        time= 76
    def B77(event): 
        global time
        time= 77
    def B78(event): 
        global time
        time= 78
    def B79(event): 
        global time
        time= 79
    def B80(event): 
        global time
        time= 80
    def B81(event): 
        global time
        time= 81

    #Con esta función escribe lo que el jugador seleccionando en las casillas y lo guarda en las variables que mencionamos al inicio del código 
    def valores(numero):
        global time,Primer,segundo,tercero,cuarto,quinto,sexto
        if time ==1:
            b1['text']= numero
            Primer[0]=numero
        elif time==2:
            b2['text']= numero
            Primer[1]=numero
        elif time== 3:
            b3['text']= numero
            Primer[2]=numero
        elif time== 4:
            b4['text']= numero
            Primer[3]=numero
        elif time== 5:
            b5['text']= numero
            Primer[4]=numero
        elif time== 6:
            b6['text']= numero
            Primer[5]=numero
        elif time== 7:
            b7['text']= numero
            segundo[0]=numero
        elif time== 8:
            b8['text']= numero
            segundo[1]=numero
        elif time== 9:
            b9['text']= numero
            segundo[2]=numero
        elif time== 10:
            b10['text']= numero
            segundo[3]=numero
        elif time== 11:
            b11['text']= numero
            segundo[4]=numero
        elif time== 12:
            b12['text']= numero
            segundo[5]=numero
        elif time== 13:
            b13['text']= numero
            tercero[0]=numero
        elif time== 14:
            b14['text']= numero
            tercero[1]=numero
        elif time== 15:
            b15['text']= numero
            tercero[2]=numero
        elif time== 16:
            b16['text']= numero
            tercero[3]=numero
        elif time== 17:
            b17['text']= numero
            tercero[4]=numero
        elif time== 18:
            b18['text']= numero
            tercero[5]=numero
        elif time== 19:
            b19['text']= numero
            cuarto[0]=numero
        elif time== 20:
            b20['text']= numero
            cuarto[1]=numero
        elif time== 21:
            b21['text']= numero
            cuarto[2]=numero
        elif time== 22:
            b22['text']= numero
            cuarto[3]=numero
        elif time== 23:
            b23['text']= numero
            cuarto[4]=numero
        elif time== 24:
            b24['text']= numero
            cuarto[5]=numero
        elif time== 25:
            b25['text']= numero
            quinto[0]=numero
        elif time== 26:
            b26['text']= numero
            quinto[1]=numero
        elif time== 27:
            b27['text']= numero
            quinto[2]=numero
        elif time== 28:
            b28['text']= numero
            quinto[3]=numero
        elif time== 29:
            b29['text']= numero
            quinto[4]=numero
        elif time== 30:
            b30['text']= numero
            quinto[5]=numero
        elif time== 31:
            b31['text']= numero
            sexto[0]=numero
        elif time== 32:
            b32['text']= numero
            sexto[1]=numero
        elif time== 33:
            b33['text']= numero
            sexto[2]=numero
        elif time== 34:
            b34['text']= numero
            sexto[3]=numero
        elif time== 35:
            b35['text']= numero
            sexto[4]=numero
        elif time== 36:
            b36['text']= numero
            sexto[5]=numero
    def labels_tamanos():
        global tamano
        if tamano>=3:

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
            b37=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b37.bind("<1>",B37)
            b37.place(x=530,y=110)
            b38=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b38.bind("<1>",B38)
            b38.place(x=530,y=161)
            b39=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b39.bind("<1>",B39)
            b39.place(x=530,y=212)
            b40=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b40.bind("<1>",B40)
            b40.place(x=530,y=263)
            b41=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b41.bind("<1>",B41)
            b41.place(x=530,y=314)
            b42=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b42.bind("<1>",B42)
            b42.place(x=530,y=365)

            b43=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b43.bind("<1>",B43)
            b43.place(x=200,y=416)
            b44=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b44.bind("<1>",B44)
            b44.place(x=255,y=416)
            b45=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b45.bind("<1>",B45)
            b45.place(x=310,y=416)
            b46=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b46.bind("<1>",B46)
            b46.place(x=365,y=416)
            b47=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b47.bind("<1>",B47)
            b47.place(x=420,y=416)
            b48=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b48.bind("<1>",B48)
            b48.place(x=475,y=416)
            b49=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b49.bind("<1>",B49)
            b49.place(x=530,y=416)
        if tamano>=8:
            b50=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b50.bind("<1>",B50)
            b50.place(x=585,y=110)
            b51=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b51.bind("<1>",B51)
            b51.place(x=585,y=161)
            b52=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b52.bind("<1>",B52)
            b52.place(x=585,y=212)
            b53=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b53.bind("<1>",B53)
            b53.place(x=585,y=263)
            b54=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b54.bind("<1>",B54)
            b54.place(x=585,y=314)
            b55=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b55.bind("<1>",B55)
            b55.place(x=585,y=365)
            b56=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b56.bind("<1>",B56)
            b56.place(x=585,y=416)

            #ultima fila
            
            b57=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b57.bind("<1>",B57)
            b57.place(x=200,y=467)
            b58=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b58.bind("<1>",B58)
            b58.place(x=255,y=467)
            b59=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b59.bind("<1>",B59)
            b59.place(x=310,y=467)
            b60=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b60.bind("<1>",B60)
            b60.place(x=365,y=467)
            b61=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b61.bind("<1>",B61)
            b61.place(x=420,y=467)
            b62=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b62.bind("<1>",B62)
            b62.place(x=475,y=467)
            b63=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b63.bind("<1>",B63)
            b63.place(x=530,y=467)
            b64=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b64.bind("<1>",B64)
            b64.place(x=585,y=467)

        if tamano>=9:

            b65=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b65.bind("<1>",B65)
            b65.place(x=640,y=110)
            b66=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b66.bind("<1>",B66)
            b66.place(x=640,y=161)
            b67=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b67.bind("<1>",B67)
            b67.place(x=640,y=212)
            b68=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b68.bind("<1>",B68)
            b68.place(x=640,y=263)
            b69=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b69.bind("<1>",B69)
            b69.place(x=640,y=314)
            b70=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b70.bind("<1>",B70)
            b70.place(x=640,y=365)
            b71=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b71.bind("<1>",B71)
            b71.place(x=640,y=416)
            b72=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b72.bind("<1>",B72)
            b72.place(x=640,y=467)

            #ultima fila

            b73=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b73.bind("<1>",B73)
            b73.place(x=200,y=518)
            b74=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b74.bind("<1>",B74)
            b74.place(x=255,y=518)
            b75=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b75.bind("<1>",B75)
            b75.place(x=310,y=518)
            b76=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b76.bind("<1>",B76)
            b76.place(x=365,y=518)
            b77=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b77.bind("<1>",B77)
            b77.place(x=420,y=518)
            b78=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b78.bind("<1>",B78)
            b78.place(x=475,y=518)
            b79=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b79.bind("<1>",B79)
            b79.place(x=530,y=518)
            b80=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b80.bind("<1>",B80)
            b80.place(x=585,y=518) 
            b81=Label(menu,height=3,width=7,bd=2,relief="solid",activebackground="SteelBlue1",bg="white")
            b81.bind("<1>",B81)
            b81.place(x=640,y=518)
    labels_tamanos()
    



    

        
    validar=Button(menu, text="Validar Juego", font=("Arial 18"),bg="green",command=validarcasillas)
    validar.place(x=230,y=450)
    nuevo=Button(menu, command=lambda:partinaAiniciar(),text="Nuevo Juego", font=("Arial 18"),bg="SteelBlue1")
    nuevo.place(x=400,y=450)
    restart=Button(menu, text="Reiniciar Juego", font=("Arial 18"),bg="orange",command=reiniciajuego)
    restart.place(x=565,y=450)
    terminar=Button(menu, text="Terminar Juego", font=("Arial 18"),bg="light coral",command=terminarya)
    terminar.place(x=300,y=505)

    nombred=Label(menu,text="Nombre del Jugador:",font="Arial 14")
    nombred.place(x=30,y=575)
    global nombre
    nombreya=Label(menu,text=nombre,font="Arial 14")
    nombreya.place(x=30,y=605)

    #Botones de los numeros
    uno=Button(menu,text=1,command=lambda:valores(1),bg="lightgreen",font=("Helvetica",24))
    uno.place(x=750,y=50)

    dos=Button(menu,text=2,command=lambda:valores(2),bg="lightgreen",font=("Helvetica",24))
    dos.place(x=750,y=105)

    tres=Button(menu,text=3,command=lambda:valores(3),bg="lightgreen",font=("Helvetica",24))
    tres.place(x=750,y=180)

    cuatro=Button(menu,text=4,command=lambda:valores(4),bg="lightgreen",font=("Helvetica",24))
    cuatro.place(x=750,y=240)

    cinco=Button(menu,text=5,command=lambda:valores(5),bg="lightgreen",font=("Helvetica",24))
    cinco.place(x=750,y=310)

    seis=Button(menu,text=6,command=lambda:valores(6),bg="lightgreen",font=("Helvetica",24))
    seis.place(x=750,y=375)
    
    mainloop()

    


#Primera ventana donde inica despue´s se ejecutar el botón incio de la primera parte
def menu():
    global defaultbg,Laf1,Laf2,Laf3,Laf4,Laf5,Laf6,Laf7,Laf8,Laf9,Laf10,Laf11,Laf12,Laf13,Laf14,Laf15,Laf16,Laf17,Laf18,Laf19
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

    def partinaAiniciar():
        global nombre
        if nombre == "N":
            messagebox.showinfo("Aviso importante","Primero debe indicar un nombre de jugador")
        else:
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
        global dificultad, OpcionReloj, OpcionSonido, tamano
        if tam.get()==3:
            tamano=3
        if tam.get()==4:
            tamano=4
        if tam.get()==5:
            tamano=5
        if tam.get()==6:
            tamano=6
        if tam.get()==7:
            tamano=7
        if tam.get()==8:
            tamano=8
        if tam.get()==9:
            tamano=9
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
    global dificultad, partidaActual
    f = open("kenken_juegos.dat")
    numero_partida= 0   # consecutivo para cada partida en el diccionario
    numero_partidaI= 0
    numero_partidaD= 0
    cantidadF=0
    cantidadI=0
    cantidadD=0
    partidas = {}   # diccionario con todas las partidas
    while True:
        l = f.readline()
        if l=="": break  # EOF fin de archivo
        
        n = l[0] # nivel de la partida
        d = eval(l[2:-1]) # diccionario de esta partida
        if l[0]== "F":
            numero_partida = numero_partida + 1
            partidas [n + str(numero_partida)]= d
            cantidadF= cantidadF + 1

        if l[0]=="I":
            numero_partidaI = numero_partidaI + 1
            partidas [n + str(numero_partidaI)]= d
            cantidadI= cantidadI + 1
        if l[0]== "D":
            numero_partidaD = numero_partidaD + 1
            partidas [n + str(numero_partidaD)]= d
            cantidadD= cantidadD + 1
            
    
    if dificultad== "F":
        cantidadFinal=numero_partida
    if dificultad=="I":
        cantidadFinal=numero_partidaI
    if dificultad=="D":
        cantidadFinal=numero_partidaD
            
    f.close()
    juego= dificultad + str(random.randint(1,cantidadFinal))
    partidaActual=partidas[juego]
    
    partida_juego(partidas[juego])


#Colorea cada label como tiene que arbirse para la próxima                
def valorycolora():
    global labels,sobrelabel,colores
    global  Laf1,Laf2,Laf3,Laf4,Laf5,Laf6,Laf7,Laf8,Laf9,Laf10,Laf11,Laf12,Laf13,Laf14,Laf15,Laf16,Laf17,Laf18,Laf19, texto1,texto1,texto2,texto3,texto4,texto5,texto6,texto7,texto8,texto9,texto10,texto11,texto12,texto13,texto14,texto15,texto16,texto17,texto18,texto19
    

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
            
#Comprueba las validaciones de las fórmulas        
def comprobadorfinal():
    global partidaActual

    for h in partidaActual:
        m= partidaActual[h]
        if compruebadic(m)==True:
            continue
        else:
            messagebox.showinfo("Error:", "Lo sentimos, mejor suerte para la próxima")
            print("  ")
    return ("Correcto")
    print("Correcto")

def compruebadic(lista):
    global Primer,segundo,tercero,cuarto,quinto,sexto
    m= list(lista)
    n=1

    if len(m[0])==1:
        if m[1] == (1,1):
            m[1]=int(Primer[0])
            if int(m[0])==m[1]:
                return True
            else:
                return False
    

        elif m[1] == (1,2):
            m[1]=int(Primer[1])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (1,3):
            m[1]=int(Primer[2])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (1,4):
            m[1]=int(Primer[3])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (1,5):
            m[1]=int(Primer[4])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (1,6):
            m[1]=int(Primer[5])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (2,1):
            m[1]=int(segundo[0])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (2,2):
            m[1]=int(segundo[1])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (2,3):
            m[1]=int(segundo[2])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (2,4):
            m[1]=int(segundo[3])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (2,5):
            m[1]=int(segundo[4])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (2,6):
            m[1]=int(segundo[5])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (3,1):
            m[1]=int(tercero[0])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (3,2):
            m[1]=int(tercero[1])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (3,3):
            m[1]=int(tercero[2])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (3,4):
            m[1]=int(tercero[3])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (3,5):
            m[1]=int(tercero[4])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (3,6):
            m[1]=int(tercero[5])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (4,1):
            m[1]=int(cuarto[0])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (4,2):
            m[1]=int(cuarto[1])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (4,3):
            m[1]=int(cuarto[2])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (4,4):
            m[1]=int(cuarto[3])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (4,5):
            m[1]=int(cuarto[4])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (4,6):
            m[1]=int(cuarto[5])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (5,1):
            m[1]=int(quinto[0])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (5,2):
            m[1]=int(quinto[1])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (5,3):
            m[1]=int(quinto[2])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (5,4):
            m[1]=int(quinto[3])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (5,5):
            m[1]=int(quinto[4])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (5,6):
            m[1]=int(quinto[5])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (6,1):
            m[1]=int(sexto[0])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (6,2):
            m[1]=int(sexto[1])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (6,3):
            m[1]=int(sexto[2])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (6,4):
            m[1]=int(sexto[3])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (6,5):
            m[1]=int(sexto[4])
            if int(m[0])==m[1]:
                return True
            else:
                return False
        elif m[1] == (6,6):
            m[1]=int(sexto[5])
            if int(m[0])==m[1]:
                return True
            else:
                return False

    
        
           
    else:
        l=lista[1:]
        l= list(l)
        nuevo=[lista[0][:-1]]+[lista[0][-1]]+l
        n=2
        
        while n<=len(nuevo)-1:
            
            if nuevo[n] == (1,1):
                nuevo[n]=int(Primer[0])
                n= n+1

            elif nuevo[n] == (1,2):
                nuevo[n]=int(Primer[1])
                n= n+1
                
            elif nuevo[n] == (1,3):
                nuevo[n]=int(Primer[2])
                n= n+1
            elif nuevo[n] == (1,4):
                nuevo[n]=int(Primer[3])
                n= n+1
            elif nuevo[n] == (1,5):
                nuevo[n]=int(Primer[4])
                n= n+1
            elif nuevo[n] == (1,6):
                nuevo[n]=int(Primer[5])
                n= n+1
            elif nuevo[n] == (2,1):
                nuevo[n]=int(segundo[0])
                n= n+1
            elif nuevo[n] == (2,2):
                nuevo[n]=int(segundo[1])
                n= n+1
            elif nuevo[n] == (2,3):
                nuevo[n]=int(segundo[2])
                n= n+1
            elif nuevo[n] == (2,4):
                nuevo[n]=int(segundo[3])
                n= n+1
            elif nuevo[n] == (2,5):
                nuevo[n]=int(segundo[4])
                n= n+1
            elif nuevo[n] == (2,6):
                nuevo[n]=int(segundo[5])
                n= n+1
            elif nuevo[n] == (3,1):
                nuevo[n]=int(tercero[0])
                n= n+1
            elif nuevo[n] == (3,2):
                nuevo[n]=int(tercero[1])
                n= n+1
            elif nuevo[n] == (3,3):
                nuevo[n]=int(tercero[2])
                n= n+1
            elif nuevo[n] == (3,4):
                nuevo[n]=int(tercero[3])
                n= n+1
            elif nuevo[n] == (3,5):
                nuevo[n]=int(tercero[4])
                n= n+1
            elif nuevo[n] == (3,6):
                nuevo[n]=int(tercero[5])
                n= n+1
            elif nuevo[n] == (4,1):
                nuevo[n]=int(cuarto[0])
                n= n+1
            elif nuevo[n] == (4,2):
                nuevo[n]=int(cuarto[1])
                n= n+1
            elif nuevo[n] == (4,3):
                nuevo[n]=int(cuarto[2])
                n= n+1
            elif nuevo[n] == (4,4):
                nuevo[n]=int(cuarto[3])
                n= n+1
            elif nuevo[n] == (4,5):
                nuevo[n]=int(cuarto[4])
                n= n+1
            elif nuevo[n] == (4,6):
                nuevo[n]=int(cuarto[5])
                n= n+1
            elif nuevo[n] == (5,1):
                nuevo[n]=int(quinto[0])
                n= n+1
            elif nuevo[n] == (5,2):
                nuevo[n]=int(quinto[1])
                n= n+1
            elif nuevo[n] == (5,3):
                nuevo[n]=int(quinto[2])
                n= n+1
            elif nuevo[n] == (5,4):
                nuevo[n]=int(quinto[3])
                n= n+1
            elif nuevo[n] == (5,5):
                nuevo[n]=int(quinto[4])
                n= n+1
            elif nuevo[n] == (5,6):
                nuevo[n]=int(quinto[5])
                n= n+1
            elif nuevo[n] == (6,1):
                nuevo[n]=int(sexto[0])
                n= n+1
            elif nuevo[n] == (6,2):
                nuevo[n]=int(sexto[1])
                n= n+1
            elif nuevo[n] == (6,3):
                nuevo[n]=int(sexto[2])
                n= n+1
            elif nuevo[n] == (6,4):
                nuevo[n]=int(sexto[3])
                n= n+1
            elif nuevo[n] == (6,5):
                nuevo[n]=int(sexto[4])
                n= n+1
            elif nuevo[n] == (6,6):
                nuevo[n]=int(sexto[5])
                n= n+1
        

        if nuevo[1]=="+":
            sumadores=nuevo[2:]
            suma=0
            while sumadores!=[]:
                suma=suma+sumadores[0]
                sumadores=sumadores[1:]
            if suma== int(nuevo[0]):
                return True
            else:
                return False
                 
        elif nuevo[1]=="-":
            restadores= nuevo[2:]
            restadores.sort(reverse=True)
            resta= restadores[0]
            restadores=restadores[1:]

            while restadores!=[]:
                resta= resta - restadores[0]
                restadores= restadores[1:]

            if resta== int(nuevo[0]):
                return True
            else:
                return False
        elif nuevo[1]=="x":
            multiplicadores= nuevo[2:]
            multiplica= 1
            while multiplicadores!=[]:
                multiplica= multiplica * multiplicadores[0]
                multiplicadores= multiplicadores[1:]

            if multiplica== int(nuevo[0]):
                print(nuevo)
                return True
            else:
                return False
        
        else:
            divisores= nuevo[2:]
            divisores.sort(reverse=True)
            divisor= divisores[0]
            divisores=divisores[1:]
            while divisores!=[]:
                divisor=divisor//divisores[0]
                divisores=divisores[1:]
            if divisor== int(nuevo[0]):
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
    
    C1= "spring green" 
    C2= "yellow"
    C3= "rosy brown"
    C4= "indian red"
    C5= "goldenrod"
    C6= "cadet blue"
    C7= "pink1"
    C8= "coral1"
    C9= "Darkorange4"
    C10= "LightPink1"
    C11= "plum3"
    C12= "gold4"
    C13= "LightYellow4"
    C14= "azure2"
    C15= "azure4"
    C16= "MistyRose4"
    C17= "DarkSeaGreen1"
    C18= "cyan2"
    C19= "ivory2"

    colores=[C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,C14,C15,C16,C17,C18,C19]
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
        nContador= nContador + 1

    
def motrar():
    global OpcionReoj

    if OpcionReloj=="N":
        kenken_juego_Abierto(A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16,A17,A18,A19,A20,A21,A22,A23,A24,A25,A26,A27,A28,A29,A30,A31,A32,A33,A34,A35,A36,"N")
    else:
        kenken_juego_Abierto(A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16,A17,A18,A19,A20,A21,A22,A23,A24,A25,A26,A27,A28,A29,A30,A31,A32,A33,A34,A35,A36,OpcionReloj)

        
def colorear(color,par,orden):
    global A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16,A17,A18,A19,A20,A21,A22,A23,A24,A25,A26,A27,A28,A29,A30,A31,A32,A33,A34,A35,A36

    
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


guardador = cronoguardador()
inicioD()
