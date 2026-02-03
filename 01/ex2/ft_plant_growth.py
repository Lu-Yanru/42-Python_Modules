class Plant:
    """Define Plant class with name, height in cm, age in days."""
    def __init__(self, name: str, height: int, days: int) -> None:
        """Method to create an empty object."""
        self.name = name
        self.height = height
        self.days = days

    def grow(self, growth: int) -> None:
        """Plant growth in height."""
        self.height += growth

    def age(self, time: int) -> None:
        """Plant's age growth in days."""
        self.days += time

    def get_info(self) -> None:
        """Print out plant info."""
        print(f"{self.name}: {self.height}cm, {self.days} days old")


def main() -> None:
    """Displays plant growth info."""
    plant1 = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    plant1.get_info()
    day1_height = plant1.height
    print("=== Day 7 ===")
    plant1.grow(6)
    plant1.age(6)
    plant1.get_info()
    print(f"Growth this week: +{plant1.height - day1_height}cm")


if __name__ == "__main__":
    main()
