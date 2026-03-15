import importlib
import sys
from types import ModuleType


def check_import(package: str) -> ModuleType | None:
    """Prints a specific message depending on whether a package is imported."""
    try:
        module = importlib.import_module(package)
        name = getattr(module, "__name__", "Unknown")
        version = getattr(module, "__version__", "Unknown")
        print(f"[OK] {name} ({version})", end="")
        return module
    except ImportError:
        print(f"[KO] {package} dependency missing")
        return None


def matrix_analysis() -> None:
    # alias the imported modules cached in sys.modules
    pd = sys.modules["pandas"]
    np = sys.modules["numpy"]
    plt = sys.modules["matplotlib.pyplot"]

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    # generate 1000 random numbers
    data = np.random.randint(1000, size=(1000))
    # convert data into pandas dataframe
    df = pd.DataFrame(data, columns=["Data"])
    # add another column which is the index of each data point
    df["Index"] = np.arange(len(df))

    print("Generating visualization...")
    plt.figure()
    plt.plot(df["Index"], df["Data"])

    print("\nAnalysis complete!")
    res = "matrix_analysis.png"
    plt.savefig(res)
    print(f"Results saved to: {res}")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    pd = check_import("pandas")
    if pd:
        print(" - Data manipulation ready")
    np = check_import("numpy")
    if np:
        print(" - Numpy ready")
    mpl = check_import("matplotlib")
    if mpl:
        importlib.import_module("matplotlib.pyplot")
        print(" - Visualization ready")

    print("")
    if pd and np and mpl:
        matrix_analysis()
    else:
        print("Install dependencies with:")
        print("pip install -r requirements.txt # with pip")
        print("poetry install # with poetry")


if __name__ == "__main__":
    main()
