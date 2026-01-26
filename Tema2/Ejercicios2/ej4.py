"""4. Para realizar este ejercicio es necesario que definas 2 procesos distintos y un Main:

Proceso 1: Recibe como parámetros una ruta de fichero y un año. El proceso leerá el fichero 
el cual almacena en cada línea la información de una película: nombre y año de estreno 
separados por punto y coma (;). Ejemplo:
Debe enviar al siguiente proceso únicamente aquellas películas que se hayan estrenado en 
el año introducido por parámetro.

Proceso 2: Recibirá un número indeterminado de películas y debe almacenarlas en un fichero 
de nombre peliculasXXXX, donde XXXX es el año de estreno de las películas.

Main: Pide al usuario que introduzca un año por teclado, debe ser menor al actual. 
También solicitará la ruta al fichero donde se encuentran almacenadas las películas.

Piensa cuál es la mejor forma de comunicación entre los procesos e implementa las llamadas 
a los mismos atendiendo a ella. """

from multiprocessing import Process, Pipe
import time

def proceso1(pipe, ruta, año):
    try:
        with open(ruta, 'r') as f:
            for linea in f:
                linea = linea.strip()
                if not linea:       # Si la línea está vacía, la ignoramos
                    continue
                nombre, añoEstreno_str = linea.split(';')
                añoEstreno = int(añoEstreno_str)
                if añoEstreno == año:
                    pipe.send(nombre)  # Enviar por la tubería
    except FileNotFoundError:
        print(f"Fichero no encontrado: {ruta}")
        try:
            pipe.send(None)
        except Exception:
            pass
        pipe.close()
        print("Lectura finalizada")
        return
    pipe.send(None)  # Señal de fin
    pipe.close()
    print("Lectura finalizada")


def proceso2(pipe, año):
    with open(f'peliculas{año}.txt', 'w') as f:
        while True:
            nombre = pipe.recv()  # Recibir de la tubería
            if nombre is None:
                break
            f.write(f"{nombre};{año}\n")
            print(f"Se ha guardado la película: {nombre}")
    pipe.close()
    print(f"Películas guardadas en {año}.txt")


if __name__ == '__main__':  
    inicio = time.perf_counter()

    año_usuario = int(input("Introduce el año de estreno de la película (menor al actual):"))
    ruta_fichero = input("Introduce la ruta al fichero de películas: ")

    
    # Tuberías
    pipe1, pipe2 = Pipe()
    
    # Procesos
    p1 = Process(target=proceso1, args=(pipe1, ruta_fichero, año_usuario))
    p2 = Process(target=proceso2, args=(pipe2, año_usuario))
    

    p1.start()
    p2.start()
    
    pipe1.close() 
    pipe2.close()
    
    p1.join()
    p2.join()


    final = time.perf_counter()
    tiempoFinal = final - inicio
    print(f"El proceso ha tardado {tiempoFinal:.2f} segundos")