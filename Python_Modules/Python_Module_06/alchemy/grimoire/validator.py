def validate_ingredients(ingredients: str) -> str:
    valid = ["fire", "water", "air", "earth"]
    for data in valid:
        if data in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
