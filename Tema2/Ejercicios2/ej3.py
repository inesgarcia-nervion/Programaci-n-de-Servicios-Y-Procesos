"""3. En este ejercicio debes implementar los siguientes procesos y el Main como se explica a 
continuación:

Proceso 1: Genera 6 números aleatorios entre 1 y 10, ambos inclusive, y los guarda en un fichero. 
Estos números deben contener decimales. La ruta a este fichero se le indicará como parámetro de 
entrada. Estos 6 números representan las notas de un alumno.

Proceso 2: Lee un fichero pasado por parámetro que contiene las notas de un alumno, cada una en 
una línea distinta, y realiza la media de las notas. También recibe como parámetro el nombre del 
alumno. Esta media se almacenará en un fichero de nombre medias.txt. Al lado de cada media debe 
aparecer el nombre del alumno, separados por un espacio.

Proceso 3: Lee el fichero medias.txt. En cada línea del fichero aparecerá una nota, un espacio y 
el nombre del alumno. Este proceso debe leer el fichero y obtener la nota máxima. Imprimirá por 
pantalla la nota máxima junto con el nombre del alumno que la ha obtenido.

Main: Lanza 10 veces el primer proceso de forma concurrente. Cada una de esas veces debe guardarse
el resultado en un fichero distinto. Es decir, al final tiene que haber 10 ficheros distintos con 
las notas de cada alumno. Pon a los ficheros nombres como Alumno1.txt, Alumno2.txt, …, Alumno10.txt.

A continuación, se debe lanzar el proceso 2 que toma los ficheros creados en el paso anterior como 
entrada. Por lo que el proceso 2 se lanzará 10 veces también, una por cada fichero generado por el 
proceso 1, y realizarlo todo de forma simultánea/concurrente. Es decir, debe haber 10 procesos 
ejecutándose simultáneamente.

Por último, debe lanzarse el proceso 3. Hay que tener presente que para que este proceso pueda 
funcionar correctamente deben estar todas las notas ya escritas.

Prueba a realizar el ejercicio haciendo uso de Pool y haciendo uso de bucles for. """

from multiprocessing import Process, Pool
import time, random


def proceso1(notas = "notas.txt"):      # Para generar las notas aleatorias y guardarlas en un fichero
    notaTotal = [round(random.uniform(1, 10), 2) for i in range(6)]      # Uniform es para decimales
    with open(notas, "w") as f:   # Guardamos las notas en el fichero "w" de escritura
        for n in notaTotal:
            f.write(f"{n}\n")
    print(f"Notas totales: {notaTotal}")
    return notaTotal


def proceso2(notas = "notas.txt", alumno = "Alumno"):     # Para calcular la media de las notas y guardarlas en medias.txt
    with open(notas, "r") as f:  # Leemos las notas del fichero "r" de lectura
        listaNotas = [float(linea.strip()) for linea in f if linea.strip()]            # Leemos todas las líneas, eliminamos espacios y convertimos a float
    media = round(sum(listaNotas)/len(listaNotas), 2)
    print(f"Media de {alumno}: {media}")
    return media, alumno


def proceso3(medias = "medias.txt"):      # Para leer medias.txt y obtener la nota máxima
    maxNota = None      # Inicializamos la nota máxima como None
    maxAlumno = ""      # Inicializamos el nombre del alumno con la nota máxima como cadena vacía
    with open(medias, "r") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:       # Si la línea está vacía, la ignoramos
                continue
            notaFinal, alumno = linea.split(" ", 1)   # Dividimos en nota y nombre del alumno
            nota = float(notaFinal)
            if maxNota is None or nota > maxNota:     # Si es la primera nota o es mayor que la máxima actual
                maxNota = nota
                maxAlumno = alumno  
    print(f"La nota máxima es {maxNota} obtenida por {maxAlumno}")




if __name__ == "__main__":
    inicio = time.perf_counter()

    # Proceso 1
    with Pool(processes=10) as pool:
        nombresAlumnos = [f"Alumno{i+1}.txt" for i in range(10)]
        pool.map(proceso1, nombresAlumnos)
    tiempo1 = time.perf_counter()
    tiempo_proceso1 = tiempo1 - inicio
    print(f"El proceso 1 ha tardado {tiempo_proceso1: .2} segundos\n")


    # Proceso 2
    with Pool(processes=10) as pool:
        argumentos = [f"Alumno{i+1}.txt" for i in range(10)]    # Ficheros generados en el proceso 1
        nombresAlumnos = [f"Alumno{i+1}" for i in range(10)]    # Nombres de los alumnos (sin txt)
        resultados = pool.starmap(proceso2, zip(argumentos, nombresAlumnos))    # Zip combina dos listas en tuplas
    with open("medias.txt", "w") as f:
        for media, alumno in resultados:
            f.write(f"{media} {alumno}\n")
    tiempo2 = time.perf_counter()
    tiempo_proceso2 = tiempo2 - tiempo1
    print(f"El proceso 2 ha tardado {tiempo_proceso2: .2} segundos\n")


    # Proceso 3
    proceso3()
    tiempo3 = time.perf_counter()
    tiempo_proceso3 = tiempo3 - tiempo2
    print(f"El proceso 3 ha tardado {tiempo_proceso3: .2} segundos\n")
    tiempo_total = tiempo3 - inicio
    print(f"El tiempo total ha sido de {tiempo_total: .2} segundos\n")
