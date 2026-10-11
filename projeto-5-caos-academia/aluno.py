import random

from academia import Academia
from constantes import TipoPersonalidade

class Aluno:
    def __init__(self, nome: str, tipo: TipoPersonalidade, academia: Academia, meta_treinos: int) -> None:
        self.nome: str = nome
        self.tipo: TipoPersonalidade = tipo
        self.academia: Academia = academia
        self.peso: int = -1
        self.meta_treinos: int = meta_treinos
        self.treinos_realizados: int = 0

    def iniciar_treino(self) -> None:
        halteres_disponiveis = self.academia.listar_halteres_disponiveis()

        if not halteres_disponiveis:
            print("Não há halteres disponíveis.")
            return

        self.peso = random.choice(halteres_disponiveis)
        self.academia.pegar_haltere(self.peso)
        print(f"{self.nome} iniciou um treino com o haltere de peso {self.peso} kg.")

    def terminar_treino(self) -> None:
        if not self.academia.verificar_posicao_livre(self.peso) or self.tipo == TipoPersonalidade.BAGUNCEIRO:
            posicoes_disponiveis = self.academia.listar_posicoes_disponiveis()
            posicao_selecionada = random.choice(posicoes_disponiveis)
        else:
            posicao_selecionada = self.peso
        self.academia.devolver_haltere(self.peso, posicao_selecionada)

        print(f"{self.nome} terminou um treino com o haltere de peso {self.peso} kg e deixou na posição {posicao_selecionada}.")

        self.peso = -1
        self.treinos_realizados += 1

    def __str__(self) -> str:
        return f"Aluno: {self.nome}, Tipo: {self.tipo}, Meta de treinos: {self.meta_treinos}, Treinos realizados: {self.treinos_realizados}"


