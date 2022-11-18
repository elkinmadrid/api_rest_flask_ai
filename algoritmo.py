# Datos
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.pipeline import Pipeline

class algoritmo():

    def initialize(self):



        data = pd.read_csv("creditos - copia.csv", delimiter=';')
        data = data[["monto_credito",
                            "Edad",
                    "estado_civil",
                    "educacion",
                    "sexo",
                            "pago"]]


        X = data.drop(columns='pago')
        y = data['pago'].values

        escalador = preprocessing.MinMaxScaler()

        X = escalador.fit_transform(X)

        # Separar en entrenamiento y prueba

        X_train,X_test,y_train,y_test = train_test_split(X,y,
                                                        test_size = 0.3,
                                                        random_state = 2352,
                                                        stratify = y)

        clasificador = KNeighborsClassifier(n_neighbors = 13, weights = 'uniform')
        clasificador.fit(X_test, y_test)
        clasificador.fit(X_train, y_train)

        monto_credito = 145000
        Edad = 25
        sexo = 1
        educacion = 2
        estado_civil = 3

        solicitante =  escalador.transform([[monto_credito,Edad, estado_civil,  educacion,sexo]])
        print("Clase", clasificador.predict(solicitante))
        print("Probabilidad x clase ¿", clasificador.predict_proba(solicitante))
        respuesta = {
            "clase": str(clasificador.predict(solicitante)[0]),
            "probabilidad": str(clasificador.predict_proba(solicitante)[0][0])
        }
        print(respuesta)
        return respuesta
