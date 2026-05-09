class Prestamo:

    def __init__(self, usuario, equipo):
        self.usuario = usuario
        self.equipo = equipo

    def mostrar_prestamo(self):

        print("Usuario:", self.usuario.nombre)
        print("Equipo:", self.equipo.nombre)
        print("-------------------")