def main() -> None:
    print("=== Game Analytics Dashboard ===\n")

    players = ["alice", "bob", "charlie", "diana"]
    scores = [2300, 1800, 2150, 2050]
    active = [True, True, True, False]
    regions = ["north", "east", "central", "north"]

    achievements = {
        "alice": {"first_kill", "level_10", "treasure_hunter", "speed_demon"},
        "bob": {"first_kill", "level_10", "boss_slayer", "collector"},
        "charlie": {"level_10", "treasure_hunter", "boss_slayer",
                    "speed_demon", "perfectionist"},
        "diana": {"first_kill"}
    }

    player_num = len(players)

    print("=== List Comprehension Examples ===")

    print(f"High scorers (>2000): {[players[i] for i in range(player_num)
                                    if scores[i] > 2000]}")
    print(f"Scores doubled: {[score * 2 for score in scores]}")
    print(f"Active players: {[players[i] for i in range(player_num)
                             if active[i] is True]}")

    print("\n=== Dict Comprehension Examples ===")
    players_dict = {players[i]: scores[i] for i in range(player_num - 1)}
    print(f"Player scores: {players_dict}")

    score_cat = {
        "high": len([score for score in scores if score >= 2100]),
        "medium": len([score for score in scores if 1900 <= score < 2100]),
        "low": len([score for score in scores if score < 1900])
    }
    print(f"Score categories: {score_cat}")

    achieve_count = {player: len(achievements[player])
                     for player in players[:player_num - 1]}
    print(f"Achievenment counts: {achieve_count}")

    print("\n=== Set Comprehension Examples ===")
    players_set = {player for player in players}
    print(f"Unique players: {players_set}")

    unique_achieve = {ach for player in players
                      for ach in achievements[player]}
    print(f"Unique achievements: {unique_achieve}")

    unique_regions = {region for region in regions}
    print(f"Active region: {unique_regions}")

    print("\n=== Combined Analytics ===")
    print(f"Total players: {player_num}")
    print(f"Total unique achievements: {len(unique_achieve)}")
    print(f"Average score: {sum(scores) / player_num:.1f}")

    top_score = max(scores)
    top_index = 0
    for i in range(player_num):
        if scores[i] == top_score:
            top_index = i
            break
    top_player = players[top_index]
    top_achieve = len(achievements[top_player])
    print(f"Top performer: {top_player} ({top_score} points, "
          f"{top_achieve} achievements)")


if __name__ == "__main__":
    main()
