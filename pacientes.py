#Elaborado por: Nicole Tatiana Parra Valverde y Mariano Soto
#Fecha de creacion: 15/05/2023 12:25am
#Ultima version: 15/05/2023 5:34pm
#Version: 3.10.6

#Importación de bibliotecas
import archivos
import funciones
import clases
import re

#Definición de funciones
def validarCedula(pCedula: str):
    """
    Funcionalidad: valida una cédula contra regex
    Entradas:
    -pCedula(str): la cedula a validar
    Salidas:
    -pCedula: la cédula si cumple con las validaciones
    """
    while True:
        if re.match(r"[\d]{1}-[\d]{4}-[\d]{4}", pCedula):
            return pCedula
        else:
            pCedula = input("ERROR: Cédula inválida, recuerde usar el siguente formato: 0-0000-0000\nIntente de nuevo: ")

def validarBin(pString: str):
    """
    Funcionalidad: Valida un sí o no y retorna el binario
    Entradas:
    -pEntrada(str): Texto conteniendo sí o no
    Salida:
    return(bool): True si sí, False si no 
    """
    while True:
        if pString in ["1", "2"]:
            return pString == "1"
        else:
            pString = input("ERROR: Opción inválida, ingrese 1 o 2 (1: si, 2: no)\nIntente de nuevo: ")

def limpiarNombre(pNombre):
    """
    Funcionalidad: Saca el nombre de la tupla
    Entradas:
    -pNombre(tuple): tupla que contiene el nombre y los apellidos
    Salida:
    -return(str): string con el nombre y los apellidos 
    """
    return f"{pNombre[0]} {pNombre[1]} {pNombre[2]}"

def ESReporteInactivos(pPacientes):
    """
    Funcionalidad: Llama a las funciones necesarias para mostrar el reporte de pacientes inactivos
    Entradas:
    -pPacientes(list): Contiene a los pacientes
    Salida:
    return(list):  Lista de pacientes
    """
    for paciente in funciones.filtrarPacientes(pPacientes, filtros=[lambda x: not x.mostrarActivo()]):
        print("_"*100)
        print(
            f"Nombre: {limpiarNombre(paciente.mostrarNombre())}\n"
            f"Correo: {paciente.mostrarCorreo()}"
            )
        print("Anotaciones: ")
        for num, anotacion in enumerate(paciente.mostrarAsignaciones()):
            print(f"\t{num+1}. {anotacion}")
        print(f"Estado: {'activo' if paciente.mostrarActivo() else 'inactivo'}")
        print("_"*100)
    return pPacientes

def ESReportePaciente(pPacientes):
    """
    Funcionalidad: Muestra la informacion de un solo paciente
    Entradas:
    -pPacientes(list): Contiene a los pacientes
    Salida:
    return(list):  Lista de pacientes
    """
    cedula = validarCedula(input("Ingrese el número de cédula a buscar: "))
    
    try:
        paciente : clases.Paciente = next(funciones.filtrarPacientes(pPacientes, filtros=[lambda x: x.cedula==cedula]))
    except StopIteration:
        print("No es paciente aún")
        return pPacientes
    print("_"*100)
    print(
        f"Nombre: {limpiarNombre(paciente.mostrarNombre())}\n"
        f"Correo: {paciente.mostrarCorreo()}")
    print("Anotaciones: ")
    for num, anotacion in enumerate(paciente.mostrarAsignaciones()):
        print(f"\t{num+1}. {anotacion}")
    print(f"Estado: {'activo' if paciente.mostrarActivo() else 'inactivo'}")
    print("_"*100)
    return pPacientes

def ESInsertarPacientes(pPacientes):
    """
    Funcionalidad: Pide la cantidad de pacientes y llama a la funcion insertarPacientes
    Entradas:
    -pPacientes(list): lista de pacientes
    Salida:
    return(list):  Lista de pacientes
    """
    cantidad = int(input("Ingrese la cantidad de pacientes a generar: "))
    pPacientes = funciones.insertarPacientes(pPacientes, cantidad)
    return pPacientes

def ESModificarPaciente(pPacientes):
    """
    Funcionalidad: Llama a las funciones necesarias para agregarle reportes a un paciente en especifico
    Entradas:
    -pPacientes(list): Contiene a los pacientes
    Salida:
    return(list):  Lista de pacientes
    """
    cedula = validarCedula(input("Digite a cedula del paciente a agregar anotaciones: "))
    anotaciones=input("Ingrese las anotaciones: ")
    pPacientes = funciones.modificarPaciente(pPacientes, cedula, anotaciones)
    print("La anotación se agregó exitosamente!")
    return pPacientes

def modificarEstado(pPacientes):
    """
    Funcionalidad: Llama a las funciones necesarias para modificar el estado actual de un paciente
    Entradas:
    -pPacientes(list): Contiene a los pacientes
    Salida:
    return(list):  Lista de pacientes
    """
    cedula = validarCedula(input("Digite a cedula del paciente a actualizar el estado: "))
    for paciente in pPacientes:
        if paciente.mostrarCedula() == cedula:
            print(f"El estado actual del paciente es {'activo' if paciente.mostrarActivo() else 'inactivo'}")
            if validarBin(input("Esta seguro de querer cambiar el estado?\nIngrese 1 o 2 (1: si, 2: no): "))==True:
                paciente.asignarActivo(not paciente.mostrarActivo())
                print("Se actualizó el estado exitosamente! ")
                return pPacientes
            else:
                print("Se canceló el cambio!")
                return pPacientes    
    print("El paciente no existe!")
    return pPacientes

def SalirReporte(pPacientes):
    """
    Funcionalidad: Muestra mensaje para regresar al menú principal
    Entradas:
    -pPacientes: Lista de pacientes luego de uso en menú de reportes
    Salidas:
    -pPacientes: Lista de pacientes luego de uso en menú de reportes
    """
    print("Regresando a menu principal...")
    return pPacientes

def ESReportes(pPacientes):
    """
    Funcionalidad: Muestra menu de reportes
    Entradas:
    -pDicc(dict): El diccionario a analizar
    Salidas:
    -pDicc(dict): El diccionario analizado
    """
    menuDicc = {

        1: ["Pacientes inactivos", ESReporteInactivos],
        2: ["Reporte de paciente", ESReportePaciente],
        3: ["Salir a menu", SalirReporte]
    }
    while True:
        for key in menuDicc:
            print(f"{key}. {menuDicc[key][0]}")
        try:
            opcion = int(input("Ingrese el número de su opción a elegir: "))
            menuDicc[opcion][1](pPacientes)
            print("\n")
            if opcion == 3:
                break
        except ValueError:
            print("Por favor ingrese un número válido")
        except KeyError:
            print("Opción inválida")
    return pPacientes

def ESSalir(pPacientes):
    """
    Funcionalidad: LLama a exit (se creó por restricciones de la estructuda, se necesita que la función reciba pPacientes)
    Entradas:
    -pPacientes: Argumento forzado por estructura del menú
    Salidas:NA
    """
    exit()

def menu():
    """
    Funcionalidad: Muestra menu principal
    Entradas:NA
    Salidas:NA
    """
    pacientes = archivos.lee("pacientes") or []
    if pacientes == []:
        ESInsertarPacientes(pacientes)

    archivos.graba("pacientes", pacientes)

    menuDicc = {
        1: ["Registrar Datos", ESInsertarPacientes],
        2: ["Modificar Estado", modificarEstado],
        3: ["Agregar anotaciones", ESModificarPaciente],
        4: ["Reportes", ESReportes],
        5: ["Salir", ESSalir]
    }
    
    while True:
        for key in menuDicc:
            print(f"{key}. {menuDicc[key][0]}")
        try:
            opcion = int(input("Ingrese el número de su opción a elegir: "))
            pacientes = menuDicc[opcion][1](pacientes)
            print("\n")
            archivos.graba("pacientes", pacientes)
        except ValueError:
            print("Por favor ingrese un número válido")
        except KeyError:
            print("Opción inválida")

#Programa principal
menu()