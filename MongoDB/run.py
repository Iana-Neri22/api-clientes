from flask import Flask
from models.blueprints.cliente_blueprints import clientes_bp
from config import Config
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)

SWAGGER_URL="/swagger"
API_URL="/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Access API'
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

app.register_blueprint(clientes_bp, url_prefix="/cliente")

config = Config()
config.load_env_variables()

if __name__ == "__main__":
    app.run(port=5000)

