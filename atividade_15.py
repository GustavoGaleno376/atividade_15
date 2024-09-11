# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.
num1=int(input("digite um numero"))
num2=int(input("digite um numero"))
operação=str(input("escolha uma operação soma, subtração, multiplicação ou divisão"))

if operação=="soma":
    print (num1+num2)
elif operação=="subtração":
    print (num1-num2)
elif operação == "multiplicação":
    print (num1*num2)
elif operação =="divisão":
    print (num1/num2)
    
