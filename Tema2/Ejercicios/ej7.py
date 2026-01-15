"""7. Realiza el ejercicio anterior pero esta vez va a haber otra función que lea 
los números de un fichero. En el fichero habrá dos números por línea separados por 
un espacio. En este caso, tienes que llevar a cabo una comunicación entre los dos 
procesos utilizando colas (Queue), de forma que la función que se encarga de leer 
los números los guarde en la cola, y la función que realiza la suma, recibirá la 
cola y tomará de ahí los dos números."""

from multiprocessing import Process, Queue
import time

def leerFichero(cola, fichero):
    with open(fichero, 'r') as f:
        for linea in f:
            numero1, numero2 = map(int, linea.split()) # map para separarlos por espacios y convertirlos a números
            cola.put((numero1, numero2))      # Meter dos números en cola (doble paréntesis)
            print(f"Leído: {numero1} y {numero2}\n")
    cola.put(None)  # señal de fin
    print("Lectura finalizada")
    

def sumar(cola):
    while True:
        numero = cola.get() # Sacar de cola
        if numero is None:
            break
        num1, num2 = numero
        inicio = min(num1, num2)
        fin = max(num1, num2)
        resultado = sum(range(inicio, fin+1)) 
        print(f"Suma desde {inicio} hasta {fin} da de resultado {resultado}")
        
        
        

if __name__ == '__main__':
    with open('numeros.txt', 'w') as f:
        f.write("1 10\n")
        f.write("5 20\n")
        f.write("50 10\n")
    
    queue = Queue()
    inicio = time.perf_counter()
    
    # Primero se crean los procesos
    p1 = Process(target=leerFichero, args=(queue, 'numeros.txt'))
    p2 = Process(target=sumar, args=(queue,))
    
    # Después se arrancan TODOS a la vez
    p1.start()
    p2.start()
    
    # Por último, esperamos a que TODOS terminen
    p1.join()
    p2.join()
    
    
    fin = time.perf_counter()
    tiempo_proceso = fin - inicio
    print(f"Proceso terminado")
    print(f"El proceso ha tardado {tiempo_proceso: .2} segundos")