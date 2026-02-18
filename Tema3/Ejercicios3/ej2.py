import threading
import random
import time

clave = random.randint(1000, 9999)      # Clave secreta de 4 dígitos
encontrada = threading.Event()

def jugador(nombre, barrera):
	while not encontrada.is_set():
		intento = random.randint(1000, 9999)
		print(f"{nombre} intenta con la clave {intento}.")
		time.sleep(0.1)
		if intento == clave:
			print(f"{nombre} ha encontrado la clave: {clave}!")
			encontrada.set()
	print(f"{nombre} espera a los demás para salir.")
	barrera.wait()
	print(f"{nombre} ha salido de la sala.")

def main():
	N = 5
	barrera = threading.Barrier(N)
	hilos = []
	for i in range(1, N+1):
		nombre = f"Jugador {i}"
		hilo = threading.Thread(target=jugador, args=(nombre, barrera))
		hilos.append(hilo)
		hilo.start()
	for hilo in hilos:
		hilo.join()
	print("Todos han salido juntos de la Escape Room.")

if __name__ == "__main__":
	main()
