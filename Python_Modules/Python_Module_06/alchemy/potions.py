from .elements import create_water, create_air, create_earth, create_fire


def healing_potion() -> str:
    return (f"Healing potion brewed with "
            f"{create_fire()} and {create_water()}")


def strength_potion() -> str:
    return (f"Strength potion brewed with "
            f"{create_earth()} and {create_fire()}")


def invisibility_potion() -> str:
    return ("Invisibility potion brewed with "
            f"{create_air()} and {create_water()}")


def wisdom_potion() -> str:
    return ("Wisdom potion brewed with all elements: "
            f"{create_water()} and {create_fire()} and "
            f"{create_earth()} and {create_air()}")
