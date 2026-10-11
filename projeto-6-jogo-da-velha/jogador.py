from dataclasses import dataclass
from tipo_jogador import TipoJogador

@dataclass
class Jogador:
    nome: str
    simbolo: str
    tipo: TipoJogador