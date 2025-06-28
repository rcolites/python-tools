import os
import hashlib
while True:
    print("1. Scanning")
    print("2. Hashing")
    print("3. Exit")
    choice = input()
    if choice == "1":
        path = input(r"Path to scan: ")
        if not path:
            print("Path cannot be empty")
            continue
        ext = input("Extension(s) to scan (comma-separated): ").lower().split(",")
        if not ext:
            print("Extension cannot be empty")
            continue

        for root, dirs, files in os.walk(path):
            for file in files:
                if any(file.lower().endswith(e.strip()) for e in ext):
                    print(f"{root}\\{file}")



    if choice == "2":
        file = input(r"Path to hash: ")
        try:
            with open(file, "rb") as f:
                print(hashlib.sha256(f.read()).hexdigest())
        except FileNotFoundError:
            print("File not found")
    if choice == "3":
        exit()







