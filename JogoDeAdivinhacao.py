import random, time 


# VARIAVEIS
acertou = False
recorde = 0 
pontos = 100 
numero_secreto = random.randint(1, 100)
tentativas = 0 
sixsven_aura = 67
# FUNCIOES (e uma variavel ali ó)
def calcular_pontos(tentativas):
    return 100 - tentativas


def calculador_recorde(pontos, recorde):
     if pontos > recorde:
        print("novo recorde! seu novo recorde é:", pontos)
        return pontos
     else:
          print("você não bateu o seu recorde")
          return recorde


def tela_de_abertura():
    print("=================================")
    print("Bem-vindo ao jogo de adivinhação!")
    print("=================================")

def tela_de_vitoria(recorde):
        pontos = calcular_pontos(tentativas)
        print("Parabens! Você fez", pontos, "pontos!")
        print("Você acertou o número secreto em", tentativas, "tentativas.")
        print("O número secreto era:", numero_secreto)
        recorde = calculador_recorde(pontos, recorde)
        return recorde


# parte funcional do jogo
tela_de_abertura()
#parte pra repetir os bagui louco
for tentativas in range(1, 11):
    print(numero_secreto)
    try:
        escolha = int(input("escolha um numero entre 1 e 100 e tente adivinhar o número secreto (vc tem apenas 10 tentativas):"))
    except ValueError:
        print("TA LOUCÃO RAPAZ?! É NUMERO SEU BOSTA, SEU COCOZENDO! TENTA DENOVO SEU MERDA!")
        continue

    if escolha < numero_secreto:
        print("O número secreto é maior.")
    elif escolha > numero_secreto:
        print("O número secreto é menor.")
    else:
        recorde = tela_de_vitoria(recorde) 
        break
else:
    print("ERROU DMS KKKKKKKKKKKKKKKKKKKKKKKKKK seu burro")
    print(f'O numero secredo era {numero_secreto} KKKKK')

sair = input("Pressione S para continuar ou N para sair:").upper()
if sair == "N":
            time.sleep(1.5)
            print("Ok! saindo...")
            time.sleep(2)
            exit()
elif sair == "S":
    print("reiniciando o jogo...")
    time.sleep(2)