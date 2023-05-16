#Elaborado por: Nicole Tatiana Parra Valverde y Mariano Soto
#Fecha de creacion: 15/05/2023 12:25am
#Ultima version: 15/05/2023 5:34pm
#Version: 3.10.6

#Importación de bibliotecas
import random
import names
import clases

#Declaración de variables globales
DEBUG = False # Se utiliza para facililar la depuración

#Declaración de funciones
def insertarPacientes(pPacientes, pCantidad):
    """
    Funcionalidad: Crea una cantidad de pacientes y los agrega a la lista
    Entradas:
    -pPacientes(list): La lista de pacientes que modificar
    -pCantidad(int): La cantidad de pacientes a generar
    Salidas:
    -pPacientes(list): La lista de pacientes modificada
    """
    for i in range(pCantidad):
        paciente = clases.Paciente()
        paciente.asignarCedula(f"{random.randint(0,9)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}")
        paciente.asignarNombre((names.get_first_name(),names.get_last_name(),names.get_last_name()))
        paciente.asignarCorreo(f"{paciente.mostrarNombre()[0][:2].lower()}{paciente.mostrarNombre()[1][:2].lower()}{paciente.mostrarNombre()[2][:2].lower()}@gmail.com")
        paciente.asignarAnotaciones([])
        paciente.asignarActivo(True)
        pPacientes.append(paciente)
        if DEBUG:
            print(paciente.mostrarCedula())

    return pPacientes

def modificarPaciente(pPacientes, pCedula, pAnotacion):
    """
    Funcionalidad: Agrega una anotación al paciente con cedula pCedula
    Entradas:
    -pPacientes(lista): La lista sobre la que buscar
    -pCedula(str): La cédula a buscar
    -pAnotacion(str): La anotación a agregar
    Salidas:
    -pPacientes(list): La lista de pacientes modificada
    """
    for paciente in pPacientes:
        if paciente.mostrarCedula() == pCedula:
            paciente.asignarAnotaciones(paciente.mostrarAsignaciones()+[pAnotacion])
    return pPacientes

def filtrarPacientes(pPacientes, filtros=[]):
    """
    Funcionalidad: Retorna todos los pacientes que cumplen con ciertos requisitos
    Entradas:
    -pPacientes(list): La lista de pacientes sobre la que buscar
    -filtros(list): La lista de filtros a utilizar sobre pPacientes
    Salidas:
    -paciente(Paciente): cada paciente que cumple con los requisitos
    """
    for paciente in pPacientes:
        if all([filtro(paciente) for filtro in filtros]):
            yield paciente


