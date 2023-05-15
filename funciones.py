

def filtrarPacientes(pPacientes, filtros=[]):
    for paciente in pPacientes:
        if all([filtro(paciente) for filtro in filtros]):
            yield paciente