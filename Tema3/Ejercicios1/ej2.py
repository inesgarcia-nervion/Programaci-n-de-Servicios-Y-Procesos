import threading

class MiThread(threading.Thread):
	variable_compartida = 0
	lock = threading.Lock()     # Usamos Lock para sincronizar el acceso a la variable compartida

	def __init__(self, nombre):
		super().__init__()
		self.nombre = nombre

	def run(self):
		while True:
			with MiThread.lock:
				if MiThread.variable_compartida >= 1000:
					break
				MiThread.variable_compartida += 1
				print(f"{self.nombre} incrementa a {MiThread.variable_compartida}") # Uno de los hilos imprimirá el siguiente valor, pero no se garantiza cuál será

if __name__ == "__main__":
	nombres = [f"Hilo {i+1}" for i in range(10)]
	hilos = []
	for nombre in nombres:
		t = MiThread(nombre)
		t.start()
		hilos.append(t)
	for t in hilos:
		t.join()
	print(f"Número final: {MiThread.variable_compartida}")
