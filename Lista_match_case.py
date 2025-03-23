#6

semi = input(f"digite uma cor do semáforo:")

match semi:
    case "vermelho":
        print(f'pare!')
    case "amarelo":
        print(f'atenção!')
    case "verde":
        print(f'siga!')
    case _:
        print(f'Opção incorreta')

#7
print(f"vamos fazer uma operação matematica basica!Digte os numeros:")
operacao = input(f"Digite um operador matematico:")
n1 = float(input(f"numero1: "))
n2 = float(input(f'numero2: '))

match operacao:
    case "+":
        print(f'{n1} + {n2} = {n1 + n2}')
    case "-":
        print(f'{n1} - {n2} = {n1 - n2}')
    case "*":
        print(f'{n1} * {n2} = {n1 * n2}')
    case "/":
        print(f'{n1} / {n2} = {n1 / n2}')    
    case _:
        print(f'não foi possivel efetuar a operação')

#8
animal = input(f"Escolah um animal: ")

match animal:
    case "cachorro"|"gato":
        print(f'Mamifero')
    case "cobra"|"largato":
        print(f'Reptil')
    case 'aguia'|"papagaio":
        print(f'Ave')
    case _:
        print(f'animal não encontrado')

#9
personagem = input('escolha um numero entre 1 a 3: ')

match personagem:
    case "1":
        print(f"Você escolheu o Guerreiro!")
    case "2":
        print(f"Você escolheu o Mago!")
    case "3":
        print(f"Você escolheu o Arqueiro!")
    case _:
        print(f"Opção invalida!")

#10

nota = input(f"Digite sua nota de 0 a 10: ")

match nota:
    case "9"|"10":
        print(f"A")
    case "7"|"8":
        print(f"B")
    case "5"|"6":
        print(f"C")
    case "3"|"4":
        print(f"D")
    case "0"|"1"|"2":
        print(f"E")
