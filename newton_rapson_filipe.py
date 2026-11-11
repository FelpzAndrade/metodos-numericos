import sympy as sp


def preparar(formula):
    expressao = sp.sympify(formula)
    x = sp.symbols('x')
    derivada = sp.diff(expressao, x)
    funcao_numerica = sp.lambdify(x, expressao)
    derivada_numerica = sp.lambdify(x, derivada)
    return funcao_numerica, derivada_numerica



def newton(f, derivada, chute, tolerancia, max_iteracoes):
    x_atual = chute
    iteracao = 0
    erro = 100
    while True:
        if derivada(x_atual) == 0:
            print("f'(x) = 0 em x =", x_atual, "- o método não pode continuar")
            break
        x_novo = x_atual - f(x_atual) / derivada(x_atual)
        iteracao += 1
        if x_novo != 0:
            erro = abs((x_novo - x_atual) / x_novo) * 100
        x_atual = x_novo
        print(iteracao, x_atual, erro)
        if erro < tolerancia or iteracao >= max_iteracoes:
            break

    print("verificação: f(raiz) =", f(x_atual))
    return x_atual


f, derivada = preparar("exp(-x) - x")
raiz = newton(f, derivada, 0, 0.01, 50)
print("raiz:", raiz)