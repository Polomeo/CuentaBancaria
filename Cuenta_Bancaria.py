# Proyecto Día 7 - Cuenta Bancaria
from os import system

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        datos = f'''
        Cliente: {self.apellido}, {self.nombre}
        Cuenta N°: {self.numero_cuenta}
        Balance: ${self.balance}
        '''
        return datos
    
    def depositar(self, monto):
        '''
        Deposita monto en la cuenta
        '''
        self.balance += monto

    def retirar(self, monto):
        '''
        Permite extraer dinero de la cuenta
        '''
        self.balance -= monto

    def tiene_saldo_disponible(self, monto):
        '''
        (Bool) Comprueba si el saldo disponible es mayor a monto
        '''
        if monto > self.balance:
            return False
        else:
            return True

def crear_cliente():
    '''
    Función que permite crear un nuevo cliente del banco
    Retorna un objeto de tipo Cliente
    '''
    print(' Crear nuevo cliente '.center(70,'*'))
    nombre = input('Por favor, ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    numero_cuenta = int(input('Ingrese el número de cuenta: '))
    cliente = Cliente(nombre, apellido, numero_cuenta)
    print(f'Bienvenido al Banco Esperanza señor/a {apellido.capitalize()}')
    return cliente

def inicio():
    '''
    Función que ejecuta el programa
    '''
    cliente = ''
    salir = False
    
    system('cls')
    print(' Bienvenido al Banco Esperanza '.center(70,'*'))
    if cliente == '':
        cliente = crear_cliente()
    
    while not salir:
        system('cls')
        print(' Menú principal '.center(70, '*'))
        print('''
[1] - Depositar
[2] - Retirar
[3] - Ver balance
[4] - Salir
''')
        eleccion = 0
        while eleccion not in range(1,5):
            eleccion = int(input('¿Qué desea hacer? (Opción 1 a 3): '))

        match eleccion:
            # Depositar
            case 1: 
                system('cls')
                print(' Depositar '.center(70,'*'))
                monto = int(input('¿Cuánto desea depositar?: '))
                cliente.depositar(monto)
                print(f'Se han depositado $ {monto}.- en la cuenta. Balance: $ {cliente.balance}.')
                volver = ''
                while volver.lower() != 'v':
                        volver = input('Presione "v" para Volver.')
                else:
                    continue
            
            # Retirar   
            case 2:
                system('cls')
                print(' Retirar '.center(70,'*'))
                monto = int(input('¿Cuánto desea retirar?: '))
                if cliente.tiene_saldo_disponible(monto):
                    cliente.retirar(monto)
                    print(f'Se han retirado $ {monto}.- (Balance: $ {cliente.balance})')
                    volver = ''
                    while volver.lower() != 'v':
                        volver = input('Presione "v" para Volver.')
                    else:
                        continue
                
                else:
                    print(f'No tiene suficiente saldo disponible. Saldo disponible: $ {cliente.balance}.-')
                    volver = ''
                    while volver.lower() != 'v':
                        volver = input('Presione "v" para Volver.')
                    else:
                        continue
            
            # Ver balance
            case 3:
                system('cls')
                print(' Balance '.center(70,'*'))
                print(cliente)
                volver = ''
                while volver.lower() != 'v':
                        volver = input('Presione "v" para Volver.')
                else:
                    continue
            
            # Salir
            case 4:
                system('cls')
                salir = True
                break
    
    print(' Gracias por usar el sistema de cuentas '.center(70,'*'))

# Programa
inicio()
