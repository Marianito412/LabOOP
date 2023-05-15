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
    for paciente in funciones.filtrarPacientes(pPacientes, filtros=[lambda x: x.cedula=="123"]):
        print(paciente.nombreCompleto)

def ESReportePaciente(pPacientes):
    cedula = validarCedula(input("Ingrese el número de cédula a buscar: "))
    
    try:
        paciente : clases.Paciente = next(funciones.filtrarPacientes(pPacientes, filtros=[lambda x: x.cedula==cedula]))
    except StopIteration:
        print("Paciente no encontrado")
        return pPacientes
    
    print(
        f"Nombre: {paciente.nombreCompleto}\n"
        f"Correo: {paciente.correo}")
    print("Anotaciones: ")
    for num, anotacion in enumerate(paciente.anotaciones):
        print(f"\t{num+1}. {anotacion}")
    print(f"Estado: {paciente.activo}")

a = clases.Paciente()
a.nombreCompleto="hello"
a.cedula = "5-0446-0741"
b= clases.Paciente()
b.cedula="123"
b.nombreCompleto="alooo"
pacientes = [clases.Paciente(), a, b]
ESReportePaciente(pacientes)

def ESReportes(pDicc):
    """
    Funcionalidad: Muestra menu de reportes
    Entradas:
    -pDicc(dict): El diccionario a analizar
    Salidas:
    -pDicc(dict): El diccionario analizado
    """
    menuDicc = {

        1: ["Pacientes inactivos", ESReporteInactivos],
        2: ["Por categoría", ESPorCategorias],
        3: ["Por persona", ESReportePersona],
        4: ["Reporte total", ESReporteTotal],
        5: ["Salir a menu", SalirReporte]
    }
    while True:
        for key in menuDicc:
            print(f"{key}. {menuDicc[key][0]}")
        try:
            opcion = int(input("Ingrese el número de su opción a elegir: "))
            menuDicc[opcion][1](pDicc)
            if opcion == 5:
                break
        except ValueError:
            print("Por favor ingrese un número válido")
        except KeyError:
            print("Opción inválida")
    return pDicc

def menu():
    """
    Funcionalidad: Muestra menu principal
    Entradas:NA
    Salidas:NA
    """
    personalidad = archivos.lee("personalidad") or []
    ESRegistrarDatos(personalidad)
    while validarBin(input("Desea registrar más personas? (1: sí, 2: no): ")):
        ESRegistrarDatos(personalidad)
    archivos.graba("personalidad", personalidad)
    menuDicc = {
        1: ["Registrar Datos", ESRegistrarDatos],
        2: ["Modificar Datos", ESModificarDatos],
        3: ["Eliminar Datos", ESEliminarDatos],
        4: ["Reportes", ESReportes],
        5: ["Salir", exit]
    }
    
    while True:
        for key in menuDicc:
            print(f"{key}. {menuDicc[key][0]}")
        try:
            opcion = int(input("Ingrese el número de su opción a elegir: "))
            personalidad = menuDicc[opcion][1](personalidad)
            archivos.graba("personalidad", personalidad)
        except ValueError:
            print("Por favor ingrese un número válido")
        except KeyError:
            print("Opción inválida")
