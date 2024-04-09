def calcular_IMC():
    peso = float(input("Qual é o seu peso?"))
    altura = float(input("Qual é a sua altura?"))

    imc = peso/(altura * altura)
    print("O seu IMC é:", imc)
calcular_IMC()
def menssagem_agredecimento():
    print("Obrigado(a) por usar a calculadora de IMC.")
menssagem_agredecimento()
