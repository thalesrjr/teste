import forca
import adivinha
print("************************************")
print("********** escolha o jogoS ***********")
print("************************************")

print("(1) forca (2) adivinhação")

jogo = int(input("qual jogo?"))

if(jogo == 1):
    print("jogando forca")
    forca.jogar()
elif(jogo == 2):
    print("jogando forca")
    adivinha.jogar()
    