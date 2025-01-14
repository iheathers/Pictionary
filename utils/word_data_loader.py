from app import db
from app.models import Word


def load_data():
    words_dict = {
        "Difficult": [
            "Olympics",
            "Sandcastle",
            "Recycle",
            "Black hole",
            "Applause",
            "Blizzard",
            "Sunburn",
            "Time machine",
            "Lace",
            "Monday",
            "Atlantis",
            "Swamp",
            "Panama Canal",
            "Sunscreen",
            "Dictionary",
            "Vanilla",
            "Century",
        ],
        "Action": [
            "Skip",
            "Burp",
            "Cook",
            "Scratch",
            "Sleep",
            "Plant",
            "Purchase",
            "Text",
            "Tie",
            "Snore",
            "Catch",
            "Study",
            "Dance",
            "Paint",
            "Skateboard",
            "Laugh",
            "Fly",
            "Surf",
            "Sculpt",
            "Hike",
            "Juggle",
            "Nap",
            "Cheer",
            "Dive",
            "Stretch",
            "Cook",
            "Climb",
            "Sing",
            "Drive",
            "Ride",
            "Swim",
            "Write",
        ],
        "Person/Place/Animal": [
            "Paris",
            "Beach",
            "Mountains",
            "Hawaii",
            "Mount Rushmore",
            "USA",
            "Hospital",
            "Attic",
            "Japan",
            "Library",
            "Desert",
            "Mars",
            "Washington DC",
            "Las Vegas",
            "Train station",
            "North Pole",
            "Farm",
            "Disney World",
            "Mexico",
            "Giraffe",
            "Koala",
            "Wasp",
            "Scorpion",
            "Lion",
            "Salamander",
            "Dolphin",
            "Frog",
            "Panda",
            "Platypus",
            "T-rex",
            "Meerkat",
            "Eagle",
            "Mailman",
            "Superman",
            "Justin Bieber",
            "Cowboy",
            "Alexander Hamilton",
            "Robin Hood",
            "Vampire",
            "Pirate",
            "Girl Scout",
            "Pikachu",
            "Spongebob",
            "Baby Yoda",
            "Pilgrim",
            "Cinderella",
            "Baker",
            "Abe Lincoln",
            "Thief",
            "Leprechaun",
            "Harry Potter",
            "Shrek",
            "Yoshi",
            "Queen Elizabeth",
        ],
        "Object": [
            "Strawberry",
            "Eclipse",
            "Chandelier",
            "Ketchup",
            "Toothpaste",
            "Rainbow",
            "Bunk bed",
            "Boardgame",
            "Beehive",
            "Lemon",
            "Wreath",
            "Waffles",
            "Bubble",
            "Whistle",
            "Snowball",
            "Bouquet",
            "Headphones",
            "Fireworks",
            "Igloo",
            "Ferris wheel",
            "Banana peel",
            "Lawnmower",
            "Summer",
            "Whisk",
            "Cupcake",
            "Sleeping bag",
            "Bruise",
            "Fog",
            "Crust",
            "Battery",
        ],
    }
    try:
        for category, words in words_dict.items():
            for word in words:
                # Check if word already exists to avoid duplicates
                if not Word.query.filter_by(text=word, category=category).first():
                    new_word = Word(category=category, text=word)
                    db.session.add(new_word)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Failed to load data: {e}")
