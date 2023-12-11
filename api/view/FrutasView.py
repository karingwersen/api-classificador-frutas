from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from controller.FrutasController import FrutasController
from model.Fruta import Fruta


app = Flask(__name__)
CORS(app)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API de Classificacao de Frutas"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

@app.route("/")
def api_classificacao_frutas_saudavel():
    return "API de Classificacao de Frutas saudavel"

@app.route("/api/v1/classificar_fruta", methods=["POST"])
def classificar_fruta():
    fruta_request = request.json

    fruta = Fruta(float(fruta_request["fruta_massa"]), float(fruta_request["fruta_largura"]), float(fruta_request["fruta_altura"]), float(fruta_request["fruta_pontuacao_cor"]))

    predicao = FrutasController.classificar_fruta(fruta)

    return str(predicao), 200

def view_frutas():
    app.run(host="0.0.0.0", port=5000)
