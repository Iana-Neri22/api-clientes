from flask import Flask
from models.blueprints.cliente_blueprints import clientes_bp
from config import Config


app = Flask(__name__)

app.register_blueprint(clientes_bp, url_prefix="/cliente")

config = Config()
config.load_env_variables()

if __name__ == "__main__":
    app.run(port=5000)

