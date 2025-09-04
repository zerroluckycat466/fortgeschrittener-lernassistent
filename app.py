from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/lernpfad', methods=['POST'])
def create_learning_path():
    user_data = request.json
    # Logic for creating a personalized learning path would go here
    return jsonify({'message': 'The learning path has been successfully created!'}), 201

if __name__ == '__main__':
    app.run(debug=True)