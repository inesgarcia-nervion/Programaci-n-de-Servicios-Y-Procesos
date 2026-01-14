"""3. Realiza el ejercicio anterior pero esta vez va a haber otra función que lea
los números de un fichero. En el fichero habrá un número por línea. En este caso, 
tienes que llevar a cabo una comunicación entre los dos procesos utilizando colas 
(Queue), de forma que la función que se encarga de leer los números los guarde en 
la cola, y la función que realiza la suma, recibirá la cola y tomará de ahí los 
números. La función que lee el fichero, una vez haya terminado de leer y de añadir 
elementos a la cola, debe añadir un objeto None para que el receptor sepa cuándo 
terminar de leer de la cola."""

from multiprocessing import Process, Queue
import time

def leerFichero(cola, fichero):
    with open(fichero, 'r') as f:
        for linea in f:
            numero = int(linea.strip())
            cola.put(numero)  # Meter en cola
            print(f"  Leído: {numero}\n")
    cola.put(None)  # Señal de fin
    print("Lectura finalizada")
    
    
def sumar(cola):
    while True:
        numero = cola.get() # Sacar de cola
        if numero is None:
            break
        resultado = sum(range(1, numero+1)) 
        print(f"Suma hasta {numero} da de resultado {resultado}")



if __name__ == '__main__':
    with open('numeros.txt', 'w') as f:
        f.write("10\n")
        f.write("20\n")
        f.write("30\n")
    
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