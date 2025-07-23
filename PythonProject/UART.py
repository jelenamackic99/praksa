import threading
import time
import serial

messagesSend=['Helo 1\n', 'Helo 2\n', 'Helo 3\n']
ser = serial.Serial('/dev/serial0', 9600, timeout=1)

def send():
    time.sleep(2)
    for mess in messagesSend:
        print(f"[TX] Sent: {mess.strip()}")
        ser.write(mess.encode())
        time.sleep(1)


def receive():
    time.sleep(2)
    while True:
        if ser.in_waiting > 0:
            data = ser.readline()
            if data:
                print(f"[RX] Received: {data.decode().strip()}")
        time.sleep(0.1)

# Kreiranje niti
txThread = threading.Thread(target=send)
rxThread= threading.Thread(target=receive, daemon=True)

txThread.start()
rxThread.start()

txThread.join()
time.sleep(2)

ser.close()
print("Gotovo!")
