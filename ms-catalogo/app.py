from flask import Flask, jsonify
import random, time
app = Flask(__name__)

@app.route('/get_producto', methods=['GET'])
def get_producto():
    time.sleep(random.uniform(0.2, 1.0)) #simula latencia
    producto = {
        "id": random.randint(1000, 9999),
        "nombre": random.choice(["Notebook"]),
        "precio": random.randint(100, 1500),
        "cantidad": random.choice([1, 2])
    }
    return jsonify(producto), 200
if __name__ == '__main__':
    app.run(port=5001)