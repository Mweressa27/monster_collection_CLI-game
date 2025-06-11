import random
from db.models import PlayerMonster, MonsterSpecies
from db.base import SessionLocal

def calculate_catch_rate(rarity, player_level):
    base = {"Common": 0.8, "Uncommon": 0.5, "Rare": 0.2, "Legendary": 0.05}
    return min(1.0, base[rarity] + (player_level * 0.01))

def catch_monster(player_id, species_id):
    session = SessionLocal()
    species = session.query(MonsterSpecies).get(species_id)
    rate = calculate_catch_rate(species.rarity, 1)  # Replace with actual player level
    if random.random() < rate:
        new_monster = PlayerMonster(
            player_id=player_id,
            species_id=species_id,
            level=1,
            current_hp=species.base_hp,
            experience=0
        )
        session.add(new_monster)
        session.commit()
        return True
    return False
