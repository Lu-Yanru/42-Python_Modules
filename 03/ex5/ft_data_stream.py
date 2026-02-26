from typing import Generator


def fib(n: int) -> Generator[int]:
    """Fibonacci sequence generator."""
    prev, curr = 0, 1
    i = 0
    while i < n:
        yield prev
        prev, curr = curr, prev + curr
        i += 1


def main() -> None:
    print("=== Game Data Stream Processor ===")


if __name__ == "__main__":
    main()
