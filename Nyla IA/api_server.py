from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Configuración de la API
API_KEY = "your_api_key_here"

@app.route("/search_talent", methods=["GET"])
def search_talent():
    """
    Endpoint para buscar talentos en una plataforma externa.
    """
    query = request.args.get("query")
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400
    
    platform_url = "https://api.example.com/talent"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    params = {"q": query}
    
    try:
        response = requests.get(platform_url, headers=headers, params=params)
        response.raise_for_status()  # Lanza una excepción si la respuesta no es 200
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)