# Insta Follower backend

Python + Flask API for saving usernames.

## Local setup

```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

The API runs on `http://localhost:5000`.

### Save a username

`POST /api/usernames`

JSON body:

```json
{"username":"example_user"}
```

### Check saved usernames

`GET /api/usernames`

### Database

For local development the backend uses SQLite (`insta_follower.db`). For production, set `DATABASE_URL` to a PostgreSQL connection string. Do not put database credentials in frontend JavaScript or commit `.env` files.
