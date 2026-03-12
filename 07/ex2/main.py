from ex0 import Card, CreatureCard
from ex2 import Combatable, Magical, EliteCard


if __name__ == "__main__":
    print("=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print(f"Card: {[method for method in dir(Card)
                    if not method.startswith("_")]}")
    print(f"Combatable: {[method for method in dir(Combatable)
                         if not method.startswith("_")]}")
    print(f"Magical: {[method for method in dir(Magical)
                      if not method.startswith("_")]}")

    print("\nPlaying Arcane Warrior (Elite Card):\n")

    try:
        aw = EliteCard("Arcane Warrior", 4, "Legendary", 7, 5, 5, 4)
        enemy0 = CreatureCard("Enemy", 2, "Common", 3, 4)
        enemy1 = CreatureCard("Enemy1", 2, "Common", 3, 4)
        enemy2 = CreatureCard("Enemy2", 2, "Common", 3, 4)

        print("Combat Phase:")
        print(f"Attack result: {aw.attack(enemy0)}")
        print(f"Defense result: {aw.defend(enemy0.attack)}")

        print("\nMagic phase:")
        print(f"Spell cast: {aw.cast_spell("Fireball", [enemy1, enemy2])}")
        print(f"Mana channel: {aw.channel_mana(3)}")

        print("\nMultiple interface implementation successful!")
    except ValueError as e:
        print(e)
