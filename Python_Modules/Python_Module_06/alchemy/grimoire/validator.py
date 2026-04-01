def validate_ingredients(ingredients: str) -> str:
    valid = ["fire", "water", "air", "earth"]
    if ingredients.lower in valid:
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
