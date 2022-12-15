import pandas as pd
from flask import Flask
from flask import request, jsonify
import json
import numpy as np

app = Flask(__name__)

df = pd.read_excel(r"api_data_processed.xlsx")
print(df)
n = df.shape[0]
m = df.shape[1]
col = df.columns
data = []
for i in range(n):
    temp = {}
    for j in range(m):
        temp[col[j]] = df.iloc[i][j]
    
    data.append(temp)
# data[9]['No'] = 10000
# data = data
print(data)

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

@app.route('/', methods=['GET'])
def home():
    return 'GIS DATA API'

@app.route('/api', methods=['GET'])
def api_all():
    return json.dumps(data,cls=NpEncoder)

# @app.route('/api/v1/resources/books', methods=['GET'])
# def api_id():
#     # Check if an ID was provided as part of the URL.
#     # If ID is provided, assign it to a variable.
#     # If no ID is provided, display an error in the browser.
#     if 'id' in request.args:
#         id = int(request.args['id'])
#     else:
#         return "Error: No id field provided. Please specify an id."

#     # Create an empty list for our results
#     results = []

#     # Loop through the data and match results that fit the requested ID.
#     # IDs are unique, but other fields might return many results
#     for book in books:
#         if book['id'] == id:
#             results.append(book)

#     # Use the jsonify function from Flask to convert our list of
#     # Python dictionaries to the JSON format.
#     return jsonify(results)

if __name__ == '__main__':
    app.run(port=3000)