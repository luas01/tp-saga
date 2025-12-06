from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/saga', methods=['POST'])
def saga():
    try:
        # 1. Obtener producto
        producto = requests.get("http://localhost:5001/obtener_producto").json()

        # 2. Procesar pago
        pago_resp = requests.post("http://localhost:5002/procesar_pago", json=producto)
        if pago_resp.status_code != 200:
            return jsonify({"error": "Fallo en el pago"}), 409
        pago = pago_resp.json()

        # 3. Procesar compra
        compra_resp = requests.post("http://localhost:5003/procesar_compra", json=producto)
        if compra_resp.status_code != 200:
            # compensar pago
            requests.post("http://localhost:5002/cancelar_pago", json=producto)
            return jsonify({"error": "Fallo en la compra, pago compensado"}), 409
        compra = compra_resp.json()

        # 4. Actualizar inventario
        inv_resp = requests.post("http://localhost:5004/actualizar_inventario", json=producto)
        if inv_resp.status_code != 200:
            # compensar compra y pago
            requests.post("http://localhost:5003/cancelar_compra", json=producto)
            requests.post("http://localhost:5002/cancelar_pago", json=producto)
            return jsonify({"error": "Fallo en inventario, compra y pago compensados"}), 409
        inventario = inv_resp.json()

        # Si todo salió bien
        return jsonify({
            "producto": producto,
            "pago": pago,
            "compra": compra,
            "inventario": inventario,
            "estado": "Saga completada exitosamente"
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
