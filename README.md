# CrimeApi
import pandas as pd
from flask import Flask
from flask import request, jsonify
import json
import numpy as np

app = Flask(__name__)

df = pd.read_excel(r"exp.xlsx")
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
    
if __name__ == '__main__':
    app.run()
