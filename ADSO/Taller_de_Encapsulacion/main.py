from CuentaBancaria import CuentaBancaria

cuenta = CuentaBancaria("Juan Perez", 100)

cuenta.mostrar()

cuenta.depositar(50)
cuenta.retirar(30)

cuenta.mostrar()

# prueba de error
try:
    cuenta.saldo = -200
except ValueError as e:
    print("Error:", e)