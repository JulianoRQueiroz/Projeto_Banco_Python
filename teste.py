from models.cliente import Cliente
from models.conta import Conta

cliente1: Cliente = Cliente('Juliano Queiroz', 'juju@gmail.com', '02508416061', '20/02/1991')
cliente2: Cliente = Cliente('Graziela Ascoleze', 'graziAscoleze@gmail.com', '00254415818', '14/07/1989')

print(cliente1)
print('------------------------------------------')
print(cliente2)


conta1: Conta = Conta(cliente1)
conta2: Conta = Conta(cliente2)

print(conta1)
print('------------------------------------------')
print(conta2)