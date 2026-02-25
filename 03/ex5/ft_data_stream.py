from typing import Generator


def fib() -> Generator:
    """Fibonacci sequence generator."""
    prev, curr = 0, 1
    while True:
        yield prev
        prev, curr = curr, prev + curr


def main() -> None:
    print("=== Game Data Stream Processor ===")


if __name__ == "__main__":
    main()
