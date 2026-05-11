from flask import Flask, render_template, jsonify
import requests
import time
import sqlite3

app = Flask(__name__)

# --- CONFIGURATION ---
API_URL = "https://api.agify.io"
MY_NAME = "mehdi"

def run_api_test():
    """Fonction qui appelle l'API et mesure la performance"""
    try:
        start = time.time()
        response = requests.get(API_URL, params={"name": MY_NAME})
        latency = time.time() - start
        return response.status_code, round(latency, 3)
    except Exception:
        return 500, 0

@app.route("/")
def home():
    # Affiche la page des consignes ou ton futur dashboard
    return render_template('consignes.html')

@app.route("/run-test")
def run_test():
    """Route pour déclencher le test manuellement depuis le navigateur"""
    status, latency = run_api_test()
    return jsonify({
        "service": "Agify",
        "status": status,
        "latency": f"{latency}s",
        "message": "Test réussi !" if status == 200 else "Erreur"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
