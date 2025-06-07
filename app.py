from flask import Flask
from flask_cors import CORS
from routes import routes  # Asumiendo que usas un blueprint

app = Flask(__name__)

# ✅ Habilita CORS para todas las rutas
CORS(app)

# Si prefieres limitarlo a solo tu frontend:
# CORS(app, origins=["http://localhost:5173"])

app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
