#1
nota = float(input("digite sua nota(notas quebradas com .): "))

if nota >= 9:
 print(f'A')
elif nota >=7:
    print(f'B')
elif nota >=5:
   print(f'C')
else:
   print(f'F')

   #2
num = int(input("digite um numero: "))

if num % 2 == 0:

        print(f'numero par!')
else:
        print(f'numero ímpar!')

#3

peso = float(input("digite seu peso: "))
altura = float(input('digite sua altura: '))
imc = (peso / (altura ** 2))
print(f'seu imc é: {imc: .1f}Kg/M^2')

if imc <18.5:
    print(f'Abaixo do peso')

elif 18.5 < imc < 24.9:
    print(f'Peso nomral')

elif 25 < imc < 29.9:
    print(f'Sobrepeso')

else:
    print(f'Obesidade')
    
#4
print(f'coloque numeros para comparar e ver qual é o maior!')
n1 = input(f'digite o num1: ')
n2 = input(f'digite o num2: ')
n3 = input(f'digite o num3: ')

if n1 > n2 and n1 > n3:
    print(f'n 1 é o numero maior')

elif n3 > n1 and n3 > n2:
        print(f'n 3 é o numero maior')

elif n2 > n1 and n2 > n3:
    print(f'n 2 é o numero maior')

else:
    print(f'todos são iguais')

#5

nt1 = float(input(f'nota 1: '))
nt2 = float(input(f'nota 2: '))
nt3 = float(input(f'nota 3: '))

media = (nt1 + nt2 + nt3)/3

print(f'{media:.1f}')

if media >= 6:
    print(f'aprovado')

else:
    print(f'reprovado')
