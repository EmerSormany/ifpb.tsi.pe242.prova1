def q1():
    """
    Dado um número inteiro x, retorne verdadeiro se x for um palíndromo, e falso caso contrário.

    """
    x = input("")
    if x == x[::-1]:
        print(True)
    else:
        print(False)

def q2():
    """
    Dado um numeral romano, converta-o para um número inteiro.
    I	1 feito
    V	5 feito
    X	10 feito
    L	50
    C	100
    D	500
    M	1000
    """
    roman = input("digite")
    value = 0

    inicio = 0
    fim = 2

    for i in roman:
        if i == 'I':
            if roman[inicio:fim] == 'IV':
                value += 4
                value -= 5
            elif roman[inicio:fim] == 'IX':
                value += 9
                value -= 10
            else:
                value += 1
        elif i == 'V':
            value += 5
        elif i == 'X':
            if roman[inicio:fim] == 'XL':
                value += 40
                value -= 50
            elif roman[inicio:fim] == 'XC':
                value += 90
                value -= 100
            else:
                value += 10
        elif i == 'L':
            value += 50
        elif i == 'C':
            if roman[inicio:fim] == 'CD':
                value += 400
                value -= 500
            elif roman[inicio:fim] == 'CM':
                value += 900
                value -= 1000
            else:
                value += 100
        elif i == 'D':
            value += 500
        elif i == 'M':
            value += 1000 

        inicio+=1
        fim+=1
    print(value)
    

def q3():
    count = 0
    number = int(input('digite '))
    for x in range(1, number+1):
        if number % x == 0:
            if x % 3 == 0:
                count+=1
    
    if count == 0:
        print('O número não possui divisores multiplos de 3')
    else:
        print('Quantidade de divisores divisiveis por 3:', count)

def q4():
    a = int(input(""))
    b = int(input(""))

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

    