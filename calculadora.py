import math
def preparo (exs):
    global ex
    for qq in s:
        exs = exs.replace(f'{qq}', f' {qq} ').strip()
    ex = exs.split()
    for mm, m in enumerate(ex):
        if mm != len(ex) - 1:
            if ex[mm + 1] in '(sct' and m.isnumeric():
                ex.insert(mm + 1, '*')
    return ' '.join(ex)
def erro (a):
    erros = 0
    for e,c in enumerate (a):
        if not c.isnumeric():
            if c.isalpha():
                if c not in 'sct':
                    erros += 1
                    local.append(e)
                else:
                    sct = not a [e-1].isalnum() and a[e+1] == '('
                    if not sct:
                        erros += 1
                        local.append (e)
            elif c not in '+-:*^#!()':
                erros += 1
                local.append (e)
            else:
                if c in '()!':
                    if c == ')':
                        val =  a [e-1].isalnum() or a [e-1] in '!)'
                    elif c == '!':
                        val =  a [e-1].isalnum() or a [e-1] == ')' and not a[e+1].isalnum()
                    else:
                        val = a[e+1].isalnum() or a[e+1] in '-'
                else:
                    val = a [e-1].isalnum() or a [e-1] in ')!-' if c != '-' else ')!-(' and a[e+1].isalnum() or a[e+1] in '-('
                if not val:
                    erros += 1
                    local.append (e)
    return erros
def abrefecha (p):
    conta = contf = erros = 0
    for pos, c in enumerate(p):
        if c == '(':
            conta += 1
        elif c == ')':
            if conta > 0:
                conta -= 1
            else:
                erros += 1
                local.append(pos)
    for c in range (len(p) - 1, -1, -1):
        if p [c] == ')':
            contf += 1
        elif p [c] == '(':
            if contf > 0:
                contf -= 1
            else:
                erros += 1
                local.append(c)
    return erros
def validacao (n):
    exn = n.replace('',' ').split ()
    nerros = erro (exn) + abrefecha (exn)
    if nerros > 0:
        print (f'INVÁLIDO! {nerros} erros encontrados:')
        for e,c in enumerate(exn):
            if (e == len(exn) - 1 or (not c.isalnum() and not exn[e + 1].isalnum() and not exn[e + 1] in '+-:#*^') or
            (c.isalnum() and exn[e + 1].isalnum())):
                sep = ''
            else:
                sep = ' '
            print (f'{'\033[1;31m' if e in local else ''}{c}{'\033[m' if e in local else ''}',end= sep)
    return nerros
def soma (num, num1):
    return num + num1
def sub (num, num1):
    return num - num1
def div (num,num1):
    return num / num1
def mult (num,num1):
    return  num * num1
def pot (num,num1):
    return num ** num1
def rad (num,num1):
    return num ** (1/num1)
def fact (pilha):
    for g, cont4 in enumerate (pilha):
        f = 1
        if '!' in cont4:
            if len (cont4) == 1:
                num = int (float (pilha [g -1]))
                apr = True
            else:
                num = int (float (cont4 [:len (cont4) - 1]))
                apr = False
            for i in range(num, 0, -1):
                f *= i
            if apr:
                pilha [g -1] = str (f)
                pilha.pop (g)
            else:
                pilha [g] = str (f)
def socatoa (pilha):
    parametro = {'s': math.sin, 'c': math.cos , 't': math.tan}
    if 's' in pilha or 'c' in pilha or 't' in pilha:
        for d, cont3 in enumerate(pilha):
            if cont3 in 'sct':
                r = parametro [cont3] (math.radians ((float (pilha [d + 1]))))
                pilha [d] = str (r)
                pilha.pop (d + 1)
def procedimentos (x,y,pilha):
    simbolos = {'+': soma, '-': sub, '*': mult, ':': div, '^': pot, '#': rad}
    if x not in ('^', '#') and y not in ('^','#'):
        cont1 = 0
        while cont1 < len(pilha):
            if pilha[cont1] == x:
                r = simbolos[x](float(pilha[cont1 - 1]), float(pilha[cont1 + 1]))
                pilha[cont1 - 1] = str(r)
                del pilha[cont1: cont1 + 2]
                cont1 -= 1
            elif pilha[cont1] == y:
                r = simbolos[y](float(pilha[cont1 - 1]), float(pilha[cont1 + 1]))
                pilha[cont1 - 1] = str(r)
                del pilha[cont1: cont1 + 2]
                cont1 -= 1
            cont1 += 1
    else:
        cont1 = len (pilha) - 1
        while cont1 >= 0:
            if pilha [cont1] == x:
                r = simbolos [x] (float (pilha[cont1 - 1]),float (pilha[cont1 + 1]))
                pilha[cont1 - 1] = str (r)
                del pilha [cont1: cont1 + 2]
            elif pilha [cont1] == y:
                r = simbolos [y] (float (pilha[cont1 - 1]), float (pilha[cont1 + 1]))
                pilha[cont1 - 1] = str (r)
                del pilha[cont1: cont1 + 2]
            cont1 -= 1
def resolve (expr):
    operadores = [ '!', ['^', '#'], ['*', ':'], ['+', '-']]
    for e, cont in enumerate(expr):
        p = cont.split()
        neg = 0
        pneg = []
        while neg < len (p):
            if p [neg] == '-' and (neg == 0 or p [neg - 1] in s and p [neg - 1] != '!'):
                pneg.append (p [neg] + p[neg + 1])
                neg += 2
            else:
                pneg.append (p[neg])
                neg += 1
        p = pneg
        socatoa (p)
        for grupo in operadores:
            while any(z in p for z in grupo):
                if grupo == '!':
                    fact (p)
                else:
                    procedimentos (grupo [0], grupo [1],p)
        expr [e] = ' '. join (p)
        if e != len (expr) -1:
            if '@' in expr [e + 1]:
                p1 = expr[e + 1].split()
                for b, cont2 in enumerate (p1):
                    if '@' in cont2:
                        p1 [b] = expr [int (cont2 [1:])]
                p1 =' '.join (p1)
                expr [e + 1] = p1
    expr = p
    return expr
def calculo (n):
        parenteses = []
        dentro = ['']
        for c in n:
            if c == '(':
                dentro.append('')
            elif c == ')':
                fechado = dentro.pop()
                parenteses.append(fechado)
                if dentro:
                    dentro[-1] += f"@{len(parenteses) - 1}"
            else:
                dentro [-1] += c
        parenteses.append(dentro[0])
        parenteses = resolve (parenteses)
        return parenteses [0]
while True:
    opc = 0
    while opc < 1 or opc > 2:
        try:
            print (f"""{'\033[1;31m' if opc != 0 else '\033[1m'}1 -> Instruções
2 -> Calculadora\033[m""")
            opc = int(input())
        except ValueError:
            print ('\033[1;31mERRO! TENTE DE NOVO! \033[m')
    if opc == 1:
        print ('-=-'*40)
        print ("""--> CALCULADORA <--
    LEGENDA:
        + = SOMA
        - = SUBTRAÇÃO
        : = DIVISÃO
        * = MULTIPLICAÇÃO
        ^ = POTÊNCIA
        # = RADICIAÇÃO 
        ! = FATORIAL
        s(),c(),t(): SENO, COSSENO, TANGENTE""")
        print ("""    -> Não use [] ou {}, apenas ()
    -> A calculadora segue a ordem de precedência: '()'; 's', 'c' e 't'; '!'; '^', '#'; '*', ':'; '+', '-'
    -> Use () depois de s,c e t
    -> Não use outras letras
    -> O uso de ')(' é interpretado como multiplicação
    -> Números antes de '(' ou 's', 'c' e 't' são interpretados como multiplicações
    -> Código de saída da calculadora: ###""")
        print('-=-' * 40)
    elif opc == 2:
        print ('INICIADO')
        while True:
            ex = input().strip().replace(')(', ') * (').replace(') (', ') * (')
            if ex == '###':
                break
            while True:
                s = ['(', ')','s', 'c', 't','!','^', '#', '*', ':', '+','-']
                local = []
                ex = preparo (ex)
                valido = validacao (ex)
                if valido == 0:
                    try:
                       resultado = calculo(ex)
                       print (resultado)
                    except OverflowError:
                        print ('\033[1;31mERRO! Cálculo fora de escala :(\033[m')
                else:
                    print()
                break