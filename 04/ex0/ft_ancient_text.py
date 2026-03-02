# from typing import TextIO


# def check_closed(file: TextIO) -> None:
#     if file.closed is True:
#         print("File is closed.")
#     else:
#         print("File is open.")


def main() -> None:
    """Retrieve data from a file."""
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    filename = "ancient_fragment.txt"

    print(f"Accessing Storage Vault: {filename}")

    try:
        file = open(filename, "r")
    except (FileNotFoundError, PermissionError):
        print("\nERROR: Storage vault not found.")
        return

    print("Connection established...\n")
    print("RECOVERED DATA:")
    # Read and print the entire file
    print(file.read())

    # check_closed(file)
    print("\nData recovery complete. Storage unit disconnected.")

    file.close()
    # check_closed(file)


if __name__ == "__main__":
    main()
