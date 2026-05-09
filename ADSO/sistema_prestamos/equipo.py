class Equipo:

    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.disponible = True

    def mostrar_equipo(self):

        estado = "Disponible"

        if self.disponible == False:
            estado = "Prestado"

        print("Código:", self.codigo)
        print("Nombre:", self.nombre)
        print("Estado:", estado)
        print("__________   ")