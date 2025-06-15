import click
from db.models import Player
from db.base import SessionLocal
from game.catching import catch_monster
from db.seed import seed_monsters

@click.group()
def cli():
    pass

@cli.command()
def seed():
    seed_monsters()

@cli.command()
@click.argument('username')
def create(username):
    session = SessionLocal()
    new_player = Player(username=username)
    session.add(new_player)
    session.commit()
    print(f"✅ Player '{username}' created.")

@cli.command()
@click.argument('player_id', type=int)
@click.argument('species_id', type=int)
def catch(player_id, species_id):
    success = catch_monster(player_id, species_id)
    if success:
        print("🎉 You caught the monster!")
    else:
        print("😢 The monster escaped...")

@cli.command()
def setup():
    from db.base import Base, engine
    Base.metadata.create_all(engine)
    print("✅ All tables created.")


if __name__ == '__main__':
    cli()
