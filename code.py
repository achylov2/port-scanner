import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, init
from tqdm import tqdm

init(autoreset=True)

PORT_FILE = "all_ports_0-65535.txt"
OUTPUT_FILE = "open_ports.txt"

TIMEOUT = 0.5
THREADS = 500

def check_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(TIMEOUT)
        result = sock.connect_ex((ip, port))
        sock.close()

        if result == 0:
            return port
        else:
            return None
    except:
        return None

def main():
    # 👉 Ввод IP
    ip = input("🌍 Введи IP адрес: ")

    # 👉 Загружаем порты
    with open(PORT_FILE, "r") as f:
        ports = [int(p.strip()) for p in f.read().split(",")]

    open_ports = []

    print(Fore.CYAN + f"\n🎯 Сканируем IP: {ip}")
    print(Fore.YELLOW + f"Всего портов: {len(ports)}\n")

    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        futures = [executor.submit(check_port, ip, port) for port in ports]

        for future in tqdm(as_completed(futures), total=len(futures), desc="Сканирование", ncols=100):
            result = future.result()

            if result:
                open_ports.append(result)
                tqdm.write(Fore.GREEN + f"✅ OPEN: {result}")

    # 👉 Сохраняем
    with open(OUTPUT_FILE, "w") as f:
        for port in sorted(open_ports):
            f.write(str(port) + "\n")

    print(Fore.CYAN + "\n🎯 Готово!")
    print(Fore.GREEN + f"✔ Открытые порты: {len(open_ports)}")
    print(Fore.YELLOW + "📁 Сохранено в open_ports.txt")

if __name__ == "__main__":
    main()