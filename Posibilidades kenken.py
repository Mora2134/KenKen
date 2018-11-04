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
    for n1 in range(1,tamaño):
        for n2 in range(1,tamaño):
            if resultado2(n1,n2,result,signo)==True:
                fin.append((n1,n2))
    return(fin)




def posibles3(tam,result,signo):#Esta es para las casillas de 3 numeros
    fin=[]
    for n1 in range(1,tam):
        for n2 in range(1,tam):
            for n3 in range(1,tam):
                if resultado3(n1,n2,n3,result,signo)==True:
                    fin.append((n1,n2,n3))
    return (fin)

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
#def sults(fin):
 #   messagebox.showinfo(fin)
