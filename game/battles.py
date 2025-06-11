def calculate_damage(attacker, defender, move_power, type_effectiveness):
    return int(((attacker['attack'] - defender['defense']) + move_power) * type_effectiveness)

def type_effectiveness(attacker_type, defender_type):
    chart = {
        "Fire": {"Grass": 2, "Water": 0.5},
        "Water": {"Fire": 2, "Grass": 0.5},
        "Grass": {"Water": 2, "Fire": 0.5},
        "Electric": {"Water": 2, "Ground": 0},
    }
    return chart.get(attacker_type, {}).get(defender_type, 1)
