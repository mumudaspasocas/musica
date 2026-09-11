## variaveis
vida = 100
ataque = 20
moedas = 67
ataque_six = 10
ataque = 30

sair = False
import time, random
## funcoes  
def encerrar_jogo():
    exit()

def iniciar_jogo():
    print(""""
    ========================
      ❤️ SIX SEVEN RPG ⚔️
    ========================
    """)
    print("❤️ Vida: 100")
    print("⚔️ Ataque: 20")
    print("💰 Moedas: 67")
    
    print("1 - Explorar")
    print("2 - Status")
    print("3 - Sair")

def status():
        print("===== STATUS =====")
        print(f"Vida: {vida} ❤️")
        print(f"Ataque: {ataque} ⚔️")
        print(f"Moedas:  {moedas} 💰")
def combate_globin():
    print("=====================")
    print("DIGITE 1 PARA ATACAR")
    print(" OU 2 PARA FUGIR")
    print("=====================")


#parte funcional do jogo
iniciar_jogo()
while True:
    vida = 100 
    vida_six = 67
    escolha = input("escolha entre 1, 2 e 3 : ")
    if escolha == "1":
        print("Você saiu pra explorar! (conserteza vai ser moggado kkkk)")
        time.sleep(3)
        print("VOCE ACHOU UM SIX! ele esta sem o seven, então não sera dificil o combater...")
        time.sleep(1)
        combate_globin()
        while vida > 0 and vida_six > 0:
                try:
                    escolha_combate = int(input("escolha! :"))
                    if escolha_combate == 1:
                        vida_six -= ataque
                        print(f"Voce atacou o six , e agora ele esta com {vida_six} de vida! (você deu {ataque} de dano )")
                        time.sleep(2)
                        if vida_six <= 0:
                            print("o six morreu!")
                            break
                        print("o turno do six agora!")
                        time.sleep(3)
                        vida -= ataque_six
                        print(f"O six atacou você! você ficou com {vida} de vida! (betinha kkkk) (o six deu {ataque_six} de dano!)")
                        time.sleep(2)
                        if vida <= 0:
                            print("tu morreu ksksksk ")
                            break
                    elif escolha_combate == 2:
                        resultado = random.choices(
                            ["fugiu", "batalha", "tropeçou"],
                            weights=[50, 50, 50]
                        )[0]
                        if resultado == "fugiu":
                            print("Você conseguiu fugi! perdeu 67 de aura, mais fugiu (não abuse da sorte)")
                            break
                        elif resultado == "batalha":
                            print("você não consegui fugir! seu betinha")

                        elif resultado == "tropeçou":
                            print("você foi tentar fugir, escorregou e morreu kkkkkkkkk (o dev desse jogo não superou essa piada ainda ksksskskss)")
                            vida = 0
                    else:
                        print("SEU COCOZÃO! PARA DE SER BURRO E COLOCA UM NUEMRO DE 1 A 2 UMMMMMMMM OU DOOOOOOOOIS!!!!!")
                except ValueError:
                    print("Seu bosta, é pra digitar 1 ou 2 UM OU DOIS SEU BOSTINHA ESCREVE DIREITO")
                
    elif escolha == "2":
        status()
    elif escolha == "3":
        print("que isso six seven kkkk, blz então")
        time.sleep(2)
        print("saindo...")
        time.sleep(2)
        encerrar_jogo()
    else:
        print("DIGITA DIREITO SEU NEANDERTAL!!!")