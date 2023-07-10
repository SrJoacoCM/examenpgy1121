asientos = list(range(1, 101))
comprar = [None] * 100
r_platinium= []
r_gold=[]
r_silver=[]
v_platinium = 120000
v_gold = 80000
v_silver = 50000
comprador=[]
def menu():
    print("""
    CONCIERTO MICHAEL JAM:

    1- Comprar Entradas
    2- Ver Asientos Disponibles
    3- Ver Listado De Asistentes
    4- Mostrar ganancias totales
    5- Salir
        """)
    
def comprar_entrada(comprador):
    nombre = input("\nIngrese su nombre: ")
    run = (input("\nIngrese su run (Sin punto ni digito verificador): "))
    while len(run)!=8 and run not in "123456789":
        run = input("Ingrese un run valido (ej:20694971): ")
        comprador = [nombre, run]
    while True:
        entrada = input("Ingrese el número del Asiento que desea comprar: ")
        if entrada.isdigit() and int(entrada) in asientos and comprar[int(entrada)-1] is None:
            entrada_index = int(entrada) - 1
            asientos[entrada_index] = "X"
            comprar[entrada_index] = comprador
            print("¡Entrada Comprada con éxito!")
            if int(entrada) >= 1 and int(entrada) <= 20:
                total = v_platinium
                r_platinium.append(total)
            elif int(entrada) >= 21 and int(entrada) <= 50:
                total = v_gold
                r_gold.append(total)
            elif int(entrada) >= 51 and int(entrada) <= 100:
                total = v_silver
                r_silver.append(total)
            print(f"El valor a cancelar es: {total}")
            return
        else:
            print("El número de asiento elegido no esta disponible")

def disponibilidad():
    print ("Los asientos disponibles saldran con su respectiva enumeracion y los asientos ocupados con una X: ")
    print(asientos)
    
def asistentes():
    print ("Asistentes al concierto: ")
    for i, comprador in enumerate(comprar):
        if comprador is not None:
            print(f"Asiento {i + 1} - Comprador: {comprador}")
def recaudacion():
    print(f"   Tipo Entrada     |  Cantidad   |   Total")
    print(f"Platinium $120.000  |      {len(r_platinium)}      |     {(len(r_platinium))*v_platinium}")
    print(f"Gold      $80.000   |      {len(r_gold)}      |     {(len(r_gold))*v_gold}")
    print(f"Silver    $50.000   |      {len(r_silver)}      |     {(len(r_silver))*v_silver}")
    print(f"TOTAL               |      {(len(r_silver))+(len(r_gold))+(len(r_platinium))}      |     {((len(r_silver))*v_silver)+((len(r_gold))*v_gold)+((len(r_platinium))*v_platinium)}")



def salir():
    print ("Joaquin Cabrera Macaya 10/07/23")

while True:
    menu()
    opcion = input("Ingrese una opción: ")

    while opcion not in "12345" or len(opcion)!=1:
        opcion = input("Ingrese una opción Valida: ")
    
    match opcion:

        case "1":
            disponibilidad()
            
            comprar_entrada(comprador)
        
        case "2":
            disponibilidad()
        
        case "3":
            asistentes()
        
        case "4":
            recaudacion()
        
        case "5":
            salir()
            break
