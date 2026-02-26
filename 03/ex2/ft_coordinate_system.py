import math
import sys


def calc_distance(coor1: tuple,
                  coor2: tuple) -> float:
    """
    Calculates the distance btw 2 3D coordinates
    using Euclidean distance formula.
    """
    (x1, y1, z1) = coor1
    (x2, y2, z2) = coor2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


def main() -> None:
    """Creates and parse 3D coordinates as tuples."""
    if len(sys.argv) < 2:
        print("No coordinates provided. "
              "Usage: 'x1,y1,z1' 'x2,y2,z2' ...")
        return

    print("=== Game Coordinate System ===")
    print("")

    start = (0, 0, 0)
    default_coor = (10, 20, 5)
    print(f"Position created: {default_coor}")
    print(f"Distance between {start} and {default_coor}: "
          f"{calc_distance(start, default_coor): .2f}")
    print("")

    for arg in sys.argv[1:]:
        print(f"Parsing coordinates: \"{arg}\"")
        str_lst = arg.split(",")
        int_lst: list[int] = []
        for i in str_lst:
            try:
                num = int(i)
                int_lst.append(num)
            except ValueError:
                print("Error parsing coordinates: "
                      f"invalid literal for int() with base 10: '{i}'")
                print("Error details - Type: ValueError, Args: "
                      "(\"invalid literal for int() with base 10: "
                      f"'{i}'\",)")
                print("")
                break

        if len(int_lst) != 3:
            print(f"Invalid coordinate {int_lst}")
            print("")
            continue

        new_coor = tuple(int_lst)
        print(f"Parsed position: {new_coor}")
        print(f"Distance between {start} and {new_coor}: "
              f"{calc_distance(start, new_coor): .2f}")
        print("")

    print("Unpacking demonstration:")
    (x, y, z) = new_coor
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
