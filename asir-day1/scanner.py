
import socket
target = input("Enter IP to scan:  ")

print(f"Scanning {target} ")

for port in [21,22,23,80,443,445,8080]:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    sock.close()
    
print("Scan complete.")




    

    