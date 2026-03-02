def main() -> None:
    """Using context manager."""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    error = False
    print("Initiating secure vault access...")
    filename1 = "classified_data.txt"
    try:
        with open(filename1, "r") as reader:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            print(reader.read())
    except (FileNotFoundError, PermissionError):
        print(f"ERROR: Cannot access archive {filename1}.")
        error = True

    filename2 = "security_protocols.txt"
    try:
        with open(filename2, "w") as writer:
            print("\nSECURE PRESERVATION:")
            data = "[CLASSIFIED] New security protocols archived"
            print(data)
            writer.write(data)
            print("Vault automatically sealed upon completion")
    except OSError:
        print(f"Error: Fail to write to archive {filename2}")
        error = True

    if error is False:
        print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
