from time import sleep

print('~'*40)
print('CALCULADORA BÁSICA')
print('~'*40)

print('Aqui estão as opções disponíveis para você solicitar:')
print('    [1] SOMA')
print('    [2] MULTIPLICAÇÃO')
print('    [3] DIVISÃO')
print('    [4] SUCESSOR E ANTECESSOR')
print('    [5] ENCERRAR CALCULADORA')
print('=-='*20)

print("\033[91mVocê também pode tirar algumas dúvidas, selecione uma das opções abaixo:\033[0m")
print("\033[91mD1:\033[0m O QUE É SOMA?")
print("\033[91mD2:\033[0m O QUE É FATORIAL?")
print("\033[91mD3:\033[0m O QUE É DIVISÃO?")
print('=-='*20)

while True:
    opcao = input("\033[91m" + "DIGITE O NÚMERO DESEJADO, OU CASO SEJA UMA DÚVIDA DIGITE [" + "\033[93m" + "D + O NÚMERO SOLICITADO, TODOS JUNTOS" + "\033[91m" + "]: " + "\033[0m")

    if opcao.isdigit():  # Verifica se a opção é um número
        opcao = int(opcao)  # Converte para inteiro se for um número
        # Coloque aqui a lógica para as operações matemáticas

    elif opcao.upper().startswith('D'):
        if opcao.upper() == 'D1':
            print('\033[92mEm matemática, somatório ou somatória é a adição de uma sequência de quaisquer tipos de números, chamados parcelas ou somando; o resultado é sua soma ou total\033[0m')
        elif opcao.upper() == 'D2':
            print('\033[92mNa matemática, o fatorial de um número natural n, representado por n!, é o produto de todos os inteiros positivos menores ou iguais a n. A notação n! foi introduzida por Christian Kramp em 1808\033[0m')
        elif opcao.upper() == 'D3':
            print('\033[92mDivisão é a operação matemática inversa da multiplicação. O ato de dividir por algum elemento de um conjunto só faz sentido quando a multiplicação por aquele elemento for uma função bijetora. No anel dos números inteiros a hipótese da bijetividade não é satisfeita para o zero, assim, não se define divisão por zero\033[0m')
    else:
        print('Opção inválida! Por favor, selecione uma opção válida.')

    if opcao == 1:
        numerosomado1 = float(input('Digite o primeiro número: '))
        numerosomado2 = float(input('Digite o segundo número: '))
        soma = numerosomado1 + numerosomado2
        print(f'A SOMA ENTRE {numerosomado1} e {numerosomado2} FICA --> \033[92m{soma}\033[0m')
    
    elif opcao == 2:
        numeromulti1 = float(input('Digite o primeiro número: '))
        numeromulti2 = float(input('Digite o segundo número: '))
        multi = numeromulti1 * numeromulti2
        print(f'A MULTIPLICAÇÃO DE {numeromulti1} e {numeromulti2} FICA --> \033[92m{multi}\033[0m')

    elif opcao == 3:
        numerodivi1 = float(input('Digite o primeiro número: '))
        numerodivi2 = float(input('Digite o segundo número: '))
        divi = numerodivi1 / numerodivi2
        print (f'A DIVISÃO ENTRE {numerodivi1} e {numerodivi2} FICA --> {divi}')

    elif opcao == 4:
        numerosolicitado = int(input('Digite o número para descobrir o seu ANTECESSOR e seu SUCESSOR: '))
        sucessor = numerosolicitado + 1
        antecessor = numerosolicitado - 1
        print (f'SEU NÚMERO SOLICITADO FOI \033[92m{numerosolicitado}\033[0m, LOGO SEU SUCESSOR É \033[92m{sucessor}\033[0m e seu ANTECESSOR É \033[92m{antecessor}\033[0m')
    
    elif opcao == 5:
        print ('SAINDO DA CALCULADORA...')
        sleep (0.5)
        print ('finalizando...')
        sleep (1.0)
        print ('-'*10)
        print ('\033[91mCALCULADORA FINALIZADA, VOLTE SEMPRE!!!\033[0m')
        print ('-'*10)
        break