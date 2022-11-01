from funcoes import continuar, exibirPalavera, vitoria, derrota, limparTela

dicas = list
chutes = list
palavraChave = list
erros = int
escolha = int
acertos = int
derrota = int


def main():
    global jogador, perdedor, vencedor, derrota, desafiante
    
    def inicio():
        global dicas, palavraChave, chutes, erros, acertos, mensagem, desafiante, jogador, perdedor, vencedor, derrota
        dicas = []
        palavraChave = []
        chutes = []
        mensagem = ""
        desafiante = ""
        jogador = ""
        perdedor = ""
        vencedor = ""
        erros = 5
        acertos = 0
        derrota = 0    

    def chutar():
        global erros, acertos, mensagem, derrota
        chute = str(input("Tentativa:").upper())
        if len(chute) > 1:
            if chute == "".join(palavraChave):
                acertos = len(palavraChave)
                return
            else:
                mensagem = ((chute), "Esta incorreto.")
                erros -= 1
                derrota += 1
                return        
        else:
            chutes.append(chute)

        if chute in palavraChave:
            acertos += 1
            mensagem = "{} esta na palavra chave".format(chute.upper())
        else:
            erros -= 1
            derrota += 1
            mensagem = "{} está incorreta!".format(chute.upper())
        print("\n")
    inicio()
    limparTela()    
    desafiante = str(input("Desafiante:"));
    jogador = str(input("Jogador:"));

    if len(desafiante) and len(jogador) >= 3: 
        limparTela();

        palavraChave = list(input("Digite a palavraChave :").upper());            
        dicas.append (str(input("Dica 1:").upper()));
        dicas.append (str(input("Dica 2:").upper()));
        dicas.append (str(input("Dica 3:").upper()));

        limparTela()
        while acertos < len(palavraChave) and erros > 0:

            print("{}".format(mensagem));
            exibirPalavera(palavraChave, chutes);
            print("Restam", (erros), "tentativas");
            print("Escolha 1 para jogar e 2 para dica.");           
            
            try:
                escolha = int(input("Escolha:"))
                if escolha == 1:
                    limparTela()
                    chutar()
                elif escolha == 2:
                    if len(dicas) > 0:
                        limparTela()
                        print(dicas[0])
                        dicas.pop(0)
                    if len(dicas) > 0:
                        print("Restam {} dicas".format(len(dicas)))
                    else:
                        print("Acabou as dicas!")
                    chutar()
            except:
                limparTela()
                print("Opção invalida!")
            limparTela()

        if erros == 0:
            perdedor = "jogador " + jogador.capitalize()
            vencedor = "Desafiante " + desafiante.capitalize()
            

        elif acertos == len(palavraChave):
            perdedor = "Desafiante " + desafiante.capitalize()
            vencedor = "jogador " + jogador.capitalize()
            vitoria()

        abrir = open("historico.txt", "a")
        abrir.write('Palavra: {} - Vencedor: {}\n'.format(''.join(palavraChave).capitalize(), vencedor))
        abrir.close()
        abrirHistorico = open("historico.txt", "r")
        print("Jogadas")
        print(abrirHistorico.read())
        continuar()
        print("Se quiser jogar nomavente digite 1, se quiser parar por qaui digite 2.")
        
        sair = int
        while sair != 1 or sair != 2: 
            try:
                sair = int(input("Escolha:"))
                if sair == 1:
                    main()
                elif sair == 2:
                    break
            except:
                print("Escolha inexistente")
    else:
        print("Nome não suportado!")
        continuar()
        main()
main()
