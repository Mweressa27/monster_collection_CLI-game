from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    level = Column(Integer, default=1)
    experience = Column(Integer, default=0)
    money = Column(Integer, default=100)

    monsters = relationship('PlayerMonster', back_populates='player')
    achievements = relationship('PlayerAchievement', back_populates='player')

class MonsterSpecies(Base):
    __tablename__ = 'monster_species'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    type = Column(String)
    base_hp = Column(Integer)
    base_attack = Column(Integer)
    base_defense = Column(Integer)
    rarity = Column(String)
    abilities = Column(String)

class PlayerMonster(Base):
    __tablename__ = 'player_monsters'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    species_id = Column(Integer, ForeignKey('monster_species.id'))
    level = Column(Integer, default=1)
    current_hp = Column(Integer)
    experience = Column(Integer, default=0)

    player = relationship('Player', back_populates='monsters')
    species = relationship('MonsterSpecies')

class Battle(Base):
    __tablename__ = 'battles'
    id = Column(Integer, primary_key=True)
    player1_id = Column(Integer)
    player2_id = Column(Integer)
    result = Column(String)
    date = Column(DateTime, default=datetime.utcnow)

class Trade(Base):
    __tablename__ = 'trades'
    id = Column(Integer, primary_key=True)
    from_player = Column(Integer)
    to_player = Column(Integer)
    offered_monsters = Column(String)  # e.g., "1,2"
    requested_monsters = Column(String)
    status = Column(String, default="pending")

class Achievement(Base):
    __tablename__ = 'achievements'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

class PlayerAchievement(Base):
    __tablename__ = 'player_achievements'
    player_id = Column(Integer, ForeignKey('players.id'), primary_key=True)
    achievement_id = Column(Integer, ForeignKey('achievements.id'), primary_key=True)
    unlocked_at = Column(DateTime, default=datetime.utcnow)

    player = relationship('Player', back_populates='achievements')
