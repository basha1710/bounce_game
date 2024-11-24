from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample game state (for demonstration)
game_state = {
    "score": 0,
    "ball_position": {"x": 50, "y": 50},
    "ball_velocity": {"x": 2, "y": 3},
}

@app.route("/")
def index():
    """Serve the main game page."""
    return render_template("index.html")

@app.route("/game_state")
def get_game_state():
    """API to fetch the current game state."""
    return jsonify(game_state)

@app.route("/update_game", methods=["POST"])
def update_game():
    """Update game state (stub example)."""
    global game_state
    game_state["score"] += 1
    return jsonify(success=True, game_state=game_state)

if __name__ == "__main__":
    app.run(debug=True)
