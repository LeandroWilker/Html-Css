from time import sleep
while True:
        num = int(input('digite um numero é veja sua tabuada: '))
        print(f'{num} x 1 = {num * 1}')
        print(f'{num} x 2 = {num * 2}')
        print(f'{num} x 3 = {num * 3}')
        print(f'{num} x 4 = {num * 4}')
        print(f'{num} x 5 = {num * 5}')
        print(f'{num} x 6 = {num * 6}')
        print(f'{num} x 7 = {num * 7}')
        print(f'{num} x 8 = {num * 8}')
        print(f'{num} x 9 = {num * 9}')
        print(f'{num} x 10 = {num * 10}')
        print('*'*40)
        resp = str(input('Quer continuar? [S/N] '))
        if resp in 'Nn''não''nao''NÃO''NAO':
            break
print('Finalizando... <<TABUADA>>')
for c in range(3, -1, -1):
    print(f'Finalizando...{c}')
    sleep(0.5)
print('<< FIM! VOLTE SEMPRE! >>')