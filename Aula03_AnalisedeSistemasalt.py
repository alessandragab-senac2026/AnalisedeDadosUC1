##laços de repetição
## while (enquanto) - aqui não amarra a quantidade de vezes que será repetido - verifica uma determinada condição antes de começar a rodar
## for: tem a quantidade de vezes pré-determinada, menor chance de erro
## exemplo For
##  for x em y:
##  print(x)
## for i in range(0,10,1) -> para o contador começando em 0, indo para 10, contando de um em um -- geralmente começa em 0
##    print (i)
## para usar decremento ( decrescer), mudar a ordem -> (10, 0 , -1) , para o contador começando em 10, indo para o 0, pule -1

### cálculo da média escolar 
### são 10 alunos




# não definindo a quantidade de alunos - usar um contador dentro do for, para usar ele como o divisor da média geral fora
contador = 0
media_total = 0
for aluno in range(0,2):
  nota1 = float(input("Digite a 1ª nota:"))
  nota2 = float(input("Digite a 2ª nota:")) 
  media = (nota1 + nota2)/2
  print (media)
  media_total += media
  contador += 1 

print(media_total/contador)


## usar o while para aceitar notas somente dentro de uma faixa estiipulada:

nota = float(input("Digite a 1ª nota:")) 

while nota > 0 or nota < 10:
   print("Nota fora do padrão ( 0 a 10).")  ## aqui é quando ñ atender
   nota = float(input("Digite a uma nota:"))


## lista simples em python = usar [ ]
## dicionário = { }
## em pandas iremos usar bastante dicionários - ou seja, usar bastante os colchetes , onde cada colchete seria uma tabela ou coluna

nota = ["João","111111111",25]
pessoa = {
   "nome" : "João",
    "cpf" : "111111111",
    "idade" : 25,
   "data_nascimento" : "10/05/2025",
}

funcionarios = [pessoa, pessoa2]






















