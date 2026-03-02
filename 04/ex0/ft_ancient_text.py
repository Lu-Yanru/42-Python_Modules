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
    except FileNotFoundError:
        print("\nERROR: Storage vault not found.")
    except PermissionError:
        print("\nERROR: Access to storage vault denied.")


if __name__ == "__main__":
    main()
