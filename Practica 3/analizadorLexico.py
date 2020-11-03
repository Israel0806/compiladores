class Token:
    word = "" #almacena una copia de la palabra
    idx = -1 #en donde apareció en la sentencia
    type = "" #E (entero), V (variable), O (operador)
    def toString(self):
        return ("Token[" + self.word + "]: pos = " + str(self.idx) + ", tipo = " + self.type)

def getNumber (line, idx):
    number = 0
    token = Token()
    token.idx = idx
    multiplier = 1
    while idx < len(line) and line[idx].isdigit():
        number = number * multiplier + int(line[idx])
        multiplier = multiplier * 10
        idx = idx + 1
    token.word = str(number)
    token.type = 'E'
    return token,idx

def getVariable (line, idx):
    token = Token()
    token.idx = idx
    var = ""
    while idx < len(line) and (line[idx].isalpha() or line[idx].isdigit()):
        var = var + line[idx]
        idx = idx + 1
    token.word = var
    token.type = 'V'
    return token, idx

def getOperator (line, idx):
    token = Token()
    token.idx = idx
    var = ""
    while idx < len(line) and line[idx] in ['+','-','*','/','=','(',')']:
        var = var + line[idx]
        idx = idx + 1

    token.word = var
    token.type = 'O'
    return token, idx


def analizadorLexico ( line ):
    tokens = []
    idx = 0
    while idx < len(line):
##          <”1546”,E,0> , 4
##          <”78”,E,13> , 15
        if line[idx].isdigit():
            token, idx = getNumber ( line, idx)
            tokens.append(token);
        elif line[idx].isalpha():
            token, idx = getVariable ( line, idx)
            tokens.append(token);
        elif line[idx] in ['+','-','*','/','=','(',')']:
            token, idx = getOperator(line, idx)
            tokens.append(token)
        else:
            idx = idx + 1
    # Completar: obviar los espacios
    # Completar: tokenizar los operandos +-*/()
    return tokens;

tokens = analizadorLexico ( input("Enter a statement: ") )
for token in tokens:
    print ( token.toString() )