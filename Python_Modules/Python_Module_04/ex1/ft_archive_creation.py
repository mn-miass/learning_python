if __name__ == "__main__":

    file_name = "new_discovery.txt"
    file = open(file_name, "w")

    data = ["[ENTRY 001] New quantum algorithm discovered\n",
            "[ENTRY 002] Efficiency increased by 347%\n",
            "[ENTRY 003] Archived by Data Archivist trainee\n"]

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print(f"Initializing new storage unit: {file_name}")
    print("Storage unit created successfully...\n")

    print("Inscribing preservation data...")
    for line in data:
        file.write(line)
        print(line, end="")
    print()
    print("Data inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")
