from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/learning-paths', methods=['POST'])
def create_learning_path():
    user_data = request.json
    if not user_data or 'name' not in user_data:
        return jsonify({'error': 'Invalid input: name is required.'}), 400
    # Logic for creating a personalized learning path based on the user_data would go here
    return jsonify({'message': 'The learning path has been successfully created!'}), 201

if __name__ == '__main__':
    app.run(debug=True)