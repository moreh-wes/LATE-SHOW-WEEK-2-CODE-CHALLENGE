# Episodes & Guests API

Flask API for managing TV show episodes, guests, and their appearances.

## Setup

1. Install dependencies:
```bash
venv/bin/pip install -r requirements.txt
```

2. Run migrations:
```bash
venv/bin/flask db upgrade
```

3. Seed database:
```bash
venv/bin/python seed.py
```

4. Run application:
```bash
venv/bin/python app.py
```

## Usage

**Frontend:** http://localhost:5000

**Backend API:**
- GET /episodes
- GET /episodes/:id
- GET /guests
- POST /appearances
- DELETE /episodes/:id

## Models

- **Episode**: id, date, number
- **Guest**: id, name, occupation
- **Appearance**: id, rating (1-5), episode_id, guest_id

## Features

- Many-to-many relationship through Appearance
- Cascade deletes
- Rating validation (1-5)
- Frontend interface for all operations
