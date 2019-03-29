def a_power_b (a , b):
    prod = 1
    for i in range(0, b):
        prod=prod*a
    print(prod)
    return(prod)

num1=int(input("digite un numero"))
num2=int(input("digite la potencia a elevar el numero"))        
a_power_b(num1,num2)
while True:

    a=int(input("Digite un numero:"))
    if a==0:
        print("numero es cero")
        break
    b=int(input("Digite el numero a elevar:"))
    result=a_power_b(a,b)
    print("el resultado es: ",result)
    if a==0:
        break

a_power_b(a,b)
