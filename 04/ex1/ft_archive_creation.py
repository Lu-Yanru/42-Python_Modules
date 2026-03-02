def main() -> None:
    """Write to a file."""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    filename = "new_discovery.txt"
    print(f"Initializing new storage unit: {filename}")
    try:
        with open(filename, "w") as writer:
            print("Storage unit created successfully...\n")
            print("Inscribing preservation data...")

            data1 = "[ENTRY 001] New quantum algorithm discovered\n"
            print(f"{data1}", end="")
            writer.write(data1)

            data2 = "[ENTRY 002] Efficiency increased by 347%\n"
            print(f"{data2}", end="")
            writer.write(data2)

            data3 = "[ENTRY 003] Archived by Data Archivist trainee\n"
            print(f"{data3}", end="")
            writer.write(data3)

        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{filename}' ready for long-term preservation.")

    except OSError as e:
        print("An error occured while writing the archive: ", e)


if __name__ == "__main__":
    main()
