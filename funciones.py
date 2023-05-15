import random
import names

def insertarPacientes(pCantidad):
    for i in range(pCantidad):
        clases.asignarCedula(f"{random.randint(0,9)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}")
        clases.asignarNombre(get_first_name(),names.get_last_name(),names.get_last_name())
        clases.asignarAnotaciones(["",""])
        clases.asignarActivo(True)
    return 

def modificarPaciente(pCedula,pAnotacion):
    clases.asignarAnotaciones([pAnotacion])

def modificarEstado(pCedula):
    clases.asignarActivo(True)