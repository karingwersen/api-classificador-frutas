

class Fruta:
    def __init__(self):
        self.fruta_label = None
        self.fruta_nome = None
        self.fruta_subtipo = None
        self.fruta_massa = None
        self.fruta_largura = None
        self.fruta_altura = None
        self.fruta_pontuacao_cor = None

    def __init__(self, fruta_massa: float, fruta_largura: float, fruta_altura: float, fruta_pontuacao_cor: float):
        self.fruta_label = None
        self.fruta_nome = None
        self.fruta_subtipo = None
        self.fruta_massa = fruta_massa
        self.fruta_largura = fruta_largura
        self.fruta_altura = fruta_altura
        self.fruta_pontuacao_cor = fruta_pontuacao_cor
