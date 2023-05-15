
class Paciente:
    def __init__(self):
        cedula=""
        nombreCompleto=("nombre", "apellido1", "apellido2")
        correo = ""
        anotaciones=[]
        activo = True
    
    def asignarCedula(self,pCedula):
        """
        Funcionalidad: Asigna la cedula
        Entrada: el número de cedula (string)
        Salida: Asigna un numero al atributo cedula del paciente
        """   
        self.cedula=pCedula
        return
    
    def asignarNombre(self,pNombre):
        """
        Funcionalidad: Asigna el nombre
        Entrada: el nombre del paciente (string)
        Salida: Asigna un nombre al atributo nombreCompleto del paciente
        """   
        self.nombreCompleto=pNombre
        return
    
    def asignarCorreo(self,pCorreo):
        """
        Funcionalidad: Asigna el correo
        Entrada: el correo electronico (string)
        Salida: Asigna un str al atributo correo del paciente
        """   
        self.correo=pCorreo
        return
    
    def asignarAnotaciones(self,pAnotaciones):
        """
        Funcionalidad: Asigna la cedula
        Entrada: el número de cedula (string)
        Salida: Asigna un numero al atributo cedula del paciente
        """   
        self.anotaciones=pAnotaciones
        return
    
    def asignarActivo(self,pActivo):
        """
        Funcionalidad: Asigna el estado de activo
        Entrada: el estado de activo (bool)
        Salida: Asigna un estado al atributo activo del paciente
        """   
        self.activo=pActivo
        return
    
    def mostrarCedula(self):
        """
        Funcionalidad: Devuelve el numero de cedula
        Entrada: N/A
        Salida: Número de cedula del paciente
        """   
        return self.cedula
    
    def mostrarNombre(self):
        """
        Funcionalidad: Devuelve el nombre
        Entrada: N/A
        Salida: Nombre del paciente
        """   
        return self.nombreCompleto

    def mostrarCorreo(self):
        """
        Funcionalidad: Devuelve el correo
        Entrada: N/A
        Salida: Correo del paciente
        """   
        return self.correo
    
    def mostrarAsignaciones(self):
        """
        Funcionalidad: Devuelve las anotaciones de las asignaciones
        Entrada: N/A
        Salida: Asignaciones del paciente
        """   
        return self.anotaciones
    
    def mostrarActivo(self):
        """
        Funcionalidad: Devuelve el estado del activo
        Entrada: N/A
        Salida: activo del paciente
        """   
        return self.activo
    
    def indicarDatos(self):
        return self.cedula,self.nombreCompleto,self.correo,self.anotaciones,self.activo

