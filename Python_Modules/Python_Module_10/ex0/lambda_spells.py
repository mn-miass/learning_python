def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {"max_power": max(mages, key=lambda x: x["power"])["power"],
            "min_power": min(mages, key=lambda x: x["power"])["power"],
            "avg_power": round(sum(list(map(lambda x: x["power"], mages))) /
                               len(mages), 2)}


if __name__ == "__main__":
    artifacts = [{'name': 'Light Prism', 'power': 119, 'type': 'weapon'},
                 {'name': 'Lightning Rod', 'power': 67, 'type': 'focus'},
                 {'name': 'Storm Crown', 'power': 60, 'type': 'accessory'},
                 {'name': 'Light Prism', 'power': 69, 'type': 'accessory'}]
    mages = [{'name': 'Riley', 'power': 95, 'element': 'shadow'},
             {'name': 'Nova', 'power': 63, 'element': 'lightning'},
             {'name': 'Zara', 'power': 56, 'element': 'earth'},
             {'name': 'Storm', 'power': 92, 'element': 'water'},
             {'name': 'Zara', 'power': 77, 'element': 'wind'}]
    spells = ['fireball', 'freeze', 'flash', 'meteor']

    print("Testin  artifact sorter...")
    sort = artifact_sorter(artifacts)

    if len(sort) > 1:
        for i in range(len(sort) - 1):
            print(f"{sort[i]['name']} ({sort[i]['power']} power) comes before "
                  f"{sort[i + 1]['name']} ({sort[i + 1]['power']} power)")

    elif len(sort) == 1:
        print(f"{sort[1]['name']} ({sort[1]['power']} power)")

    print("\nTesting power filter ...")

    p_f = power_filter(mages, 80)

    if p_f:
        for element in p_f:
            print(f"{element['name']} has power more then 80")

    print("\nTesting spell transformer...")
    spell = spell_transformer(spells)
    for element in spell:
        print(element, "", end="")
    print()
    print("\nTesting mage states")
    stats = mage_stats(mages)

    print(f"biggest power level: {stats["max_power"]}")
    print(f"smalelst power level: {stats["min_power"]}")
    print(f"average total power: {stats["avg_power"]}")
