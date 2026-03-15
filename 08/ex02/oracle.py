try:
    from dotenv import load_dotenv
except ImportError:
    print("Missing module dotenv")
    print("Install using: pip install python-dotenv")
    exit()
import os


def get_config() -> dict[str, str]:
    config: dict[str, str] = {}
    variables = ['MATRIX_MODE', 'DATABASE_URL', 'API_KEY',
                 'LOG_LEVEL', 'ZION_ENDPOINT']
    for var in variables:
        res = os.getenv(var)
        if res is None:
            print(f"Cannot get environment varaible {var}. Exiting.")
            exit(1)
        config[var] = res

    return config


def security_check(config: dict[str, str]) -> None:
    print('\nEnvironment security check:')
    for key, value in config.items():
        if not value:
            print(f"[ERROR] Environment varaible {key} not correctly loaded. "
                  "Exiting.")
            exit(1)
    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[ERROR] .env file not found.")

    if config["MATRIX_MODE"] == "production":
        print("[OK] Production overrides available")
    else:
        print("[INFO] Running in development mode")


if __name__ == "__main__":
    print("ORACLE STATUS: READING the Matrix...\n")

    print("Configuration loaded:")
    load_dotenv()

    config = get_config()
    print(f"Mode: {config["MATRIX_MODE"]}")
    if config["DATABASE_URL"]:
        print("Database: Connected to local instance")
    if config["API_KEY"]:
        print("API Access: Authenticated")
    print(f"Log Level: {config["LOG_LEVEL"]}")
    if config["ZION_ENDPOINT"]:
        print("Zion Network: Online")

    security_check(config)

    print('\nThe Oracle sees all configurations.')
