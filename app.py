from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/lernpfad', methods=['POST'])
def create_learning_path():
    user_data = request.json
    # Hier würde die Logik zur Erstellung eines personalisierten Lernpfades stehen
    return jsonify({'message': 'Lernpfad erfolgreich erstellt!'}), 201

if __name__ == '__main__':
    app.run(debug=True)
