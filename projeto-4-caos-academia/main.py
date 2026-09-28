import random

from academia import Academia
from aluno import Aluno
from constantes import TipoPersonalidade

def main():

    academia = Academia(list(range(10, 37, 2)))

    print(academia.porta_halteres)

    alunos: list[Aluno] = []
    for i in range(10):
        alunos.append(Aluno(f"Aluno {i+1}", TipoPersonalidade.ORGANIZADO, academia, random.choice(range(1, 11))))

    alunos.append(Aluno(f"Aluno {len(alunos)+1}", TipoPersonalidade.BAGUNCEIRO, academia, random.choice(range(1, 11))))
    alunos.append(Aluno(f"Aluno {len(alunos)+1}", TipoPersonalidade.BAGUNCEIRO, academia, random.choice(range(1, 11))))

    for aluno in alunos:
        print(aluno)

    while True:
        alunos_em_treinamento = [aluno for aluno in alunos if aluno.treinos_realizados < aluno.meta_treinos]

        if not alunos_em_treinamento:
            break

        aluno_selecionado = random.choice(alunos_em_treinamento)

        if aluno_selecionado.peso == -1:
            aluno_selecionado.iniciar_treino()
        else:
            aluno_selecionado.terminar_treino()

    print(academia.porta_halteres)
    print(f"Caos na academia: {academia.calcular_caos()}")

if __name__ == "__main__":
    main()