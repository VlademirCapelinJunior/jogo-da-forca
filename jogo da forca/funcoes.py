import os;
import sys;

palavraChave = list
erros = int

def limparTela():
    os.system("cls")

def continuar():
    os.system("pause")
 
def exibirPalavera(chave, chutes):
    for i in range(len(chave)): 
        if (chave[i] in chutes):
            sys.stdout.write(chave[i])
        else: 
            sys.stdout.write('*')
        sys.stdout.write(' ')


def derrota(chave):
    print("Você foi enforcado e perdeu")
    print("A palavra correta era:", (chave))

def vitoria():
    print("Você é o vencedor.")
    return

def chutar():
        global erros, acertos, mensagem, derrota
        chute = str(input("Sua tentativa:").upper())
        if len(chute) > 1:
            if chute == "".join(palavraChave):
                acertos = len(palavraChave)
                return
            else:
                mensagem = ((chute), "não é a palavra correta.")
                erros -= 1
                derrota += 1
                return

        if chute in palavraChave:
            acertos += 1
            mensagem = ((chute.upper()), "esta correto !")
        else:
            erros -= 1
            derrota += 1
            mensagem = ((chute.upper()), " esta incorreto !")
        print("\n") 