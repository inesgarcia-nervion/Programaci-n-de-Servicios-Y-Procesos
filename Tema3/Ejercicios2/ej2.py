import threading
import time
import random

class Panaderia(threading.Thread):
	lock = threading.Lock()

	def __init__(self, nombre):
		super().__init__()
		self.nombre = nombre

	def run(self):
		print(f"{self.nombre} está esperando a ser atendido.")
		with Panaderia.lock:
			print(f"{self.nombre} está siendo atendido.")
			tiempo = random.randint(1, 5)
			time.sleep(tiempo)
			print(f"{self.nombre} ha terminado de ser atendido.")

if __name__ == "__main__":
	clientes = [f"Cliente {i+1}" for i in range(10)]
	hilos = []
	for nombre in clientes:
		c = Panaderia(nombre)
		c.start()
		hilos.append(c)
	for c in hilos:
		c.join()
	print("Todos los clientes han sido atendidos.")
