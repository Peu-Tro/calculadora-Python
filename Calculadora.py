def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

def main():
    print("Calculadora em Python")
    print("----------------------")
    print("Operações disponíveis:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    operacao = input("\nEscolha a operação desejada (1/2/3/4): ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == '1':
        resultado = adicao(num1, num2)
        print(f"\nResultado: {resultado}")
    elif operacao == '2':
        resultado = subtracao(num1, num2)
        print(f"\nResultado: {resultado}")
    elif operacao == '3':
        resultado = multiplicacao(num1, num2)
        print(f"\nResultado: {resultado}")
    elif operacao == '4':
        resultado = divisao(num1, num2)
        print(f"\nResultado: {resultado}")
    else:
        print("Operação inválida. Por favor, escolha uma operação válida (1/2/3/4).")

if __name__ == "__main__":
    main()