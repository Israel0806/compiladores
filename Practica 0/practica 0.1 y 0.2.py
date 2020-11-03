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
        
class TestExercise1(unittest.TestCase):
    def test_Exp1(self):
        self.assertFalse(balanceo("("))

    def test_Exp2(self):
        self.assertFalse(balanceo("((("))

    def test_Exp3(self):
        self.assertTrue(balanceo("()()"))

    def test_Exp4(self):
        self.assertTrue(balanceo("[ [ ( ) ] ]"))

    def test_Exp5(self):
        self.assertFalse(balanceo(")))"))

    def test_Exp6(self):
        self.assertFalse(balanceo("[)"))

    def test_Exp7(self):
        self.assertFalse(balanceo(")]"))

    def test_Exp8(self):
        self.assertFalse(balanceo("() ["))

    def test_Exp9(self):
        self.assertFalse(balanceo("[( )"))

    def test_Exp10(self):
        self.assertFalse(balanceo("[ ( [)] ]"))

    def test_Exp11(self):
        self.assertTrue(balanceo("[[[[[[[[[[()]]]]]]]]]]"))


class TestExercise2(unittest.TestCase):
    def test_Exp1(self):
        self.assertTrue(gerundio("amar amando"))

    def test_Exp2(self):
        self.assertTrue(gerundio("llover lloviendo"))

    def test_Exp3(self):
        self.assertTrue(gerundio("reir riendo"))

    def test_Exp4(self):
        self.assertTrue(gerundio("abatir abatiendo"))

    def test_Exp5(self):
        self.assertFalse(gerundio("caer caindo"))

    def test_Exp6(self):
        self.assertFalse(gerundio("correr correndo"))

    def test_Exp7(self):
        self.assertFalse(gerundio("salir salendo"))
    

if __name__ == '__main__':
    unittest.main()
