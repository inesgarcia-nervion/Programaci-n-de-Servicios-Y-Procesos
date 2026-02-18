import threading
import time
import random

def trabajador(nombre, barrera, pedido_evento):
	print(f"{nombre} listo para empezar.")
	barrera.wait()
	while True:
		print(f"{nombre} espera un pedido...")
		pedido_evento.wait()
		print(f"{nombre} empieza a preparar el pedido.")
		pedido_evento.clear()
		time.sleep(random.uniform(1, 3))
		print(f"{nombre} ha terminado el pedido.")
		# Espera a que se genere un nuevo pedido
		time.sleep(0.5)

def generador_pedidos(pedido_evento, repeticiones):
	for i in range(repeticiones):
		time.sleep(random.uniform(2, 4))
		print(f"\nNuevo pedido generado.")
		pedido_evento.set()
	print("\nNo hay más pedidos.")

def main():
	N = 4  # Número de trabajadores
	REPETICIONES = 5  # Número de pedidos
	barrera = threading.Barrier(N)
	pedido_evento = threading.Event()
	hilos = []
	for i in range(1, N+1):
		nombre = f"Trabajador {i}"
		hilo = threading.Thread(target=trabajador, args=(nombre, barrera, pedido_evento))
		hilos.append(hilo)
		hilo.daemon = True
		hilo.start()
	generador_pedidos(pedido_evento, REPETICIONES)
	time.sleep(2)

if __name__ == "__main__":
	main()
