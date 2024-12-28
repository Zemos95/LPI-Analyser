from flask import Flask, request, jsonify

app = Flask(__name__)

# Beispielhafte Anmeldedaten
USER_CREDENTIALS = {
    "admin": "password",
    "user1": "securepassword"
}


@app.route('/login', methods=['POST'])
def login():
    """
    Verarbeitet Login-Anfragen vom Client.
    Erwartet JSON-Daten mit 'username' und 'password'.
    """
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        return jsonify({"success": True, "message": "Login erfolgreich."}), 200
    else:
        return jsonify({"success": False, "message": "Ungültige Anmeldedaten."}), 401


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
