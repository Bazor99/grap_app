from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()
from pprint import pprint

from graph.graph import app
import os


flask_app = Flask(__name__)

@flask_app.route('/input', methods=['POST'])
def handle_input():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        
        # Extract the string from the JSON, assuming the key is 'input_string'
        input_string = data.get('input_string')

        if not input_string:
            return jsonify({'message': 'No input_string provided'}), 400
        else:
            question1 = input_string
            inputs = {"question": question1}

            for output in app.stream(inputs, config={"configurable": {"thread_id": "2"}}):
                for key, value in output.items():
                    pprint(f"Finished running: {key}:")
            pprint(value["generation"])
        return {"result": value["generation"]}
        # Return success response
        #return jsonify({'message': 'Success'}), 200
    
    except Exception as e:
        # Handle error
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    flask_app.run(debug=True)
