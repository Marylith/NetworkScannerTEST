import socket

def leer_archivo(filename:str):
    with open(filename, "r") as file:
        lineas= file.readlines()
        lineas_limpias=[]
        for linea in lineas:
            lineas_limpias.append(linea.rstrip())
        return lineas_limpias

hosts = leer_archivo("ips.txt")

ports = leer_archivo("common_ports.txt")

for host in hosts:
    print(f"En la ip {host}")
    for actualport in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result=sock.connect_ex((host, int(actualport)))
        if result ==0:
            print(f"El puerto {actualport} está abierto")
        else:
            print(f"El puerto {actualport} está cerrado")
        sock.close()
    print(f"\n")
