import threading
import time
import random

class PasoPeatones:
	def __init__(self, capacidad):
		self.capacidad = capacidad
		self.lock = threading.Lock()
		self.esperando = []
		self.semaforo_verde = threading.Event()

	def esperar_para_cruzar(self, nombre):
		with self.lock:
			self.esperando.append(nombre)
		print(f"{nombre} espera para cruzar.")
		self.semaforo_verde.wait()
		print(f"{nombre} cruza el paso de peatones.")

	def liberar_peatones(self):
		with self.lock:
			if self.esperando:
				print(f"\nSemáforo en verde: ¡Peatones pueden cruzar!")
				self.semaforo_verde.set()
				time.sleep(1)  # Tiempo para cruzar
				self.esperando.clear()
				self.semaforo_verde.clear()

def peaton(nombre, paso):
	time.sleep(random.uniform(0, 3))  # Llegada aleatoria
	paso.esperar_para_cruzar(nombre)

def semaforo(paso, intervalos):
	for _ in range(intervalos):
		time.sleep(3)
		paso.liberar_peatones()

def main():
	N = 10
	INTERVALOS = 5
	paso = PasoPeatones(N)
	hilos = []
	for i in range(1, N+1):
		nombre = f"Peatón {i}"
		hilo = threading.Thread(target=peaton, args=(nombre, paso))
		hilos.append(hilo)
		hilo.start()
	t_semaforo = threading.Thread(target=semaforo, args=(paso, INTERVALOS))
	t_semaforo.start()
	for hilo in hilos:
		hilo.join()
	t_semaforo.join()
	print("\nTodos los peatones han cruzado.")

if __name__ == "__main__":
	main()
