from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)
notes = {}
API_KEY = "dev-key-123"

def check_auth():
    return request.headers.get("X-API-Key") == API_KEY

@app.route("/notes", methods=["POST"])
def create_note():
    if not check_auth():
        return jsonify({"error": "unauthorized"}), 401
    data = request.get_json()
    note_id = str(uuid.uuid4())
    notes[note_id] = {"id": note_id, "content": data.get("content", ""), "tags": data.get("tags", [])}
    return jsonify(notes[note_id]), 201

@app.route("/notes", methods=["GET"])
def list_notes():
    if not check_auth():
        return jsonify({"error": "unauthorized"}), 401
    # tag filtering documented in README but never implemented here
    return jsonify(list(notes.values()))

@app.route("/notes/<note_id>", methods=["GET"])
def get_note(note_id):
    if not check_auth():
        return jsonify({"error": "unauthorized"}), 401
    note = notes.get(note_id)
    return (jsonify(note), 200) if note else (jsonify({"error": "not found"}), 404)

@app.route("/notes/<note_id>", methods=["PUT"])
def update_note(note_id):
    if not check_auth():
        return jsonify({"error": "unauthorized"}), 401
    note = notes.get(note_id)
    if not note:
        return jsonify({"error": "not found"}), 404
    data = request.get_json()
    note.update({"content": data.get("content", note["content"]), "tags": data.get("tags", note["tags"])})
    return jsonify(note)

@app.route("/notes/<note_id>", methods=["DELETE"])
def delete_note(note_id):
    if not check_auth():
        return jsonify({"error": "unauthorized"}), 401
    if note_id not in notes:
        return jsonify({"error": "not found"}), 404
    del notes[note_id]
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
