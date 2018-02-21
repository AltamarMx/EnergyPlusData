import pandas as pd
import time

class readEP:
    """
    Class to read csv files from an EnergyPlus Simulation and load data into a DataFrame.

    Use:
    readEP(arg1,arg2)

    Parameters
    ----------
    arg1 : path of the file to load into a DataFrame
        csv file containing date in the first column and variables in the followings.
        arg1 = 'data/cubo.csv'
    arg2 : list of names of the columns
        Always the first column should be time, and the user should define the name each column. t is suggested for time.
        arg2 = ['t','Ein','Eout', 'Nin','Nout', 'Oin','Oout', 'Sin','Sout', 'Pin','Pout','Tein','Teout']

    Returns
    -------
    DataFrame
        Returns a DataFrame with the date/time column as index for easy manipulation or visualization.

    """
    
    
    def __init__(self,archivo,nombres):
        self.datos  = pd.read_csv(archivo,sep=',',skiprows=[0],names=nombres)
        self.datos[nombres[0]] =self.datos[nombres[0]].str.replace(" ","",n=2)
        self.datos[nombres[0]] = self.datos[nombres[0]].str.replace(" ","/2017 ")
        self.datos[nombres[0]] = self.datos[nombres[0]].str.replace(" 24:00:00", " 23:59:59")
        self.datos[nombres[0]] = pd.to_datetime(self.datos[nombres[0]])
        self.datos.set_index(nombres[0], inplace=True)
