import sys
import time
import os

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def main():
    os.system('clear')
    print(GREEN + "[*] Initializing system diagnostic..." + RESET)
    time.sleep(1)

    for i in range(3, 0, -1):
        print(RED + f"[!] Alert trigger in {i}..." + RESET)
        time.sleep(1)

    # Fast alert and scrolling warning loop that keeps going until closed
    try:
        while True:
            sys.stdout.write(RED + "\a[CRITICAL] SYSTEM COMPROMISED - MALWARE DETECTED!\n" + RESET)
            sys.stdout.flush()
            time.sleep(0.08)
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()
