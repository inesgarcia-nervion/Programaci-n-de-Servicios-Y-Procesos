import threading
import random
import time

class NumeroOcultoThread(threading.Thread):
	numero_a_adivinar = random.randint(0, 100)  # Número aleatorio entre 0 y 100
	acertado = False
	lock = threading.Lock()

	def __init__(self, nombre):
		super().__init__()
		self.nombre = nombre

	def run(self):
		while True:
			with NumeroOcultoThread.lock:
				if NumeroOcultoThread.acertado:
					break
				intento = random.randint(0, 100)
				print(f"{self.nombre} prueba con {intento}")
				if intento == NumeroOcultoThread.numero_a_adivinar:
					print(f"{self.nombre} ha acertado el número: {intento}")
					NumeroOcultoThread.acertado = True
					break
			time.sleep(0.01)

if __name__ == "__main__":
	print(f"Número a adivinar: {NumeroOcultoThread.numero_a_adivinar}")
	hilos = []
	for i in range(10): # 10 hilos
		t = NumeroOcultoThread(f"Hilo {i+1}")
		t.start()
		hilos.append(t)
	for t in hilos:
		t.join()
	print("Fin del juego")
