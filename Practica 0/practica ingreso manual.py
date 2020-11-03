# Israel Lopez Cruz
# israel.lopez@ucsp.edu.pe
import unittest


# Exercise1
def balanceo(str):
    tmp = "";
    for c in str:
        if c != '[' and c != '(' and c != ']' and c != ')':
            continue
        elif  c == '[' or c == '(':
            tmp = tmp + c
        else:
            if(( c == ')' or c == ']') and len(tmp) == 0):
                return False
            if (c == ')' and tmp.strip()[-1] == '(') or (c == ']' and tmp.strip()[-1] == '['):
                tmp = tmp[:-1]
            else:
                return False
    if not tmp:
        return True
    return False

def gerundio(str):
    words = str.split(' ')
    str1 = ""
    str2 = ""
 
    if(len(words) == 2):
        str1 = words[0].strip()[-2:]
        str2 = words[1].strip()
    else:
        return False

##    Caso especial
    if words[0].strip() == "reir":
        if words[1].strip() == "riendo":
            return True
        return False
    if words[0].strip() == "salir":
        if words[1].strip() == "saliendo":
            return True
        return False
    if words[0].strip() == "ir":
        if words[1].strip() == "yendo":
            return True
        return False
##    ar ando
    elif str1 == "ar" and len(str2) > 4 and str2[-4:] == "ando":
        return True
    elif str1 == "er" or str1 == "ir":
##        er ir yendo
        if words[0][-3] in ['a','e','i','o','u'] and len(str2) > 4 and str2[-4:] == "yendo":
            return True    
##        er iendo
        elif str1 == "er" and len(str2) > 5 and str2[-5:] == "iendo":
            return True
##        ir endo
        elif str1 == "ir" and len(str2) > 4 and str2[-4:] == "endo":
            return True
    return False

def calculate(str1):
    U = ""
    multU = 1
    I = ""
    multI = 1
    P = ""
    multP = 1
    for i in range(len(str1)):
        if(str1[i] == 'U' and str1[i+1] == "="):
            i = i+2
            while str1[i] != 'V':
                if str1[i] == 'm':
                    multU = 0.001
                elif str1[i] == 'k':
                    multU = 1000
                elif str1[i] == 'M':
                    multU = 1000000
                else:
                    U = U + str1[i]
                i = i+1
            U = float(U) * multU
        elif(str1[i] == 'P' and str1[i+1] == "="):
            i = i+2
            while str1[i] != 'W':
                if str1[i] == 'm':
                    multP = 0.001
                elif str1[i] == 'k':
                    multP = 1000
                elif str1[i] == 'M':
                    multP = 1000000
                else:
                    P = P + str1[i]
                i = i+1
            P = float(P) * multP
        elif(str1[i] == 'I' and str1[i+1] == "="):
            i = i+2
            while str1[i] != 'A':
                if str1[i] == 'm':
                    multI = 0.001
                elif str1[i] == 'k':
                    multI = 1000
                elif str1[i] == 'M':
                    multI = 1000000
                else:
                    I = I + str1[i]
                i = i+1
            I = float(I) * multI
    if isinstance(U, str) :
        return "U=" + str("{:.2f}".format(round(P/I,2))) + "V"
    elif isinstance(P, str) :
        return "P=" + str("{:.2f}".format(round(U*I,2))) + "W"
    elif isinstance(I, str) :
        return "I=" + str("{:.2f}".format(round(P/U,2))) + "A"

while(True):
    print("Menu\n\t1. Ejercicio1\n\t2. Ejercicio 2\n\t3. Ejercicio 3\n\t4. Salir")
    op = int(input("Elija una opcion: "))
    if op == 1:
        print("Respuesta: " + str(balanceo(input("Ingrese un set de parentesis y corchetes: "))))
    elif op == 2:
        print("Respuesta: " + str(gerundio(input("Ingrese un verbo y un conjugado: "))))
    elif op == 3:
        print( calculate(input("Ingrese los datos o el problema: ")))
    elif op == 4:
        print("bye, bye...")
        break
    else:
        print("Opcion incorrecta")
