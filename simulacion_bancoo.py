# Miguel Marines
# Actividad: Simulación de Banco

# """

# El programa permite al usuario:

# 1. Crear Cuenta
# 2. Abonar a cuneta
# 3. Cargar a cuenta
# 4. Mostrar estado de cuenta
# 5. Mostrar estado de todas las cunetas
# 6. Saldo de una cuenta en diferente divisa
# 7. Pasar cambio de divisa a archivo de texto
# 8. Transferencia de cuenta a cuenta
# 9. Salir

# """


import numpy as np

# Funcion que permite al usuario __________CREAR UNA CUENTA__________ designar un nombre y un saldo inicial.

def crear_cuenta(cuentas, nombre, saldo):
    continua = True
    contador = 0
    
    for i in range(len(cuentas)):
        if(cuentas[i][0] == 0 and continua == True):
            cuentas[i][0] = i+1
            cuentas[i][1] = nombre
            cuentas[i][2] = saldo
            contador += 1
            continua = False
    
    if (contador != 1):
        print("Ya no hay espacio en la base de datos para registrar nuevas cuentas, por favor acuda a otra sucursal.")


# Funcion que permite al usuario __________DEPOSITAR__________ designar una cantidad y abonar esa cantidad a un saldo inicial.

def abonar(cuentas, num_cuenta, abono):
    for i in range(len(cuentas)):
        if(cuentas[i][0] == num_cuenta):
            cuentas[i][2] = cuentas[i][2] + abono


# Funcion que permite al usuario __________RETIRAR__________ designar una cantidad y retirar esa cantidad a un saldo inicial.

def retirar(cuentas, num_cuenta, retiro):
    for i in range(len(cuentas)):
        if(cuentas[i][0] == num_cuenta):
            cuentas[i][2] = cuentas[i][2] -  retiro


# Funcion que permite al usuario mostrar el __________ESTADO DE CUENTA__________ de una cuenta en especifico.

def estado_cuenta(cuentas, num_cuenta):
    print("No.Cuenta  Nombre  Cantidad")
    for i in range(len(cuentas)):
        if(cuentas[i][0] == num_cuenta):
            print(cuentas[i][0],"         ",cuentas[i][1],"   ",cuentas[i][2])  


# Funcion que permite al usuario mostrar el __________ESTADO DE CUENTAS__________ de TODAS LAS CUENTAS.

def estados_cuentas(cuentas):
    print("No.Cuenta  Nombre  Cantidad")
    for i in range(len(cuentas)):
        if(cuentas[i][0] != 0):
            print(cuentas[i][0],"         ",cuentas[i][1],"   ",cuentas[i][2])  

    
# Funcion que permite al usuario hacer un __________CAMBIO DE DIVISAS__________ de un saldo de una cuenta en especifico.

def cambio_divisa(cuentas, num_cuenta):
    conversion = 0
    for i in range(len(cuentas)):
         
        if(cuentas[i][0] == num_cuenta):
            
            menu_divisas()
            opcion = int(input("Ingrese la divisa: "))
            
            if opcion == 1:
                print("Dolar Estadunidense")
                dolar = float(input("Ingrese el valor acutal del dolar: "))
                conversion = (cuentas[i][2] - 1) / dolar
                print(conversion)
            elif opcion == 2:
                print("Dolar Canadiense")
                dolar_canadiense = float(input("Ingrese el valor acutal del dolar canadiense: "))
                conversion = (cuentas[i][2] - 1) / dolar_canadiense
                print(conversion)
            elif opcion == 3:
                print("Euro")
                euro = float(input("Ingrese el valor acutal del euro: "))
                conversion = (cuentas[i][2] - 1) / euro 
                print(conversion)
            elif opcion == 4:
                print("Libra")
                libra = float(input("Ingrese el valor acutal de la libra: "))
                conversion = (cuentas[i][2] - 1) / libra
                print(conversion)
            elif opcion == 5:
                print("Salió con exito")
            else:
                print("Ingrese una opcion valida")
    return conversion
        

def escribe_archivo(cuentas, num_cuenta, name):
    
    file = open(name, "w")
    for i in range(1):
        conversion = str(cambio_divisa(cuentas, num_cuenta))
        file.write(conversion)
        file.write('\n')
    file.close()
            

# Funcion que permite al usuario hacer una __________TRANSFERENCIA__________ de una cantidad en especifico de una cuenta a otra cuenta.

def transferencia(cuentas, num_cuenta1, num_cuenta2, cantidad):
    
    comprobacion_cuenta1 = 0
    comprobacion_cuenta2 = 0
    comprobacion_cuenta = 0

    for i in range(len(cuentas)):
        
        if(cuentas[i][0] == num_cuenta1): 
            comprobacion_cuenta1 += 1
        
        if(cuentas[i][0] == num_cuenta2):
            comprobacion_cuenta2 += 2
            
            
    if(comprobacion_cuenta1 != 1):
        print("No se encontró la cuenta que hace la transferencia, por favor verifique el número de cuenta.")
    
    if(comprobacion_cuenta2 != 2):
        print("No se encontró la cuenta que recibe la transferencia, por favor verifique el número de cuenta.")
        
        
    comprobacion_cuenta = comprobacion_cuenta1 + comprobacion_cuenta2
    
    if(comprobacion_cuenta != 3):
        print("Ocurrió un problema por favor realize de nuevo la operación.")
        
    if(comprobacion_cuenta == 3):
        
        if(cuentas[num_cuenta1 - 1][2] >= cantidad):
            cuentas[num_cuenta1 - 1][2] = cuentas[num_cuenta1 - 1][2] - cantidad
            cuentas[num_cuenta2 - 1][2] = cuentas[num_cuenta2 - 1][2] + cantidad

        if(cuentas[num_cuenta1 -1][2] < cantidad):
            print("La cuenta que hace la transferencia, no cuenta con suficientes fondos para realizar la transferencia.")
        

# Funcion del menu que permitira al usuario ve el __________MENU__________ de opciones que contiene este programa.

def menu():
    print("\n#---------------------------------------------#")
    print("#                      BANCO                  #")
    print("#                  Miguel Marines             #")
    print("#---------------------------------------------#")
    
    
    print("\nSeleccione Una Opción del menú: ")
    print()
    print("1. Crear Cuenta")
    print("2. Abono a cuneta")
    print("3. Cargo a cuenta")
    print("4. Estado de cuenta")
    print("5. Estado de todas las cunetas")
    print("6. Saldo en diferente divisa")
    print("7. Pasar cambio de divisa a archivo de texto")
    print("8. Transferencia de cuenta a cuenta")
    print("9. Salir")
    print()
    

# Funcion del menu que permitira al usuario ve el __________MENU_DE_DIVISAS__________ de opciones que contiene este programa.
def menu_divisas():
    
    print("Opciones de Divisa: ")
    print()
    print("1. Dolar Estadunidense")
    print("2. Dolar Canadiense")
    print("3. Euro ")
    print("4. Libra")
    print("5. Cancelar")
    print("v")
    
    
# __________ MAIN __________
def main():
    
    # Matriz con las cuentas
    cuentas = [
    [1, 'Pedro', 1000],
    [2, 'Juan', 2500], 
    [3, 'Pablo', 1500],
    [4, 'Andres',2100],
    [5, 'Mario', 4500],
    [6, 'Jose', 900],
    [7, 'Andrea',1100],
    [8, 'Valeria',3300],
    [9, 'Manuel', 5000],
    [10, 'Victor', 7300],
    [0,'',0],
    [0,'',0],
    [0,'',0],
    [0,'',0],
    [0,'',0]
    ]
    
    # Variable para controlar la continuidad de la ejecución del programa.
    continua = True
    
    # Ciclo While, para continuar ejecutando el programa mientras la variable continua sea TRUE.
    while continua:
        
        #Función para ejecutar el menú.
        menu()
        
        # Variable que almacena la el input del usuario según la opción que seleccionó del menú.
        opcion = int(input("Seleccione una opcion del menu: "))
        
        # If's y Elif's para ejecutar la parte del programa adecuada según el input del usuario.
        
        # Opcion 1 crear una cuenta.
        if opcion == 1:
            
            # Inputs del usuario (parametros de la funcion).
            nombre = str(input("Ingrese el nombre del titular de la cuenta: "))
            saldo = float(input("Ingrese el saldo inicial de la cuenta: "))
            
            # Llamado a la funcion con sus parametros.
            crear_cuenta(cuentas, nombre, saldo)
            
        # Opcion 2 hacer un abono/deposito.
        elif opcion == 2:
            
            # Inputs del usuario (parametros de la funcion).
            num_cuenta = int(input("Ingrese el numero de cuenta: "))
            abono = float(input("Ingrese la cantidad que se va a abonar: "))
            
            # Llamado a la funcion con sus parametros.
            abonar(cuentas, num_cuenta, abono)
       
       # Opcion 3 hacer un retiro.
        elif opcion == 3:
            
            # Inputs del usuario (parametros de la funcion).
            num_cuenta = int(input("Ingrese el numero de cuenta: "))
            retiro = float(input("Ingrese la cantidad que se va a retirar: "))
            
            # Llamado a la funcion con sus parametros.
            retirar(cuentas, num_cuenta, retiro)
            
        # Opcion 4 mostrat estado de UNA cuenta.
        elif opcion == 4:
            
            # Input del usuario (parametro de la funcion).
            num_cuenta = int(input("Ingrese el numero de cuenta: "))
            
            # Llamado a la funcion con su parametro.
            estado_cuenta(cuentas, num_cuenta)
        
        # Opcion 5 mostar estado de TODOAS las cuentas.
        elif opcion == 5:
            
            # Llamado a la funcion con su parametro.
            estados_cuentas(cuentas)
        
        # Opcion para hacer una conversion de divisas.
        elif opcion == 6:
            
            # Input del usuario (parametro de la funcion).
            num_cuenta = int(input("Ingrese el numero de cuenta: "))
            
            # Llamado a la funcion con su parametro.
            cambio_divisa(cuentas, num_cuenta)

        
        elif opcion == 7:
            '''
            # Inputs del usuario (parametros de la funcion).
            num_cuenta = int(input("Ingrese el numero de cuenta: "))
            name = str(input("Ingrese el archivo de texto en el que desea poner los valores: "))
           
            # Llamado a la funcion con sus parametros.
            escribe_archivo(cuentas, num_cuenta, name)
            
            np.savetxt('matriz.txt', cuentas)'''
            
            
        # Opcion para realizar transferencia entre cuentas.
        elif opcion == 8:
            
            # Inputs del usuario (parametros de la funcion).
            num_cuenta1 = int(input("Ingrese el numero de cuenta que va a hacer la transferencia: "))
            num_cuenta2 = int(input("Ingrese el numero de cuenta que va a recibir la transferencia: "))
            cantidad = float(input("Ingrese la cantidad a transferir: "))
            
            # Llamado a la funcion con sus parametros.
            transferencia(cuentas, num_cuenta1, num_cuenta2, cantidad)
        
        elif opcion == 9:
            print("Se cerró de forma correcta el prgrama.")
            print("Gracias por su preferencia.")
            continua = False
              
        else:
            print("Error, por favor ingrese una opcion valida")


main()


# ___________ CASOS_DE_PRUEBA ____________


# """
# input: 1
# input: Jorge
# input: 1000
# input: 5
# output:
# No.Cuenta  Nombre  Cantidad
# 1           Pedro     1000
# 2           Juan     2500
# 3           Pablo     1500
# 4           Andres     2100
# 5           Mario     4500
# 6           Jose     900
# 7           Andrea     1100
# 8           Valeria     3300
# 9           Manuel     5000
# 10           Victor     7300
# 11           Jorge     1000.0


# input: 2
# input: 3
# input: 50
# input: 5
# output:
# No.Cuenta  Nombre  Cantidad
# 1           Pedro     1000
# 2           Juan     2500
# 3           Pablo     1550.0
# 4           Andres     2100
# 5           Mario     4500
# 6           Jose     900
# 7           Andrea     1100
# 8           Valeria     3300
# 9           Manuel     5000
# 10           Victor     7300
# 11           Jorge     1000.0


# input: 3
# input: 4
# input: 200
# input: 5
# output:
# No.Cuenta  Nombre  Cantidad
# 1           Pedro     1000
# 2           Juan     2500
# 3           Pablo     1500
# 4           Andres     1900.0
# 5           Mario     4500
# 6           Jose     900
# 7           Andrea     1100
# 8           Valeria     3300
# 9           Manuel     5000


# input: 4
# input: 4
# output:
# No.Cuenta  Nombre  Cantidad
# 4           Andres     1900.0


# input: 5
# output:
# No.Cuenta  Nombre  Cantidad
# 1           Pedro     1000
# 2           Juan     2500
# 3           Pablo     1500
# 4           Andres     1900.0
# 5           Mario     4500
# 6           Jose     900
# 7           Andrea     1100
# 8           Valeria     3300
# 9           Manuel     5000
# 10           Victor     7300


# input: 6
# input: 1
# input: 1
# input: 20
# output: 49.95


# input: 6
# input: 2
# input: 2
# input: 15
# output: 166.6


# input: 6
# input: 2
# input: 3
# input: 24
# output: 104.125


# input: 6
# input: 10
# input: 4
# input: 21
# output: 347.57142857142856


# input: 6
# input: 5
# input: 5
# output: Salio con exito


# input: 9
# output: Se cerró de forma correcta el prgrama.


# input: 0
# output: Error, por favor ingrese una opcion valida