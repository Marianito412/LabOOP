import random
import names
import clases

def insertarPacientes(pPacientes, pCantidad):
    for i in range(pCantidad):
        pedro = clases.Paciente()
        pedro.asignarCedula(f"{random.randint(0,9)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}")
        pedro.asignarNombre((names.get_first_name(),names.get_last_name(),names.get_last_name()))
        pedro.asignarAnotaciones(["",""])
        pedro.asignarActivo(True)
        
        pedro.asignarCorreo(f"{pedro.mostrarNombre()[0][:2].lower()}{pedro.mostrarNombre()[1][:2].lower()}{pedro.mostrarNombre()[2][:2].lower()}@gmail.com")
        print(pedro.mostrarNombre())
        print(pedro.mostrarCorreo())
        pPacientes.append(pedro)

    return pPacientes

def modificarPaciente(pPacientes, pCedula, pAnotacion):
    for paciente in pPacientes:
        if paciente.mostrarCedula() == pCedula:
            paciente.asignarAnotaciones([pAnotacion])
    return pPacientes

def modificarEstado(pCedula):
    clases.asignarActivo(True)


insertarPacientes([], 5)