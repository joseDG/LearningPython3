import persona

class Profesor(persona.Persona):

    def __init__(self):
        self.__Antiguedad=""
        self.__Tutorias=""
        self.__Telefono=""
        super().__init__()

    def GetAntiguedad(self):
        return self.__Antiguedad

    def GetTutorias(self):
        return self.__Tutorias

    def GetTelefono(self):
        return self.__Telefono

    def SetAntiguedad(self, antiguedad):
        self.__Antiguedad = antiguedad

    def SetTutorias(self, tutorias):
        self.__Tutorias = tutorias

    def SetTelefono(self, telefono):
        self.__Telefono = telefono

    def MostrarProfesora(self):
        print("Profesor:")
        print("\tNombre:",self.GetNombre())
        print("\tApellidos:",self.GetApellidos())
        print("\tEdad:",self.GetEdad())
        print("\tAntiguedad:",self.__Antiguedad)
        print("\tTutorias:",self.__Tutorias)
        print("\tTelefono:",self.__Telefono)

    