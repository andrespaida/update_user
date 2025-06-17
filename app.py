from flask import Flask
from flask_cors import CORS
from routes import routes  # Asumiendo que usas un blueprint

app = Flask(__name__)

# ✅ Habilita CORS correctamente para todos los orígenes y rutas
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})

# ✅ Registra el blueprint de rutas
app.register_blueprint(routes)

if __name__ == '__main__':
    # ✅ Corre en el puerto correcto y accesible desde fuera del contenedor
    app.run(host='0.0.0.0', port=3003, debug=False)
