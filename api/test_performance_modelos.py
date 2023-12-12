from model.Modelo import Modelo
from model.Avaliador import Avaliador
from sklearn.model_selection import cross_validate
import numpy as np

avaliador = Avaliador()

def test_modelo_knn():
    modelo_knn, X_treino, X_teste, y_treino, y_teste, scaler = Modelo.carrega_modelo("ml/classificador-frutas.joblib")

    acuracia_knn, recall_knn, precisao_knn, f1_knn = avaliador.avaliar(modelo_knn, X_teste, y_teste)

    assert acuracia_knn >= 0.9
    assert recall_knn.all() >= 0.5
    assert precisao_knn.all() >= 0.5
    assert f1_knn.all() >= 0.5

def test_modelo_gnb():
    modelo_gnb, X_treino, X_teste, y_treino, y_teste, scaler = Modelo.carrega_modelo("ml/classificador-frutas-gnb.joblib")

    acuracia_gnb, recall_gnb, precisao_gnb, f1_gnb = avaliador.avaliar(modelo_gnb, X_teste, y_teste)

    assert acuracia_gnb >= 0.9
    assert recall_gnb.all() >= 0.5
    assert precisao_gnb.all() >= 0.5
    assert f1_gnb.all() >= 0.5

def test_modelo_svc():
    modelo_svc, X_treino, X_teste, y_treino, y_teste, scaler = Modelo.carrega_modelo("ml/classificador-frutas-svc.joblib")

    acuracia_svc, recall_svc, precisao_svc, f1_svc = avaliador.avaliar(modelo_svc, X_teste, y_teste)

    assert acuracia_svc >= 0.9
    assert recall_svc.all() >= 0.5
    assert precisao_svc.all() >= 0.5
    assert f1_svc.all() >= 0.5

def test_modelo_arvore():
    modelo_arvore, X_treino, X_teste, y_treino, y_teste, scaler = Modelo.carrega_modelo("ml/classificador-frutas-arvore.joblib")

    acuracia_arvore, recall_arvore, precisao_arvore, f1_arvore = avaliador.avaliar(modelo_arvore, X_teste, y_teste)

    assert acuracia_arvore >= 0.9
    assert recall_arvore.all() >= 0.5
    assert precisao_arvore.all() >= 0.5
    assert f1_arvore.all() >= 0.5
