from multiprocessing import Process
import time

def saludar(nombre):
    print(f"Hola {nombre}")
    time.sleep(2)
    print(f"Adiós {nombre}")

if __name__ == '__main__':
    p = Process(target=saludar, args=('Inés',))
    
    p.start()   # Arranca el proceso
    p.join()    # Espera a que termine

    print("El proceso ha terminado")
