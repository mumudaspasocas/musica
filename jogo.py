while True:
    import time, random
    desafio = random.choice(["seu desafio é: fazer o six seven!", "o seu desafio é: beber um copo de agua com um pouquinho de sal!", "o seu desafio é: fazer 10 flexões!", "o seu desafio é: fazer 10 abdominais!", "o seu desafio é: dar 10 pulinhos!"])
    print("==============")
    print("jogo dos MMs")
    print("==============")
    escolha = input("Escolha uma cor para o seu MM (vermelho, azul, verde, amarelo, roxo, laranja): ")
    if escolha.lower() == "vermelho":
        time.sleep(1.5)
        print(f"você escolhei o vermelho, então o seu desafio é: {desafio}")
        time.sleep(5)
    elif escolha.lower() == "laranja":
        eu_nunca = input("vc escolhei laranja, ele significa 'eu nunca eu ja', então digite algo que vc nunva fez!")
        time.sleep(1.5)
        print("ologo tu tem que fazer isso ein kkkk")
        eu_ja = input("agora digite algo que vc ja fez!")
        time.sleep(1.5)
        print("ai não mano kkkkkkkk")
        time.sleep(2)
    elif escolha.lower() == "amarelo":
        while True:
            escolha = input("beija casa ou mata? :")
            if escolha.lower() == "beija":
                time.sleep(1.5)
                print("eita beijo bom ein kkkkkkkkkkkk")
                time.sleep(2)
                break
            elif escolha.lower() == "casa":
                time.sleep(1.5)
                print("CASOU CASOU KSAKSKAS mais com quem ein?")
                time.sleep(2)
                break
                
            elif escolha.lower() == "mata":
                time.sleep(1.5)
                print("vixe kkkk")
                time.sleep(2)
                break
                
            else:
                print("escolha invalida seu cocozinho!")
    elif escolha.lower() == "verde":
        time.sleep(0.5)
        print("verdade 👍")
        time.sleep(2)
    elif escolha.lower() == "azul":
        escolha2 = input("o que vc prefere? :")
        time.sleep(1.5)
        print(f"muito bom ein kkk vc gostar de {escolha2}!")
        time.sleep(2)
    elif escolha.lower() == "marrom":
        segredo = input("conte um segredo! : ")
        time.sleep(1.5)
        print("kkkkkkkkkkk então o seu segredo não é mais um segredo kkkkkkk")
        time.sleep(2)
    elif escolha.lower() == "roxo":
        time.sleep(1.5)
        print("não sei o que fazer com roxo")
        time.sleep(2)
    else:
        time.sleep(1.5)
        print("vixe para de ser doido kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
        time.sleep(2)

    sair = input("deseja sair? (s/n): ")
    if sair.lower() == "s":
        print("obrigado por jogar!")
        break
    elif sair.lower() == "n":
        continue
    else:
        print("escolha invalida!")
        time.sleep(2)

