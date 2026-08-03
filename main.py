import qrcode
import msvcrt
import time
import sys
import os
from colorama import init, Fore, Style
init()

def clear():
    os.system("cls")

def press_any_key():
    clear()
    print("=" * 40)
    print(Fore.GREEN + "QrGenerator - v1.0".center(40) + Style.RESET_ALL)
    print("=" * 40)
    print()

    dots = ["", ".", "..", "..."]
    i = 0
    while not msvcrt.kbhit():
        print(f"\rPress any key to continue{dots[i % 4]}   ", end="", flush=True)
        i += 1
        time.sleep(0.6)

    msvcrt.getch()

def fake_processing():
    pasos = [
        "Validating...",
        "Doing stuff...",
        "Generating QR code..."
    ]
    for paso in pasos:
        print(f"[*] {paso}")
        time.sleep(0.8)
    print(Fore.GREEN + "\n[✓] Process completed." + Style.RESET_ALL)
    print("=" * 40)
    print("\n")
    time.sleep(1.9)
    clear() 

def generate_qr():
    clear()
    print("=" * 40)
    link = ""
    while not link:
        link = input("Paste the link or text you want to convert: ").strip()

        if not link:
            print(Fore.RED + "\nInvalid input. Please provide a valid link or text." + Style.RESET_ALL)
            time.sleep(1.5)
            print("=" * 40)

    print()
    fake_processing()

    qr = qrcode.make(link)

    print("=" * 40)
    fName = ""
    while not fName.endswith(".png"):
        fName = input("Enter the name for the QR code image file (include .png): ").strip()

        if not fName.endswith(".png"):
            print(Fore.RED + "\nInvalid input. The file name must end with .png" + Style.RESET_ALL)
            time.sleep(1.5)
            print("=" * 40)

    qr.save(fName)

    print(Fore.GREEN + "QR code generated successfully!" + Style.RESET_ALL)
    print(f"File name: {fName}")
    print(f"Saved in: {os.path.abspath(fName)}")
    print("=" * 40)
    time.sleep(1)
    

def main():
    while True:
        press_any_key()
        generate_qr()

        respuesta = input("\nDo you want to generate another QR? (y/n): ").strip().lower()
        while respuesta not in ["y", "n"]:
            print("\nInvalid input. Please enter 'y' for yes or 'n' for no.")
            time.sleep(1.5)
            respuesta = input("\nDo you want to generate another QR? (y/n): ").strip().lower()
        clear()
        if respuesta != "y":
            print("\nClosing program")
            time.sleep(0.4)
            for i in range(3):
                print(".", end="", flush=True)
                time.sleep(0.5)
            break

if __name__ == "__main__":
    main()