import random

def MenuInicio(): #Muestra la bienvenida al juega, solicita el nombre del jugador y lo muestra
    Bienvenida= "► Hola, Bienvenido a la Sopa de letras *Themes* ◄"
    nrogrupo= "Grupo 3"
    Grupo= "Autores: Julian Santamaria - Diego Martinez - Francisco Anderson - Marcos Romero"
    formato= Bienvenida.center(155," ")
    nrogrupoformato= nrogrupo.center(155, " ")
    Grupoformato= Grupo.center(155, " ")
    print(formato)
    print("\n")
    print(nrogrupoformato)
    print("\n")
    print(Grupoformato)
    print("\n")
    nombreusuario= input("Ingrese su Nickname por favor:")
    print("\n")
    MensajeConfirmacion=(f"¿Esta seguro que {nombreusuario} sera su Nickname?")
    print(MensajeConfirmacion)
    print("\n")
    confirmar= input("Confirme con Si o Escriba No para volver a ingresar otro Nickname:")
    print("\n")
    while confirmar.lower() != "no" and confirmar.lower()!= "si":
        print("\n")
        print("Error, ingrese solo si o no")
        print("\n")
        confirmar= input("Confirme con Si o Escriba No para volver a ingresar otro Nickname:")
        print("\n")
    while confirmar.lower() == "no":
        nombreusuario= input("\n\n Reingrese su Nickname por favor:")
        print(MensajeConfirmacion)
        confirmar= input("Confirme con Si o Escriba No para volver a ingresar otro Nickname:")
    print("\n Nickname Confirmado, sera direccionado al Menu Principal")
    return nombreusuario

def Menuprincipal(nombreusuario): #solicita elegir un apartado y lo retorna
    mensaje=  "Menu principal"
    mensajeformato= mensaje.center(50)
    print(mensajeformato)
    print("\n")
    print("1) Comenzar Juego")
    print("2) Instrucciones")
    print("3) Mostrar Partidas Jugadas")
    print("4) Salir del Juego")
    print("-"*50)
    Seleccionaropcion= input("ingrese el numero de la opcion a la que desee acceder: ")
    while Seleccionaropcion.isdigit() == False or int(Seleccionaropcion) < 1 or int(Seleccionaropcion) > 4:
        Seleccionaropcion= input("\nError, Ingrese un numero de opcion valido")
    Seleccionaropcion= int(Seleccionaropcion)
    return Seleccionaropcion

def MenuJuego(): #Funcion que muestra el menu de la opcion "Comenzar Juego"
    Mensaje_MenuJugar= "Menu de juego"
    Mensaje_MenuJugar= Mensaje_MenuJugar.center(50)
    print(Mensaje_MenuJugar)
    print("\n")
    print("*TEMATICAS:*")
    print("\n")
    print("1) Tematica: GenerosMusicales")
    print("2) Tematica: CuerpoHumano")
    print("3) Tematica: Computadoras")
    print("4) Tematica: Mundial Qatar")
    print("5) Volver al menu principal")
    print("-" * 50)
    Seleccionar= input("\nSeleccione el numero de tematica que desee jugar o ingrese 5 para volver:")
    while Seleccionar.isdigit() == False or int(Seleccionar) < 1 or int(Seleccionar) > 5:
        Seleccionar= input("\n Opcion no valida, Seleccione el numero de tematica que desee jugar o ingrese 5 para volver")
    Seleccionar= int(Seleccionar)
    
    return Seleccionar

def crearmatriz(tamaniomatriz, f, matriz):  # Hecho con recursividad
    filas = tamaniomatriz+1  
    columnas = tamaniomatriz+1
    if f < filas:
        matriz.append([0] * columnas)
        matriz = crearmatriz(tamaniomatriz, f+1, matriz)  # incremento f
    return matriz


def Guia(matriz, f, c):  # Hecho con recursividad
    """Agrega una guia con el numero correspondiente a cada fila y cada columna y devuelve la matriz"""
    columnas = len(matriz[0])
    coord= 0
    if c < columnas and coord == 0:
        matriz[0][c] = c
        matriz = Guia(matriz, f, c+1)
    matriz[f][0] = f  
    m = Guia(matriz, f+1, 0)
    coord += 1
    return matriz


def InsertarLetras(tamaniomatriz, matriz, fil, col):  # Hecho con recursividad #Esta funcion rellena la matriz con letras al azar 
    LetrasAbecedario = "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    if col < tamaniomatriz+1:
        matriz[fil][col] = random.choice(LetrasAbecedario)
        matriz = InsertarLetras(tamaniomatriz, matriz, fil, col+1)  
    matriz = InsertarLetras(tamaniomatriz, matriz, fil+1, col=1)
    return matriz


def imprimirMatriz(matriz, f, c):  #Hecho con recursividad
    """Imprime la matriz"""
    columnas = len(matriz[0])  
    if c < columnas:
        print("%2s" % matriz[f][c], end=" ")
        imprimirMatriz(matriz, f, c+1)
    print()  
    imprimirMatriz(matriz, f+1, c=0)


def seleccionarPalabras(nrotematica):     #Esta funcion retorna 1 lista con 10 palabras seleccionadas al azar dependiendo de la tematica que se haya escogido
    TematicaMusica= "BLUES", "JAZZ", "CLASICA", "ROCK", "CUMBIA", "HIPHOP", "RAP", "HEAVYMETAL","ELECTRONICA","SOUL","COUNTRY","POP","PUNK","FUNK","REGGAE"
    TematicaCuerpoHumano= "ESTOMAGO", "CEREBRO", "HIGADO", "OJOS", "INTESTINOS", "PIES", "MANOS", "CABEZA", "UÑAS", "DIENTES", "HUESOS", "OIDOS", "BRAZOS", "TIMPANOS"
    TematicaComputadora= "PROCESADOR", "RAM", "DISCODURO", "SSD", "PLACADEVIDEO", "FUENTE", "MOTHERBOARD", "USB", "PLACAWIFI", "MONITOR", "TECLADO", "AURICULARES", "HDMI", "COOLERS"
    TematicaMundial= "QATAR", "HOLANDA","SENEGAL","ECUADOR","INGLATERRA","IRAN","ESTADOSUNIDOS","GALES","ARGENTINA","MEXICO","POLONIA","FRANCIA","DINAMARCA","TUNES","AUSTRALIA"
    Palabrastematica= set()  #Conjunto para que no hayan repetidos
    if nrotematica == 1:
        for palabras in range(10):
            palabra= random.choice(TematicaMusica)
            Palabrastematica.add(palabra)
    elif nrotematica == 2:
         for palabras in range(10):
            palabra= random.choice(TematicaCuerpoHumano)
            Palabrastematica.add(palabra)
    elif nrotematica == 3:
         for palabras in range(10):
            palabra= random.choice(TematicaComputadora)
            Palabrastematica.add(palabra)
    elif nrotematica == 4:
         for palabras in range(10):
            palabra= random.choice(TematicaMundial)
            Palabrastematica.add(palabra)
    return Palabrastematica


def llenarSopaPalabras(tamanio, matriz, PalabrasSeleccionadas): #Esta funcion sirve para llenar la lista con las palabras seleccionadas en la funcion "seleccionarPalabras", ya sea horizontalmente o vertical
    filasyausadas= [] #listas para fijarme que filas ya fueron utilizadas para que no se pisen las palabras
    filasUsadasHorizontal= []   #Lista para fijarme que filas en horizontal ya fueron utilizadas para que no se pisen las palabras
    columnas= [] #Lista para fijarme que columnas ya fueron utilizadas para que no se pisen las palabras
    listaEspacio= [] # Lista que servira como guia para ver que espacios estan ocupados
    cantpalabrashorizontales= len(PalabrasSeleccionadas) /2 #La mitad de las palabras se insertaran en horizontal
    contpalabrashorizontal= 0
    contpalabrasvertical= 0
    contpalabras= 0
    for i in range(1, tamanio+1):  
        listaEspacio.append(i)
    for palabra in PalabrasSeleccionadas: #Las palabras con indice impar se ingresaran en la matriz al reves
        if contpalabras % 2 != 0:
            palabra= palabra[::-1]
        if contpalabrashorizontal < cantpalabrashorizontales: #Se valida que las palabras en horizontal no sean mas de la mitad
            fila= random.randint(1, tamanio+1)
            columna= random.randint(1, tamanio-len(palabra)-1)
        while fila in filasyausadas: #Loop donde se ver
            fila= random.randint(1, tamanio+1)
        filasyausadas.append(fila)
        filasUsadasHorizontal.append(fila)
        for i in range(len(palabra)):
            columnas.append(columna+i)
            matriz[fila][columna + i] = palabra[i]
        contpalabrashorizontal = contpalabrashorizontal + 1
    else:
        fila= random.randint(1, tamanio-len(palabra)-1)
        columna= random.randint(1,tamanio+1)
        contador= 0
        for i in range(1, len(listaEspacio)):
            if listaEspacio[i] in columnas:
                contador= contador + 1
        while columna in columnas:
            columna= random.randint(1, tamanio+1)
        filasyausadas.append(fila)
        columnas.append(columna)
        for i in range(len(palabra)):
            matriz[fila + i][columna] = palabra[i]
            filasyausadas.append(fila+i)
        contpalabrasvertical= contpalabrasvertical + 1
        contpalabras= contpalabras + 1
    return matriz

def Instrucciones(): #Se muestra el menu de instrucciones
    print("\n")
    primermensaje= "►Estas en el Menu de instrucciones◄"
    primermensaje= primermensaje.center(50," ")
    print(primermensaje)
    print("\n \n")
    print("~Siga las siguientes instrucciones para mejorar su experiencia~")
    print("\n \n")
    instruccion1= "1) Debe de ingresar los numeros de fila y columna donde comienza y luego donde termina la palabra que quiere hallar"
    instruccion2= "2) Al confirmar solo escriba si / no"
    instruccion3= "3) Puede elegir entre varias tematicas de palabras a hallar en la sopa de letras: Generos Musicales, Componentes de computadora, Partes del cuerpo humano, Equipos del mundial Qatar"
    instruccion4= "4) En el menu historial encontrara el progreso y datos de sus anteriores partidas guardadas"
    instruccion5= "5) Por ultimo, disfrute del Juego"
    print(instruccion1)
    print("\n")
    print(instruccion2)
    print("\n")
    print(instruccion3)
    print("\n")
    print(instruccion4)
    print("\n")
    print(instruccion5)
    print("\n")
    Direccionar= "~Sera enviado al Menu principal~"
    print(Direccionar)
    print("\n \n \n")


def HallarPalabras(PalabrasSeleccionadas, matriz, palabrasencontradas, progreso, intentos):
    palabrahallada= "" #En esta cadena se almacenaran las palabras halladas
    confirmar= "" #En esta cadena se almacena
    while confirmar.lower() != "si":
        confirmar= ""
        #Input para ingresar la fila donde comienza la palabra
        Comienzofila= input("ingrese el nro de fila en donde empieza la palabra:")
        while Comienzofila.isdigit() == False or int(Comienzofila) == 0:
            Comienzofila= input("\n ERROR, ingrese un numero de fila valido por favor:")
        Comienzofila= int(Comienzofila)
        #Input para ingresar la columna donde comienza la palabra
        Comienzocolumna= input("Ingrese el nro de columna en donde empieza la palabra:")
        while Comienzocolumna.isdigit() == False or int(Comienzocolumna) == 0:
            Comienzocolumna= input("\n ERROR, ingrese un nro de columna valido por favor:")
        Comienzocolumna= int(Comienzocolumna)
        #Input para ingresar la fila donde termina la palabra
        Filafinal= input("ingrese el nro de fila en donde termina la palabra:")
        while Filafinal.isdigit() == False or int(Filafinal) == 0:
            Filafinal= input("\n ERROR, ingrese un nro de fila valido por favor:")
        Filafinal= int(Filafinal)
        #Input para ingresar la columna donde termina la palabra
        Finalcolumna= input("ingrese el nro de columna en donde termina la palabra:")
        while Finalcolumna.isdigit() == False or int(Finalcolumna) == 0:
            Finalcolumna= input("\n ERROR, ingrese un nro de columna valido por favor:")
        Finalcolumna= int(Finalcolumna)
        print()
        
        while confirmar.lower() != "no" and confirmar.lower() != "si": 
            confirmar= input(f"La palabra comienza en la fila ({Comienzofila} y columna {Comienzocolumna}) y termina en la fila({Filafinal} y la columna {Finalcolumna}, ¿Estas seguro? Si / No:")
    intentos += 1
    Encontrada= ""
    if Comienzofila == Filafinal:
        f= Comienzofila
        if Comienzocolumna < Finalcolumna:
            for c in range(Comienzocolumna, Finalcolumna+1):
                palabrahallada += matriz[f][c]
            Encontrada= "Horizontal"
        else:
            for c in range(Comienzocolumna, Finalcolumna-1, -1):
                palabrahallada += matriz[f][c]
            Encontrada= "invertidahorizontal"
    elif Comienzocolumna == Finalcolumna:
        col= Comienzocolumna
        if Comienzofila < Finalfila:
            for f in range(Comienzofila, Filafinal+1):
                palabrahallada += matriz[f][c]
                Encontrada= "Vertical"
        else:
            for f in range(Comienzofila, Filafinal-1, -1):
                palabrahallada += matriz[f][c]
                Encontrada= "Verticalinvertida"
    
    if palabrahallada in PalabrasSeleccionadas:                    #Si la palabra que se ingreso (mediante coordenadas) esta en la lista de palabras a encontrar y
        if palabrahallada not in palabrasencontradas:             #a su vez no esta en la lista de palabras encontradas, se ha encontrado una palabra
            print("\n \n")
            print(f"Bien Hecho!, has encontrado una palabra: *{palabrahallada}* ")
            palabrasencontradas.append(palabrahallada)
            progreso += 1
            if Encontrada == "Horizontal":
                for c in range(Comienzocolumna, Finalcolumna+1):
                    matriz[f][c] = ("-")
            elif Encontrada == "invertidaHorizontal":
                for c in range(Comienzocolumna, Finalcolumna-1, -1):
                    matriz[f][c]= ("-")
            elif Encontrada == "Vertical":
                for f in range(Comienzofila, Filafinal+1):
                    matriz[f][c]= ("-")
            elif Encontrada == "Verticalinvertida":
                for f in range(Comienzofila, Filafinal-1, -1):
                    matriz[f][c]= ("-")
    else:
            print(f"\n Coordenadas Incorrectas, intentalo de nuevo")
    print("\n")
    progresoPorcentaje= str(float(progreso/len(PalabrasSeleccionadas) * 100)) + "%"
    print(f"Tu progreso es del {progresoPorcentaje}")
    print("\n")
    print(f"Las palabras encontradas son: {palabrasencontradas}")
    
    return progreso, intentos, palabrasencontradas


def Resumen(progreso, palabrasInsertadas, finalizarPartida, intentos, palabrasHalladas, usuario, Tematica):
    estadoDeLaPartida = ""
    tematica= ""
    progresoPorcentaje= ""
    if progreso == len(palabrasInsertadas):
        finalizarPartida = True
        frasefelicitaciones= "¡Felicitaciones, Has encontrado todas las palabras!"
        print(frasefelicitaciones)
    else:
        Continuarpartida= input("Desea continuar con la partida?")
        while Continuarpartida.lower() != "no" and Continuarpartida.lower() != "si":
            Continuarpartida = input("ERROR, Desea Continuar con la partida? Si / No : ")
        if Continuarpartida.lower() == "no":
            finalizarPartida = True
    if finalizarPartida == True:  #si se llega aqui, es porque el usuario decidio terminar con la partida y se muestra el resumen
        progresoPorcentaje= str(float((progreso/len(palabrasInsertadas))*100)) + "%"
        progresomensaje= float(progreso/len(palabrasInsertadas))*100
        if int(progresomensaje) <= 30:
            mensajealentador= "Lo siento, mejor suerte la proxima"
        elif int(progresomensaje) > 30 and int(progresomensaje) < 70:
            mensajealentador="Bien hecho, has tenido un buen juego"
        elif int(progresomensaje) > 70:
            mensajealentador="Excelente, sigue asi!"
        print("\n\n---> Partida finalizada <---")
        print("\n\n")
        print("---> RESUMEN <---")
        print(f"-> Tu progreso fue de {progresoPorcentaje}")
        print(f"-> Realizaste {intentos} intentos")
        print(f" {mensajealentador}")
        print("\n\n")
        if Tematica == 1:
                tematica = "Generos Musicales"
        elif Tematica == 2:
            tematica= "Cuerpo Humano"
        elif Tematica == 3:
            tematica= "Computadoras"
        elif Tematica == 4:
            tematica= "Mundial Qatar"
    ResumenMarcador= {          #Diccionario donde se almacenara los datos de las partidas del usuario
        "USUARIO: ": usuario,
        "PROGRESO:": progresoPorcentaje,
        "INTENTOS: ": intentos,
        "TEMATICA DE LA PARTIDA:": tematica,
        "PALABRAS ENCONTRADAS: ": palabrasHalladas
    }

    return finalizarPartida, ResumenMarcador if finalizarPartida == True else finalizarPartida

# PROGRAMA PRINCIPAL
Nickname = MenuInicio()
print("\n""\n")
while 1:  #Hasta que el usuario no se decida a salir del juego, el programa no saldra de este loop
    OpcionSeleccionada = Menuprincipal(Nickname)
    print("\n""\n")
    if OpcionSeleccionada == 1:
        tamaniomatriz= 20 #tamanio de la matriz (20+1) x (20+1) # +1 por la guia
        Tematica= MenuJuego() 
        if Tematica < 5:  #si se elije un valor menor que 5, es porque se eligio una tematica y no salir al menu principal
            palabrasInsertadas = seleccionarPalabras(Tematica) # Se seleccionan las palabras que van a incluirse en la sopa de letras
            while 1: #Aqui se empieza a crear y rellenar la matriz
                matriz = []  # creo la matriz 
                try:
                    while True: #Bloque donde se vuelve a crear la matriz por la duda de que haya errores
                        matriz = []  
                        while True: #Bloque donde se rellena la matriz creada con ceros
                            try:
                                matriz = crearmatriz(tamaniomatriz, 0, matriz)
                            except IndexError:
                                matriz = []
                                pass  # si tira index error, vuelve a crearla
                            except RecursionError:
                                break
                            else:
                                break
                        
                        while True: # bloque de proteccion al rellenar la matriz con letras aleatorias
                            try:
                                matriz = InsertarLetras(tamaniomatriz, matriz, 1, 1) #Se Rellena la matriz creada con letras aleatorias
                            except IndexError:
                                break  # si tira index error, termino de rellenarla
                            except RecursionError:
                                break
                            else:
                                break
                        
                        while True: # bloque donde se agrega la guia a la matriz 
                            try:
                                matriz = Guia(matriz, 0, 0)
                            except IndexError:
                                break  # si llega a este indexError es porque ya se termino de rellenar la matriz
                            except RecursionError:
                                break
                            else:
                                break
                        # La sopa de letras se creo exitosamente, ahora falta agregarle las palabras que se seleccionaron anteriormente
                        
                        try: # bloque de proteccion para insertar palabras
                            matriz = llenarSopaPalabras(tamaniomatriz, matriz, palabrasInsertadas)
                        except IndexError:
                            matriz = []  # si tira indexerror, crea todo de 0.
                            pass
                        except AssertionError:
                            # si tira AssertionError (no hay columnas para asegurar que las palabras no se pisen), crea todo de 0.
                            pass
                        else:
                            break  #si salio todo bien, se pasa al siguiente else

                except ValueError:
                    pass  #si algo salio mal en la matriz creada, se vuelve a crear todo de 0
                except KeyboardInterrupt:
                    break
                else:
                    progreso= 0
                    intentos= 0
                    finalizar = False
                    palabrasHalladas = []
                    
                    while finalizar == False:
                        while True:
                            try:
                                print()  
                                imprimirMatriz(matriz, 0, 0)
                            except IndexError:  
                                break
                        progreso, intentos, palabrasHalladas = HallarPalabras(palabrasInsertadas, matriz, palabrasHalladas, progreso, intentos)  
                        finalizar, archivo = Resumen(progreso, palabrasInsertadas, finalizar, intentos, palabrasHalladas, Nickname, Tematica)  
                    break
        if Tematica != 5:  # 
            try:
                archivoMarcador = open("Marcador.txt", "at")
                for palabra in archivo:
                    linea = str(palabra) + \
                        str(archivo[palabra]) + \
                        "\n"  
                    archivoMarcador.write(linea)
            except OSError:
                print("No se puede grabar el archivo")
            finally:
                try:
                    archivoMarcador.close()
                except NameError:
                    pass
    elif OpcionSeleccionada == 2: #Se muestran las instrucciones
        Instrucciones()  
    elif OpcionSeleccionada == 3:   #Se muestra el historial de partidas jugadas
        cadena =  "Estas en el historial de partidas jugadas"
        cadena = cadena.center(50)
        print("\n")
        print(cadena)
        try:
            archivoMarcador = open("Marcador.txt", "rt")
            for linea in archivoMarcador:
                if linea is not "":  # Mientras que linea contenga un valor, se imprime el archivo linea a linea
                    print(linea)
        except OSError:
            print("No se puede grabar el archivo")
        finally:
            # ETAPA DE CIERRE
            try:
                archivoMarcador.close()
            except NameError:
                pass
        print("\n")
        cadena = "* Será direccionado al MENÚ PRINCIPAL *"
        cadena = cadena.center(50)
        print(cadena)

    elif OpcionSeleccionada == 4:
        break
# Si el usuario salio del juego
cadena = "♥ El juego se ha cerrado exitosamente, Muchas gracias por jugar ♥"
cadenacentrada= cadena.center(50)
print("\n")
print(cadenacentrada)
print("\n")