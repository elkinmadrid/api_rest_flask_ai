from Reglas import *

class sistemadereglas(KnowledgeEngine):

   
    @Rule(AND(reglas(ingresos="No")),
             (reglas(contrato="No")), 
             (reglas(antiguedad="No")), 
             (reglas(tipo_credito="No")), 
             (reglas(meses_credito="No")))
    def regla1(self):
        print('regla1 -- Credito personal')
   
    