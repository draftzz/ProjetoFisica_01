from math import *

#Constantes
h = 6.6260 * 10**-34 #Constante de Planck em [J*s]
h2 = 4.136 * 10 **-15 #Constande de Planck em [eV*s]
e = 1.6021 * 10**-19 #Carga elementar/Módulo da carga do elétron em [C]
mc = 9.1093 * 10**-31 #Massa do elétron em [Kg]
R = 1.0973 * 10**7 #Constante de Rydberg em [m ^-1]
c = 3 * 10**8 #Velocidade da luz em [m/s]
e0 = 8.8541 * 10**-12 #Constante Elétrica em [C^2 / N*m^2]
a0 = 5.2917 * 10**-11 #Raio de Bohr em [m]

#Entra com comprimento de onda/frequência e retorna a energia do fóton
def energiaFoton():
    print()
    #Dá as duas opções de entrada para o usuário
    print("1 - Entrar com comprimento de onda")
    print("2 - Entrar com frequência")
    entrada = int(input("Opção de entrada: "))
    print()

    if entrada == 1: #Caso o usuário entre com o comprimento de onda
        comprimentoOnda = float(input("Comprimento de onda [m/s]: "))
        E = (h2*c)/comprimentoOnda
        print()
        #Formatação para sair com a Energia em [eV] e [J] // format() para sair em notação científica
        print("Energia do fóton é " + format(E,'.3E') + " eV")
        print("Energia do fóton é " + format(E*1.6*10**-19,'.3E') + " J")

    elif entrada == 2: #Caso o usuário entre com a frequência
        frequencia = float(input("Frequência [Hz]: "))
        E = h2*frequencia
        print()
        #Formatação para sair com Energia em [eV] e [J] // format() para sair em notação científica
        print("Energia do fóton é " + format(E,'.3E') + " eV")
        print("Energia do fóton é " + format(E*1.6*10**-19,'.3E') + " J")

#Entra com o número quântico e retorna 1)raio da órbita, 2)velocidade do elétron, 3)energia cinética, 4)energia potencial, 5)energia total e
#6)comprimento de onda
def numeroQuantico():
    numQuantico = int(input("Digite o número quântico: "))
    print()

    #1) Raio da órbita
    raioOrbita = numQuantico**2 *a0
    raioOrbita = raioOrbita * 10**9 #Transforma de [m] para [nm]
    print("O raio da órbita do elétron no átomo de hidrogênio é " + format(raioOrbita, '.3E') + " nm")

    #2) Velocidade orbital
    velocidadeOrbital = (numQuantico*h)/(2*pi*mc*raioOrbita*10**-9)
    print("A velocidade do elétron na órbita %d é " %numQuantico + format(velocidadeOrbital, '.3E') + " m/s")

    #3)Energia cinética
    energiaCinetica = 13.6/(numQuantico**2)
    print("A energia cinética do elétron é " + format(energiaCinetica, '.3E') + " eV")

    #4) Energia potencial
    energiaPotencial = -27.2/(numQuantico**2)
    print("A energia potencial do elétron é " + format(energiaPotencial, ".3E") + " eV")

    #5) Energia total
    energiaTotal = energiaCinetica + energiaPotencial
    print("A energia total do elétron é " + format(energiaTotal, '.3E') + " eV")

    #6) Comprimento de onda de De Broglie
    comprimentoOnda = h/(mc * velocidadeOrbital)
    comprimentoOnda = comprimentoOnda * 10**9 #Transforma de [m] para [nm]
    print("O comprimento de onda de De Broglie é " + format(comprimentoOnda, '.3E') + " nm")

# entra com os números quânticos inicial e final da transição do elétron no átomo de hidrogênio e retorna o comprimento de onda e
# a frequência do fóton emitido ou absorvido. Informa também o tipo do fóton, se absorvido ou emitido.
def absorcaoEmissao():
    numQuanticoini = int(input("Digite o número quântico inicial: "))
    print()
    numQuanticofin = int(input("Digite o número quântico final: "))
    print()

    comprimentoonda = 1/(R*((1/(numQuanticofin**2))-(1/(numQuanticoini**2))))
    comprimentoonda = comprimentoonda * 10**9 #Transforma de [m] para [nm]
    if comprimentoonda < 0 :
        comprimentoonda = comprimentoonda * (-1)
    energiafoton = ((h*c)/comprimentoonda)
    freqFoton = (energiafoton/h)
    print("Comprimento da onda é: " + format(comprimentoonda, '3E')+ "nm")
    print("A frequência do Fóton é: " + format(freqFoton, '3E')+ "Hz")
    if numQuanticoini > numQuanticofin:
        print("O Fóton foi emitido!")
    elif numQuanticofin > numQuanticoini:
        print("O Fóton foi absorvido!")

#entra com o nuymero quantico inicial e retorna o numero quantico final, o comprimento da onda e frequencia na transicao, e a cor do foton.
def espectroemissao():
    ni = int(input("Digite o número quântico inicial: "))

    print("número quântico final para a série de Lyman: nf = 1")
    print("número quântico final para a série de Balmer: nf = 2")
    print("número quântico final para a série de Paschen: nf = 3")
    print("número quântico final para a série de Brackett: nf = 4")
    print("número quântico final para a série de Pfund: nf = 5")

    if 1<ni<5 :
        compronda1 = 1/(R*((1/(1**2))-(1/(ni**2))))
        compronda1T = compronda1 * 10**9 #Transforma de [m] para [nm]
        efoton1 =  ((h*c)/compronda1T)
        freqfoton1 = (efoton1/h)
        if compronda1T < 0:
            compronda1T = compronda1T * (-1)
        
        if compronda1 < 656.3:
            cor1 = "Ultravioleta"
        elif compronda1  > 656.3:
            cor1 = "infravermelho"

        print("Usando a série de Lyman:")
        print("O Fóton é: ", cor1)
        print("O comprimento da onda: "+ format(compronda1T, '3E')+ "nm")
        print("A frequência do Fóton: "+ format(freqfoton1, '3E')+ "Hz")
    elif 2<ni<6 :
        compronda2 = 1/(R*((1/(2**2))-(1/(ni**2))))
        compronda2T = compronda2 * 10**9 #Transforma de [m] para [nm]
        efoton2 =  ((h*c)/compronda2T)
        freqfoton2 = (efoton2/h)
        if compronda2T < 0:
            compronda2T = compronda2T * (-1)
        
        if compronda2 < 656.3:
            cor2 = "Ultravioleta"
        elif compronda2  > 656.3:
            cor2 = "infravermelho"

        print("Usando a série de Balmer:")
        print("O Fóton é: ", cor2) 
        print("O comprimento da onda: "+ format(compronda2T, '3E')+ "nm")
        print("A frequência do Fóton: "+ format(freqfoton2, '3E')+ "Hz")
    elif 3<ni<7 :
        compronda3 = 1/(R*((1/(3**2))-(1/(ni**2))))
        compronda3T = compronda3 * 10**9 #Transforma de [m] para [nm]
        efoton3 =  ((h*c)/compronda3T)
        freqfoton3 = (efoton3/h)
        if compronda3T < 0:
            compronda3T = compronda3T * (-1)
        
        if compronda3 < 656.3:
            cor3 = "Ultravioleta"
        elif compronda3  > 656.3:
            cor3 = "infravermelho"

        print("Usando a série de Paschen:")
        print("O Fóton é: ", cor3)
        print("O comprimento da onda: "+ format(compronda3T, '3E')+ "nm")
        print("A frequência do Fóton: "+ format(freqfoton3, '3E')+ "Hz")
    elif 4<ni<8 :
        compronda4 = 1/(R*((1/(4**2))-(1/(ni**2))))
        compronda4T = compronda4 * 10**9 #Transforma de [m] para [nm]
        efoton4 =  ((h*c)/compronda4T)
        freqfoton4 = (efoton4/h)
        if compronda4T < 0:
            compronda4T = compronda4T * (-1)
        
        if compronda4 < 656.3:
            cor4 = "Ultravioleta"
        elif compronda4  > 656.3:
            cor4 = "infravermelho"

        print("Usando a série de Brackett:")
        print("O Fóton é: ", cor4)
        print("O comprimento da onda: "+ format(compronda4T, '3E')+ "nm")
        print("A frequência do Fóton: "+ format(freqfoton4, '3E')+ "Hz")
    elif 5<ni :
        compronda5 = 1/(R*((1/(5**2))-(1/(ni**2))))
        compronda5T = compronda5 * 10**9 #Transforma de [m] para [nm]
        efoton5 =  ((h*c)/compronda5T)
        freqfoton5 = (efoton5/h)
        if compronda5T < 0:
            compronda5T = compronda5T * (-1)
        
        if compronda5 < 656.3:
            cor5 = "Ultravioleta"
        elif compronda5  > 656.3:
            cor5 = "infravermelho"

        print("Usando a série de Pfund:")
        print("O Fóton é: ", cor5)
        print("O comprimento da onda: "+ format(compronda5T, '3E')+ "nm")
        print("A frequência do Fóton: "+ format(freqfoton5, '3E')+ "Hz")    
   
     

#Menu
def menu():
    while True:
        print()
        print("Menu:")
        print("1 - Energia do Fóton")
        print("2 - Entrar com o valor do número quântico (n)")
        print("3 - Entrar com os números quânticos inicial e final da transição do elétron")
        print("4 - Entrar com o número quântico inicial para receber o espectro de emissão do átomo")
        print("0 - Sair")
        print()

        entrada = int(input("Opção: "))

        if entrada == 1: #Caso deseje realizar a operação 1, é chamada a função abaixo
            energiaFoton()

        if entrada == 2: #Caso deseje realizar a operação 2, é chamada a função abaixo
            numeroQuantico()
        
        if entrada == 3:  #Caso deseje realizar a operação 3, é chamada a função abaixo
            absorcaoEmissao()

        if entrada == 4:  #Caso deseje realizar a operação 4, é chamada a função abaixo
            espectroemissao()

        if entrada == 0:
            break

menu()