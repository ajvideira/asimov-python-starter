
class Academia:
    def __init__(self, halteres: list[int]) -> None:
        self.halteres: list[int] = halteres
        self.porta_halteres: dict[int, int] = {}
        self.reorganizar_halteres()

    def reorganizar_halteres(self) -> None:
        self.porta_halteres = {i: i for i in self.halteres}

    def listar_halteres_disponiveis(self) -> list[int]:
        return [peso for peso in self.porta_halteres.values() if peso != 0]

    def listar_posicoes_disponiveis(self) -> list[int]:
        return [posicao for posicao, peso in self.porta_halteres.items() if peso == 0]

    def pegar_haltere(self, haltere_desejado: int) -> bool:
        for posicao, peso in self.porta_halteres.items():
            if haltere_desejado == peso:
                self.porta_halteres[posicao] = 0
                return True
        return False

    def verificar_posicao_livre(self, posicao: int) -> bool:
        return self.porta_halteres[posicao] == 0

    def devolver_haltere(self, haltere: int, posicao: int) -> bool:
        if posicao not in self.porta_halteres:
            return False

        if self.porta_halteres[posicao] == 0:
            self.porta_halteres[posicao] = haltere
            return True
        return False

    def calcular_caos(self) -> float:
        if len(self.porta_halteres) == 0:
            return 0.0

        return sum(posicao != peso for posicao, peso in self.porta_halteres.items()) / len(self.porta_halteres)