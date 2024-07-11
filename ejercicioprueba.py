
import os

# Limpia la pantalla
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

# Definición de los pedidos
pedidos = []

# Registrar un pedido       
def registrar_pedido():
    limpiar_pantalla()
    print("opcion de Registro de Pedido")
    nombre = input("Ingrese nombre: ").strip()
    apellido = input("Ingrese apellido: ").strip()
    direccion = input("Ingrese direccion: ").strip()
    comuna = input("Ingrese comuna: ").strip()
    
    cilindros_5kg = 0 #contador
    cilindros_15kg = 0 #contador
    cilindros_45kg = 0 #contador

    while True:
        print("Seleccione tipo de cilindro:\n 1. 5kg\n 2. 15kg\n 3. 45kg")
        tipo_cilindro = input("Seleccione una opcion: ").strip()
        
        if tipo_cilindro not in ["1", "2", "3"]:
            print("Tipo de cilindro no valido.")
            continue
        
        try:
            cantidad = int(input("Ingrese la cantidad de cilindros: ").strip())
        except ValueError:
            print("Cantidad no valida.")
            continue
        
        if tipo_cilindro == "1":
            cilindros_5kg += cantidad
        elif tipo_cilindro == "2":
            cilindros_15kg += cantidad
        elif tipo_cilindro == "3":
            cilindros_45kg += cantidad
        
        otro = input("¿Desea agregar otro tipo de cilindro? (s/n): ").strip().lower()
        if otro != 's':
            break

    pedido = {
        "nombre": nombre,
        "apellido": apellido,
        "direccion": direccion,
        "comuna": comuna,
        "cilindros_5kg": cilindros_5kg,
        "cilindros_15kg": cilindros_15kg,
        "cilindros_45kg": cilindros_45kg
    }
    
    pedidos.append(pedido)
    print(f"Pedido registrado con éxito para: {nombre} {apellido}")

# Listar todos los pedidos
def listar_pedidos():
    limpiar_pantalla()
    print("Lista de todos los pedidos:")
    if not pedidos:
        print("No hay pedidos registrados.")
        return
    for p in pedidos:
        print(f"Cliente: {p['nombre']} {p['apellido']}, direccion: {p['direccion']}, Comuna: {p['comuna']}, Cil. 5kg: {p['cilindros_5kg']}, Cil. 15kg: {p['cilindros_15kg']}, Cil. 45kg: {p['cilindros_45kg']}")

# Imprimir hoja de ruta 
def imprimir_hoja_ruta():
    limpiar_pantalla()
    print("opcion de Imprimir Hoja de Ruta")
    comunas = ["maipu", "cerrillos", "pudahuel"]
    print("Seleccione una comuna:")
    for i, comuna in enumerate(comunas, 1):
        print(f"{i}. {comuna}")
    
    try:
        op = int(input("Seleccione una opcion: ").strip())
        if op not in range(1, len(comunas) + 1):
            print("opcion no valida.")
            return
        comuna_elegida = comunas[op - 1]
    except ValueError:
        print("Por favor ingrese un numero valido.")
        return

    try:
        pedidos_comuna = [p for p in pedidos if p['comuna'].lower() == comuna_elegida.lower()]
        
        if not pedidos_comuna:
            print(f"No hay pedidos para la comuna {comuna_elegida}.")
            return
        
        with open(f"hoja_ruta{comuna_elegida}.txt", "w") as file:
            for p in pedidos_comuna:
                validacion1 = (f"Cliente: {p['nombre']} {p['apellido']}, direccion: {p['direccion']}, Comuna: {p['comuna']}, "
                         f"Cil. 5kg: {p['cilindros_5kg']}, Cil. 15kg: {p['cilindros_15kg']}, Cil. 45kg: {p['cilindros_45kg']}\n")
                file.write(validacion1)
        
        print(f"Hoja de ruta impresa en hoja_ruta{comuna_elegida}.txt")
    except Exception as e:
        print(f"Ocurrió un error al imprimir la hoja de ruta: {e}")

# Main principal
def main():
    while True:
        limpiar_pantalla()
        print("1. Registrar pedido")
        print("2. Listar todos los pedidos2")
        print("3. Imprimir hoja de ruta")
        print("4. Salir")
        try:
            op = int(input("\nPor favor ingrese su opcion: "))
            if op == 1:
                registrar_pedido()
            elif op == 2:
                listar_pedidos()
                input("\nPresione Enter para continuar...")
            elif op == 3:
                imprimir_hoja_ruta()
                input("\nPresione Enter para continuar...")
            elif op == 4:
                print("Saliendo....")
                break
            else:
                print("Por favor ingrese opcion valida")
                input("\nPresione Enter para continuar...")
        except ValueError:
            print("Por favor ingrese un numero valido.")

# Invocando función principal para iniciar el programa
if __name__ == "__main__":
    main()