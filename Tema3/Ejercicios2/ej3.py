import threading
import time
import random

def atender_cliente(nombre, semaforo):
	with semaforo:
		print(f"El cliente {nombre} está siendo atendido.")
		tiempo = random.randint(1, 10)
		time.sleep(tiempo)
		print(f"El cliente {nombre} ha terminado en la carnicería.")

def main():
	semaforo = threading.Semaphore(4)  # Semaphore limita a 4 clientes atendidos simultáneamente
	hilos = []
	for i in range(1, 11):
		nombre = f"Cliente {i}"
		hilo = threading.Thread(target=atender_cliente, args=(nombre, semaforo), name=nombre)
		hilos.append(hilo)
		hilo.start()
	for hilo in hilos:
		hilo.join()

if __name__ == "__main__":
	main()
