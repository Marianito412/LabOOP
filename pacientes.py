import archivos

def ESModificarPaciente():
    cedula=input("Digite a cedula del paciente a agregar anotaciones: ")
    anotaciones=input("Ingrese las anotaciones: ")
    funciones.modificarPaciente(cedula,anotaciones)

def modificarEstado(pCedula):
    

def ESReportes(pDicc):
    """
    Funcionalidad: Muestra menu de reportes
    Entradas:
    -pDicc(dict): El diccionario a analizar
    Salidas:
    -pDicc(dict): El diccionario analizado
    """
    menuDicc = {

        1: ["Por personalidad", ESReportePersonalidades],
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
    personalidad = archivos.lee("personalidad") or {}
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