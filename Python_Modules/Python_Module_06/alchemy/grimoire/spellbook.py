def record_spell(spell_name: str, ingredients: str) -> str:
    valid = ["fire", "water", "air", "earth"]
    if ingredients.lower in valid:
        return f"Spell recorded: {spell_name} ([validation_result])"
    return f"Spell rejected: {spell_name} ([validation_result])"
