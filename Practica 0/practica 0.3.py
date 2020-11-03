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


n = int(input())
result = []
for i in range(n):
    result.append(calculate(input()))

for i in range(n):
    print(f"Problem #{i+1}")
    print(result[i])
    print()

##P = U*I
##U = P/I
##I = P/U
##P = 2.5M/2
##P = 2500000/2
##M = 1000000
##k = 1000
##m = 0.001
