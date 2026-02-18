import threading
import time
import random

class Mensaje(threading.Thread):
    lock = threading.Lock()

    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.trabajo_realizado = False

    def run(self):
        while True:
            with Mensaje.lock:
                if self.trabajo_realizado:
                    break
                print(f"Soy {self.nombre} y estoy trabajando")
                tiempo = random.randint(1, 10)
                time.sleep(tiempo)
                print(f"Soy {self.nombre} y he terminado de trabajar")
                self.trabajo_realizado = True
                break

if __name__ == "__main__":
    nombres = ["Inés", "Ángela", "Dylan", "Paula", "Ale"]
    print("Soy el hilo principal")
    hilos = []
    for nombre in nombres:
        nom = Mensaje(nombre)
        nom.daemon = True  # Para que el programa termine si el principal termina
        nom.start()
        hilos.append(nom)
    while not all(hilo.trabajo_realizado for hilo in hilos):
        time.sleep(0.5)
    print("Fin del hilo principal.")