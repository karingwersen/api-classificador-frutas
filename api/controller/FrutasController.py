from model.Fruta import Fruta
from model.Modelo import Modelo

class FrutasController:
    
    @staticmethod
    def classificar_fruta(fruta: Fruta):
        modelo, X_treino, X_teste, y_treino, scaler = Modelo.carrega_modelo("ml/classificador-frutas.joblib")

        fruta_classificacao = Modelo.prever(modelo, X_treino, X_teste, y_treino, fruta, scaler)

        if fruta_classificacao == 1:
            return "Maçã"
        elif fruta_classificacao == 2:
            return "Tangerina"
        elif fruta_classificacao == 3:
            return "Laranja"
        elif fruta_classificacao == 4:
            return "Limão"
        else:
            return None
