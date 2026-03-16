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

        with open(file_name, "w") as file:
            print("\nSECURE PRESERVATION:")
            file.write("[CLASSIFIED] New security protocols archived")
            print("[CLASSIFIED] New security protocols archived")
            print("Vault automatically sealed upon completion\n")

        print("All vault operations completed with maximum security.")
    except FileNotFoundError:
        print("File not found")
