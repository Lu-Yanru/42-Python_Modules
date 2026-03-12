from ex3 import AggressiveStrategy, FantasyCardFactory, GameEngine


if __name__ == "__main__":
    print("=== DataDeck Game Engine ===\n")

    print("Configureing Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    engine_stats = engine.get_engine_status()
    for key, value in engine_stats.items():
        print(f"{key}: {value}")
    print(f"Available types: {factory.get_supported_types()}")
