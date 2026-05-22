#Jokenpo

#var
escolha1: str
escolha2: str
vencer: str

# A) verificar forma de usar uma variável chamada vencer junto a caso. o caso 1 seria meios em que haveria ganho, caso 2 seria meios que haveria perda,
# meios que haveria empate
# B) verificar uma forma do próprio programa jogar, escolhendo aleatoriamente a escolha 1 ( usando a lista ) e escolhendo aleatoriamente a escolha 2 (usando a lista)
# 

#inicio
jokenpo = {"pedra", "papel", "tesoura"}


print("JOKENPO - GO!\n")
print("Pedra\n")
print("Papel\n")
print("Tesoura\n")
escolha1 = input(print("Digite a escolha do 1º jogador:"))
escolha2 = input(print("Digite a escolha do 2º jogador:"))

if (escolha1 == "Pedra") and (escolha2 == "Tesoura"):
   print("Jogador 1 ganhou")
elif (escolha1 =="Pedra") and (escolha2 == "Papel"):
   print("Jogador 2 ganhou")
elif (escolha1 == "Pedra")  and (escolha2 == "Pedra"):
    print ("Empatou")
elif (escolha1 == "Papel") and (escolha2 == "Tesoura"):
    print("Jogador 2 Ganhou")
elif (escolha1 == "Papel") and (escolha2 == "Pedra"):
    print("Jogador 1 Ganhou") 
elif (escolha1 == "Papel")  and (escolha2 == "Papel"):
    print ("Empatou")     
elif (escolha1 == "Tesoura") and (escolha2 == "Papel"):
    print("Jogador 1 ganhou") 
elif (escolha1 == "Tesoura") and (escolha2 == "Pedra"):
    print("Jogador 2 ganhou")      
else:  
    print ("Empatou")
      


