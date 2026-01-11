from flask import Flask, request, jsonify, render_template
from flask_migrate import Migrate
from models import db, Episode, Guest, Appearance

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/episodes')
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([e.to_dict(only=('id', 'date', 'number')) for e in episodes])

@app.route('/episodes/<int:id>')
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404
    return jsonify(episode.to_dict(only=('id', 'date', 'number', 'appearances.id', 'appearances.rating', 'appearances.episode_id', 'appearances.guest_id', 'appearances.guest.id', 'appearances.guest.name', 'appearances.guest.occupation')))

@app.route('/guests')
def get_guests():
    guests = Guest.query.all()
    return jsonify([g.to_dict(only=('id', 'name', 'occupation')) for g in guests])

@app.route('/episodes/<int:id>', methods=['DELETE'])
def delete_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404
    db.session.delete(episode)
    db.session.commit()
    return jsonify({}), 204

@app.route('/appearances', methods=['POST'])
def create_appearance():
    try:
        data = request.get_json()
        appearance = Appearance(
            rating=data.get('rating'),
            episode_id=data.get('episode_id'),
            guest_id=data.get('guest_id')
        )
        db.session.add(appearance)
        db.session.commit()
        return jsonify(appearance.to_dict(only=('id', 'rating', 'guest_id', 'episode_id', 'episode.id', 'episode.date', 'episode.number', 'guest.id', 'guest.name', 'guest.occupation'))), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400

if __name__ == '__main__':
    app.run(port=5000, debug=True)
