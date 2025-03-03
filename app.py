from flask import Flask, request, jsonify
import app_utils

app = Flask(__name__)

@app.route('/recommend/from_id', methods=['POST'])
def recommend_from_id():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No JSON data received'}), 400
        
        return_data = {"hello im docker": ""}  # Placeholder for recommendation logic

        return jsonify({'processed_data': return_data}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/recommend/from_id_list', methods=['POST'])
def recommend_from_id_list():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No JSON data received'}), 400
        
        return_data = {}  # Placeholder for recommendation logic
        
        return jsonify({'processed_data': return_data}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/search/from_str', methods=['POST'])
def search_from_str():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No JSON data received'}), 400
        
        return_data = {}  # Placeholder for search logic
        
        return jsonify({'processed_data': return_data}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
