from ex4 import TournamentCard, TournamentPlatform


def get_superclasses(card: TournamentCard) -> list:
    res = []
    classes = card.__class__.__bases__
    for element in classes:
        res.append(element.__name__.split(".")[-1])
    return res


if __name__ == "__main__":
    print("=== DataDeck Tournament Platform ===\n")
    tournament = TournamentPlatform()

    print("Registering Tournament Cards...\n")

    try:
        fd = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5, 5, 1200)
        iw = TournamentCard("Ice Wizard", 4, "Legendary", 6, 4, 6, 1150)
        fd_id = tournament.register_card(fd)
        iw_id = tournament.register_card(iw)

        for id, card in tournament.cards.items():
            info = card.get_rank_info()
            print(f"{card.name} (ID: {id}):")
            print(f"- Interfaces: {get_superclasses(card)}")
            print(f"- Rating: {card.rating}")
            print(f"- Record: {info["record"]}")
            print("")

        print("Creating tournament match...")
        print(f"Match result: {tournament.create_match(fd_id, iw_id)}")

        print("\nTournament Leaderboard:")
        leaderboard = tournament.get_leaderboard()
        for i in range(len(leaderboard)):
            card = leaderboard[i]
            info = card.get_rank_info()
            print(f"{i + 1}. {card.name} - Rating: {card.rating} "
                  f"({info["record"]})")

        print("\nPlatform Report:")
        print(f"{tournament.generate_tournament_report()}")

        print("\n=== Tournament Platform Successfully Deployed! ===")
        print("All abstract patterns working together harmoniously!")

    except (ValueError, KeyError) as e:
        print(e)
