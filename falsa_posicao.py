import sympy as sp


def preparar(formula):
   
    formula = formula.replace("^", "**")
    nomes = {"e": sp.E, "ln": sp.log, "sen": sp.sin}
    expressao = sp.sympify(formula, locals=nomes)
    x = sp.symbols('x')
    return sp.lambdify(x, expressao)



def falsa_posicao(f, a, b, tolerancia, max_iteracoes):
    if f(a) * f(b) > 0:
        print("f(a) e f(b) tem o mesmo sinal, nao da pra garantir raiz em [", a, ",", b, "]")
        return None

    x_atual = a
    iteracao = 0
    erro = 100
    while True:
        x_anterior = x_atual
        
        x_atual = (a * f(b) - b * f(a)) / (f(b) - f(a))
        iteracao += 1

        
        if iteracao > 1 and x_atual != 0:
            erro = abs((x_atual - x_anterior) / x_atual) * 100

       
        teste = f(a) * f(x_atual)
        if teste < 0:
            b = x_atual
        elif teste > 0:
            a = x_atual
        else:
            erro = 0

        print(iteracao, x_atual, erro)
        if erro < tolerancia or iteracao >= max_iteracoes:
            break

    print("verificação: f(raiz) =", f(x_atual))
    return x_atual


f = preparar("ln(x) + x - 2")
print("raiz:", falsa_posicao(f, 1, 2, 0.01, 50))

f = preparar("cos(x) - x")
print("raiz:", falsa_posicao(f, 0, 1, 0.01, 50))

f = preparar("e^x - 3*x")
print("raiz:", falsa_posicao(f, 0, 1, 0.01, 50))