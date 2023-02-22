# Programa criado por	Bismilla <matheusalmcn@gmail.com>
# "log2u.py (v:1.1)"
# Mais informações no download na página do log2u do GitHub.
# {Link GiHub}

# Imports:
import datetime
from random import randint
from collections import Counter

# User Profile:
user = 0

# Home:
print('-------------------------------------------\n')
print('       Bancada de Logaritmos: log2u       ')
print('       [Criado por Matheus Almeida]       ')
print('                Versão 1.1                ')
print('\n-------------------------------------------')
print('     Para mais informações digite "0"     ')
print(' ')
print('Selecione o Módulo a partir de seu número:')
print(' 1 - Fatoração')
print(' 2 - Movimento Uniforme')
print(' 3 - Conversor de unidades')
print(' 4 - Médias')
print(' 5 - Fórmula de Bhaskara')
print(' 6 - Funções')
print(' 7 - Regra de 3')
print(' 8 - Triângulos')
print(' 9 - Info caracteres')
print(' 10 - Conversor de ângulos')
print(' 11 - Girar dado')
print(' 12 - Conversor de moedas')
print(' 13 - Gerador de matriz')
print(' 14 - Calculadora de derteminante')
totalmodulos = 14

modulo = int(input(': '))

# Módulo error:
if modulo < 0:
    print('.')
    print(modulo, ' não é um Módulo viável.')
if modulo == 99:
    totalmodulos = 99
if modulo >= (totalmodulos + 1):
    print('.')
    print('O Módulo ', modulo, ' não está disponível.')

# Módulo - Fatoração:
if modulo == 1:
    run = 1
    while run == 1:
        print(' ')
        logt = int(input('___________________________________\n[Digite 0 para encerrar o programa]\n Número a ser fatorado: '))
        if logt == 0:
            run = 0
            print('\nEncerrado.')
        else:
            logti = logt
            logr2 = logt % 2
            logr3 = logt % 3
            logr5 = logt % 5
            logr7 = logt % 7
            logr11 = logt % 11
            logr13 = logt % 13
            logr17 = logt % 17
            logr19 = logt % 19
            logr23 = logt % 23
            logr29 = logt % 29
            logr31 = logt % 31
            logr37 = logt % 37
            logr41 = logt % 41
            logr43 = logt % 43
            logr47 = logt % 47
            logr53 = logt % 53
            logr59 = logt % 59
            logr61 = logt % 61
            logr67 = logt % 67
            logr71 = logt % 71
            logr73 = logt % 73
            logr79 = logt % 79
            logr83 = logt % 83
            logr89 = logt % 89
            logr97 = logt % 97

            logd = []

            while logr2 == 0:
                logt = logt / 2
                logr2 = logt % 2
                logd = logd + [2]
            while logr3 == 0:
                logt = logt / 3
                logr3 = logt % 3
                logd = logd + [3]
            while logr5 == 0:
                logt = logt / 5
                logr5 = logt % 5
                logd = logd + [5]
            while logr7 == 0:
                logt = logt / 7
                logr7 = logt % 7
                logd = logd + [7]
            while logr11 == 0:
                logt = logt / 11
                logr11 = logt % 11
                logd = logd + [11]
            while logr13 == 0:
                logt = logt / 13
                logr13 = logt % 13
                logd = logd + [13]
            while logr17 == 0:
                logt = logt / 17
                logr17 = logt % 17
                logd = logd + [17]
            while logr19 == 0:
                logt = logt / 19
                logr19 = logt % 19
                logd = logd + [19]
            while logr23 == 0:
                logt = logt / 23
                logr23 = logt % 23
                logd = logd + [23]
            while logr29 == 0:
                logt = logt / 29
                logr29 = logt % 29
                logd = logd + [29]
            while logr31 == 0:
                logt = logt / 31
                logr31 = logt % 31
                logd = logd + [31]
            while logr37 == 0:
                logt = logt / 37
                logr37 = logt % 37
                logd = logd + [37]
            while logr41 == 0:
                logt = logt / 41
                logr41 = logt % 41
                logd = logd + [41]
            while logr43 == 0:
                logt = logt / 43
                logr43 = logt % 43
                logd = logd + [43]
            while logr47 == 0:
                logt = logt / 47
                logr47 = logt % 47
                logd = logd + [47]
            while logr53 == 0:
                logt = logt / 53
                logr53 = logt % 53
                logd = logd + [53]
            while logr59 == 0:
                logt = logt / 59
                logr59 = logt % 59
                logd = logd + [59]
            while logr61 == 0:
                logt = logt / 61
                logr61 = logt % 61
                logd = logd + [61]
            while logr67 == 0:
                logt = logt / 67
                logr67 = logt % 67
                logd = logd + [67]
            while logr71 == 0:
                logt = logt / 71
                logr71 = logt % 71
                logd = logd + [71]
            while logr73 == 0:
                logt = logt / 73
                logr73 = logt % 73
                logd = logd + [73]
            while logr79 == 0:
                logt = logt / 79
                logr79 = logt % 79
                logd = logd + [79]
            while logr83 == 0:
                logt = logt / 83
                logr83 = logt % 83
                logd = logd + [83]
            while logr89 == 0:
                logt = logt / 89
                logr89 = logt % 89
                logd = logd + [89]
            while logr97 == 0:
                logt = logt / 97
                logr97 = logt % 97
                logd = logd + [97]
            logtw = []
            logtw2 = 0
            if logt > 97:
                print(' ')
                print('A Fatoração de ', logti, ' é:')
                print('     [Possui Numero Primo acima de 100]')
                logtw = logtw + ['?']
                logtw2 = 1

            elif len(logd) <= 1:
                logd = '[Número Primo]'
            print(' ')
            if logtw2 == 0:
                print('A Fatoração de ', logti, ' é:')
            if logtw2 == 1:
                print('    ', logd, logtw)
            if logtw2 == 0:
                print('    ', logd)

# Módulo - Movimento Uniforme:
if modulo == 2:
    print('.')
    print('O que desejas descobrir?')
    print('1 - Espaço percorrido')
    print('2 - Espaço inicial')
    print('3 - Velocidade')
    print('4 - Tempo')
    descobrir = int(input(':'))
    if descobrir == 1:
        print('.')
        print('LEMBRE-SE DE MANTER AS UNIDADES DE MEDIDAS')
        print('(km/h) ou (m/s)')
        So = float(input('Espaço Inicial: '))
        v = float(input('Velocidade: '))
        t = float(input('Tempo Percorrido: '))
        S = So + v * t
        print('.')
        print('Seu espaço percorrido foi:')
        print('    ', S)

    if descobrir == 2:
        print('.')
        print('LEMBRE-SE DE MANTER AS UNIDADES DE MEDIDAS')
        print('(km/h) ou (m/s)')
        S = float(input('Espaço Percorrido: '))
        v = float(input('Velocidade: '))
        t = float(input('Tempo Percorrido: '))
        So = S - v * t
        print('.')
        print('Seu espaço inicial foi:')
        print('    ', So)

    if descobrir == 3:
        print('.')
        print('LEMBRE-SE DE MANTER AS UNIDADES DE MEDIDAS')
        print('(km/h) ou (m/s)')
        So = float(input('Espaço Inicial: '))
        S = float(input('Espaco Percorrido: '))
        t = float(input('Tempo Percorrido: '))
        v = (S - So) / t
        print('.')
        print('Sua velocidade foi:')
        print('    ', v)

    if descobrir == 4:
        print('.')
        print('LEMBRE-SE DE MANTER AS UNIDADES DE MEDIDAS')
        print('(km/h) ou (m/s)')
        So = float(input('Espaço Inicial: '))
        v = float(input('Velocidade: '))
        S = float(input('Espaço Percorrido: '))
        t = (S - So) / v
        print('.')
        print('Seu Tempo foi:')
        print('    ', t)

# Módulo - Conversor de Unidades:
if modulo == 3:
    print('.')
    print('Escolha a unidade:')
    print('1 - Km/h ---> m/s')
    print('2 - m/s ---> Km/s')
    print('3 - m³ ---> Litro')
    print('4 - Polegada ---> Metro')
    print('5 - Celsius ---> Kelvin')
    print('6 - Celsius ---> Fahrenheit')
    print('7 - Minutos ---> Horas')
    print('8 - Horas ---> Minutos')
    print('9 - Horas ---> Dias')
    cv = int(input(': '))
    if cv == 1:
        print('.')
        cv1 = float(input('Km: '))
        cv1a = cv1
        cv1 = cv1 * 36 / 10
        print('.')
        print(cv1a, ' Km/h para m/s é:')
        print('    ', cv1, 'm/s')
    if cv == 2:
        print('.')
        cv2 = float(input('m/s: '))
        cv2a = cv2
        cv2 = cv2 * 10 / 36
        print('.')
        print(cv2a, ' m/s para Km/h é:')
        print('    ', cv2, ' Km/h')
    if cv == 3:
        print('.')
        cv3 = float(input('m³: '))
        cv3a = cv3
        cv3 = cv3 * 1000
        print('.')
        print(cv3a, ' m³ para litros é:')
        print('    ', cv3, ' litros')
    if cv == 4:
        print('.')
        cv4 = float(input('Polegadas: '))
        cv4a = cv4
        cv4 = cv4 * 100 / 3937
        print('.')
        print(cv4a, ' polegadas para Metros é:')
        print('    ', round(cv4, 5), ' metros')
    if cv == 5:
        print('.')
        cv5 = float(input('Graus Celsius: '))
        cv5a = cv5
        cv5 = cv5 + 27315 / 100
        print('.')
        print(cv5a, ' graus celsius para graus kelvin é:')
        print('    ', cv5, ' graus kelvin')
    if cv == 6:
        print('.')
        cv6 = float(input('Graus Celsius: '))
        cv6a = cv6
        cv6 = cv6 * 9 / 5 + 32
        print('.')
        print(cv6a, ' graus celsius para grau Fahrenheit é:')
        print('    ', round(cv6, 5), ' graus Fahrenheit')
    if cv == 7:
        print('.')
        cv7 = float(input('Minutos: '))
        cv7a = cv7
        cv7 = cv7 / 60
        print('.')
        print(cv7a, ' minutos para horas é:')
        print('    ', round(cv7, 5), ' Horas')
    if cv == 8:
        print('.')
        cv8 = float(input('Horas: '))
        cv8a = cv8
        cv8 = cv8 * 60
        print('.')
        print(cv8a, ' horas para minutos é:')
        print('    ', round(cv8, 5), ' Minutos')
    if cv == 9:
        print('.')
        cv9 = float(input('Horas: '))
        cv9a = cv9
        cv9 = cv9 / 24
        print('.')
        print(cv9a, ' horas para dias é:')
        print('    ', round(cv9, 5), ' Dias')

# Módulo - Médias:
if modulo == 4:
    print('.')
    print('Selecione o modo:')
    print('1 - Média Aritmética')
    print('2 - Média Geométrica')
    print('3 - Média Harmônica')
    print('4 - Média Ponderada')
    md = int(input(': '))
    if md == 1:
        md1 = 1
        if md1 == 1:
            mt = 10
            a = 0
            while a == 0:
                print('[O máximo de termos é 10, caso seja menor do que isso, ponha "0"]')
                a = float(input('Valor do termo 1: '))
                if a == 0:
                    print('.')
                    print('Não é possível o valor do termo 1 ser nulo.')
                    print('.')
            b = float(input('Valor do termo 2: '))
            if b == 0:
                mt = mt - 1
            c = float(input('Valor do termo 3: '))
            if c == 0:
                mt = mt - 1
            d = float(input('Valor do termo 4: '))
            if d == 0:
                mt = mt - 1
            e = float(input('Valor do termo 5: '))
            if e == 0:
                mt = mt - 1
            f = float(input('Valor do termo 6: '))
            if f == 0:
                mt = mt - 1
            g = float(input('Valor do termo 7: '))
            if g == 0:
                mt = mt - 1
            h = float(input('Valor do termo 8: '))
            if h == 0:
                mt = mt - 1
            i = float(input('Valor do termo 9: '))
            if i == 0:
                mt = mt - 1
            j = float(input('Valor do termo 10: '))
            if j == 0:
                mt = mt - 1

            tt1 = a + b + c + d + e + f + g + h + i + j
            tt = tt1 / mt
            md = 0
            print('.')
            print('A média aritmética é: ', tt)

    if md == 2:
        md1 = 1
        if md1 == 1:
            mt = 10
            a = 0
            while a == 0:
                print('[O máximo de termos é 10, caso seja menor do que isso, ponha "0"]')
                a = float(input('Valor do termo 1: '))
                if a == 0:
                    print('.')
                    print('Não é possível o valor do termo 1 ser nulo.')
                    print('.')
            b = 0
            while b == 0:
                b = float(input('Valor do termo 2: '))
                if b == 0:
                    print('.')
                    print('Não é possível o valor do termo 2 ser nulo.')
                    print('.')
            if b == 0:
                mt = mt - 1
                b = 1
            c = float(input('Valor do termo 3: '))
            if c == 0:
                mt = mt - 1
                c = 1
            d = float(input('Valor do termo 4: '))
            if d == 0:
                mt = mt - 1
                d = 1
            e = float(input('Valor do termo 5: '))
            if e == 0:
                mt = mt - 1
                e = 1
            f = float(input('Valor do termo 6: '))
            if f == 0:
                mt = mt - 1
                f = 1
            g = float(input('Valor do termo 7: '))
            if g == 0:
                mt = mt - 1
                g = 1
            h = float(input('Valor do termo 8: '))
            if h == 0:
                mt = mt - 1
                h = 1
            i = float(input('Valor do termo 9: '))
            if i == 0:
                mt = mt - 1
                i = 1
            j = float(input('Valor do termo 10: '))
            if j == 0:
                mt = mt - 1
                j = 1
            if mt == 2:
                rr = 'quadrada'
            if mt == 3:
                rr = 'cúbica'
            if mt == 4:
                rr = 'quarta'
            if mt == 5:
                rr = 'quinta'
            if mt == 6:
                rr = 'sexta'
            if mt == 7:
                rr = 'sétima'
            if mt == 8:
                rr = 'oitava'
            if mt == 9:
                rr = 'nona'
            if mt == 10:
                rr = 'décima'

            tt1 = a * b * c * d * e * f * g * h * i * j
            tt = tt1 ** (1 / mt)
            md = 0
            print('.')
            print('A média geométrica é: ', tt)
            print('.')
            print('    [ raiz {rr} de {tt1} ]'.format(rr=rr, tt1=tt1))

    if md == 3:
        md1 = 1
        if md1 == 1:
            mt = 10
            a = 0
            while a == 0:
                print('[O máximo de termos é 10, caso seja menor do que isso, ponha "0"]')
                a = float(input('Valor do termo 1: '))
                if a == 0:
                    print('.')
                    print('Não é possível o valor do termo 1 ser nulo.')
                    print('.')
            b = float(input('Valor do termo 2: '))
            if b == 0:
                mt = mt - 1
                b = 1
            c = float(input('Valor do termo 3: '))
            if c == 0:
                mt = mt - 1
                c = 1
            d = float(input('Valor do termo 4: '))
            if d == 0:
                mt = mt - 1
                d = 1
            e = float(input('Valor do termo 5: '))
            if e == 0:
                mt = mt - 1
                e = 1
            f = float(input('Valor do termo 6: '))
            if f == 0:
                mt = mt - 1
                f = 1
            g = float(input('Valor do termo 7: '))
            if g == 0:
                mt = mt - 1
                g = 1
            h = float(input('Valor do termo 8: '))
            if h == 0:
                mt = mt - 1
                h = 1
            i = float(input('Valor do termo 9: '))
            if i == 0:
                mt = mt - 1
                i = 1
            j = float(input('Valor do termo 10: '))
            if j == 0:
                mt = mt - 1
                j = 1

            tt1 = mt / (1 / a + 1 / b + 1 / c + 1 / c + 1 / e + 1 / f + 1 / g + 1 / h + 1 / i + 1 / j - (10 - mt))
            tt2 = (1 / a + 1 / b + 1 / c + 1 / c + 1 / e + 1 / f + 1 / g + 1 / h + 1 / i + 1 / j - (10 - mt))
            print('A média harmônica é: ', round(tt1, 5))
            print('    [ {mt} / {tt2} ]'.format(mt=mt, tt2=tt2))

    if md == 4:
        md1 = 1
        if md1 == 1:
            mt = 10
            ap = 0
            bp = 0
            cp = 0
            dp = 0
            ep = 0
            fp = 0
            gp = 0
            hp = 0
            ip = 0
            jp = 0
            a = 0
            while a == 0:
                print('[O máximo de termos é 10, caso seja menor do que isso, ponha "0"]')
                a = float(input('Valor do termo 1: '))
                if a == 0:
                    print('.')
                    print('Não é possível o valor do termo 1 ser nulo.')
                    print('.')
                else:
                    ap = 0
                    while ap == 0:
                        ap = float(input('Valor do Peso do termo 1: '))
                        if ap == 0:
                            print('.')
                            print('Não é possível o valor do Peso 1 ser nulo.')
                            print('.')
            b = 0
            while b == 0:
                b = float(input('Valor do termo 2: '))
                if b == 0:
                    print('.')
                    print('Não é possível o valor do termo 2 ser nulo.')
                    print('.')
            if b == 0:
                mt = mt - 1
            else:
                bp = 0
                while bp == 0:
                    bp = float(input('Valor do Peso do termo 2: '))
                    if bp == 0:
                        print('.')
                        print('Não é possível o valor do Peso 2 ser nulo.')
                        print('.')
            c = float(input('Valor do termo 3: '))
            if c == 0:
                mt = mt - 1
            else:
                cp = float(input('Valor do Peso do termo 3: '))
            d = float(input('Valor do termo 4: '))
            if d == 0:
                mt = mt - 1
            else:
                dp = float(input('Valor do Peso do termo 4: '))
            e = float(input('Valor do termo 5: '))
            if e == 0:
                mt = mt - 1
            else:
                ep = float(input('Valor do Peso do termo 5: '))
            f = float(input('Valor do termo 6: '))
            if f == 0:
                mt = mt - 1
            else:
                fp = float(input('Valor do Peso do termo 6: '))
            g = float(input('Valor do termo 7: '))
            if g == 0:
                mt = mt - 1
            else:
                gp = float(input('Valor do Peso do termo 7: '))
            h = float(input('Valor do termo 8: '))
            if h == 0:
                mt = mt - 1
            else:
                hp = float(input('Valor do Peso do termo 8: '))
            i = float(input('Valor do termo 9: '))
            if i == 0:
                mt = mt - 1
            else:
                ip = float(input('Valor do Peso do termo 9: '))
            j = float(input('Valor do termo 10: '))
            if j == 0:
                mt = mt - 1
            else:
                jp = float(input('Valor do Peso do termo 10: '))

            tt1 = a * ap + b * bp + c * cp + d * dp + e * ep + f * fp + g * gp + h * hp + i * ip + j * jp
            tt2 = ap + bp + cp + dp + ep + fp + gp + hp + ip + jp
            tt3 = tt1 / tt2
            print('.')
            print('A média ponderada é: ', tt3, '\n    ({tt1} / {tt2})'.format(tt1=tt1, tt2=tt2))

# Módulo - Fórmula de Bhaskara:
if modulo == 5:
    print('.')
    print('Utilize a base: P(x) = ax² + bx + c')
    a = float(input('Valor de A: '))
    b = float(input('Valor de B: '))
    c = float(input('Valor de C: '))
    delta = b * b - 4 * a * c
    if delta < 0:
        print('.')
        print('Não há raizes reais.')
    elif delta == 0:
        x1 = (-1 * b) / (2 * a)
        print('.')
        print('A única raíz de:')
        print('P(x) = ', a, 'x² + ', b, 'x + ', c)
        print('É: ', x1)
    else:
        rdelta = delta ** 0.5
        deltaw = round(rdelta, 2)
        if rdelta != deltaw:
            x1 = (-1 * b + delta) / (2 * a)
            x2 = (-1 * b - delta) / (2 * a)
            print('.')
            print('A raiz não é exata')
            print('As raízes são:')
            print('x¹ =   ', -1 * b, ' + raiz de', delta)
            print('        --------------------')
            print('                ', 2 * a)
            print('.')
            print('x² =   ', -1 * b, ' - raiz de', delta)
            print('        --------------------')
            print('                ', 2 * a)
        if rdelta == deltaw:
            x1 = (-1 * b + rdelta) / (2 * a)
            x2 = (-1 * b - rdelta) / (2 * a)
            print('As raízes de:')
            print('P(x) = ', a, 'x² + ', b, 'x + ', c)
            print('São: ', x1, ' e ', x2)

# Módulo - Funções:
if modulo == 6:
    print('.')
    print('Tipo de função:')
    print('1 - Função Afim')
    print('2 - Função Quadrática')
    print('3 - Vértice da Função')
    fun = int(input(': '))
    if fun == 1:
        print('.')
        print('Utilize F(x) = ax + b')
        a = float(input('Valor de A: '))
        b = float(input('Valor de B: '))
        funx = 1
        while funx == 1:
            print('.')
            print('Digite 0.01 para encerrar o programa.')
            print('F(x) = {a}x + {b}'.format(a=a, b=b))
            x = float(input('Valor de X: '))
            if x == 0.01:
                funx = 0
                print('.')
                print('Encerrado.')
            y = a * x + b
            if x != 0.01:
                print('.')
                print('F(x) será -----> ', y)
                x = 0

    if fun == 2:
        print('.')
        print('Utilize F(x) = ax² + bx + c')
        a = float(input('Valor de A: '))
        while a == 0:
            print('.')
            print('O valor de A não pode ser nulo.')
            a = float(input('Valor de A: '))
        b = float(input('Valor de B: '))
        c = float(input('Valor de C: '))
        funx = 1
        while funx == 1:
            print('.')
            print('Digite 0.01 para encerrar o programa.')
            print('F(x) = {a}x² + {b}x + {c}'.format(a=a, b=b, c=c))
            x = float(input('Valor de X: '))
            if x == 0.01:
                funx = 0
                print('.')
                print('Encerrado.')
            y = a * (x ** 2) + b * x + c
            if x != 0.01:
                print('.')
                print('F(x) será -----> ', y)
                x = 0

    if fun == 3:
        grafico = 0
        print('.')
        print('Utilize F(x) = ax² + bx + c')
        a = float(input('Valor de A: '))
        if a > 0:
            grafico = 'Crescente'
            ponto = 'mais baixo'
        if a < 0:
            grafico = 'Decrescente'
            ponto = 'mais alto'
        while a == 0:
            print('.')
            print('O valor de A não pode ser nulo.')
            a = float(input('Valor de A: '))
        b = float(input('Valor de B: '))
        c = float(input('Valor de C: '))
        xv = (-1 * b) / (2 * a)
        yv = (4 * a * c - b * b) / (4 * a)
        delta = b * b - 4 * a * c
        if delta < 0:
            raizes = 'Não há raízes reais.'
        if delta == 0:
            raizes = 'Há apenas 1 raiz real.'
        if delta > 0:
            raizes = 'Há 2 raízes reais distintas.'
        print('.')
        print('[', raizes, ']')
        print('[ Grafico ', grafico, ' ]')
        print('O ponto ', ponto, ' do gráfico é:')
        print('({xv}, {yv})'.format(xv=xv, yv=yv))

# Módulo - Regra de 3:
if modulo == 7:
    print('.')
    print('Selecione o modo:')
    print('1 - Simples')
    print('2 - Composta')
    reg = int(input(': '))
    if reg == 1:
        regw = 1
        while regw == 1:
            print('.')
            print('[X é o resultado final]')
            print('[Utilize 0 para encerrar]')
            print('.')
            print('A  está para  B')
            print('   assim como  ')
            print('C  está para  X')
            print('.')
            a = float(input('A = '))
            if a == 0:
                regw = 0
                print('.')
                print('Encerrado.')
            else:
                b = float(input('B = '))
                if b == 0.01:
                    regw = 0
                    print('.')
                    print('Encerrado.')
                else:
                    c = float(input('C = '))
                    if c == 0.01:
                        regw = 0
                        print('.')
                        print('Encerrado.')
                    else:
                        x = (c * b) / a
                        xw = c * b
                        print('.')
                        print('X será -----> ', x, ' ({xw} / {a})'.format(xw=xw, a=a))

    if reg == 2:
        res = 0
        print('.')
        print('Adicione os nomes dos grupos.')
        print('Exemplos: Tempo, Dias, Pessoas, Progresso...')
        gr1n = input('Grupo 1 (Que possui a variável X): ')
        gr2n = input('Grupo 2: ')
        gr3n = input('Grupo 3: ')
        gr1a = float(input('. \n Primeira etapa \n Quanto(s) {gr1n} ? '.format(gr1n=gr1n)))
        gr2a = float(input(' Quanto(s) {gr2n} ? '.format(gr2n=gr2n)))
        gr3a = float(input(' Quanto(s) {gr3n} ? '.format(gr3n=gr3n)))
        gr1b = 0
        gr2b = float(input('. \n Segunda etapa: \n Quanto(s) {gr2n} ? '.format(gr2n=gr2n)))
        gr3b = float(input(' Quanto(s) {gr3n} ? '.format(gr3n=gr3n)))
        pp1 = int(input(
            '. \n {gr2n} é proporcional ao {gr1n}? \n 1 - Proporcional \n 2 - Não proporcional \n : '.format(gr2n=gr2n,
                                                                                                             gr1n=gr1n)))
        if pp1 == 1:
            pp2 = int(input(
                '. \n {gr3n} é proporcional ao {gr1n} ? \n 1 - Proporcional \n 2 - Não proporcional \n : '.format(
                    gr3n=gr3n, gr1n=gr1n)))
            if pp2 == 1:
                res1 = gr2a * gr3a
                res2 = gr2b * gr3b
                gw = gr1a * res2
                gr1b = gw / res1
                print('...')
                print('O resultado de X no contexto de ', gr1n, ' é:')
                print('    X = {gr1b}   ({gw} / {res1})'.format(gr1b=gr1b, gw=gw, res1=res1))
            if pp2 == 2:
                res1 = gr2a * gr3b
                res2 = gr2b * gr3a
                gw = gr1a * res2
                gr1b = gw / res1
                print('...')
                print('O resultado de X no contexto de ', gr1n, ' é:')
                print('    X = {gr1b}   ({gw} / {res1})'.format(gr1b=gr1b, gw=gw, res1=res1))

        if pp1 == 2:
            print('.')
            print(' ', gr3n, ' é proporcional ao ', gr1n, ' ?')
            print('1 - Proporcional')
            print('2 - Não proporcional')
            pp2 = int(input(': '))
            if pp2 == 1:
                res1 = gr2b * gr3a
                res2 = gr2a * gr3b
                gw = gr1a * res2
                gr1b = gw / res1
                print('...')
                print('O resultado de X no contexto de ', gr1n, ' é:')
                print('    X = {gr1b}   ({gw} / {res1})'.format(gr1b=gr1b, gw=gw, res1=res1))
            if pp2 == 2:
                res1 = gr2b * gr3b
                res2 = gr2a * gr3a
                gw = gr1a * res2
                gr1b = gw / res1
                print('...')
                print('O resultado de X no contexto de ', gr1n, ' é:')
                print('    X = {gr1b}   ({gw} / {res1})'.format(gr1b=gr1b, gw=gw, res1=res1))

# Módulo - Triângulos:
if modulo == 8:
    print('.')
    print('Selecione o modo:')
    print('1 - Condição de existência e forma')
    print('2 - Teorema de Pitágoras')
    print('3 - Lei dos cossenos')
    tri = int(input(': '))
    if tri == 1:
        l1 = float(input('Medida do lado 1: '))
        l2 = float(input('Medida do lado 2: '))
        l3 = float(input('Medida do lado 3: '))
        if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l1 + l2):
            te = 'Triângulo existente'
            tw = 1
        else:
            te = 'Triângulo inexistente'
            tw = 0

        if l1 > l2 and l1 > l2:
            lm = l1
            ln1 = l2
            ln2 = l3
        if l2 > l1 and l2 > l3:
            lm = l2
            ln1 = l1
            ln2 = l3
        if l3 > l1 and l3 > l2:
            lm = l3
            ln1 = l1
            ln2 = l2
        if l1 == l2 and l1 > l3:
            lm = l1
            ln1 = l2
            ln2 = l3
        if l2 == l3 and l2 > l1:
            lm = l2
            ln1 = l1
            ln2 = l3
        if l1 == l3 and l1 > l3:
            lm = l1
            ln1 = l2
            ln2 = l3

        if l1 == l2 and l2 == l3:
            tf = 'Equilátero'
        if lm < ((ln1 * 2 + ln2 * 2) ** (1 / 2)):
            tf = 'Acutângulo'
        if lm > ((ln1 * 2 + ln2 * 2) ** (1 / 2)):
            tf = 'Obtusângulo'
        if lm == ((ln1 * 2 + ln2 * 2) ** (1 / 2)):
            tf = 'Retângulo'

        print('Informações do triângulo:')
        print('[ ', te, ' ]')
        if tw == 1:
            print('[ Triângulo ', tf, ' ]')

    if tri == 2:
        print('.')
        print('O que desejas descobrir?')
        print('1 - Um cateto qualquer')
        print('2 - A hipotenusa')
        pit1 = int(input(': '))
        if pit1 == 1:
            print('.')
            cat1 = float(input('Tamanho do Cateto 1: '))
            hip = float(input('Tamanho da Hipotenusa: '))
            cat2 = hip * 2 - cat1 * 2
            if cat1 >= hip:
                print('.')
                print('[Ocasionamento Impossivel.]')
                print('[É impossivel um cateto ser maior ou igual a  Hipotenusa.]')
            else:
                cat2b = cat2
                cat2 = cat2 ** (1 / 2)
                cat2a = round(cat2, 2)
                if cat2a != cat2:
                    print('.')
                    print('O valor do outro cateto é de:')
                    print('    ', cat2)
                    print('[O Resultado é a raiz de ', cat2b, ']')
                else:
                    print('.')
                    print('O valor do outro cateto é:')
                    print('    ', cat2)
        if pit1 == 2:
            cat1 = float(input('Tamanho do Cateto 1: '))
            cat2 = float(input('Tamanho do Cateto 2: '))
            hip = cat1 * 2 + cat2 * 2
            hipb = hip
            hip = hip ** (1 / 2)
            hipa = round(hip, 2)
            if hipa != hip:
                print('.')
                print('O valor da Hipotenusa é de:')
                print('    ', hip)
                print('[O Resultado é a raiz de ', hipb, ']')
            else:
                print('.')
                print('O valor da Hipotenusa é de:')
                print('    ', hip)

    if tri == 3:
        print('.')
        r2 = 1.4142135624
        r3 = 1.7320508076
        cos = 0
        a = float(input('Valor do lado adjacente 1: '))
        b = float(input('Valor do lado adjacente 2: '))
        alp = int(input('Ângulo entre os lados: '))
        cosw = 1
        if alp == 0:
            cos = 1
            cosw = 0
        if alp == 30:
            cos = r3 / 2
            c3 = 'raiz de 3'
        if alp == 45:
            cos = r2 / 2
            c3 = 'raiz de 2'
        if alp == 60:
            cos = 1 / 2
            cosw = 0
        if alp == 90:
            cos = 0
            cosw = 0
        if alp == 120:
            cos = -1 / 2
            cosw = 0
        if alp == 135:
            cos = r2 / -2
            c3 = 'raiz de 2'
        if alp == 150:
            cos = r3 / -2
            c3 = 'raiz de 3'
        if alp >= 180 or alp < 0:
            print('Triângulo inexistente.')
        if alp != 0 and alp != 30 and alp != 45 and alp != 60 and alp != 90 and alp != 120 and alp != 135 and alp != 150:
            print('.')
            print('[Esse ângulo não é um Ângulo Notável.]')
            cos = float(input('Valor do cosseno de {alp}:'.format(alp=alp)))
            cosw = 0

        if cosw == 0:
            c = (a * 2 + b * 2 - 2 * a * b * cos) ** (1 / 2)
            cw = a * 2 + b * 2 - 2 * a * b * cos
            print('O outro lado terá comprimento de:')
            print('    C = ', c)
            print('.')
            print('[raiz quadrada de ', cw, ' ]')
        else:
            c1 = (a * 2 + b * 2)
            c2 = -2 * a * b
            print('O outro lado terá comprimento de:')
            print('.')
            print('C = raiz quadrada de ', c1, c2, c3)

# Módulo - Info Caracteres:
if modulo == 9:
    print('.')
    fr1 = str(input('Digite a frase: '))
    fr2 = fr1.split()
    print('.\n-------------------------------------------\n                 Informações:\n')
    print(Counter(fr2))
    print('.')
    print(Counter(fr1))
    print('.')
    print('Total de palavras: ', len(fr2))
    print('.')
    print('Total de letras: ', len(fr1))
    print('-------------------------------------------')

# Módulo - Conversor de Ângulos:
if modulo == 10:
    m10 = 1
    while m10 == 1:
        print(' ')
        m10a = input('0 - Encerrar programa\n1 - Converter Graus --> Radianos\n2 - Converter Radianos --> Graus\n :')
        if m10a == '1':
            ag4 = int(input('\nSelecione o ângulo em Graus\n:'))
            agi = ag4
            if ag4 > 360:
                ag4 = ag4 % 360
                if ag4 == 0:
                    ag4 = 360
            agd2 = ag4 % 2
            agd3 = ag4 % 3
            agd5 = ag4 % 5
            agd = 180
            agda = agd % 2
            agdb = agd % 3
            agdc = agd % 5
            while agd2 == 0 and agda == 0:
                ag4 = ag4 / 2
                agd2 = ag4 % 2
                agd = agd / 2
                agda = agd % 2
            while agd3 == 0 and agdb == 0:
                ag4 = ag4 / 3
                agd3 = ag4 % 3
                agd = agd / 3
                agdb = agd % 3
            while agd5 == 0 and agdc == 0:
                ag4 = ag4 / 5
                agd5 = ag4 % 5
                agd = agd / 5
                agdc = agd % 5
            if agd == 1 and ag4 == 1:
                print('\n O resultado de ', agi, ' graus em radianos é:\n\n    π')
            elif ag4 == 1 and agd != 1:
                print('\n O resultado de ', agi, ' graus em radianos é:\n\n    π\n----------\n  ', agd)
                print('\n______________________________')
            else:
                print('\n O resultado de ', agi, ' graus em radianos é:\n\n  ', ag4, 'π\n-----------\n  ', agd)
                print('\n______________________________')
        elif m10a == '2':
            arn = int(input('\nSelecione o ângulo em radianos:\n  π . '))
            ard = int(input('\nSelecione o ângulo em radianos:\n  π . {a}\n---------\n    '.format(a=arn)))
            while ard == 0:
                print('\n [Você nao pode dividir algo por 0.]\n')
                ard = int(input('Selecione o ângulo em radianos:\n π . ', ar1, '\n---------\n    '))
            ar1 = 180 * arn
            agd2 = ar1 % 2
            agd3 = ar1 % 3
            agd5 = ar1 % 5
            agda = ard % 2
            agdb = ard % 3
            agdc = ard % 5
            while agd2 == 0 and agda == 0:
                ar1 = ar1 / 2
                agd2 = ar1 % 2
                ard = ard / 2
                agda = ard % 2
            while agd3 == 0 and agdb == 0:
                ar1 = ar1 / 3
                agd3 = ar1 % 3
                ard = ard / 3
                agdb = ard % 3
            while agd5 == 0 and agdc == 0:
                ar1 = ar1 / 5
                agd5 = ar1 % 5
                ard = ard / 5
                agdc = ard % 5

            print('\n O resultado de tal angulo em graus é:\n\n')
            if ard == 1:
                if ar1 > 360:
                    ar1 = ar1 % 360
                    if ar1 == 0:
                        ar1 = 360
                print(' ', ar1, '°\n')
            else:
                print(' ', ar1, '     graus\n---------\n  ', ard, '\n')


        elif m10a == '0':
            m10 = 0
            print('\nEncerrado.')
        else:
            print('\nCaractere inválido, tente novamente.\n')

# Módulo - Girar dado:
if modulo == 11:
    a = input(
        '\nSelecione o seu dado:\n 1 - Moeda\n 2 - Dado de 3 faces\n 3 - Dado de 6 faces\n 4 - Dado de 12 faces\n 5 - Dado de 25 faces\n 6 - Dado de 50 faces\n 7 - Dado de 100 faces\n :')
    while a == '1':
        a1 = randint(1, 2)
        b = input('\nPressione Enter para girar.\n[Ou selecione 0 para encerrar]\n')
        if b != '0':
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nVocê jogou a moeda e caiu:')
        if b == '0':
            a = 0
            print('\n\nEncerrado.')
        if a1 == 1 and b != '0':
            print('          Cara')
        if a1 == 2 and b != '0':
            print('          Coroa')
    while a == '2' or a == '3' or a == '4' or a == '5' or a == '6' or a == '7':
        if a == '2':
            a1 = randint(1, 3)
        if a == '3':
            a1 = randint(1, 6)
        if a == '4':
            a1 = randint(1, 12)
        if a == '5':
            a1 = randint(1, 25)
        if a == '6':
            a1 = randint(1, 50)
        if a == '7':
            a1 = randint(1, 100)
        b = input('\nPressione Enter para girar.\n[Ou selecione 0 para encerrar]\n')
        if b != '0':
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nVocê jogou o dado e caiu:')
            print('           ', a1)
        if b == '0':
            a = 0
            print('\n\nEncerrado.')
    if a != 0 and a != '0' and a != '1' and a != '2' and a != '3' and a != '4' and a != '5' and a != '6' and a != '7':
        print('\nCaractere inválido, reinicie o programa.\n')

# Módulo - Conversor de Moedas:
if modulo == 12:
    a = input('\nSelecione a moeda base\n 1 - Real\n 2 - Dólar\n :')
    if a == '1':
        mb = 'Reais'
    if a == '2':
        mb = 'Dólares'
    mc = input('\nSelecione a moeda que será convertida\n :')
    mc = mc.capitalize()
    vl = float(input('\nSelecione o valor de 1 {mc} hoje (em {mb})\n :'.format(mc=mc, mb=mb)))

    print('\n[Digite 0 para encerrar o programa]')
    md12 = 1
    while md12 == 1:
        c = float(input('\n_______________\n{mc} ---> '.format(mc=mc)))
        if c == 0:
            md12 = 0
            print('\n\nEncerrado.')
        if c != 0:
            res = c * vl
            res = round(res, 2)
            print(' {c} {mc} = {res} {mb}'.format(c=c, mc=mc, res=res, mb=mb))

#Módulo - Gerador de Matriz:
if modulo == 13:
    run = 1
    while run == 1:
        mod = input("\nSelecione o tipo de matriz que você quer gerar:\n 0 - Encerrar programa \n 1 - Geração de Lei de Formação \n 2 - Matriz 2x2 \n 3 - Matriz 2x3 \n 4 - Matriz 3x2 \n 5 - Matriz 3x3 \n 6 - Matriz 3x4 \n 7 - Matriz 4x3 \n : ")
        if mod == '0':
            run = 0
            print('\nEncerrado.')
        while mod == '1':
            a = randint(-5, 5)
            while a == 0:
                a = randint(-5, 5)
            sinal = randint(1, 2)
            b = randint(1, 5)
            while b == 0:
                b = randint(-5, 5)
            if sinal == 1:
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nA Lei de Formação gerada foi:   {a}i + {b}j'.format(a=a, b=b))
            if sinal == 2:
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nA Lei de Formação gerada foi:   {a}i - {b}j'.format(a=a, b=b))
                b = b * (-1)
            msg = input('\n [Gerar outra lei de formação = Pressione enter.]\n [Montar matriz 2x2: digite "2x2".]\n [Montar matriz 3x3: digite "3x3".]\n [Voltar ao menu: pressione 0.]\n [Encerrar programa: digite "end".]\n : ')
            if msg == '2x2':
                a11 = a * 1 + b * 1
                a12 = a * 1 + b * 2
                a21 = a * 2 + b * 1
                a22 = a * 2 + b * 2
                b = b * (-1)
                print('\n\n\nA geração de {a}i - {b}j é:\n'.format(a=a, b=b))
                print('   {a11}     {a12}'.format(a11=a11, a12=a12))
                a = input('   {a21}     {a22}\n\n'.format(a21=a21, a22=a22))
            if msg == '3x3':
                a11 = a * 1 + b * 1
                a12 = a * 1 + b * 2
                a13 = a * 1 + b * 3
                a21 = a * 2 + b * 1
                a22 = a * 2 + b * 2
                a23 = a * 2 + b * 3
                a31 = a * 3 + b * 1
                a32 = a * 3 + b * 2
                a33 = a * 3 + b * 3
                b = b * (-1)
                print('\n\n\nA geração de {a}i - {b}j é:\n'.format(a=a, b=b))
                print('   {a11}     {a12}     {a13}'.format(a11=a11, a12=a12, a13=a13))
                print('   {a21}     {a22}     {a23}'.format(a21=a21, a22=a22, a23=a23))
                a = input('   {a31}     {a32}     {a33}\n\n'.format(a31=a31, a32=a32, a33=a33))
            if msg == '0':
                mod = 0
            if msg == 'end':
                mod = 0
                run = 0
                print('\nEncerrado.')
        while mod == '2':
            a11 = randint(-20, 20)
            a12 = randint(-20, 20)
            a21 = randint(-20, 20)
            a22 = randint(-20, 20)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nA Matriz gerada foi:\n')
            print('   {a11}     {a12}'.format(a11=a11, a12=a12))
            print('   {a21}     {a22}'.format(a21=a21, a22=a22))
            msg = input(
                '\n [Gerar outra matriz: Qualquer dígito]\n [Mostrar derteminante: digite "det".]\n [Voltar ao menu: pressione 0.]\n [Encerrar programa: digite "end".]\n : ')
            if msg == 'det':
                det = a11 * a22 - a21 * a12
                a = input('\nO derteminante dessa matriz é: {det}\n'.format(det=det))
            if msg == '0':
                mod = 0
            if msg == 'end':
                mod = 0
                run = 0
                print('\nEncerrado.')
        while mod == '3':
            a11 = randint(-20, 20)
            a12 = randint(-20, 20)
            a13 = randint(-20, 20)
            a21 = randint(-20, 20)
            a22 = randint(-20, 20)
            a23 = randint(-20, 20)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nA Matriz gerada foi:\n')
            print('   {a11}     {a12}     {a13}'.format(a11=a11, a12=a12, a13=a13))
            print('   {a21}     {a22}     {a23}'.format(a21=a21, a22=a22, a23=a23))
            msg = input(
                '\n [Gerar outra matriz: Qualquer dígito]\n [Voltar ao menu: pressione 0.]\n [Encerrar programa: digite "end".]\n : ')
            if msg == 'det':
                a = input('\nNão é possível descobrir o derteminante de uma matriz 2x3.\n')
            if msg == '0':
                mod = 0
            if msg == 'end':
                mod = 0
                run = 0
                print('\nEncerrado.')
        while mod == '4':
            a11 = randint(-20, 20)
            a12 = randint(-20, 20)
            a21 = randint(-20, 20)
            a22 = randint(-20, 20)
            a31 = randint(-20, 20)
            a32 = randint(-20, 20)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nA Matriz gerada foi:\n')
            print('   {a11}     {a12}'.format(a11=a11, a12=a12))
            print('   {a21}     {a22}'.format(a21=a21, a22=a22))
            print('   {a31}     {a32}'.format(a31=a31, a32=a32))
            msg = input(
                '\n [Gerar outra matriz: Qualquer dígito]\n [Voltar ao menu: pressione 0.]\n [Encerrar programa: digite "end".]\n : ')
            if msg == 'det':
                a = input('\nNão é possível descobrir o derteminante de uma matriz 3x2.\n')
            if msg == '0':
                mod = 0
            if msg == 'end':
                mod = 0
                run = 0
                print('\nEncerrado.')
        while mod == '5':
            a11 = randint(-20, 20)
            a12 = randint(-20, 20)
            a13 = randint(-20, 20)
            a21 = randint(-20, 20)
            a22 = randint(-20, 20)
            a23 = randint(-20, 20)
            a31 = randint(-20, 20)
            a32 = randint(-20, 20)
            a33 = randint(-20, 20)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nA Matriz gerada foi:\n')
            print('   {a11}     {a12}     {a13}'.format(a11=a11, a12=a12, a13=a13))
            print('   {a21}     {a22}     {a23}'.format(a21=a21, a22=a22, a23=a23))
            print('   {a31}     {a32}     {a33}'.format(a31=a31, a32=a32, a33=a33))
            msg = input(
                '\n [Gerar outra matriz: Qualquer dígito]\n [Mostrar derteminante: digite "det".]\n [Voltar ao menu: pressione 0.]\n [Encerrar programa: digite "end".]\n : ')
            if msg == 'det':
                det = (a11 * a22 * a33 + a12 * a23 * a31 + a13 * a21 * a32) - (a31 * a22 * a13 + a32 * a23 * a11 + a33 * a21 * a12)
                a = input('\nO derteminante dessa matriz é: {det}\n'.format(det=det))
            if msg == '0':
                mod = 0
            if msg == 'end':
                mod = 0
                run = 0
                print('\nEncerrado.')
        while mod == '6':
            a11 = randint(-20, 20)
            a12 = randint(-20, 20)
            a13 = randint(-20, 20)
            a14 = randint(-20, 20)
            a21 = randint(-20, 20)
            a22 = randint(-20, 20)
            a23 = randint(-20, 20)
            a24 = randint(-20, 20)
            a31 = randint(-20, 20)
            a32 = randint(-20, 20)
            a33 = randint(-20, 20)
            a34 = randint(-20, 20)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nA Matriz gerada foi:\n')
            print('   {a11}     {a12}     {a13}     {a14}'.format(a11=a11, a12=a12, a13=a13, a14=a14))
            print('   {a21}     {a22}     {a23}     {a24}'.format(a21=a21, a22=a22, a23=a23, a24=a24))
            print('   {a31}     {a32}     {a33}     {a34}'.format(a31=a31, a32=a32, a33=a33, a34=a34))
            msg = input(
                '\n [Gerar outra matriz: Qualquer dígito]\n [Voltar ao menu: pressione 0.]\n [Encerrar programa: digite "end".]\n : ')
            if msg == 'det':
                a = input('\nNão é possível descobrir o derteminante de uma matriz 3x4.\n')
            if msg == '0':
                mod = 0
            if msg == 'end':
                mod = 0
                run = 0
                print(end)
        while mod == '7':
            a11 = randint(-20, 20)
            a12 = randint(-20, 20)
            a13 = randint(-20, 20)
            a21 = randint(-20, 20)
            a22 = randint(-20, 20)
            a23 = randint(-20, 20)
            a31 = randint(-20, 20)
            a32 = randint(-20, 20)
            a33 = randint(-20, 20)
            a41 = randint(-20, 20)
            a42 = randint(-20, 20)
            a43 = randint(-20, 20)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nA Matriz gerada foi:\n')
            print('   {a11}     {a12}     {a13}'.format(a11=a11, a12=a12, a13=a13))
            print('   {a21}     {a22}     {a23}'.format(a21=a21, a22=a22, a23=a23))
            print('   {a31}     {a32}     {a33}'.format(a31=a31, a32=a32, a33=a33))
            print('   {a41}     {a42}     {a43}'.format(a41=a41, a42=a42, a43=a43))
            msg = input(
                '\n [Gerar outra matriz: Qualquer dígito]\n [Voltar ao menu: pressione 0.]\n [Encerrar programa: digite "end".]\n : ')
            if msg == 'det':
                a = input('\nNão é possível descobrir o derteminante de uma matriz 4x3.\n')
            if msg == '0':
                mod = 0
            if msg == 'end':
                mod = 0
                run = 0
                print(end)
        if mod != 0 and mod != '0' and mod != '1' and mod != '2' and mod != '3' and mod != '4' and mod != '5' and mod != '6' and mod != '7':
            a = input('\n\n[Você inseriu um dígito inválido.]\n[Tente novamente.]\n\n')

# Módulo - Calculadora de Derteminante:
if modulo == 14:
    run = 1
    while run == 1:
        mod = input('\nSelecione o tamanho da matriz:\n 0 - Encerrar programa\n 1 - Matriz 2x2\n 2 - Matriz 3x3\n 3 - Matriz 4x4\n : ')
        if mod == '0':
            run = 0
            print('\nEncerrado.')
        elif mod == '1':
            a11 = float(input('\nValor de a11: '))
            a12 = float(input('\nValor de a12: '))
            a21 = float(input('\nValor de a21: '))
            a22 = float(input('\nValor de a22: '))
            det = a11*a22-a21*a12
            a = input('\nO derteminante da matriz selecionada foi de:\n ---> {det}\n[Pressione qualquer dígito para continuar]\n'.format(det=det))
        elif mod == '2':
            a11 = float(input('\nValor de a11: '))
            a12 = float(input('\nValor de a12: '))
            a13 = float(input('\nValor de a13: '))
            a21 = float(input('\nValor de a21: '))
            a22 = float(input('\nValor de a22: '))
            a23 = float(input('\nValor de a23: '))
            a31 = float(input('\nValor de a31: '))
            a32 = float(input('\nValor de a32: '))
            a33 = float(input('\nValor de a33: '))
            det = a11*a22*a33+a12*a23*a31+a13*a21*a32-(a31*a22*a13+a32*a23*a11+a33*a21*a12)
            a = input('\nO derteminante da matriz selecionada foi de:\n ---> {det}\n[Pressione qualquer dígito para continuar]\n'.format(det=det))
        elif mod == '3':
            a11 = float(input('\nValor de a11: '))
            a12 = float(input('\nValor de a12 '))
            a13 = float(input('\nValor de a13: '))
            a14 = float(input('\nValor de a14: '))
            a21 = float(input('\nValor de a21: '))
            a22 = float(input('\nValor de a22: '))
            a23 = float(input('\nValor de a23: '))
            a24 = float(input('\nValor de a24: '))
            a31 = float(input('\nValor de a31: '))
            a32 = float(input('\nValor de a32: '))
            a33 = float(input('\nValor de a33: '))
            a34 = float(input('\nValor de a34: '))
            a41 = float(input('\nValor de a41: '))
            a42 = float(input('\nValor de a42: '))
            a43 = float(input('\nValor de a43: '))
            a44 = float(input('\nValor de a44: '))
            det = a11*a22*a33*a44-a11*a22*a34*a43-a11*a23*a32*a44+a11*a23*a34*a42+a11*a24*a32*a43-a11*a24*a33*a42-a12*a21*a33*a44+a12*a21*a34*a43+a12*a23*a31*a44-a12*a23*a34*a41-a12*a24*a31*a43+a12*a24*a33*a41+a13*a21*a32*a44-a13*a21*a34*a42-a13*a22*a31*a44+a13*a22*a34*a41+a13*a24*a31*a42-a13*a24*a32*a41-a14*a21*a32*a43+a14*a21*a33*a42+a14*a22*a31*a43-a14*a22*a33*a41-a14*a23*a31*a42+a14*a23*a32*a41
            a = input('\nO derteminante da matriz selecionada foi de:\n ---> {det}\n[Pressione qualquer dígito para continuar]\n'.format(det=det))
        else:
            a = input('\n\n[Você inseriu um dígito inválido.]\n[Tente novamente.]\n\n')

# Módulo - Informações:
if modulo == 0:
    md = 1
    while md == 1:
        print(' ')
        print('Instagram: @matheusalmcn | Twitter: @Bismilla | Discord: Berd#0033\nPrograma criado em: 1 de julho de 2022.')
        print('Atualizações (Patchs):')
        print('  0 - Encerrar programa')
        print('  1 - Links')
        print('  2 - Versão 0.8')
        print('  3 - Versão 0.9')
        print('  4 - Versão 1.0')
        print('  5 - Versão 1.1')
        print(' ')
        patches = 5
        att = int(input(': '))
        if att >= (patches + 1) or att < 0:
            print('.\n [O Patch Note ', att, ' não está disponível.]\n.')

        if att == 0:
            md = 0
            print('\nEncerrado.')
        if att == 1:
            print('\n[Links indisponíveis.]')
        if att == 2:
            print(
                '\nAtualização V:0.8:\n  Adicionado Módulo 0 - "Informações"\n  Reparação do Módulo 4 - "Médias":\n    Adicionado Média Aritmética\n    Adicionado Média Geométrica\n    Adicionado Média Harmônica\n    Adicionado Média Ponderada\n  Data: 12/06/22\n')
        if att == 3:
            print(
                '\nAtualização V:0.9:\n  Reformulação do layout do menu\n  Correção de bugs\n  Adicionado Módulo 9 - "Info caracteres"\n  Data: 27/10/22\n')
        if att == 4:
            print(
                '\nAtualização V:1.0:\n  Adicionado módulo 10 - "Conversor de ângulos"\n  Atualização no while do módulo 1 - "Fatoração"\n  Adicionado módulo 11 - "Girar dado"\n  Adicionado módulo 12 - "Conversor de moedas"\n  Data:18/02/23\n')
        if att == 5:
            print(
                '\nAtualização V:1.1:\n  Lançamento do log2u no GitHub\n  Adicionado Módulo 13 - "Gerador de matriz"\n  Adicionado Módulo 14 - "Calculadora de derteminante"\n  Reformulação do layout "Home"\n  Data: 21/02/23\n')
        if att != 0:
            b = input(' ')

# UwU?:
if modulo == 69:
    x = 0
    xa = ['UwU']
    xc = 0
    while xc <= 0:
        x = x + 1
        xa = xa * x
        print(xa)
        print(xa)
        print(xa)
        xa = ['UwU']
        if x == 6:
            xc = xc + 1
            xa = ['UwU']
        while xc >= 1:
            x = x - 1
            xa = xa * x
            print(xa)
            print(xa)
            print(xa)
            xa = ['UwU']
            if x == 1:
                xc = xc - 1
                xa = ['UwU']

# MODO DESENVOLVEDOR:
if modulo == 99:
    today1 = datetime.date.today()
    today2 = datetime.time()
    print('.')
    print('MODO DESENVOLVEDOR ATIVADO')
    print(today1, ' - ', today1.ctime())

    desnv = 1
    while desnv == 1:
        teste = input(': ')

# LICENÇA:
#
# Não era para você estar aqui, entretanto, como sua curiosidade fala mais alto, fique ciente:
# Favor não alterar nenhuma informação do código. Foram meses de trabalho, ideias e correção de bugs. Espero que compreenda.
# Não finja ser o dono desse programa sem ter gastado uma gota de suor em todo esse esforço. Seja ético, pense no outro lado.
# Este programa foi criado com o intuito de ajudar a todos. Desejo muito que minha dedicação quanto a isso tenha valido a pena.
# Novas ideias sempre são bem-vindas. Saiba que você está livre em entrar em contato comigo. Lista de contato abaixo.
# Discord: Berd#0033 | Twitter: @Bismilla__ | Instagram: @matheusalmcn
# "Ainda vem muito pela frente..."
#
# Matheus Almeida @ 2023
