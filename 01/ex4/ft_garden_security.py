class SecurePlant:
    """Define Plant class with name, height in cm, age in days."""
    def __init__(self, name: str, height: int = 0, age: int = 0) -> None:
        """Method to create an empty object."""
        self.name = name
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        """
        Update height info if the height is positive,
        otherwise print an error message.
        """
        if height >= 0:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int) -> None:
        """
        Update age info if the age is positive,
        otherwise print an error message.
        """
        if age >= 0:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self) -> int | None:
        """Get the height of the plant."""
        try:
            return self.__height
        except Exception:
            return None

    def get_age(self) -> int | None:
        """Get the age of the plant."""
        try:
            return self.__age
        except Exception:
            return None

    def plant_info(self) -> None:
        """Print out current plant info."""
        try:
            print("Current plant: "
                  f"{self.name} ({self.__height}cm, {self.__age} days)")
        except Exception:
            print("Invalid plant info.")


def main() -> None:
    """Displays secured plant info."""
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", -1, -1)

    print("")
    plant.set_height(-5)
    height1 = plant.get_height()
    print(f"Height before: {height1}")

    # plant.__height = 25
    plant.set_height(25)
    height2 = plant.get_height()
    # height2 = plant.__height
    print(f"Height after: {height2}cm")

    plant.plant_info()
    plant.set_age(30)

    print("")
    plant.plant_info()


if __name__ == "__main__":
    main()
