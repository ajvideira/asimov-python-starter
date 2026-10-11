from jogo_da_velha import JogoDaVelha
from jogador import Jogador
from tipo_jogador import TipoJogador

def main():
    jogadores = [Jogador("Jogador 1", "X", TipoJogador.HUMANO), Jogador("Jogador 2", "O", TipoJogador.COMPUTADOR)]

    jogo_da_velha = JogoDaVelha(jogadores)
    jogo_da_velha.iniciar_jogo()

if __name__ == "__main__":
    main()