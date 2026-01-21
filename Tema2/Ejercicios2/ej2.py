"""2. En este ejercicio vamos a lanzar varios procesos, cuyas entradas y salidas 
están enlazadas. Para ello tendremos tres procesos distintos:

Proceso 1: Va a generar 10 direcciones IP de forma aleatoria y se las enviará al
Proceso 2.

Proceso 2: Va a leer las direcciones IP que recibe del Proceso 1 y va a enviar al 
Proceso 3 únicamente aquellas que pertenezcan a las clases A, B o C.

Proceso 3: Va a leer las direcciones IP procedentes del Proceso 2 (no se sabe qué 
número llegarán) y va a imprimir por consola la dirección IP y a continuación la 
clase a la que pertenece.

	Lanza los tres procesos en orden. """

from multiprocessing import Process, Queue
import time, random

def proceso1(q1):
    for i in range(10):
        ip = ".".join(str(random.randint(0,255)) for i in range(4))     # Máximo 255 números
        q1.put(ip)
        print(f"Leído: {ip}")
    q1.put(None)
    print("Lectura finalizada\n")
    return ip
    
def proceso2(q1, q2):
    # Filtra las IPs por clase y las envía a la siguiente cola junto con su clase
    while True:
        ip = q1.get()           # Trae las ips de el proceso1 
        if ip is None:          # Si el valor recibido es el marcador de fin
            q2.put(None)        # Pasa el marcador de fin al siguiente proceso
            break
        primer_numero = int(ip.split('.')[0])       # Separa la IP en partes usando el punto como separador y toma el primer elemento
        if (1 <= primer_numero <= 126):
            q2.put((ip, 'A'))
            print(f"IP A: {ip}")
        elif (128 <= primer_numero <= 191):
            q2.put((ip, 'B'))
            print(f"IP B: {ip}")
        elif (192 <= primer_numero <= 223):
            q2.put((ip, 'C'))
            print(f"IP C: {ip}")
    print("\n")

    
def proceso3(q2):
    # Lee las IPs y su clase desde la cola y las imprime
    while True:
        resultado = q2.get()         # Lo trae
        if resultado is None:        # Si el valor recibido es el marcador de fin
            break
        ip, clase = resultado           
        print(f"IP: {ip} - Clase: {clase}\n")
        
        
if __name__ == "__main__":
    # Creamos dos colas para comunicar los procesos
    q1 = Queue()
    q2 = Queue()
    inicio = time.perf_counter()
    
    # Lanzamos los procesos con las colas correspondientes
    p1 = Process(target=proceso1, args=(q1,))
    p2 = Process(target=proceso2, args=(q1, q2))
    p3 = Process(target=proceso3, args=(q2,))
    
    p1.start()
    p2.start()
    p3.start()
    
    p1.join()
    p2.join()
    p3.join()
    
    fin = time.perf_counter()
    tiempo_proceso = fin - inicio
    print(f"El proceso ha tardado {tiempo_proceso:.2f} segundos")