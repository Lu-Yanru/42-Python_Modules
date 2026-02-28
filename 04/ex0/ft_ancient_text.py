def main() -> None:
    """Retrieve data from a file."""
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    filename = "ancient_fragment.txt"

    print(f"Accessing Storage Vault: {filename}")

    try:
        with open(filename, "r") as reader:
            print("Connection established...\n")
            print("RECOVERED DATA:")
            # Read and print the entire file
            print(reader.read())
        print("\nData recovery complete. Storage unit disconnected.")
    except (FileNotFoundError, PermissionError):
        print("\nERROR: Storage vault not found.")


if __name__ == "__main__":
    main()
