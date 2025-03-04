from flask import Flask, request, jsonify
from app_utils import get_recommendation_from_id, get_recommendation_from_id_list, get_search_from_str

app = Flask(__name__)

@app.route('/recommend/from_id', methods=['POST'])
def recommend_from_id():
    """
    {
        "id": "my_id"
    }
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No JSON data received'}), 400
        
        # prep data
        id: str = data['id']
        return_data: dict = get_recommendation_from_id(id)

        return jsonify({'processed_data': return_data}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/recommend/from_id_list', methods=['POST'])
def recommend_from_id_list():
    """
    {
        "ids": [
            "id_1",
            "id_2",
            "id_3"
        ]
    }
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No JSON data received'}), 400
        
        # parse data
        ids: list = data['ids']
        return_data: dict = get_recommendation_from_id_list(ids)
        
        return jsonify({'processed_data': return_data}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/search/from_str', methods=['POST'])
def search_from_str():
    """
    api call: 
    {
        "search_input": "the songs I'm searching"
    }
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No JSON data received'}), 400
        
        search_str: str = data['search_input']
        return_data: dict = get_search_from_str(search_str) 
        
        return jsonify({'processed_data': return_data}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
