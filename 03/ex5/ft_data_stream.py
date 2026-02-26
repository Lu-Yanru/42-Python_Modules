from time import perf_counter
from typing import Generator


def formate_list(lst: list[str] | list[int]) -> str:
    """Formate list items into a string separated by comma."""
    res = ""
    length = len(lst)
    for item in lst:
        res += str(item)
        if length > 1:
            res += ", "
        length -= 1
    return res


# Generator[yield_type, send_type, return_type]
def fib(n: int) -> Generator[int, None, None]:
    """Fibonacci sequence generator."""
    prev, curr = 0, 1
    i = 0
    while i < n:
        yield prev
        prev, curr = curr, prev + curr
        i += 1


def print_fib(n: int) -> None:
    """Print out first n Fibonacci sequence separated by comma."""
    fibo = fib(n)
    fib_lst: list[int] = []
    while True:
        try:
            fib_lst += [next(fibo)]
        except StopIteration:
            break
    fib_str = formate_list(fib_lst)
    print(f"Fibonacci sequence (first {n}): {fib_str}")


def prim() -> Generator[int, None, None]:
    """Prim nunber generator."""
    num = 2
    while True:
        i = 2
        while i < num:
            if num % i == 0:
                break
            i += 1
        if i == num:
            yield num
        num += 1


def print_prim(n: int) -> None:
    """Print out first n prim numbers separated by comma."""
    prim_num = prim()
    prim_lst: list[int] = []
    for _ in range(n):
        prim_lst += [next(prim_num)]
    prim_str = formate_list(prim_lst)
    print(f"Prim numbers (first {n}): {prim_str}")


def event_generator(n: int) -> Generator[dict[str, str | int], None, None]:
    """
    Game event generator.

    Yields:
    "event_num: int
    "player": str
    "lvl": int
    "event": str
    """
    players = ["alice", "bob", "charlie", "david"]
    len_players = len(players)
    events = ["killed monster", "found treasure", "leveled up"]
    len_events = len(events)
    for i in range(1, n + 1):
        yield {
            "event_num": i,
            "player": players[i % len_players],
            "lvl": (i * 3) % 20 + 1,
            "event": events[i % len_events]
        }


def main() -> None:
    print("=== Game Data Stream Processor ===")

    n = 1000
    print(f"\nProcessing {n} game events...\n")
    start = perf_counter()
    high_lvl_players = 0
    treasure = 0
    lvl_up = 0
    events = event_generator(n)
    for i in range(n):
        event = next(events)
        if int(event["lvl"]) >= 10:
            high_lvl_players += 1
        if event["event"] == "found treasure":
            treasure += 1
        if event["event"] == "leveled up":
            lvl_up += 1
        if i < 3:
            print(f"Event {event["event_num"]}: Player {event["player"]} "
                  f"(level {event["lvl"]}) {event["event"]}")

    print("...")
    end = perf_counter()

    print("")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {n}")
    print(f"High-level players (10+): {high_lvl_players}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {lvl_up}")

    print("")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {end - start:.3f} seconds")

    print("")
    print("=== Generator Demonstration ===")
    print_fib(10)
    print_prim(5)


if __name__ == "__main__":
    main()
