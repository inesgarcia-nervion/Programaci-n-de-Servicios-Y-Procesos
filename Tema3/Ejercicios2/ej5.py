import threading
import time
import random

NumEstudiantes = 4     # Número de estudiantes
NumLibros = 9          # Número de libros disponibles

libros = [threading.Lock() for _ in range(NumLibros)]

def estudiante(nombre):
	while True:
		idx1, idx2 = random.sample(range(NumLibros), 2) 		# Selecciona dos libros distintos al azar
		primero, segundo = sorted([idx1, idx2])
		acquired1 = libros[primero].acquire(timeout=0.1)		# Intentar adquirir ambos libros (si no puede, espera y reintenta)
  
		if not acquired1:
			continue
		acquired2 = libros[segundo].acquire(timeout=0.1)
  
		if not acquired2:
			libros[primero].release()
			continue

		print(f"{nombre} ha cogido los libros {primero+1} y {segundo+1}.")  		# Ambos libros adquiridos
		tiempo = random.randint(3, 5)
		time.sleep(tiempo)
		print(f"{nombre} ha liberado los libros {primero+1} y {segundo+1}.")        # Ambos libros liberados
		libros[primero].release()
		libros[segundo].release()
		break

def main():
	hilos = []
	for i in range(1, NumEstudiantes+1):
		nombre = f"Estudiante {i}"
		hilo = threading.Thread(target=estudiante, args=(nombre,), name=nombre)
		hilos.append(hilo)
		hilo.start()
  
	for hilo in hilos:
		hilo.join()

if __name__ == "__main__":
	main()
