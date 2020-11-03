import re

def validIPAddress():
    p = re.compile('[0-2]{1}[0-9]{1,2}\.[0-2]{1}[0-9]{1,2}\.[0-2]{1}[0-9]{1,2}\.[0-2]{1}[0-9]{1,2}')

    if p.match(input("Ingrese un IP: ")):
        print ("IP valida")
    else:
        print ("IP no valida")

def validVariableName():
    p = re.compile('^[^0-9]')

    if p.match(input("Ingrese nombre de variable: ")):
        print ("Nombre valido")
    else:
        print ("Nombre no valido")

#Por ese motivo, me gustaría pedirle más información sobre los temas recientemente tocados. Estaria muy agradecido
def searchRequests():
    request = input("Enter request text: ")
    
    pattern = '(me gustaría pedirle|Les ruego que|les pido que|Solicito)'
    groups = re.findall(pattern, request)
    subject = ""
    if groups:
        for group in groups:
            print ("Request keywords: ",group)
            start = request.index(group) + len(group) + 1
            for i in range (start,len(request)):
                if request[i] == '.':
                    print ("Request: ",request[start:i])
                    break
    else:
        print ("No luck...\n")
while(True):
    print("\n\t\t\tMenu\n\t1. Ejercicio 1\n\t2. Ejercicio 2\n\t3. Ejercicio 3\n\t4. Salir")
    op = int(input("Elija una opcion: "))
    if op == 1:
        validIPAddress()
    elif op == 2:
        validVariableName()
    elif op == 3:
        searchRequests()
    elif op == 4:
        print("bye, bye...")
        break
    else:
        print("Opcion incorrecta")
