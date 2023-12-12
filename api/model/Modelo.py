from model.Fruta import Fruta
import pickle
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

class Modelo:

    def carrega_modelo(path):
        if path.endswith('.pkl'):
            modelo = pickle.load(open(path, 'rb'))
        elif path.endswith('.joblib'):
            modelo, X_treino, X_teste, y_treino, y_teste, scaler = joblib.load(path)
        return modelo, X_treino, X_teste, y_treino, y_teste, scaler
    
    def prever(modelo, X_treino, X_teste, y_treino, fruta: Fruta, scaler):
        X_input = np.array([fruta.fruta_massa, fruta.fruta_largura, fruta.fruta_altura, fruta.fruta_pontuacao_cor])

        X_input = X_input.reshape(1, -1)

        X_input = scaler.transform(X_input)
        
        predicao = modelo.predict(X_input)

        print(predicao)
        
        return predicao[0]

