import alumno
import profesor

alumno = alumno.Alumno()
alumno.SetNombre("Alfredo")
alumno.SetApellidos("Diaz")
alumno.SetEdad(35)
alumno.SetCurso("Bachillerato")
alumno.SetAsignaturas(["Matematicas","Tegnologia","Ingles"])
alumno.MostrarAlumno()

profesor = profesor.Profesor()
profesor.SetNombre("Jose")
profesor.SetApellidos("Diaz")
profesor.SetEdad(50)
profesor.SetAntiguedad(15)
profesor.SetTutorias([["Lunes","16-18"],["Jueves","12-14"],["Viernes","11-13"]])
profesor.SetTelefono("654123789")
profesor.MostrarProfesora()