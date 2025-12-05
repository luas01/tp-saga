from flask import Flask, request, jsonify
import random, time
app = Flask(__name__)

@app.route('/procesar_pago', methods=['POST'])
def procesar_pago():
    data=request.get_json() #recibe datos del producto
    time.sleep(random.uniform(0.2, 1.0)) #simula latencia

    if random.choice([True, False]):
        pago = {
            "pago_id":random.randint(1000, 9999),
            "estado":"exitoso",
            "producto":data
        }
        return jsonify(pago), 200
    else:
        return jsonify({"error":"conflicto en el pago"}), 409
    
@app.route('/cancelar_pago', methods=['POST'])
def cancelar_pago():
    data = request.get_json()
    time.sleep(random.uniform(0.2, 0.5)) #latencia mas corta
    return jsonify({"estado": "pago cancelado", "producto":data}), 200
if __name__ == '__main__':
    app.run(port=5002)
    