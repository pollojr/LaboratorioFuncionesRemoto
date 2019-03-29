def a_power_b (a , b):
    prod = 1
    for i in range(0, b):
        prod=prod*a
    return(prod)

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
     
