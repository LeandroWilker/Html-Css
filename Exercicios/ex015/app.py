from rich import print
import os
bolso = 0
lula = 0
nulo = 0
print('*'*30)
print('Eleições 2022')
print('*'*30)
while True:
    print('*'*30)
    print(f'[on green]Bolsonaro [/] - VOTOS = {bolso}')
    print(f'[on red]Lula  [/] - VOTOS = {lula}')
    print(f'[on white black]Nulos[/] - VOTOS = {nulo}')
    print('*'*30)
    try:
        votos = int(input('''Para quem gostaria de votar 
        para presidente da república?
        1 - Bolsonaro
        2 - Lula
        3 - para encerrar votação
        qual é seu voto: '''))
        if votos == 1:
            bolso += 1
        elif votos == 2:
            lula += 1
        else:
            nulo += 1
    except:
        print('digite apenas 1 ou 2')
        os.system('cls')
