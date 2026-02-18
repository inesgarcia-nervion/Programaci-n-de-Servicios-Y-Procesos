import threading
import queue
import time
import random

def productor(q, n):
	for i in range(n):
		dato = f"dato-{i}"
		q.put(dato)
		print(f"Productor produce: {dato}")
		time.sleep(random.uniform(0.5, 1.5))

def consumidor(q, n):
	for _ in range(n):
		dato = q.get()
		print(f"Consumidor consume: {dato}")
		time.sleep(random.uniform(0.5, 1.5))

def main():
	N = 5  # Número de datos a producir/consumir
	q = queue.Queue(maxsize=1)  # Cola de tamaño 1
	t_prod = threading.Thread(target=productor, args=(q, N))
	t_cons = threading.Thread(target=consumidor, args=(q, N))
	t_prod.start()
	t_cons.start()
	t_prod.join()
	t_cons.join()

if __name__ == "__main__":
	main()

# Si el máximo a almacenar fueran 5 elementos, solo habría que cambiar maxsize=5.
