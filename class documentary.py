class Documentaire():
    _count =0
   
    def __init__(self, code ,title, date):
        self.__code = code
        self.__title = title
        self.__date = date
        Documentaire._count += 1
#getters and setters 
    def getcode(self,):
        return self.__code
    def setcode(self):
        return self.__code
    
    def gettitle(self):
        return self.__title
    def settitle(self):
        return self.__title
    
    
    def getdate(self):
        return self.__date
    def setdate(self):
        return self.__date
#methodes
    def Tostring(self):
        print("the code is =", self.getcode())
        print("the titile is =", self.gettitle())
        print("the date is =", self.gettitle())

    def Equals(self,C):
        code1 = self.getcode()
        code2 = C.getcode()

        if (code1 == code2):
            return True
        else:
            return False
class exemplaire(Documentaire):
    def __init__(self, code ,title, date, numero, date_d_achat ):
        super().__init__ (code ,title, date)
        self.__numero = numero
        self.__date_d_achat = date_d_achat

    def getnumero(self):
        return self.__numero

    def setnumero(self, numero):
        self.__numero = numero
    
    def getdate_d_achat(self):
        return self.__date_d_achat

    def setdate_d_achat(self,date_d_achat):
        self.__date_d_achat = date_d_achat
#methodes
    def Tostring(self):
        print("the code is =", self.getcode())
        print("the titile is =", self.gettitle())
        print("the date is =", self.getdate())
        print("the numero is =", self.getnumero())
        print("the date of achat is =", self.getdate_d_achat())

    def Equals(self, n2):
        numero1 = self.getcode()
        numero2 = n2.getcode()
        if (numero1 == numero2):
            return True
        else:
            return False
        
