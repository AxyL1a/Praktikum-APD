# necessaryFunction.py

import time
import os

def load():
    """Tampilkan pesan sambutan saat program dimulai."""
    print("=" * 50)
    print("        🌈 Selamat Datang di Mood Tracker!        ")
    print("=" * 50)

def delayInput():
    """Memberikan jeda 1 detik agar tampilan lebih nyaman."""
    time.sleep(1)

def clear():
    """Membersihkan layar terminal (kompatibel Windows & Mac/Linux)."""
    os.system('cls' if os.name == 'nt' else 'clear')