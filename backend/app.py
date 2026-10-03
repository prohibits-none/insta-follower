import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Use DATABASE_URL in production (PostgreSQL recommended).
# Locally, this falls back to a SQLite database file.
database_url = os.getenv("DATABASE_URL", "sqlite:///insta_follower.db")
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Username(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True, index=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }


with app.app_context():
    db.create_all()


@app.get("/api/health")
def health():
    return jsonify({"ok": True, "message": "Insta Follower backend is running"})


@app.post("/api/usernames")
def save_username():
    data = request.get_json(silent=True) or {}
    username = str(data.get("username", "")).strip()

    if not username:
        return jsonify({"ok": False, "error": "Username is required"}), 400

    if len(username) > 100:
        return jsonify({"ok": False, "error": "Username is too long"}), 400

    # Store the username without changing its case.
    existing = Username.query.filter_by(username=username).first()
    if existing:
        return jsonify({"ok": True, "message": "Username already saved", "user": existing.to_dict()}), 200

    user = Username(username=username)
    db.session.add(user)
    db.session.commit()

    return jsonify({"ok": True, "message": "Username saved", "user": user.to_dict()}), 201


@app.get("/api/usernames")
def get_usernames():
    users = Username.query.order_by(Username.id.desc()).all()
    return jsonify({"ok": True, "users": [user.to_dict() for user in users]})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)
