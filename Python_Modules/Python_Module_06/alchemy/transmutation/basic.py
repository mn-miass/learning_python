from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    return ("Lead transmuted to "
            f"gold using {create_fire()}")


def stone_to_gem() -> str:
    return (f"Stone transmuted to "
            f"gem using {create_earth()}")
