"""8. En este caso, vuelve a realizar la comunicación entre procesos pero usando 
tuberías (Pipe), de forma que la función que se encarga de leer los números del 
fichero se los envíe (send) al proceso que los suma. El proceso que suma los 
números tiene que recibir (recv) los dos números y realizar la suma entre ellos."""

from multiprocessing import Process, Pipe
import time

def leerFichero(pipe, fichero):
    with open(fichero, 'r') as f:
        for linea in f:
            numero1, numero2 = map(int, linea.split())
            pipe.send((numero1, numero2))  # Enviar por la tubería
            print(f"Leído: {numero1} y {numero2}\n")
    pipe.send(None)  # Señal de fin
    pipe.close()
    print("Lectura finalizada")
    
def sumar(pipe):
    while True:
        numeros = pipe.recv() # Recibir de la tubería
        if numeros is None:
            break
        num1, num2 = numeros
        inicio = min(num1, num2)
        fin = max(num1, num2)
        resultado = sum(range(inicio, fin+1)) 
        print(f"Suma de {inicio} a {fin} = {resultado}")
    pipe.close()


if __name__ == '__main__':
    with open('numeros.txt', 'w') as f:
        f.write("1 10\n")
        f.write("5 20\n")
        f.write("50 10\n")
        
        
    # Crear tubería 
    pipe1, pipe2 = Pipe()
    
    inicio = time.perf_counter()
    
    # Primero se crean los procesos
    p1 = Process(target=leerFichero, args=(pipe1, 'numeros.txt'))
    p2 = Process(target=sumar, args=(pipe2,))
    
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