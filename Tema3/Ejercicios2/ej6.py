import threading
import time
import random

NumFilosofos = 5
palillos = [threading.Lock() for _ in range(NumFilosofos)]

def filosofo(i):
	izq = i
	der = (i + 1) % NumFilosofos
	print(f"Filósofo {i} está pensando.")
	time.sleep(random.uniform(1, 3))

	if i == NumFilosofos - 1:           # El último filósofo toma los palillos en orden inverso para evitar interbloqueo
		primero, segundo = der, izq
	else:
		primero, segundo = izq, der
  
	with palillos[primero]:
		print(f"Filósofo {i} ha cogido el palillo {primero}.")
		with palillos[segundo]:
			print(f"Filósofo {i} ha cogido el palillo {segundo} y está comiendo.")
			time.sleep(random.uniform(1, 2))
			print(f"Filósofo {i} ha terminado de comer y suelta los palillos {primero} y {segundo}.")

def main():
	hilos = []
	for i in range(NumFilosofos):
		hilo = threading.Thread(target=filosofo, args=(i,), name=f"Filosofo-{i}")
		hilos.append(hilo)
		hilo.start()
	for hilo in hilos:
		hilo.join()

if __name__ == "__main__":
	main()


# ¿Interbloqueo? No, porque el último filósofo toma los palillos en orden inverso para evitar interbloqueo.
# No comer nunca? Sí, es posible por el planificador, aunque muy poco probable.