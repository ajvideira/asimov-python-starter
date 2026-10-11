import random
from jogador import Jogador
from tipo_jogador import TipoJogador


class JogoDaVelha:
    COMBINACOES_VITORIA = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6))

    def __init__(self, jogadores: list[Jogador]) -> None:
        self.jogadores: list[Jogador] = jogadores
        self.posicoes: list[Jogador | None] = [None] * 9

    def imprimir_tabuleiro(self) -> None:
        print(f" {self.imprimir_posicao(0)} | {self.imprimir_posicao(1)} | {self.imprimir_posicao(2)} ")
        print("---+---+---")
        print(f" {self.imprimir_posicao(3)} | {self.imprimir_posicao(4)} | {self.imprimir_posicao(5)} ")
        print("---+---+---")
        print(f" {self.imprimir_posicao(6)} | {self.imprimir_posicao(7)} | {self.imprimir_posicao(8)} ")

    def imprimir_posicao(self, posicao: int) -> str:
        jogador = self.posicoes[posicao]
        return f'{posicao + 1}' if jogador is None else jogador.simbolo

    def perguntar_jogada(self, jogador: Jogador) -> None:
        print(f"{jogador.nome}, informe a posição da sua jogada: ")

        while True:
            try:
                jogada = int(input())

                if jogada < 1 or jogada > 9 or self.posicoes[jogada-1] is not None:
                    raise ValueError

                self.posicoes[jogada - 1] = jogador

                break
            except ValueError:
                print("Posição inválida ou já ocupada. Informe novamente: ")
                continue

    def randomizar_jogada(self, jogador: Jogador) -> None:
        jogada = random.choice([i for i, pos in enumerate(self.posicoes) if pos is None])

        self.posicoes[jogada] = jogador

        print(f'{jogador.nome} jogou na posição {jogada + 1}.')

    def verificar_vitoria(self) -> bool:
        for a, b, c in self.COMBINACOES_VITORIA:
            if self.posicoes[a] is not None and self.posicoes[a] == self.posicoes[b] == self.posicoes[c]:
                return True
        return False

    def iniciar_jogo(self) -> None:
        print("Bem-vindo ao Jogo da Velha!")
        self.imprimir_tabuleiro()
        for i in range(9):
            jogador_atual = self.jogadores[0] if i % 2 == 0 else self.jogadores[1]

            print(f'É a vez do {jogador_atual.nome} ({jogador_atual.tipo})')

            if jogador_atual.tipo == TipoJogador.HUMANO:
                self.perguntar_jogada(jogador_atual)
            else:
                self.randomizar_jogada(jogador_atual)

            self.imprimir_tabuleiro()

            if self.verificar_vitoria():
                print(f'{jogador_atual.nome} venceu!')
                break
            elif i == 8:
                print('Deu empate!')