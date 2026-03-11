from ex0 import CreatureCard


if __name__ == "__main__":
    print("=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:\n")

    fd = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print("CreatureCard Info:")
    print(fd.get_card_info())

    mana = 6
    print(f"\nPlaying Fire Dragon with {mana} available:")
    print(f"Playable: {fd.is_playable(mana)}")
    print(f"Play result: {fd.play({})}")

    gw = CreatureCard("Goblin Warrior", 2, "Common", 3, 5)
    print(f"\n{fd.name} attacks {gw.name}:")
    print(f"Attack result: {fd.attack_target(gw)}")

    mana -= 3
    print(f"\nTesting insufficient mana ({mana} available):")
    print(f"Playable: {fd.is_playable(mana)}")

    print("\nAbstract pattern successfully demonstrated!")
