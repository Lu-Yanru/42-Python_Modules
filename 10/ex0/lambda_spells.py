def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    print("Testing artifaact sorter...")
    res = sorted(artifacts,
                 key=lambda x: x["power"],
                 reverse=True)
    print(res)
    return res


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    print("Testing power filer...")
    res = list(filter(lambda x: x["power"] >= min_power, mages))
    print(res)
    return res


def spell_transformer(spells: list[str]) -> list[str]:
    print("Testing spell transformer...")
    res = list(map(lambda x: "* " + x + " *", spells))
    print(res)
    return res


def mage_stats(mages: list[dict]) -> dict:
    print("Testing mage stats...")
    total_power = sum(list(map(lambda x: x["power"], mages)))
    res = {
        "max_power": max(mages, key=lambda x: x["power"])["power"],
        "min_power": min(mages, key=lambda x: x["power"])["power"],
        "avg_power": round(total_power / len(mages), 2)
    }
    print(res)
    return res


if __name__ == "__main__":
    artifacts = [{'name': 'Lightning Rod', 'power': 110, 'type': 'armor'},
                 {'name': 'Fire Staff', 'power': 85, 'type': 'armor'},
                 {'name': 'Shadow Blade', 'power': 99, 'type': 'relic'},
                 {'name': 'Crystal Orb', 'power': 76, 'type': 'weapon'}]
    artifact_sorter(artifacts)
    print("")

    mages = [{'name': 'Ash', 'power': 82, 'element': 'lightning'},
             {'name': 'River', 'power': 55, 'element': 'light'},
             {'name': 'Storm', 'power': 98, 'element': 'fire'},
             {'name': 'Casey', 'power': 92, 'element': 'fire'},
             {'name': 'Kai', 'power': 56, 'element': 'water'}]
    power_filter(mages, 80)
    print("")

    spells = ['heal', 'fireball', 'tornado', 'freeze']
    spell_transformer(spells)
    print("")

    mage_stats(mages)
