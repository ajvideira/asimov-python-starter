from enum import Enum


class TipoJogador(Enum):
    HUMANO = 1
    COMPUTADOR = 2

    def __str__(self) -> str:
        return self.name.title()