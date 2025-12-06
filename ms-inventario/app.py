from flask import Flask, request, jsonify
import random, time

app = Flask(__name__)


@app.route('/actualizar_inventario', methods=['POST'])
def actualizar_inventario():
    data = request.get_json()
    time.sleep(random.uniform(0.2, 1.0))  # simula latencia
    
    if random.choice([True, False]):
        inventario = {
            "inventario_id": random.randint(1000, 9999),
            "estado": "inventario actualizado",
            "producto": data
        }
        return jsonify(inventario), 200
    else:
        return jsonify({"error": "conflicto en el inventario"}), 409

if __name__ == '__main__':
    app.run(port=5004)
