import threading
import time

# Se crea el archivo
with open('vocales.txt', 'w') as f:
    f.write("Texto de ejemplo\n")
    f.write("Hola hola hola\n")

resultados = {}
resultados_lock = threading.Lock()

# Se lee ese archivo y busca las vocales
def contarVocales(vocal):
    with open("vocales.txt", 'r') as f:
        veces = f.read().lower().count(vocal)
    with resultados_lock:
        resultados[vocal] = veces
        hilo_nombre = threading.current_thread().name
        resultados[vocal] = (veces, hilo_nombre)

if __name__ == "__main__":
    inicio = time.perf_counter()
    vocales = ['a', 'e', 'i', 'o', 'u']
    hilos = []
    
    for vocal in vocales:
        t = threading.Thread(target=contarVocales, args=(vocal,))
        t.start()
        hilos.append(t)
        
    for t in hilos:
        t.join()
        
    for vocal in vocales:
            veces, hilo_nombre = resultados[vocal]
            print(f"{hilo_nombre}: La vocal {vocal} aparece {veces} veces")
        
    tiempo = time.perf_counter()
    tiempo_proceso = tiempo - inicio
    print(f"El proceso ha tardado {tiempo_proceso: .2} segundos")