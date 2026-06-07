# ft(T) = a * (T − Tideal)^2 + 1
# fu(U) = 1 + b * log10(U+1)
# fo(O) = e ** (c * O)
# fl(t) = 1 + g * t
# fr(t) = e ** (d * t)

# MODELO FINAL
# N(t) = N0 * e**(-k * ft * fu * fo * fr * fl * t)



# importação de biblioteca
import math

# PARÂMETROS


# Sensibilidade à temperatura
a = 0.05  
# Sensibilidade à umidade     
b =0.20
# Intensidade da oxidação 
c =0.10
# Intensidade do efeito da radiação
d =0.010 
# Intensidade do efeito da luz
g = 0.0002
# Taxa básica de degradação 
k = 0.010 
Tideal = 12

# PARÂMETROS PARA NORA
dNora = 0.002
gNora = 0

def menu():
    print("\n===== MENU =====")
    print("1 - Calcular Nutrientes preservados")
    print("2 - Comparar com e sem NORA")
    print("3 - Sair")
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

                N0, t, T, U, O = dados

                resposta = input("Utiliza a proteção NORA? (s/n): ").lower()

                usaNora = resposta == "s"

                resultado = nutrientesPreservados(N0, t, T, U, O, usaNora)

                print(f"\nNutrientes preservados: {resultado:.2f}")

        case 2:
            dados = inserirDados()
            if dados != None:

                N0, t, T, U, O = dados

                resultadoSemNora = nutrientesPreservados(N0, t, T, U, O, False)
                resultadoComNora = nutrientesPreservados(N0, t, T, U, O, True)

                diferenca = resultadoComNora - resultadoSemNora


                print("\n===== COMPARAÇÃO =====")
                print(f"\nNutrientes preservados sem NORA: {resultadoSemNora:.2f}")
                print(f"Nutrientes preservados com NORA: {resultadoComNora:.2f}")
                print(f"\nDiferença: {diferenca:.2f}")

        case 3:
            print("Encerrando o programa.")
            break

        case _:
            print("Opção inválida. Por favor, escolha uma opção válida.") 


                