def generar_numeros():
    "Genera una lista de números entre 10 y 55, pares, que no sean 16 ni múltiplos de 3."
    numeros = []
    for i in range(10, 55):
        if i % 2 == 0 and i != 16 and i % 3 != 0:
            numeros.append(i)
    return numeros

def fibonacci(num):
    "Determina si un número es parte de la serie de fibonacci."
    a, b = 0, 1
    while b <= num:
        if b == num:
            return True
        a, b = b, a + b
    return False

def imprime_numeros_con_fibonacci(numeros):
    "Imprime los números del vector con la indicación si cumplen con la serie de fibonacci."
    for num in numeros:
        if fibonacci(num):
            print(f"{num}  Cumple con la serie de fibonacci")
        else:
            print(f"{num}  No cumple con la serie de fibonacci")
def main():
    numeros = [8,10,55,45,38]
    imprime_numeros_con_fibonacci(numeros)

if __name__ == "__main__":
    main()

