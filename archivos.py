#Elaborado por: Nicole Tatiana Parra Valverde y Mariano Soto
#Fecha de creacion: 15/05/2023 12:25am
#Ultima version: 15/05/2023 5:34pm
#Version: 3.10.6

import pickle

#Definición de funciones
def graba(nomArchGrabar, varGuardar):
    """
    Funcionalidad: Graba un archivo
    Entradas:
    -nomArchGrabar(str): Nombre del archivo a escribir
    -varGuardar(any): La variable a guardar
    Salidas: NA
    """
    try:
        f=open(nomArchGrabar,"wb")
        pickle.dump(varGuardar,f)
        f.close()
    except:
        print("Error al grabar el archivo: ", nomArchGrabar)

def lee (nomArchLeer):
    #Función que lee un archivo con una lista de estudiantes
    """
    Funcionalidad: Lee un archivo
    Entradas:
    -nomArchGrabar(str): Nombre del archivo a leer
    Salidas: NA
    """
    lista=[]
    try:
        f=open(nomArchLeer,"rb")
        lista = pickle.load(f)
        f.close()
        return lista
    except FileNotFoundError:
        print("Archivo no encontrado: ", nomArchLeer)