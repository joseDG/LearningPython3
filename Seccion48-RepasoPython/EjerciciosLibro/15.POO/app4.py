#NOTA HERENCIA
#la relacion "es un"
class Persona:
    def __init__(self):
        self.__Nombre = ""
        self.__Apellidos = ""
        self.__Edad = 0
    
    def GetNombre(self):
        return self.__Nombre
    
    def GetApellidos(self):
        return self.__Apellidos

    def GetEdad(self):
        return self.__Edad

    def SetNombre(self, nombre):
        self.__Nombre = nombre

    def SetApellidos(self, apellidos):
        self.__Apellidos = apellidos

    def SetEdad(self, edad):
        self.__Edad = edad



class Alumno(Persona):
    def __init__(self):
        self.__Curso = ""
        self.__Asignatura = ""

    def GetCurso(self):
        return self.__Curso

    def GetAsignatura(self):
        return self.__Asignatura
    
    def SetCurso(self, curso):
        self.__Curso = curso

    def SetAsignatura(self, asignatura):
        self.__Asignatura = asignatura

    def MostrarAlumno(self):
        print("Alumno:")
        print("\tNombre:",self.GetNombre())
        print("\tApellidos:",self.GetApellidos())
        print("\tEdad:",self.GetEdad())
        print("\tCurso:",self.__Curso)
        print("\tMatriculas:",self.__Asignatura)


class Profesor(Persona):
    def __init__(self):
        self.__Antiguedad = ""
        self.__Tutorias = ""
        self.__Telefono = ""
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


    def MostrarProfesor(self):
        print("Profesor:")
        print("\tNombre:",self.GetNombre())
        print("\tApellidos:",self.GetApellidos())
        print("\tEdad:",self.GetEdad())
        print("\tAntiguedad:",self.__Antiguedad)
        print("\tTutorias:",self.__Tutorias)
        print("\tTelefono:",self.__Telefono)

class Investigador(Persona):
    def __init__(self):
        self.__Especialidad = ""
        self.__Anos = ""
        super().__init__()

    def GetEspecialidad(self):
        return self.__Especialidad

    def GetAnos(self):
        return self.__Anos

    def SetEspecialidad(self, especialidad):
        self.__Especialidad = especialidad

    def SetAnos(self, anos):
        self.__Anos = anos

#Aplicando la herencia multiple
class ProfesorUniversitario(Profesor, Investigador):
    def __init__(self):
        self.__Universidad = ""
        self.__Departamento = ""
        super().__init__()

    def GetUniversidad(self):
        return self.__Universidad

    def GetDepartamento(self):
        return self.__Departamento

    def SetUniversidad(self, universidad):
        self.__Universidad = universidad

    def SetDepartamento(self, departamento):
        self.__Departamento = departamento

    def MostrarProfesorUniversitario(self):
        print("Profesor Universitario:")
        print("\tNombre:",self.GetNombre())
        print("\tApellidos:",self.GetApellidos())
        print("\tEdad:",self.GetEdad())
        print("\tAntiguedad:",self.GetAntiguedad())
        print("\tTutorias:",self.GetTutorias())
        print("\tTelefono:",self.GetTelefono())
        print("\tEspecialidad:",self.GetEspecialidad())
        print("\tAnos:",self.GetAnos())
        print("\tUniversidad:",self.GetUniversidad())
        print("\tDepartamento:",self.GetDepartamento())


alumno = Alumno()
alumno.SetNombre("Alfredo")
alumno.SetApellidos("Moreno")
alumno.SetEdad(35)
alumno.SetCurso("Bachillerato")
alumno.SetAsignatura(["Matematicas","Tecnologia","Ingles"])
alumno.MostrarAlumno()

profesor = Profesor()
profesor.SetNombre("Profesor")
profesor.SetApellidos("Casa Papel")
profesor.SetEdad(50)
profesor.SetAntiguedad(15)
profesor.SetTutorias([["Lunes","16-48"],["Jueves","12-14"],["Viernes","11-13"]])
profesor.SetTelefono("09+81173205")
profesor.MostrarProfesor()


profesor = ProfesorUniversitario()
profesor.SetNombre("Profesor")
profesor.SetApellidos("Casa Papel")
profesor.SetEdad(50)
profesor.SetAntiguedad(15)
profesor.SetTutorias([["Lunes","16-48"],["Jueves","12-14"],["Viernes","11-13"]])
profesor.SetTelefono("09+81173205")
profesor.SetEspecialidad("Desarrollo de Software")
profesor.SetAnos(15)
profesor.SetUniversidad("Universidad de Extremadura")
profesor.SetDepartamento("Lenguajes y Sistemas Informaticos")
profesor.MostrarProfesorUniversitario()






