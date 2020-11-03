tokenSeparator = ":="


class Produccion:
    izq = "" #Componente de la izquierda
    der = [] #Componente(s) de la derecha
    
    def __init__(self, produc):
        tmp = produc.split(tokenSeparator)
        if(len(tmp) != 2):
            print("Produccion mal declarada")
        self.izq = tmp[0].strip()
        self.der = tmp[1].strip().split(" ")
        for token in self.der:
            token = token.strip()
        
        
    def print(self):
        print(self.izq + " " + tokenSeparator + " " + ' '.join(self.der) )

class Gramatica:
    production = [] #Lista de producciones
    terminals = [] #Conjunto de terminales
    nonTerminals = [] #no terminals
    tas = {}

    primeros = {}
    siguientes = {}

##    Ubicar la produccion desde la cual se origino
##    el elemento nodoT (primeros de nodoNt)
##    Retornar una lista de la produccion
    def buscarProduccion(self, nodoNt, nodoT):
        nodos = []
        for proc in self.production:
            if proc.izq == nodoNt:
                if proc.der[0] == nodoT or proc.der[0] in self.nonTerminals:
                    for der in proc.der:
                        nodos.append(der)
        # print("New table entry: ", end='')
        # print(nodos)
        return nodos
            
            
    
    ##        self.tablaSintactica["F"] = {}
    ##        self.tablaSintactica["E"]["("] = ["T", "Ep"]
    def crearTabla(self):
        self.tas = {}
        for nodoNT in self.nonTerminals:
            for nodoT in self.getPrimero(nodoNT):
                if nodoT != "lambda":
                    # print("construct " + nodoNT + " with: " + nodoT)
                    if self.tas.get(nodoNT) == None:
                        self.tas[nodoNT] = {}
                    self.tas[nodoNT][ nodoT ] = self.buscarProduccion( nodoNT, nodoT)
                else:
                    for nodoT2 in self.getSiguiente(nodoNT):
                        if self.tas.get(nodoNT) == None:
                            self.tas[nodoNT] = {}
                        self.tas[nodoNT][nodoT2] = ["lambda"]
            print()
                # self.tas[?][?] = ? depende de su implementación

    def printTabla(self):
        for nonTerminalKeys in self.tas:
            for terminalKeys in self.tas[nonTerminalKeys]:
                print( "[" + nonTerminalKeys + "][" + terminalKeys + "] : ", end = '')
                print(' '.join(self.tas[nonTerminalKeys][terminalKeys]))


    def cargar(self, filename):
        #cargar un texto en gramatica
        archivo = open( filename, 'r')
        producciones = archivo.readlines()
        archivo.close()
        for produc in producciones:
            tmp = Produccion(produc)
            # print(tmp)
            self.production.append(tmp)

##            anhadir los token terminales donde correspondan
            if tmp.izq in self.terminals:
                self.terminals.remove(tmp.izq)
                self.nonTerminals.append(tmp.izq)
            elif not (tmp.izq in self.nonTerminals):
                self.nonTerminals.append(tmp.izq)
            
            for der in tmp.der:
                # anhadir nuevo token a terminales
                if (not (der in self.terminals) and not (der in self.nonTerminals)) or der == "lambda": 
                    self.terminals.append(der)

##        self.terminals = list( dict.fromkeys(self.terminals) )
##        self.nonTerminals = list( dict.fromkeys(self.nonTerminals) )
            
            
    def getPrimeros (self):
        for nodo in self.nonTerminals:
            self.primeros[nodo] = self.getPrimero(nodo)
        return self.primeros
    
    def getPrimero (self, nodo ):
        #Encontrar todas las producciones donde nodo esté a la izquierda.
        #Para todas ellas verificar el primer nodo de la derecha.
        prim = []
        for proc in self.production:
            if proc.izq == nodo:
                node = proc.der[0]
                #Si es nodo terminal, guardarlo como un primero
                if node in self.terminals:
                    prim.append(node)
                #Si es nodo no-terminal, lanzar la llamada de getPrimero a tal nodo.
                elif node in self.nonTerminals:
                    if node in self.primeros:
                        prim.extend(self.primeros[node])
                    else:
                        prim.extend(self.getPrimero(node))
                     
        return prim
        # retornar todos los no-terminales primeros.
    
    def getSiguiente(self, node): 
        siguientes = []
        # print("FOR NODE: " + node)
        for produc in self.production:
            for index in range(len(produc.der)):
                currentNode = produc.der[index]
                if node != currentNode:
                    continue
                # print(produc.izq, end =" := ")
                # print(produc.der)

                # print("CurrentNode: " + currentNode)
                if currentNode in self.terminals:
                    continue
                # Si es que no existiera un nodo a la derecha, su siguiente
                # será el siguiente del lado izquierdo de su producción original
                if index == len(produc.der) - 1:
                    # print("last pos")
                    siguientes.extend(self.siguientes[produc.izq])
                    # print(siguientes)
                else:    
                    nextNode = produc.der[index + 1]
                    # print("nextNode: " + nextNode)
                    if nextNode in self.terminals:
                        # print("next is terminal")
                        siguientes.append(nextNode)
                        continue
                    # El siguiente de un nodo, es el primero del nodo de su derecha
                    # print("add primeros")
                    siguientes.extend(self.primeros[nextNode])
                    siguientes.remove("lambda")
                    # Si uno de los primeros incluye lambda
                    if produc.izq in self.siguientes  and "lambda" in self.primeros[produc.izq]:
                        # print("add when lambda")
                        siguientes.extend(self.siguientes[produc.izq])
                        
        return siguientes


    
    def getSiguientes (self):
        i = 0
        for node in self.production:
            self.siguientes[node.izq] = []
            if i == 0:
                self.siguientes[node.izq] = ["$"]
                i = i + 1
            
            self.siguientes[node.izq].extend(self.getSiguiente(node.izq))
            self.siguientes[node.izq] =  list( dict.fromkeys(self.siguientes[node.izq]) )
            
        return self.siguientes;
            
            
    def getProduction(self, izq):
        print("Productions of " + izq)
        for produc in self.production:
            if produc.izq == izq:
                produc.print()

    def getProductions(self):
        return self.production
        #retornar el componente(s) de la derecha de la
        #produccion apuntada por izq
    def print(self): #Crear una función para imprimir
        for produc in self.production:
            produc.print()


gram = Gramatica()
gram.cargar("gramatica.txt")
gram.getPrimeros()
print()
print("primeros")
for prim in gram.primeros:
    print(prim, end =": ")
    print(gram.primeros[prim])

# print("Temrinales")
# print(gram.terminals)
gram.getSiguientes()
print()
print("Siguientes")
for sig in gram.siguientes:
    print(sig, end =": ")
    print(gram.siguientes[sig])

print("Tabla sintactica:")
gram.crearTabla()
gram.printTabla()

# =============================================================================
# print("Tabla sintactica de prediccion")
# tsp.print()
# gram = Gramatica()
# gram.cargar("gramatica.txt")
# gram.getProduccion("F")
# print("Gramatica cargada")
# gram.print()    
# =============================================================================


