def gauss(A, b):
    n = len(A)

    for k in range(n - 1):
        # pivoteamento: traz pra cima a linha com o maior valor da coluna
        maior = k
        for i in range(k + 1, n):
            if abs(A[i][k]) > abs(A[maior][k]):
                maior = i
        A[k], A[maior] = A[maior], A[k]
        b[k], b[maior] = b[maior], b[k]

        if A[k][k] == 0:
            print("sistema sem solucao unica")
            return None

        # zera os numeros embaixo do pivo
        for i in range(k + 1, n):
            m = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] = A[i][j] - m * A[k][j]
            b[i] = b[i] - m * b[k]

    # resolve de baixo pra cima
    x = [0] * n
    for i in range(n - 1, -1, -1):
        soma = b[i]
        for j in range(i + 1, n):
            soma = soma - A[i][j] * x[j]
        x[i] = soma / A[i][i]
    return x


print(gauss([[3, 2, 4], [1, 1, 2], [4, 3, -2]], [1, 2, 3]))
print(gauss([[0, 8, 2], [3, 5, 2], [6, 2, 8]], [-7, 8, 26]))