import os
import sys
import platform
import random
import base64
import uuid
import socket
import subprocess
import time
import requests

def ascii_art():
    print("""
██   ██ ███████     ██   ██ ███████ ██      ██ ██      ███████ 
██   ██ ██          ██   ██ ██      ██      ██ ██      ██      
███████ █████       ███████ █████   ██      ██ ██      █████   
██   ██ ██          ██   ██ ██      ██      ██ ██      ██      
██   ██ ███████     ██   ██ ███████ ███████ ██ ███████ ███████ 

               UT-UTILS v3.1
Tools by @biyalue2
"I knew it was wrong, but I didn’t know how deep I was in."
""")

def info_ip_lokasi():
    try:
        print("Mengambil info IP dan lokasi...")
        res = requests.get("https://ipinfo.io/json")
        data = res.json()
        for k,v in data.items():
            print(f"{k.capitalize()}: {v}")
    except Exception as e:
        print("Gagal mengambil info IP:", e)

def cek_port_terbuka():
    host = input("Masukkan host/IP: ")
    port = input("Masukkan port: ")
    try:
        port = int(port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} di {host} TERBUKA")
        else:
            print(f"Port {port} di {host} TERTUTUP")
        sock.close()
    except Exception as e:
        print("Error:", e)

def ping_website():
    host = input("Masukkan alamat website: ")
    param = "-c" if platform.system().lower() != "windows" else "-n"
    command = ["ping", param, "4", host]
    try:
        subprocess.run(command)
    except Exception as e:
        print("Error ping:", e)

def cek_password():
    pwd = input("Masukkan password untuk cek kekuatan: ")
    strength = 0
    if len(pwd) >= 8:
        strength += 1
    if any(c.isupper() for c in pwd):
        strength += 1
    if any(c.islower() for c in pwd):
        strength += 1
    if any(c.isdigit() for c in pwd):
        strength += 1
    if any(c in "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|" for c in pwd):
        strength += 1
    print("Kekuatan password:", strength, "/5")

def generator_password():
    import string
    length = input("Panjang password: ")
    try:
        length = int(length)
        chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
        pwd = ''.join(random.choice(chars) for _ in range(length))
        print("Password:", pwd)
    except:
        print("Input tidak valid")

def enkripsi_base64():
    teks = input("Masukkan teks untuk enkripsi Base64: ")
    enc = base64.b64encode(teks.encode()).decode()
    print("Hasil enkripsi:", enc)

def dekripsi_base64():
    teks = input("Masukkan teks Base64 untuk dekripsi: ")
    try:
        dec = base64.b64decode(teks).decode()
        print("Hasil dekripsi:", dec)
    except Exception as e:
        print("Error dekripsi:", e)

def kalkulator():
    expr = input("Masukkan ekspresi matematika: ")
    try:
        hasil = eval(expr)
        print("Hasil:", hasil)
    except Exception as e:
        print("Error kalkulator:", e)

def fake_identity():
    names = ["Budi", "Ani", "Siti", "Joko", "Rina"]
    surnames = ["Santoso", "Widodo", "Putri", "Saputra", "Halim"]
    city = ["Jakarta", "Bandung", "Surabaya", "Medan", "Yogyakarta"]
    umur = random.randint(18, 45)
    print(f"Nama: {random.choice(names)} {random.choice(surnames)}")
    print(f"Umur: {umur}")
    print(f"Kota: {random.choice(city)}")

def konversi_suhu():
    c = input("Masukkan suhu dalam Celsius: ")
    try:
        c = float(c)
        f = c * 9/5 + 32
        k = c + 273.15
        print(f"{c}°C = {f}°F = {k}K")
    except:
        print("Input tidak valid")

def random_quote():
    quotes = [
        "Hidup adalah perjalanan, bukan tujuan.",
        "Jangan menyerah sebelum mencoba.",
        "Kesuksesan dimulai dari mimpi.",
        "Belajar dari kegagalan.",
        "Kerja keras tidak mengkhianati hasil."
    ]
    print(random.choice(quotes))

def info_waktu_dunia():
    zones = {"Jakarta": "Asia/Jakarta", "London": "Europe/London", "New York": "America/New_York"}
    try:
        import pytz
        from datetime import datetime
        for city, zone in zones.items():
            tz = pytz.timezone(zone)
            now = datetime.now(tz)
            print(f"{city}: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    except ImportError:
        print("Modul pytz belum terinstall. Install dengan: pip install pytz")

def generate_uuid():
    print("UUID:", uuid.uuid4())

def cek_domain():
    domain = input("Masukkan domain: ")
    try:
        ip = socket.gethostbyname(domain)
        print(f"IP {domain} adalah {ip}")
    except:
        print("Domain tidak valid atau tidak ditemukan.")

def clear_cache():
    if platform.system().lower() == "linux":
        os.system("sync; echo 3 > /proc/sys/vm/drop_caches")
        print("Cache cleared (Linux)")
    else:
        print("Fitur clear cache hanya tersedia di Linux.")

def random_joke():
    jokes = [
        "Kenapa programmer suka kopi? Karena dia suka debugging!",
        "Kenapa komputer nggak pernah ngambek? Karena ada restart!",
        "Kenapa programmer suka Halloween? Karena suka bug!",
    ]
    print(random.choice(jokes))

def cek_kecepatan_internet():
    try:
        import speedtest
        st = speedtest.Speedtest()
        print("Mengukur kecepatan internet...")
        down = st.download() / 1_000_000
        up = st.upload() / 1_000_000
        print(f"Download: {down:.2f} Mbps")
        print(f"Upload: {up:.2f} Mbps")
    except ImportError:
        print("Modul speedtest-cli belum terinstall. Install dengan: pip install speedtest-cli")
    except Exception as e:
        print("Error:", e)

def generate_angka_acak():
    a = input("Masukkan angka minimum: ")
    b = input("Masukkan angka maksimum: ")
    try:
        a, b = int(a), int(b)
        print("Angka acak:", random.randint(a, b))
    except:
        print("Input tidak valid.")

def konversi_bilangan():
    num = input("Masukkan angka desimal: ")
    try:
        num = int(num)
        print(f"Biner: {bin(num)}")
        print(f"Oktal: {oct(num)}")
        print(f"Heksadesimal: {hex(num)}")
    except:
        print("Input tidak valid.")

def cek_baterai_termux():
    if platform.system().lower() == "linux":
        try:
            res = subprocess.check_output(["termux-battery-status"]).decode()
            print("Status baterai:", res)
        except Exception:
            print("Fitur hanya tersedia di Termux dengan termux-api terinstall.")
    else:
        print("Fitur cek baterai hanya untuk Termux/Linux.")

def cek_cuaca():
    api_key = "YOUR_OPENWEATHER_API_KEY"  # Ganti dengan API key sendiri
    kota = input("Masukkan nama kota: ")
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={kota}&appid={api_key}&units=metric"
        res = requests.get(url).json()
        if res.get("cod") != 200:
            print("Kota tidak ditemukan.")
            return
        print(f"Cuaca di {kota}: {res['weather'][0]['description']}")
        print(f"Suhu: {res['main']['temp']}°C")
        print(f"Kelembapan: {res['main']['humidity']}%")
    except Exception as e:
        print("Gagal mengambil data cuaca:", e)

def cek_hari_libur():
    # Contoh sederhana, cek tanggal merah Indonesia (fix)
    hari_libur = ["2023-12-25", "2024-01-01", "2024-05-01"]
    tgl = input("Masukkan tanggal (YYYY-MM-DD): ")
    if tgl in hari_libur:
        print(f"{tgl} adalah hari libur nasional.")
    else:
        print(f"{tgl} bukan hari libur nasional.")

def download_file():
    url = input("Masukkan URL file: ")
    nama = input("Simpan sebagai nama file: ")
    try:
        r = requests.get(url, stream=True)
        with open(nama, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print("Download selesai.")
    except Exception as e:
        print("Error download:", e)

def info_os_sistem():
    print("Platform:", platform.platform())
    print("System:", platform.system())
    print("Release:", platform.release())
    print("Processor:", platform.processor())

def generate_qrcode():
    try:
        import qrcode
        data = input("Masukkan data untuk QR Code: ")
        img = qrcode.make(data)
        nama_file = "qrcode.png"
        img.save(nama_file)
        print(f"QR Code disimpan sebagai {nama_file}")
    except ImportError:
        print("Modul qrcode belum terinstall. Install dengan: pip install qrcode[pil]")

def keluar():
    print("Terima kasih sudah menggunakan UT-UTILS!")
    sys.exit()

def main_menu():
    while True:
        ascii_art()
        print("""
[1] Info IP dan Lokasi
[2] Cek Port Terbuka
[3] Ping Website
[4] Cek Password
[5] Generator Password
[6] Enkripsi Teks (Base64)
[7] Dekripsi Teks (Base64)
[8] Kalkulator
[9] Fake Identity
[10] Konversi Suhu
[11] Random Quote
[12] Info Waktu Dunia
[13] Generate UUID
[14] Cek Domain
[15] Clear Cache
[16] Random Joke
[17] Cek Kecepatan Internet
[18] Generate Angka Acak
[19] Konversi Bilangan
[20] Cek Baterai (Termux)
[21] Cek Cuaca
[22] Cek Hari Libur
[23] Download File
[24] Info OS dan Sistem
[25] Generate QR Code
[0] Keluar
""")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            info_ip_lokasi()
        elif pilihan == "2":
            cek_port_terbuka()
        elif pilihan == "3":
            ping_website()
        elif pilihan == "4":
            cek_password()
        elif pilihan == "5":
            generator_password()
        elif pilihan == "6":
            enkripsi_base64()
        elif pilihan == "7":
            dekripsi_base64()
        elif pilihan == "8":
            kalkulator()
        elif pilihan == "9":
            fake_identity()
        elif pilihan == "10":
            konversi_suhu()
        elif pilihan == "11":
            random_quote()
        elif pilihan == "12":
            info_waktu_dunia()
        elif pilihan == "13":
            generate_uuid()
        elif pilihan == "14":
            cek_domain()
        elif pilihan == "15":
            clear_cache()
        elif pilihan == "16":
            random_joke()
        elif pilihan == "17":
            cek_kecepatan_internet()
        elif pilihan == "18":
            generate_angka_acak()
        elif pilihan == "19":
            konversi_bilangan()
        elif pilihan == "20":
            cek_baterai_termux()
        elif pilihan == "21":
            cek_cuaca()
        elif pilihan == "22":
            cek_hari_libur()
        elif pilihan == "23":
            download_file()
        elif pilihan == "24":
            info_os_sistem()
        elif pilihan == "25":
            generate_qrcode()
        elif pilihan == "0":
            keluar()
        else:
            print("Pilihan tidak valid.")
        input("\nTekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main_menu()
