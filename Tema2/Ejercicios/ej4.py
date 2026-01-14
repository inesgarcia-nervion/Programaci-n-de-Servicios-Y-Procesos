"""4. En este caso, vuelve a realizar la comunicación entre procesos pero usando 
tuberías (Pipe), de forma que la función que se encarga de leer los números del 
fichero se los envíe (send) al proceso que se encarga de la suma. El proceso que 
suma los números tiene que recibir (recv) un número y realizar la suma. Una vez que 
el proceso que lee el fichero termine de leer números en el fichero, debe enviar un 
None. El que recibe números dejará de realizar sumas cuando reciba un None."""

from multiprocessing import Process, Pipe
import time

def leerFichero(pipe, fichero):
    with open(fichero, 'r') as f:
        for linea in f:
            numero = int(linea.strip())
            pipe.send(numero)  # Enviar por la tubería
            print(f"  Leído: {numero}\n")
    pipe.send(None)  # Señal de fin
    pipe.close()
    print("Lectura finalizada")
    
    
def sumar(pipe):
    while True:
        numero = pipe.recv() # Recibir de la tubería
        if numero is None:
            break
        resultado = sum(range(1, numero+1)) 
        print(f"Suma hasta {numero} da de resultado {resultado}")
    pipe.close()



if __name__ == '__main__':
    with open('numeros.txt', 'w') as f:
        f.write("10\n")
        f.write("20\n")
        f.write("30\n")
    
    # Crear tubería 
    pipe1, pipe2 = Pipe()
    
    inicio = time.perf_counter()
    
    # Primero se crean los procesos
    p1 = Process(target=leerFichero, args=(pipe1, 'numeros.txt'))
    p2 = Process(target=sumar, args=(pipe2,))
    
    # Después se arrancan TODOS a la vez
    p1.start()
    p2.start()
    
    # Cerrar extremos no usados en el proceso principal 
    pipe1.close() 
    pipe2.close()
    
    # Por último, esperamos a que TODOS terminen
    p1.join()
    p2.join()
    
    
    fin = time.perf_counter()
    tiempo_proceso = fin - inicio
    print(f"Proceso terminado")
    print(f"El proceso ha tardado {tiempo_proceso: .2} segundos")