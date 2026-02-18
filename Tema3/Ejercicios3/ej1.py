import threading
import time
import random

def corredor(nombre, salida, resultados):
	print(f"{nombre} está en la línea de salida.")
	salida.wait()  # Espera a que todos estén listos
	inicio = time.time()
	duracion = random.uniform(2, 5)     	# Tiempo de carrera
	time.sleep(duracion)
	fin = time.time()
	tiempo_total = fin - inicio
	resultados[nombre] = tiempo_total
	print(f"{nombre} ha terminado la carrera en {tiempo_total:.2f} segundos.")

def main():
	N = 10
	salida = threading.Barrier(N + 1)  # +1 para el hilo principal
	resultados = {}
	hilos = []
	for i in range(1, N+1):
		nombre = f"Corredor {i}"
		hilo = threading.Thread(target=corredor, args=(nombre, salida, resultados))
		hilos.append(hilo)
		hilo.start()
  
	while salida.n_waiting < N: 	# Espera a que todos estén listos
		time.sleep(0.1)
	print("\n¡Preparados!")
	for i in range(3, 0, -1):       # Cuenta regresiva, empieza en 3 y termina en 1
		print(i)
		time.sleep(1)
	print("¡YA!\n")
	salida.wait()  # Da el pistoletazo de salida
	for hilo in hilos:
		hilo.join()

if __name__ == "__main__":
	main()
