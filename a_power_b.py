def a_power_b (a , b):
    prod = 1
    for i in range(0, b):
        prod=prod*a
    print(prod)

num1=int(input("digite un numero"))
num2=int(input("digite la potencia a elevar el numero"))        
a_power_b(num1,num2)

     
