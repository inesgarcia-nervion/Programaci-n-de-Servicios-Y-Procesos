import threading
import time
import random

class Cliente:
	def __init__(self, nombre):
		self.nombre = nombre
		self.atendido_carniceria = False
		self.atendido_charcuteria = False

def atender_seccion(cliente, semaforo, seccion):
	with semaforo:
		print(f"El cliente {cliente.nombre} está siendo atendido en {seccion}.")
		tiempo = random.randint(1, 10)
		time.sleep(tiempo)
		print(f"El cliente {cliente.nombre} ha terminado en {seccion}.")
		if seccion == "carnicería":
			cliente.atendido_carniceria = True
		else:
			cliente.atendido_charcuteria = True

def proceso_cliente(cliente, sem_carniceria, sem_charcuteria):
	# El cliente debe ser atendido en ambas secciones, en cualquier orden
	while not (cliente.atendido_carniceria and cliente.atendido_charcuteria):
		# Intentar carnicería si no ha sido atendido
		if not cliente.atendido_carniceria and sem_carniceria.acquire(blocking=False):
			atender_seccion(cliente, DummySemaphore(sem_carniceria), "carnicería")
		# Intentar charcutería si no ha sido atendido
		elif not cliente.atendido_charcuteria and sem_charcuteria.acquire(blocking=False):
			atender_seccion(cliente, DummySemaphore(sem_charcuteria), "charcutería")
		else:
			# Esperar un poco antes de volver a intentar
			time.sleep(0.1)
	print(f"El cliente {cliente.nombre} ha sido completamente atendido en ambos establecimientos.")


class DummySemaphore:       # Clase auxiliar para liberar el semáforo al salir del bloque with
	def __init__(self, sem):
		self.sem = sem
	def __enter__(self):
		return self.sem
	def __exit__(self, exc_type, exc_val, exc_tb):
		self.sem.release()

def main():
	sem_carniceria = threading.Semaphore(4)
	sem_charcuteria = threading.Semaphore(2)
	hilos = []
	for i in range(1, 11):
		cliente = Cliente(f"Cliente {i}")
		hilo = threading.Thread(target=proceso_cliente, args=(cliente, sem_carniceria, sem_charcuteria), name=cliente.nombre)
		hilos.append(hilo)
		hilo.start()
	for hilo in hilos:
		hilo.join()

if __name__ == "__main__":
	main()
