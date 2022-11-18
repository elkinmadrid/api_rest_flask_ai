from Reglas import *

class sistemadereglas(KnowledgeEngine):

    diagnostic = ""
    id = 0

    @Rule(AND(reglas(ansiedad="No")),
             (reglas(perdida_interes=P(lambda x: x >= 1)  & P(lambda x: x <= 5))),
             (reglas(descontento="No")), 
             (reglas(altibajo="No")), 
             (reglas(apatia="No")))
    def regla1(self):
        self.id = 1
        self.diagnostic = 'Su salud mental es bastante estable, ¡Felicidades!'
        print('Regla 1: Su salud mental es bastante estable, ¡Felicidades!')
   
    @Rule(AND(reglas(ansiedad="No")),
             (reglas(perdida_interes=P(lambda x: x >= 1)  & P(lambda x: x <= 5))),
             (reglas(descontento="No")), 
             (reglas(altibajo="No")), 
             (reglas(apatia="Si")))
    def regla2(self):
        self.id = 2
        self.diagnostic = 'En el momento no presentas ningun diagnostico. Pero se recomienda realizar actividades entretenidas.'
        print('Regla 2: En el momento no presentas ningun diagnostico. Pero se recomienda realizar actividades entretenidas.')
    
    @Rule(AND(reglas(ansiedad="No")),
             (reglas(perdida_interes=P(lambda x: x >= 1)  & P(lambda x: x <= 5))), 
             (reglas(descontento="No")), 
             (reglas(altibajo="Si")), 
             (reglas(apatia="No")))
    def regla3(self):
        self.id = 3
        self.diagnostic = 'En el momento no presentas ningun diagnostico. Pero se recomienda diariamente ir construyendo buenas habilidades para afrentar estos alti bajos.'
        print('Regla 3: En el momento no presentas ningun diagnostico. Pero se recomienda diariamente ir construyendo buenas habilidades para afrontar estos alti bajos.')

    
    @Rule(AND(reglas(ansiedad="No")),
             (reglas(perdida_interes=P(lambda x: x >= 1)  & P(lambda x: x <= 5))), 
             (reglas(descontento="No")), 
             (reglas(altibajo="Si")), 
             (reglas(apatia="Si")))
    def regla4(self):
        self.id = 4
        self.diagnostic = 'En el momento no presentas ningun diagnostico. Pero se recomienda en este tipo de casos es muy viable alimentar la mente de manera positiva.'
        print('Regla 4: En el momento no presentas ningun diagnostico. Pero se recomienda en este tipo de casos, alimentar la mente de manera positiva.')


    @Rule(AND(reglas(ansiedad="No")),
             (reglas(perdida_interes=P(lambda x: x >= 1)  & P(lambda x: x <= 5))), 
             (reglas(descontento="Si")), 
             (reglas(altibajo="No")), 
             (reglas(apatia="No")))
    def regla5(self):
        self.id = 5
        self.diagnostic = 'En el momento no presentas ningun diagnostico. Pero se recomienda hacer meditacion dia por medio para mejorar este estilo de vida.'
        print('Regla 5: En el momento no presentas ningun diagnostico. Pero se recomienda hacer meditacion dia por medio para mejorar tu estilo de vida.')
    
    @Rule(AND(reglas(ansiedad="No")),
             (reglas(perdida_interes=P(lambda x: x >= 1)  & P(lambda x: x <= 5))), 
             (reglas(descontento="Si")), 
             (reglas(altibajo="No")), 
             (reglas(apatia="Si")))
    def regla6(self):
        self.id = 6
        self.diagnostic = 'En el momento no presentas ningun diagnostico. Pero se recomienda Entrenar la capacidad de entender las propias emociones como base para entender las de los demás.'
        print('Regla 6: En el momento no presentas ningun diagnostico. Pero se recomienda entrenar la capacidad de entender las propias emociones como base para entender las de los demás.')

    @Rule(AND(reglas(ansiedad="No")),
             (reglas(perdida_interes=P(lambda x: x >= 1)  & P(lambda x: x <= 5))),
             (reglas(descontento="Si")), 
             (reglas(altibajo="Si")), 
             (reglas(apatia="No")))
    def regla7(self):
        self.id = 7
        self.diagnostic = 'En el momento no presentas ningun diagnostico. Pero se recomienda para poder mejorar esto  se puede recurrir a la psicoterapia.'
        print('Regla 7: En el momento no presentas ningun diagnostico. Pero se recomienda para poder mejorar esto  se puede recurrir a la psicoterapia.')

    @Rule(AND(reglas(ansiedad="No")),
             (reglas(perdida_interes=P(lambda x: x >= 1)  & P(lambda x: x <= 5))), 
             (reglas(descontento="Si")), 
             (reglas(altibajo="Si")), 
             (reglas(apatia="Si")))
    def regla8(self):
        self.id = 8
        self.diagnostic = 'Necesitas hacerte una terapia de métodos como la hipnosis y la terapia cognitiva.'
        print('Regla 8: Necesitas hacer una terapia de métodos como la hipnosis y terapia cognitiva.')


    @Rule(AND(reglas(ansiedad="No")),
             (reglas(perdida_interes=P(lambda x: x >= 6)  & P(lambda x: x <= 10))), 
             (reglas(descontento="No")), 
             (reglas(altibajo="No")), 
             (reglas(apatia="No")))
    def regla9(self):
        self.id = 9
        self.diagnostic = 'En el momento no presentas ningun diagnostico. Pero se recomienda realizar distraerse con actividades opuestas.'
        print('Regla 9: En el momento no presentas ningun diagnostico. Pero se recomienda realizar distraerse con actividades opuestas.')


    @Rule(AND(reglas(ansiedad="No")),
             (reglas(perdida_interes=P(lambda x: x >= 6)  & P(lambda x: x <= 10))), 
             (reglas(descontento="No")), 
             (reglas(altibajo="No")), 
             (reglas(apatia="Si")))
    def regla10(self):
        self.id = 10
        self.diagnostic = 'En el momento no presentas ningun diagnostico. Pero se recomienda socializar un poco mas, para mejorar estas actitudes.'
        print('Regla 10: En el momento no presentas ningun diagnostico. Pero se recomienda socializar un poco mas, para mejorar estas actitudes.')

    @Rule(AND(reglas(ansiedad="No")),
             (reglas(perdida_interes=P(lambda x: x >= 6)  & P(lambda x: x <= 10))),
             (reglas(descontento="No")), 
             (reglas(altibajo="Si")), 
             (reglas(apatia="No")))
    def regla11(self):
        self.id = 11
        self.diagnostic = 'En el momento no presentas ningun diagnostico. Pero se recomienda que duerma bien y coma adecuadamente.'
        print('Regla 11: En el momento no presentas ningun diagnostico. Pero se recomienda que duerma bien y coma adecuadamente.')

    @Rule(AND(reglas(ansiedad="No")),
             (reglas(perdida_interes=P(lambda x: x >= 6)  & P(lambda x: x <= 10))), 
             (reglas(descontento="No")), 
             (reglas(altibajo="Si")), 
             (reglas(apatia="Si")))
    def regla12(self):
        self.id = 12
        self.diagnostic = 'En estos momentos usted esta presentando Sintomas de una patologia de demencia.'
        print('Regla 12: En estos momentos usted está presentando sintomas  de demencia.')

    @Rule(AND(reglas(ansiedad="No")),
             (reglas(perdida_interes=P(lambda x: x >= 6)  & P(lambda x: x <= 10))), 
             (reglas(descontento="Si")), 
             (reglas(altibajo="No")), 
             (reglas(apatia="No")))
    def regla13(self):
        self.id = 13
        self.diagnostic = 'En el momento no presentas ningun diagnostico. Pero se recomienda ser un ser humano ejemplar para las demas personas.'
        print('Regla 13: En el momento no presentas ningun diagnostico. Pero se recomienda ser un ser humano ejemplar para las demas personas.')


    @Rule(AND(reglas(ansiedad="No")),
             (reglas(perdida_interes=P(lambda x: x >= 6)  & P(lambda x: x <= 10))), 
             (reglas(descontento="Si")), 
             (reglas(altibajo="No")), 
             (reglas(apatia="Si")))
    def regla14(self):
        self.id = 14
        self.diagnostic = 'De acuerdo a sus respuestas, le informamos que esta presentando una fase de bipolaridad'
        print('Regla 14: De acuerdo a sus respuestas, le informamos que esta presentando una fase de Bipolaridad.')

    @Rule(AND(reglas(ansiedad="No")),
             (reglas(perdida_interes=P(lambda x: x >= 6)  & P(lambda x: x <= 10))), 
             (reglas(descontento="Si")), 
             (reglas(altibajo="Si")), 
             (reglas(apatia="No")))
    def regla15(self):
        self.id = 15
        self.diagnostic = 'respecto a su respuesta se llega a la conclusion que esta presentando sintomas de Trastorno por déficit de atención.'
        print('Regla 15: De acuerdo a sus respuestas se concluye que esta presentando sintomas de Trastorno por déficit de atención. ')

    @Rule(AND(reglas(ansiedad="No")),
             (reglas(perdida_interes=P(lambda x: x >= 6)  & P(lambda x: x <= 10))), 
             (reglas(descontento="Si")), 
             (reglas(altibajo="Si")), 
             (reglas(apatia="Si")))
    def regla16(self):
        self.id = 16
        self.diagnostic = 'Usted necesita ver un psiquiatra ya que esta manifestando sintomas de trastorno depresivo mayor'
        print('Regla 16: De acuerdo a sus respuestas está manifestando sintomas de Trastorno depresivo mayor, le sugerimos acudir a un psiquiatra.')    

    
    @Rule(AND(reglas(ansiedad="Si")),
             (reglas(perdida_interes=P(lambda x: x >= 1)  & P(lambda x: x <= 5))),
             (reglas(descontento="No")), 
             (reglas(altibajo="No")), 
             (reglas(apatia="No")))
    def regla17(self):
        self.id = 17
        self.diagnostic = 'En el momento no presentas ningun diagnostico. Pero se recomienda hacer ejercicios fisicos y comer saludable.'
        print('Regla 17: En el momento no presentas ningun diagnostico. Pero se recomienda hacer ejercicios fisicos y comer saludable.')

    @Rule(AND(reglas(ansiedad="Si")),
             (reglas(perdida_interes=P(lambda x: x >= 1)  & P(lambda x: x <= 5))),  
             (reglas(descontento="No")), 
             (reglas(altibajo="No")), 
             (reglas(apatia="Si")))
    def regla18(self):
        self.id = 18
        self.diagnostic = 'En el momento no presentas ningun diagnostico. Pero se recomienda tener mas comunicación con amistades o familiares.'
        print('Regla 18: En el momento no presentas ningun diagnostico. Pero se recomienda tener más comunicación con amistades o familiares.')

    @Rule(AND(reglas(ansiedad="Si")),
             (reglas(perdida_interes=P(lambda x: x >= 1)  & P(lambda x: x <= 5))),
             (reglas(descontento="No")), 
             (reglas(altibajo="Si")), 
             (reglas(apatia="No")))
    def regla19(self):
        self.id = 19
        self.diagnostic = 'En el momento no presentas ningun diagnostico. Pero se recomienda hacer deporte y realizar actividades mentales.'
        print('Regla 19: En el momento no presentas ningun diagnostico. Pero se recomienda hacer deporte y realizar actividades mentales.')

    @Rule(AND(reglas(ansiedad="Si")),
             (reglas(perdida_interes=P(lambda x: x >= 1)  & P(lambda x: x <= 5))), 
             (reglas(descontento="No")), 
             (reglas(altibajo="Si")), 
             (reglas(apatia="Si")))
    def regla20(self):
        self.id = 20
        self.diagnostic = 'En estos momentos Usted esta presentando sintomas de Trastorno bipolar.'
        print('Regla 20: De acuerdo a sus respuestas, está presentando sintomas de Trastorno bipolar.')

    @Rule(AND(reglas(ansiedad="Si")),
             (reglas(perdida_interes=P(lambda x: x >= 1)  & P(lambda x: x <= 5))), 
             (reglas(descontento="Si")), 
             (reglas(altibajo="No")), 
             (reglas(apatia="No")))
    def regla21(self):
        self.id = 21
        self.diagnostic = 'En el momento no presentas ningun diagnostico. Pero se recomienda subir tu autoestima con actividades de superamiento.'
        print('Regla 21: En el momento no presentas ningun diagnostico. Pero se recomienda realizar actividades de superamiento para aumentar tu autoestima.')

    @Rule(AND(reglas(ansiedad="Si")),
             (reglas(perdida_interes=P(lambda x: x >= 1)  & P(lambda x: x <= 5))), 
             (reglas(descontento="Si")), 
             (reglas(altibajo="No")), 
             (reglas(apatia="Si")))
    def regla22(self):
        self.id = 22
        self.diagnostic = 'Dado un breve analisis a sus respuestas usted esta presentando sintomas de EZQUIZOFRENIA.'
        print('Regla 22: Dado un breve analisis a sus respuestas usted esta presentando sintomas de Ezquizofrenia.')

    @Rule(AND(reglas(ansiedad="Si")),
             (reglas(perdida_interes=P(lambda x: x >= 1)  & P(lambda x: x <= 5))), 
             (reglas(descontento="Si")), 
             (reglas(altibajo="Si")), 
             (reglas(apatia="No")))
    def regla23(self):
        self.id = 23
        self.diagnostic = 'Usted esta padeciendo de Trastorno bipolar.'
        print('Regla 23: De acuerdo a sus respuestas, está presentando sintomas de Trastorno bipolar.')

    @Rule(AND(reglas(ansiedad="Si")),
             (reglas(perdida_interes=P(lambda x: x >= 1)  & P(lambda x: x <= 5))), 
             (reglas(descontento="Si")), 
             (reglas(altibajo="Si")), 
             (reglas(apatia="Si")))
    def regla24(self):
        self.id = 24
        self.diagnostic = 'Debido a sus respuestas esta se esta presentando un diagnostico de Trastorno por déficit de atención.'
        print('Regla 24: Debido a sus respuestas esta se esta presentando un diagnostico de Trastorno por déficit de atención.')

    @Rule(AND(reglas(ansiedad="Si")),
             (reglas(perdida_interes=P(lambda x: x >= 6)  & P(lambda x: x <= 10))), 
             (reglas(descontento="No")), 
             (reglas(altibajo="No")), 
             (reglas(apatia="No")))
    def regla25(self):
        self.id = 25
        self.diagnostic = 'En el momento no presentas ningun diagnostico. Pero se recomienda estar en lugares de tranquilidad y paz.'
        print('Regla 25: En el momento no presentas ningun diagnostico. Pero se recomienda estar en lugares de tranquilidad y paz.')

    @Rule(AND(reglas(ansiedad="Si")),
             (reglas(perdida_interes=P(lambda x: x >= 6)  & P(lambda x: x <= 10))),  
             (reglas(descontento="No")), 
             (reglas(altibajo="No")), 
             (reglas(apatia="Si")))
    def regla26(self):
        self.id = 26
        self.diagnostic = 'Usted esta presetando sintomas leves de Ezquizofrenia.'
        print('Regla 26: De acuerdo a sus respuestas, está presetando sintomas leves de Ezquizofrenia.')

    @Rule(AND(reglas(ansiedad="Si")),
             (reglas(perdida_interes=P(lambda x: x >= 6)  & P(lambda x: x <= 10))), 
             (reglas(descontento="No")), 
             (reglas(altibajo="Si")), 
             (reglas(apatia="No")))
    def regla27(self):
        self.id = 27
        self.diagnostic = 'Esta manejando sintomas de Demencia.'
        print('Regla 27: De acuerdo a sus respuestas, está manejando sintomas de Demencia.')

    @Rule(AND(reglas(ansiedad="Si")),
             (reglas(perdida_interes=P(lambda x: x >= 6)  & P(lambda x: x <= 10))), 
             (reglas(descontento="No")), 
             (reglas(altibajo="Si")), 
             (reglas(apatia="Si")))
    def regla28(self):
        self.id = 28
        self.diagnostic = 'Esta presentando trastorno de ansiedad, por favor necesitamos volverlo a valorar.'
        print('Regla 28: De acuerdo a sus respuestas, está presentando trastorno de ansiedad, por favor necesitamos volverlo a valorar.')

    @Rule(AND(reglas(ansiedad="Si")),
             (reglas(perdida_interes=P(lambda x: x >= 6)  & P(lambda x: x <= 10))),
             (reglas(descontento="Si")), 
             (reglas(altibajo="No")), 
             (reglas(apatia="No")))
    def regla29(self):
        self.id = 29
        self.diagnostic = 'Respecto a sus respuesta nos damos cuenta que tiene sintomas de EZQUIZOFRENIA.'
        print('Regla 29: De acuerdo a sus respuestas, está presentando sintomas de Ezquizofrenia.')

    @Rule(AND(reglas(ansiedad="Si")),
             (reglas(perdida_interes=P(lambda x: x >= 6)  & P(lambda x: x <= 10))),
             (reglas(descontento="Si")), 
             (reglas(altibajo="No")), 
             (reglas(apatia="Si")))
    def regla30(self):
        self.id = 30
        self.diagnostic = 'Usted padece de trastorno bipolar.'
        print('Regla 30: De acuerdo a sus respuestas, está presentando trastorno bipolar.')

    @Rule(AND(reglas(ansiedad="Si")),
             (reglas(perdida_interes=P(lambda x: x >= 6)  & P(lambda x: x <= 10))),
             (reglas(descontento="Si")), 
             (reglas(altibajo="Si")), 
             (reglas(apatia="No")))
    def regla31(self):
        self.id = 31
        self.diagnostic = 'Debido a su condicion debemos verlo nuevamente.'
        print('Regla 31: Debido a su condicion debemos verlo nuevamente.')

    @Rule(AND(reglas(ansiedad="Si")),
             (reglas(perdida_interes=P(lambda x: x >= 6)  & P(lambda x: x <= 10))),
             (reglas(descontento="Si")), 
             (reglas(altibajo="Si")), 
             (reglas(apatia="Si")))
    def regla32(self):
        self.id = 32
        self.diagnostic = 'Usted actualmente esta diagnosticado con Trastorno depresivo mayor como tal necesita una consulta especial en un centro psicologico.'
        print('Regla 32: De acuerdo a sus respuestas, actualmente se le diagnostica con Trastorno depresivo mayor, necesita una consulta especial en un centro psicologico.')

   
    