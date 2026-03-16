if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    file_name = "classified_data.txt"

    try:
        with open(file_name, "r") as file:
            lines = file.read()
            print("Initiating secure vault access...")
            print("Vault connection established with failsafe protocols")
            print("\nSECURE EXTRACTION:")
            print(lines)

        file_name = "security_protocols.txt"
        with open(file_name, "r") as file:
            print("\nSECURE PRESERVATION:")
            line = file.read()
            print(line)
            print("Vault automatically sealed upon completion\n")

        print("All vault operations completed with maximum security.")
    except FileNotFoundError:
        print("\nFile not found")
