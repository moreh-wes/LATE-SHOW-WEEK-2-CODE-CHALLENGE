from app import app, db
from models import Episode, Guest, Appearance

with app.app_context():
    Appearance.query.delete()
    Episode.query.delete()
    Guest.query.delete()
    
    episodes = [
        Episode(date="1/11/99", number=1),
        Episode(date="1/12/99", number=2),
        Episode(date="1/13/99", number=3),
        Episode(date="1/14/99", number=4),
        Episode(date="1/15/99", number=5)
    ]
    db.session.add_all(episodes)
    
    guests = [
        Guest(name="Michael J. Fox", occupation="actor"),
        Guest(name="Sandra Bernhard", occupation="Comedian"),
        Guest(name="Tracey Ullman", occupation="television actress"),
        Guest(name="Gillian Anderson", occupation="actor"),
        Guest(name="David Duchovny", occupation="actor")
    ]
    db.session.add_all(guests)
    db.session.commit()
    
    appearances = [
        Appearance(rating=4, episode_id=1, guest_id=1),
        Appearance(rating=5, episode_id=1, guest_id=2),
        Appearance(rating=3, episode_id=2, guest_id=3),
        Appearance(rating=5, episode_id=3, guest_id=4),
        Appearance(rating=4, episode_id=3, guest_id=5)
    ]
    db.session.add_all(appearances)
    db.session.commit()
