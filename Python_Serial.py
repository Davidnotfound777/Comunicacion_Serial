import serial
import time
arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)
try:
    while True:
        comando = input("Escribe ON, OFF o SALIR: ")
        comando = comando.strip().upper()
        if comando == "SALIR":
            break
        if comando in ("ON", "OFF"):
            arduino.write((comando + "\n").encode("utf-8"))
            respuesta = arduino.readline().decode("utf-8", errors="replace").strip()
            print("Arduino:", respuesta)
        else:
            print("Comando no válido")
finally:
    arduino.close()
    print("Conexión serial cerrada")
