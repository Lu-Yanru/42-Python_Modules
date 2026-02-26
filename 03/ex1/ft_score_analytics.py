import sys


def main() -> None:
    """
    A function that takes scores from the command line
    and stores them into a list.
    """
    scores: list[int] = []

    print("=== Player Score Analytics ===")

    argc = len(sys.argv)
    if argc < 2:
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    for score in sys.argv[1:]:
        try:
            scores.append(int(score))
        except ValueError:
            print("Input contains non-digits!")
            return

    print(f"Score processed: {scores}")
    print(f"Total players: {argc - 1}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
