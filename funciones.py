import random
import names
import clases

def insertarPacientes(pPacientes, pCantidad):
    for i in range(pCantidad):
        paciente = clases.Paciente()
        paciente.asignarCedula(f"{random.randint(0,9)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}")
        paciente.asignarNombre((names.get_first_name(),names.get_last_name(),names.get_last_name()))
        paciente.asignarCorreo(f"{paciente.mostrarNombre()[0][:2].lower()}{paciente.mostrarNombre()[1][:2].lower()}{paciente.mostrarNombre()[2][:2].lower()}@gmail.com")
        paciente.asignarAnotaciones(["",""])
        paciente.asignarActivo(True)
        pPacientes.append(paciente)

    return pPacientes

def modificarPaciente(pPacientes, pCedula, pAnotacion):
    for paciente in pPacientes:
        if paciente.mostrarCedula() == pCedula:
            paciente.asignarAnotaciones([pAnotacion])
    return pPacientes

def modificarEstado(pCedula):
    for paciente in pPacientes:
        if paciente.mostrarCedula() == pCedula:
            paciente.asignarActivo(False)
    return pPacientes

    clases.asignarActivo(True)

def filtrarPacientes(pPacientes, filtros=[]):
    for paciente in pPacientes:
        if all([filtro(paciente) for filtro in filtros]):
            yield paciente


