
import random
def jogar():
    tentativas = 3
    pontos = 1000
    rodadas = 1
    print("qual nivel de deficuldade?")
    print("(1) facil (2) Medio (3) dificil")

    nivel = int(input("defina o nível: "))

    if(nivel ==1):
        tentativas = 20
    elif(nivel ==2):
        tentativas = 10
    else:
        tentativas = 5 
        
    while(rodadas <= tentativas):
        print("************************************")
        print("Bem-vindods ao jogo da adivinhação")
        print("************************************")
        print("essa e a {} rodada de {}".format(rodadas,tentativas))


        numero = random.randrange(1,101)
        chute = input("temte a sorte...")
        aux = int(chute)

        if (aux == numero):
            print("você acertou! e fez {} pontos!".format(pontos))
            break
        else: 
            if(aux > numero):
                print("muito alto seu chute")
            else:
                print("muito baixo seu chute")
            pontos_per= abs(numero - chute)
            pontos = pontos - pontos_per
        rodadas= rodadas + 1
if(__name__ == "__main__"):
      jogar()