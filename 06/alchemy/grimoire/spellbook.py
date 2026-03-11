def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    res = validate_ingredients(ingredients)
    if res.endswith("INVALID"):
        return f"Spell recorded: {spell_name} ({res})"
    return f"Spell rejected: {spell_name} ({res})"
