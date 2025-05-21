import re
import time
import sys
from datetime import datetime

# Warna ANSI
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def loading(text="Memproses"):
    for i in range(3):
        sys.stdout.write(f"\r{YELLOW}{text}{'.' * (i+1)}{' ' * (3-i)}{RESET}")
        sys.stdout.flush()
        time.sleep(0.4)
    print("")

def cek_keamanan_password(password):
    loading("Menganalisis password")
    score = 0
    length = len(password)

    if length >= 8: score += 1
    if length >= 12: score += 1
    if re.search(r'[a-z]', password): score += 1
    if re.search(r'[A-Z]', password): score += 1
    if re.search(r'[0-9]', password): score += 1
    if re.search(r'[\W_]', password): score += 1

    if score <= 2:
        return f"{RED}Lemah{RESET}"
    elif score <= 4:
        return f"{YELLOW}Sedang{RESET}"
    else:
        return f"{GREEN}Kuat{RESET}"

def cek_pintar(text):
    loading("Menganalisis teks")
    kata = len(text.split())
    huruf = len(text.replace(" ", ""))
    return f"Teks mengandung {CYAN}{kata}{RESET} kata dan {CYAN}{huruf}{RESET} huruf."

def menu():
    print(f"\n{CYAN}=== MENU CEK CERDAS ==={RESET}")
    print("1. Cek Pintar (Analisis teks)")
    print("2. Cek Keamanan Password")
    print("3. Keluar")
    print(f"{YELLOW}----------------------------{RESET}")
    print(f"Dev: {GREEN}@biyalue2{RESET}")

def main():
    print(f"{GREEN}Halo dari Termux lewat GitHub!{RESET}")
    print("Waktu sekarang:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    while True:
        menu()
        pilihan = input("Pilih menu (1/2/3): ").strip()

        if pilihan == "1":
            teks = input("Masukkan teks untuk cek pintar: ")
            hasil = cek_pintar(teks)
            print("Hasil:", hasil)
        elif pilihan == "2":
            pwd = input("Masukkan password untuk dicek: ")
            hasil = cek_keamanan_password(pwd)
            print(f"Keamanan password: {hasil}")
        elif pilihan == "3":
            print(f"{CYAN}Terima kasih, sampai jumpa!{RESET}")
            break
        else:
            print(f"{RED}Pilihan tidak valid, coba lagi.{RESET}")

if __name__ == "__main__":
    main()
