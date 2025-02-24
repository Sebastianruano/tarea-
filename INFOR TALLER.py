class pacientes:
    def _init_ (self):
        self.__nombre= ""
        self.__cedula= 0
        self.__genero= ""
        self.__servicio= ""
        
    def verNombre(self):
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula    
    
    def asignarNombre(self, n):
        self.__nombre = n
    def asignarServicio(self, s):
        self.__servicio = s
    def asignarGenero(self, g):
        self.__genero = g
    def asignarCedula(self, c):
        self.__cedula = c

class Sistema:

    def __init__(self):
        self.__lista_pacientes = [ ]
        self.__numero_pacientes = len(self.__lista_pacientes)

    def ingresarPaciente(self):
        nombre = input("Ingrese el nombre: ")
        cedula = int(input("Ingrese la cedula: "))
        genero = input("Ingrese el genero: ")
        servicio = input("Ingrese el servicio: ")

        p = pacientes()
        p.asignarNombre(nombre)
        p.asignarCedula(cedula)
        p.asignarGenero(genero)
        p.asignarServicio(servicio)
        self.__lista_pacientes.append(p)
        self.__numero_pacientes = len(self.__lista_pacientes)

    def verNumeroPacientes(self):
        return self.__numero_pacientes
    
    def verDatosPacientes(self):
        cedula = int(input("Ingrese la cedula a buscar: "))
        for paciente in self.__lista_pacientes:
            if cedula == paciente.verCedula():
                print("Nombre: " + paciente.verNombre())
                print("Cedula" + str(paciente.verNombre()))
                print("Gener: " + paciente.verGenero())
                print("Servicio: " + paciente.verServicio())

sistema = Sistema()

while True:
    opcion = int(input("1. Nuevo Paciente -2. Numero de Pacientes -3. Datos Paciente -4.Salir"))
    if opcion == 1:
        sistema.ingresarPaciente()
    elif opcion == 2:
        print("Ahora hay: " + str(sistema.verNumeroPacientes()))
    elif opcion == 3:
        sistema.verDatosPacientes()
    elif opcion == 4:
        break
    else:
        print("Opcion invalida")
         