from msilib.schema import Class
import persona

class Alumno(persona.Persona):
    
    def __init__(self):
        self.__Curso = ""
        self.__Asignaturas = ""
        super().__init__()

    def GetCurso(self):
        return self.__Curso

    def GetAsignaturas(self):
        return self.__Asignaturas

    def SetCurso(self, curso):
        self.__Curso = curso

    def SetAsignaturas(self, asignaturas):
        self.__Asignaturas = asignaturas

    def MostrarAlumno(self):
        print("Alumno:")
        print("\tNombre:",self.GetNombre())
        print("\tApellidos:",self.GetApellidos())
        print("\tEdad:",self.GetEdad())
        print("\tCurso:",self.__Curso)
        print("\tAsignaturas:",self.__Asignaturas)
        
        