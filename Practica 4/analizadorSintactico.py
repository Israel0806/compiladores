tokenSeparator = ":="

class TSP:
    terminals = []
    nonTerminals = []
    tablaSintactica = {} # mapea NoTerminales vs Terminales => produccion
    def __init__(self):
        self.tablaSintactica["E"] = {}
        self.tablaSintactica["Ep"] = {}
        self.tablaSintactica["T"] = {}
        self.tablaSintactica["Tp"] = {}
        self.tablaSintactica["F"] = {}

        self.tablaSintactica["E"]["("] = ["T", "Ep"]
        self.tablaSintactica["E"]["num"] = ["T", "Ep"]
        self.tablaSintactica["E"]["id"] = ["T", "Ep"]
        self.tablaSintactica["Ep"]["+"] = ["+","T", "Ep"]
        self.tablaSintactica["Ep"]["-"] = ["-","T", "Ep"]
        self.tablaSintactica["Ep"][")"] = ["lambda"]
        self.tablaSintactica["Ep"]["$"] = ["lambda"]
        self.tablaSintactica["T"]["("] = ["F", "Tp"]
        self.tablaSintactica["T"]["num"] = ["F", "Tp"]
        self.tablaSintactica["T"]["id"] = ["F", "Tp"]
        self.tablaSintactica["Tp"]["+"] = ["lambda"]
        self.tablaSintactica["Tp"]["-"] = ["lambda"]
        self.tablaSintactica["Tp"]["*"] = ["*", "F", "Tp"]
        self.tablaSintactica["Tp"]["/"] = ["/", "F", "Tp"]
        self.tablaSintactica["Tp"][")"] = ["lambda"]
        self.tablaSintactica["Tp"]["$"] = ["lambda"]
        self.tablaSintactica["F"]["("] = ["(E)"]
        self.tablaSintactica["F"]["num"] = ["num"]
        self.tablaSintactica["F"]["id"] = ["id"]
    def print(self):
        for nonTerminalKeys in tsp.tablaSintactica:
            print()
            for terminalKeys in tsp.tablaSintactica[nonTerminalKeys]:
                print( "[" + nonTerminalKeys + "][" + terminalKeys + "] : ", end = '')
                print(' '.join(tsp.tablaSintactica[nonTerminalKeys][terminalKeys]))
        
        

class Produccion:
    izq = "" #Componente de la izquierda
    der = [] #Componente(s) de la derecha
    
    def __init__(self, produc):
        tmp = produc.split(tokenSeparator)
        if(len(tmp) != 2):
            print("Produccion mal declarada")
        self.izq = tmp[0].strip()
        self.der = tmp[1].split(" ")
        for token in self.der:
            token = token.strip()
                    
        
    def print(self):
        print(self.izq + " " + tokenSeparator + " " + ' '.join(self.der) )

class Gramatica:
    production = [] #Lista de producciones
    terminals = [] #Conjunto de terminales
    nonTerminals = [] #no terminals
    def cargar(self, filename):
        #cargar un texto en gramatica
        archivo= open( filename, 'r')
        producciones = archivo.readlines()
        archivo.close()
        for produc in producciones:
            tmp = Produccion(produc)
            for nonTerminalKeys in tsp.tablaSintactica:
                for terminalKeys in tsp.tablaSintactica[nonTerminalKeys]:
                    if(tmp.der == terminalKeys):
                        self.terminals.append(tmp.der)
                    else:
                        self.nonTerminals.append(tmp.der)

            self.production.append(tmp)

    def getProduccion(self, izq):
        print("Productions of " + izq)
        for produc in self.production:
            #print("A comparar: " + produc.izq + " = " + izq)
            if produc.izq == izq:
                produc.print()

        #retornar el componente(s) de la derecha de la
        #produccion apuntada por izq
    def print(self): #Crear una función para imprimir
        for produc in self.production:
            produc.print()


tsp = TSP()
print("Tabla sintactica de prediccion")
tsp.print()
gram = Gramatica()
gram.cargar("gramatica.txt")
gram.getProduccion("F")
print("Gramatica cargada")
gram.print()    


