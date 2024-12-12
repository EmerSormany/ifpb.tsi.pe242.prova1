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
    

