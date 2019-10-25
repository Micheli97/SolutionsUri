valor = int(input())

valor1 = valor

cont100 = 0
cont50 = 0
cont20 = 0
cont10 = 0
cont5 = 0
cont2 = 0
cont1 = 0

cont100 = valor//100
valor = ( valor - cont100*100)

cont50 = valor//50
valor = (valor - cont50*50)

cont20 = valor//20
valor = (valor - cont20*20)

cont10 = valor//10
valor = (valor - cont10*10)

cont5 = valor//5
valor = (valor - cont5*5)

cont2 = valor//2
valor = (valor - cont2*2)

cont1 = valor//1

print(valor1)
print('%d nota(s) de R$ 100,00'%cont100)
print('%d nota(s) de R$ 50,00'%cont50)
print('%d nota(s) de R$ 20,00'%cont20)
print('%d nota(s) de R$ 10,00'%cont10)
print('%d nota(s) de R$ 5,00'%cont5)
print('%d nota(s) de R$ 2,00'%cont2)
print('%d nota(s) de R$ 1,00'%cont1)
