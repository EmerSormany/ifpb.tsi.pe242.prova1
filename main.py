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
    for i in roman:
        if i == 'I':
            value += 1
        elif i == 'V':
            value += 5
        elif i == 'X':
            value += 10
        elif i == 'L':
            value += 50
        elif i == 'C':
            value += 100
        elif i == 'D':
            value += 500
        elif i == 'M':
            value += 1000
    

