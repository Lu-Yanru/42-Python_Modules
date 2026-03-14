import os
import site
import sys


def main() -> None:
    # directory prefix where base Python is installed
    real_prefix = getattr(sys, "real_prefix", None)
    base_prefix = getattr(sys, "base_prefix", sys.prefix)

    # directory prefix that might be overwritten in virtual env
    venv_path = getattr(sys, "prefix", base_prefix)
    # venv name is the get the last str in the path
    venv_name = os.path.basename(venv_path)

    # absolute path of the executable binary for the Python interpreter
    current_python = sys.executable

    if venv_path != (real_prefix or base_prefix):
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {current_python}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {venv_path}")

        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages "
              "without affecting the global system.\n")

        print("Package installation path:")
        # a list containing all global site-packages directories.
        print(f"{site.getsitepackages()[0]}")
    else:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {current_python}")
        print("Virtual environment: None detected\n")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        print("To enter the constrct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate    # On Windows")
        print("\nThen run this program again.")


if __name__ == "__main__":
    main()
