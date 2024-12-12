

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

        print(roman[inicio:fim])
        
        inicio+=1
        fim+=1

        if i == 'I':
            value += 1
        elif i == 'V':
            if roman[inicio:fim]== 'IV':
                value += 4
            else:
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

    print(value)

q2()

