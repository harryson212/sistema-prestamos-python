class CuentaBancaria:

    def __init__(self, titular, saldo=0):
        self._titular = titular
        self._saldo = saldo

    # =========================
    # TITULAR (solo lectura)
    # =========================
    @property
    def titular(self):
        return self._titular

    # =========================
    # SALDO (con control)
    # =========================
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):

        if valor < 0:
            raise ValueError("El saldo no puede ser negativo")

        self._saldo = valor

    # =========================
    # DEPOSITAR
    # =========================
    def depositar(self, cantidad):

        if cantidad > 0:
            self.saldo = self._saldo + cantidad  # usa setter
            return True

        return False

    # =========================
    # RETIRAR
    # =========================
    def retirar(self, cantidad):

        if cantidad > 0 and cantidad <= self._saldo:
            self.saldo = self._saldo - cantidad  # usa setter
            return True

        return False

    # =========================
    # MOSTRAR
    # =========================
    def mostrar(self):
        print("Titular:", self._titular)
        print("Saldo:", self._saldo)
        print("-------------------")