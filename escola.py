#!/user/bin/env python3
"""Exibe relatório de crianças por atividade

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades
"""
__version__ = "0.1.0"

#dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["João", "Antonio","Carlos","Maria","Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria", "Isolda", "Sandro"]
aula_danca = ["Gustavo", "Sofia","Joana", "Antonio"]

#listar alunos em cada atividade por sala
aula_ingles_sala1 = []
aula_ingles_sala2 = []

for aluno in aula_ingles:
    if aluno in sala1:
        aula_ingles_sala1.append(aluno)
    elif aluno in sala2:
        aula_ingles_sala2.append(aluno)   

print("Alunos da sala 1 matriculados em Inglês: ", aula_ingles_sala1) 
print("Alunos da sala 2 matriculados em Inglês: ", aula_ingles_sala2) 


aula_musica_sala1 = []
aula_musica_sala2 = []

for aluno in aula_musica:
    if aluno in sala1:
        aula_musica_sala1.append(aluno)
    elif aluno in sala2:
        aula_musica_sala2.append(aluno)   

print("Alunos da sala 1 matriculados em Música: ", aula_musica_sala1) 
print("Alunos da sala 2 matriculados em Música: ", aula_musica_sala2) 

aula_danca_sala1 = []
aula_danca_sala2 = []

for aluno in aula_danca:
    if aluno in sala1:
        aula_danca_sala1.append(aluno)
    elif aluno in sala2:
        aula_danca_sala2.append(aluno)   

print("Alunos da sala 1 matriculados em Dança: ", aula_danca_sala1) 
print("Alunos da sala 2 matriculados em Dança: ", aula_danca_sala2) 
