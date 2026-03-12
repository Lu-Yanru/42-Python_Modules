from ex0 import CreatureCard
from ex1 import SpellCard
from ex3 import AggressiveStrategy, FantasyCardFactory, GameEngine


if __name__ == "__main__":
    print("=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    engine_stats = engine.get_engine_status()
    for key, value in engine_stats.items():
        print(f"{key}: {value}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    try:
        # Create hand
        fd = CreatureCard("Fire Dragon", 5, "Legendary", 5, 7)
        gw = CreatureCard("Goblin Warrior", 2, "Common", 3, 5)
        bolt = SpellCard("Lightning Bolt", 3, "Rare", "damage")

        engine.hand.append(fd)
        engine.hand.append(gw)
        engine.hand.append(bolt)
        engine.cards_created += len(engine.hand)

        hand_str = "Hand: ["
        for i in range(len(engine.hand)):
            hand_str += engine.hand[i].name
            hand_str += f" ({engine.hand[i].cost})"
            if i < len(engine.hand) - 1:
                hand_str += ", "
        hand_str += "]"
        print(hand_str)

        # Create enemy
        enemy = factory.create_creature("Enemy Player")
        engine.battlefield.append(enemy)

        print("\nTurn execution:")
        print(f"Strategy: {strategy.get_strategy_name()}")
        turn = engine.simulate_turn()
        print(f"Actions: {engine.log[0]}")

        print("\nGame report:")
        print(f"{turn}")

        print("\nAbstract Facotry + Strategy Pattern: "
              "Maximum flexibility achieved!")

    except ValueError as e:
        print(e)
