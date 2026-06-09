# INTEGRANTES DO GRUPO
# Amanda Oliveira Lourenço -  RM: 572572
# Gionvanna Lopes Scalzone - RM: 572285
# Nayra Sousa Duarte - RM: 573815
# Paloma do Carmo Dantas - RM: 569995

# Utilizamos uma biblioteca no código (matplotlib) que não foi aplicada em sala de aula,mas estudamos ela para 
# conseguir implementar a funcionalidade de gerar gráficos, conforme solicitado no enunciado. 


import math
import matplotlib.pyplot as plt

# PARÂMETROS
a = 0.01      
b =0.10
c =0.02
d =0.0003 
g = 0.0002 
k = 0.0002
Tideal = 12

# PARÂMETROS com NORA
dNora = 0.00005
gNora = 0

ultimosDados = None
ultimoUsaNora = None

def menu():
    print("\n===== MENU =====")
    print("1 - Calcular Nutrientes preservados")
    print("2 - Comparar com e sem NORA")
    print("3 - Gerar gráfico do último cálculo de nutrientes")
    print("4 - Sair")
    opcao = int(input("Opção: "))
    return opcao

def fatorTemperatura(T):
    return a * (T - Tideal) ** 2 + 1

def fatorUmidade(U):
    return 1 + b * math.log10(U + 1)

def fatorOxigenio(O):
    return math.exp(c * O)

def fatorLuz(t , luzParametro):
    return 1 + (luzParametro * t)

def fatorRadiacao(t, RadiacaoParametro):
    return math.exp(RadiacaoParametro * t)

def nutrientesPreservados(N0, t, T, U, O, usaNora):
        
    if usaNora:
        T = Tideal
        U = 3
        O = 0.4
        RadiacaoParametro = dNora
        luzParametro = gNora
        
    
    else:
        
        RadiacaoParametro = d
        luzParametro = g

    ft = fatorTemperatura(T)
    fu = fatorUmidade(U)
    fo = fatorOxigenio(O)
    fr = fatorRadiacao(t, RadiacaoParametro)
    fl = fatorLuz(t, luzParametro)

    nutrientes = N0 * math.exp(- (k * ft * fu * fo * fr * fl * t))
    
    return nutrientes

def gerarGrafico(N0, T, U, O, usaNora):

    dias = list(range(0, 1093, 10))
    nutrientes = []

    for t in dias:

        nutrientes.append(nutrientesPreservados(N0, t, T, U, O, usaNora))

    label = "Com NORA" if usaNora else "Sem NORA"
    cor = "green" if usaNora else "blue"

    plt.figure(figsize=(10, 6))
    plt.plot(dias, nutrientes, label=label, color=cor)
    plt.title("Preservação de Nutrientes ao Longo do Tempo")
    plt.xlabel("Tempo de armazenamento (dias)")
    plt.ylabel("Quantidade de nutrientes preservados (%)")

    plt.grid(True)
    plt.show()

def inserirDados():

    try:

        N0 = float(input("Quantidade inicial de nutrientes: "))
        t = int(input("Tempo de armazenamento (dias): "))
        T = float(input("Temperatura (°C): "))
        U = float(input("Umidade (%): "))
        O = float(input("Oxigênio Residual: "))

        return N0, t, T, U, O

    except ValueError:
        print("Entrada inválida. Por favor, insira valores numéricos.")
        return None
    
while True:

    opcao = menu()

    match opcao:

        case 1:
            dados = inserirDados()
            if dados != None:

                ultimosDados = dados
                N0, t, T, U, O = dados

                resposta = input("Utiliza a proteção NORA? (s/n): ").lower()
                usaNora = resposta == "s"
                ultimoUsaNora = usaNora

                resultado = nutrientesPreservados(N0, t, T, U, O, usaNora)

                print(f"\nNutrientes preservados: {resultado:.2f}%")

        case 2:
            dados = inserirDados()
            if dados != None:
                N0, t, T, U, O = dados

                resultadoSemNora = nutrientesPreservados(N0, t, T, U, O, False)
                resultadoComNora = nutrientesPreservados(N0, t, T, U, O, True)
                diferenca = resultadoComNora - resultadoSemNora


                print("\n===== COMPARAÇÃO =====")
                print(f"\nNutrientes preservados sem NORA: {resultadoSemNora:.2f}%")
                print(f"Nutrientes preservados com NORA: {resultadoComNora:.2f}%")
                print(f"\nDiferença: {diferenca:.2f}%")
        case 3:

            if ultimosDados != None:
                N0, t, T, U, O = ultimosDados
                gerarGrafico(N0, T, U, O, ultimoUsaNora)
            else:
                print("Nenhum cálculo realizado ainda. Use a opção 1 primeiro.")

        case 4:
            print("Encerrando o programa.")
            break

        case _:
            print("Opção inválida. Por favor, escolha uma opção válida.") 


                