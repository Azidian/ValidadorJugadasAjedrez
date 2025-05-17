from parser import ParserSAN
from tree import VisualizadorAjedrez

def obtener_san_usuario():
    print("""\nIngrese la partida en notación SAN (ej: 1. d4 d5 2. Bf4 Nf6 3. e3 e6 4. c3 c5 5. Nd2 Nc6 )""")
    
    # Leer toda la entrada de una vez
    lineas = []
    while True:
        try:
            linea = input("Ingrese movimientos: ")
            if not linea:  # Si el usuario presiona Enter sin texto
                break
            lineas.append(linea)
            # No esperar más entrada después del primer Enter
            break
        except EOFError:  # Manejar Ctrl+D (Unix) o Ctrl+Z+Enter (Windows)
            break
    
    return ' '.join(lineas).strip()

def main():
    print("""¡ANALIZADOR SINTÁCTICO DE PARTIDAS DE AJEDREZ CON VISUALIZACIÓN DE ÁRBOL BINARIO POR TURNOS!""")          
    
    try:
        # 1. Obtener entrada
        texto = obtener_san_usuario()
        
        if not texto:
            print("\n| ERROR | No se ingresó ninguna partida, vuelva a intentarlo")
            return
        
        # 2. Parsear
        
        parser = ParserSAN(texto)
        partida = parser.parse()
        movimientos = parser.obtenerElementos()
        print(f"\nPartida procesada exitosamente: {partida}")
        
        # 3. Visualizar
        visor = VisualizadorAjedrez(partida, movimientos)
        visor.mostrar_arbol()
        
    except Exception as e:
        print(f"\n| ERROR | {str(e)}")
        print("| Intente de nuevo con una notación (SAN) válida ")

if __name__ == "__main__":
    main()