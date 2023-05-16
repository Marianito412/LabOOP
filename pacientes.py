import archivos
import funciones
import clases
import re

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

def ESReporteInactivos(pPacientes):
    for paciente in funciones.filtrarPacientes(pPacientes, filtros=[lambda x: not x.mostrarActivo()]):
        print(paciente.mostrarNombre())

def ESReportePaciente(pPacientes):
    cedula = validarCedula(input("Ingrese el número de cédula a buscar: "))
    
    try:
        paciente : clases.Paciente = next(funciones.filtrarPacientes(pPacientes, filtros=[lambda x: x.cedula==cedula]))
    except StopIteration:
        print("Paciente no encontrado")
        return pPacientes
    
    print(
        f"Nombre: {paciente.mostrarNombre()}\n"
        f"Correo: {paciente.mostrarCorreo()}")
    print("Anotaciones: ")
    for num, anotacion in enumerate(paciente.mostrarAsignaciones()):
        print(f"\t{num+1}. {anotacion}")
    print(f"Estado: {paciente.mostrarActivo()}")

def ESInsertarPacientes(pPacientes):
    cantidad = int(input("Ingrese la cantidad de pacientes a generar: "))
    pPacientes = funciones.insertarPacientes(pPacientes, cantidad)
    return pPacientes

def ESModificarPaciente(pPacientes):
    cedula=input("Digite a cedula del paciente a agregar anotaciones: ")
    anotaciones=input("Ingrese las anotaciones: ")
    pPacientes = funciones.modificarPaciente(cedula,anotaciones)
    return pPacientes

def modificarEstado(pPacientes):
    cedula = validarCedula(input("Digite a cedula del paciente a agregar anotaciones: "))
    for paciente in pPacientes:
        if paciente.mostrarCedula() == cedula:
            print(f"El estado actual del paciente es{paciente.mostrarActivo()}")
            if validarBin(input("Esta seguro de querer cambiar el estado?\nIngrese 1 o 2 (1: si, 2: no): "))==True:
                paciente.asignarActivo(not paciente.mostrarActivo())
                #if paciente.mostrarActivo() == True:
                #    paciente.asignarActivo(False)
                #else:
                #    paciente.asignarActivo(True)
    return pPacientes

def SalirReporte(pPacientes):
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
            if opcion == 3:
                break
        except ValueError:
            print("Por favor ingrese un número válido")
        except KeyError:
            print("Opción inválida")
    return pPacientes

def menu():
    """
    Funcionalidad: Muestra menu principal
    Entradas:NA
    Salidas:NA
    """
    personalidad = archivos.lee("pacientes") or []
    if personalidad == []:
        ESInsertarPacientes(personalidad)

    archivos.graba("pacientes", personalidad)

    menuDicc = {
        1: ["Registrar Datos", ESInsertarPacientes],
        2: ["Modificar Estado", modificarEstado],
        3: ["Modificar paciente", ESModificarPaciente],
        4: ["Reportes", ESReportes],
        5: ["Salir", exit]
    }
    
    while True:
        for key in menuDicc:
            print(f"{key}. {menuDicc[key][0]}")
        try:
            opcion = int(input("Ingrese el número de su opción a elegir: "))
            personalidad = menuDicc[opcion][1](personalidad)
            archivos.graba("pacientes", personalidad)
        except ValueError:
            print("Por favor ingrese un número válido")
        except KeyError:
            print("Opción inválida")

menu()