from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/saga', methods=['POST'])
def saga_gateway():
    try:
        # Redirige la petición al orquestador
        resp = requests.post("http://localhost:5000/saga")
        return jsonify(resp.json()), resp.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=8000)
