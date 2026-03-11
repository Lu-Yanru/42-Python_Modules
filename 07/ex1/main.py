from ex0 import CreatureCard
from ex1 import Deck, ArtifactCard, SpellCard


if __name__ == "__main__":
    print("=== DataDeck Deck Builder ===\n")

    try:
        print("Building deck with different card types...")
        mydeck = Deck()
        bolt = SpellCard("Lightning Bolt", 3, "Common", "damage")
        crystal = ArtifactCard("Mana Crystal", 2, "Rare", 10,
                               "Permanent: +1 mana per turn")
        fd = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        mydeck.add_card(bolt)
        mydeck.add_card(crystal)
        mydeck.add_card(fd)
        print(f"Deck stats: {mydeck.get_deck_stats()}")

        print("\nDrawing and playing cards:\n")

        mydeck.shuffle()
        for i in range(3):
            card = mydeck.draw_card()
            print(f"Drew: {card.name} "
                  f"({card.__class__.__name__.replace("Card", "")})")
            print(f"Play result: {card.play({})}\n")

        print("Polymorphism in action: Same interface, "
              "different card behaviors!")
    except (ValueError, TypeError) as e:
        print(e)
