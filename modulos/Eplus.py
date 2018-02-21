import pandas as pd
import time

class readEP:
    def __init__(self,archivo,nombres):
        self.datos  = pd.read_csv(archivo,sep=',',skiprows=[0],names=nombres)
        self.datos[nombres[0]] =self.datos[nombres[0]].str.replace(" ","",n=2)
        self.datos[nombres[0]] = self.datos[nombres[0]].str.replace(" ","/2017 ")
        self.datos[nombres[0]] = self.datos[nombres[0]].str.replace(" 24:00:00", " 23:59:59")
        self.datos[nombres[0]] = pd.to_datetime(self.datos[nombres[0]])
        self.datos.set_index(nombres[0], inplace=True)
