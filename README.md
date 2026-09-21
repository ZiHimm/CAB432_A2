# CAB432_A2

# Notes API

A minimal REST API for storing and organizing personal notes.

## Features

- Create, read, update, and delete notes via REST endpoints
- Tag notes and filter your list by tag (`GET /notes?tag=work`)
- Simple API-key authentication on all endpoints

## Endpoints

| Method | Path         | Description                              |
|--------|--------------|-------------------------------------------|
| POST   | /notes       | Create a new note                         |
| GET    | /notes       | List all notes (supports `?tag=` filter)  |
| GET    | /notes/{id}  | Get a single note                         |
| PUT    | /notes/{id}  | Update a note                             |
| DELETE | /notes/{id}  | Delete a note                             |

## Running locally

\`\`\`bash
pip install -r requirements.txt
python app.py
\`\`\`

## Authentication

Include your API key in the `X-API-Key` header on every request.
