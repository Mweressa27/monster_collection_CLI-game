from .models import MonsterSpecies
from .base import SessionLocal

def seed_monsters():
    session = SessionLocal()
    species_list = [
        {"name": "Flamewyrm", "type": "Fire", "base_hp": 40, "base_attack": 15, "base_defense": 10, "rarity": "Common", "abilities": "Fire Blast"},
        {"name": "Aquafin", "type": "Water", "base_hp": 42, "base_attack": 13, "base_defense": 12, "rarity": "Common", "abilities": "Splash"},
        {"name": "Vinewhip", "type": "Grass", "base_hp": 45, "base_attack": 14, "base_defense": 14, "rarity": "Common", "abilities": "Whip Lash"},
        {"name": "Sparkbolt", "type": "Electric", "base_hp": 35, "base_attack": 18, "base_defense": 8, "rarity": "Rare", "abilities": "Thunder Bolt"}      
    ]
    for data in species_list:
        monster = MonsterSpecies(**data)
        session.add(monster)
    session.commit()
    print("Monster species seeded.")
