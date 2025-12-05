from flask import Flask, request, jsonify
import random, time

app = Flask(__name__)

@app.route('/procesar_compra', methods=['POST'])
def procesar_compra():
    data = request.get_json()
    time.sleep(random.uniform(0.2, 1.0))  # simula latencia
    
    if random.choice([True, False]):
        compra = {
            "compra_id": random.randint(1000, 9999),
            "estado": "compra realizada",
            "producto": data
        }
        return jsonify(compra), 200
    else:
        return jsonify({"error": "conflicto en la compra"}), 409

@app.route('/cancelar_compra', methods=['POST'])
def cancelar_compra():
    data = request.get_json()
    time.sleep(random.uniform(0.2, 0.5))  # latencia más corta
    return jsonify({"estado": "compra cancelada", "producto": data}), 200

if __name__ == '__main__':
    app.run(port=5003)