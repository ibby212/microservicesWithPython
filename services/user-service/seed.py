import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from app.database import SessionLocal, engine
from app.models import Base, User

USERS = [
    {"username": "nova",        "email": "nova@gamehub.io",    "bio": "Explorer of virtual worlds."},
    {"username": "alex_g",      "email": "alex@gamehub.io",    "bio": "Speedrunner. Coffee addict."},
    {"username": "maya_r",      "email": "maya@gamehub.io",    "bio": "RPG lover, lore hunter."},
    {"username": "thunderbyte", "email": "thunder@gamehub.io", "bio": "FPS main, occasional cozy gamer."},
    {"username": "pixel_queen", "email": "pixel@gamehub.io",   "bio": "Completionist. 100% or nothing."},
]

def run():
    db = SessionLocal()
    for data in USERS:
        if not db.query(User).filter(User.username == data["username"]).first():
            db.add(User(username=data["username"], email=data["email"],
                        hashed_password="hashed_password", bio=data["bio"]))
    db.commit()
    db.close()
    print("Seeded.")

if __name__ == "__main__":
    run()