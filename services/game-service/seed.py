import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database import SessionLocal, engine
from app.models import Base, Game

GAMES = [
    {"title": "Hollow Knight",            "genre": "Metroidvania", "platform": "PC",     "release_year": 2017, "cover_url": "https://cdn.akamai.steamstatic.com/steam/apps/367520/header.jpg"},
    {"title": "Celeste",                  "genre": "Platformer",   "platform": "PC",     "release_year": 2018, "cover_url": "https://cdn.akamai.steamstatic.com/steam/apps/504230/header.jpg"},
    {"title": "Hades",                    "genre": "Roguelite",    "platform": "PC",     "release_year": 2020, "cover_url": "https://cdn.akamai.steamstatic.com/steam/apps/1145360/header.jpg"},
    {"title": "Stardew Valley",           "genre": "Simulation",   "platform": "PC",     "release_year": 2016, "cover_url": "https://cdn.akamai.steamstatic.com/steam/apps/413150/header.jpg"},
    {"title": "Dead Cells",               "genre": "Roguelite",    "platform": "PC",     "release_year": 2018, "cover_url": "https://cdn.akamai.steamstatic.com/steam/apps/588650/header.jpg"},
    {"title": "Ori and the Blind Forest", "genre": "Platformer",   "platform": "PC",     "release_year": 2015, "cover_url": "https://cdn.akamai.steamstatic.com/steam/apps/261570/header.jpg"},
    {"title": "Disco Elysium",            "genre": "RPG",          "platform": "PC",     "release_year": 2019, "cover_url": "https://cdn.akamai.steamstatic.com/steam/apps/632470/header.jpg"},
    {"title": "Outer Wilds",              "genre": "Adventure",    "platform": "PC",     "release_year": 2019, "cover_url": "https://cdn.akamai.steamstatic.com/steam/apps/753640/header.jpg"},
]

def run():
    db = SessionLocal()
    imported = 0
    for data in GAMES:
        if not db.query(Game).filter(Game.title == data["title"]).first():
            db.add(Game(**data))
            imported += 1
    db.commit()
    db.close()
    print(f"Imported {imported} games.")

if __name__ == "__main__":
    run()
