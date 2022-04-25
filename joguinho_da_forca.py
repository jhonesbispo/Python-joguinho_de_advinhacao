
import random
with open("dicionario.txt", "r") as file:
    allText = file.read()
    lista = list(map(str, allText.split()))
    secreto = random.choice(lista)
    quantidade = len(secreto)
    secreto_temporario = '*' * quantidade
    digitadas = []
    chances = quantidade
    print(f'Sua palavra secreta é:{secreto_temporario}')
    print(f'Você tem {chances} chances para tentar acertar a palavra secreta.')
while True:
    if chances <= 0:
        print('Você perdeu!!!')
        print(f'A palavra secreta era {secreto}.')
        break
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Digite apenas uma letra')
        continue
    digitadas.append(letra)
    if letra in secreto:
        print("Acertou")
    else:
        print(f'{letra} não faz parte da palavra')
        digitadas.pop()
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Parabéns! Você ganhou o jogo!!!')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()
