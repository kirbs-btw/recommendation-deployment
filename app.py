from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/recommend/from_id', methods=['POST'])
def recommend_from_id():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No JSON data received'}), 400
        
        # takes a song id
        # returns a list of song_names, artis_name and id of the recommended songs 
        return_data = {}

        return jsonify({'processed_data': return_data}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/recommend/from_id_list', methods=['POST'])
def recommend_from_id_list():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No JSON data received'}), 400
        
        # takes a list of ids aka playlist from the user 
        # returns a list of song_names, artis_name and id of the recommended songs
        return_data = {}
        
        return jsonify({'processed_data': return_data}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/search/from_str', methods=['POST'])
def recommend_from_id_list():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No JSON data received'}), 400
        
        # takes the inputed data from the user 
        # and show the most fitting songs to the search to add a song 
        # the autocomplete takes way to long with a bigger dataframe
        # need to implement a new section to show the search results 
        # after pressing search for the user
        return_data = {}
        
        return jsonify({'processed_data': return_data}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
