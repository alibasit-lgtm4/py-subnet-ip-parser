import socket
import threading

def scan_host(ip, port=80):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((ip, port))
    if result == 0:
        print(f"Host {ip} is active on port {port}")
    s.close()

def main():
    base_ip = "192.168.1."
    print(f"Scanning subnet: {base_ip}0-255...")
    threads = []
    for i in range(1, 50): # Limit to 50 for quick execution
        ip = f"{base_ip}{i}"
        t = threading.Thread(target=scan_host, args=(ip,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("Subnet scan complete.")

if __name__ == "__main__":
    main()
