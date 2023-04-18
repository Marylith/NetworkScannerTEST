import socket

host = input("Introduce la IP a escanear: ")
ports = input("introduce los puertos a escanear (separados con ,): ")

ports = ports.split(",")

print(f"Se escanearán {len(ports)} para la IP: {host}")

for actualport in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result=sock.connect_ex((host, int(actualport)))
    if result ==0:
        print(f"El puerto {actualport} está abierto")
    else:
        print(f"El puerto {actualport} está cerrado")
    sock.close()
