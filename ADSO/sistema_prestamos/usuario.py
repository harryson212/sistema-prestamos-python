class Usuario:

    def __init__(self, documento, nombre):
        self.documento = documento
        self.nombre = nombre

    def mostrar_usuario(self):

        print("Documento:", self.documento)
        print("Nombre:", self.nombre)
        print("______")