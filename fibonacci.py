anterior = 0
atual = 1
proximo = atual + anterior #1

anterior = 1
atual = 1
proximo = atual + anterior #2

anterior = 1
atual = 2
proximo = atual + anterior #2

while proximo < 2000:
    proximo = atual + anterior
    anterior = atual
    atual = proximo
    proximo = atual + anterior
    print (proximo)