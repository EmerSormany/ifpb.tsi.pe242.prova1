# Escreva um programa que receba como entrada dois números inteiros e retorne a soma dos números positivos no intervalo definido por eles, considerando inclusive os extremos.
# Referência
# Obs: o intervalo pode ser crescente ou decrescente
# ### Exemplos
# #### Exemplo 1:
# Entrada:
# -2
# 2
# Saída:
# 3
# #### Exemplo 2:
# Entrada:
# 1
# 3
# Saída:
# 3
# #### Exemplo 3:
# Entrada:
# 10
# -10
# Saída:
# 55
# Formato de entrada
# Dois números inteiros
# Dica: os números podem ser informados em qualquer ordem (não necessariamente o primeiro será menor que o segundo)
# Formato de saída
# Um número inteiro

def q4(a, b):

    # a = int(input("digite "))
    # b = int(input("digite "))

    count = 0
    if a < 0 and b < 0:
        print('Não há números postivos no intervalo')
    elif a < 0 and b > 0:
        for x in range(0, b+1):
            count+=x
    elif b < 0 and a > 0:
        for x in range(0, a+1):
            count+=x
    else:
        for x in range(a, b+1):
            count+=x
    print(count)
        
q4(1,3)
q4(-2,2)
q4(10,-10)