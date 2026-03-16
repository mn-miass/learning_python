if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    try:
        file_name = "lost_archive.txt"
        file = open(file_name, "r")
        print(f"ROUTINE ACCESS: Attempting access to {file_name}...")
        line = file.read()
        print(f"SUCCESS: Archive recovered - '{line}'")
        print("STATUS: Normal operations resumed")
        file.close()

    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to {file_name}...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    try:
        file_name = "classified_vault.txt"
        file = open(file_name, "r")
        print(f"ROUTINE ACCESS: Attempting access to {file_name}...")
        line = file.read()
        print(f"SUCCESS: Archive recovered - '{line}'")
        print("STATUS: Normal operations resumed")
        file.close()

    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to {file_name}...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    try:
        file_name = "standard_archive.txt"
        file = open(file_name, "r")
        print(f"ROUTINE ACCESS: Attempting access to {file_name}...")
        line = file.read()
        print(f"SUCCESS: Archive recovered - '{line}'")
        print("STATUS: Normal operations resumed")
        file.close()

    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to {file_name}...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
