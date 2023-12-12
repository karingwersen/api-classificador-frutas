from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

class Avaliador:

    def avaliar(self, modelo, X_teste, y_teste):
        
        predicoes = modelo.predict(X_teste)

        return(accuracy_score(y_teste, predicoes), recall_score(y_teste, predicoes, average=None), precision_score(y_teste, predicoes, average=None), f1_score(y_teste, predicoes, average=None))
