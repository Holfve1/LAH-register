# pytest cache directory #

This directory contains data from the pytest's cache plugin,
which provides the `--lf` and `--ff` options, as well as the `cache` fixture.

**Do not** commit this to version control.

See [the docs](https://docs.pytest.org/en/stable/how-to/cache.html) for more information.

setting up!!!!


Here’s a clean, proven setup path for a JS/React + Flask/Python + PostgreSQL project.

Directory Layout

Client/ — React app (Vite)
Server/ — Flask app (API, DB code)
Server/routes/ — Flask blueprints or route modules
Server/lib/ — DB connection, repositories, models
Server/seeds/ — SQL to create/seed tables
requirements.txt — Python deps
.gitignore — Python, Node, OS ignores
README.md — quick start and scripts
Prerequisites

Node 18+ (node -v)
Python 3.10+ (python3 --version)
PostgreSQL 14+ installed and running
Git installed
Optional: nvm for Node, pyenv for Python
Initialize Git

git init
Create .gitignore with venv, __pycache__, .pytest_cache, .DS_Store, node_modules, dist, .vite.
Backend Setup (Flask/Python)

Create venv: python3 -m venv venv && source venv/bin/activate
Add requirements.txt with:
Flask, psycopg, python-dotenv, Flask-CORS, pytest
Install: pip install -r requirements.txt
Server/app.py: create a Flask app, enable CORS, add a test route (/api/health)
Server/lib/database_connection.py: helper to connect to PG (using psycopg)
Server/.env (not committed):
APP_ENV=dev
DATABASE_URL=postgresql://localhost/your_db_name
Run backend: export FLASK_APP=Server/app.py && flask run --port 5000
Database Setup (PostgreSQL)

Create DBs: createdb your_db_name and createdb your_db_name_test
Optional: create a DB user and grant rights if not using default user
Server/seeds/*.sql: add schema and seed data
Seed: psql your_db_name < Server/seeds/your_schema.sql
Verify connectivity from Flask (simple SELECT in a route)
Frontend Setup (React + Vite)

cd Client && npm create vite@latest . -- --template react
If already initialized: ensure vite, @vitejs/plugin-react, react, react-dom in package.json
npm install
Client/.env:
VITE_BACKEND_URL=http://localhost:5000
Start dev server: npm run dev (defaults to http://localhost:5173)
Wire Frontend to Backend

In React, call API via fetch(\${import.meta.env.VITE_BACKEND_URL}/api/health`)`
Ensure CORS on Flask:
from flask_cors import CORS
CORS(app, resources={r\"/api/*\": {\"origins\": \"http://localhost:5173\"}})
Validate end-to-end by hitting a simple JSON route
Local Dev Workflow

Terminal 1: source venv/bin/activate && flask run --port 5000
Terminal 2: cd Client && npm run dev
Update seeds when schema changes; re-seed test DB for pytest
Testing (Optional but Recommended)

Backend: pytest under Server/tests/
Frontend: add vitest later if needed
E2E: optional Playwright after basic flow works
Build/Deploy Basics

Frontend build: cd Client && npm run build → outputs dist/
Backend: keep FLASK_ENV=production, configure DATABASE_URL in env
Serve frontend via static host or behind Flask/gateway; set VITE_BACKEND_URL accordingly
Common Pitfalls

Node version mismatch (Vite 5 needs Node 18+)
Missing CORS config (frontend requests blocked)
Wrong DATABASE_URL or DB not running
Forgetting to activate Python venv before flask run
Not seeding DB before hitting endpoints
If you want, I can generate minimal starter files for Server/app.py, Server/lib/database_connection.py, seeds, and a simple React fetch to confirm the stack end-to-end.


