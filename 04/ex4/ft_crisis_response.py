def file_handler(filename: str) -> None:
    try:
        with open(filename, "r") as reader:
            print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
            content = reader.read()
            print(f"SUCCESS: Archive recovered - ``{content}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except OSError as e:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        print("RESPONSE: ", e)
        print("STATUS: Crisis handled, system stable.")


def main() -> None:
    """Context manager and error handling."""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    file_handler("lost_archive.txt")
    print("")
    file_handler("classified_vault.txt")
    print("")
    file_handler("standard_archive.txt")

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
