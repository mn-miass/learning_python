if __name__ == "__main__":

    file_name = "ancient_fragment.txt"
    try:
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
        print(f"Accessing Storage Vault: {file_name}")
        file = open(file_name, "r")
        lines = file.readlines()

    except FileNotFoundError:
        print("File not found")

    else:
        print("Connection established...\n")
        print("RECOVERED DATA:")
        for line in lines:
            print(line, end="")
        print("\n\nData recovery complete. Storage unit disconnected.")
        file.close()
