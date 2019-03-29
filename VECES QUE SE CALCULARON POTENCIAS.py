def a_power_b (a,b):
    prod=1
    for x in range (1,b+1):
        if x>=1000:
            raise StopIteration("no se puede, lo siento")
        
        prod=prod*a
    return prod



poten=0
par=0
impar=0
error=0

while True:

    
    try:
        poten=poten+1
        b=int(input("ingrese la base"))
        if b ==0:
            print("EL NUMERO ES CERO")
            break
        exponente=int(input("ingrese el numero al que se va a elevar la base"))
        result=a_power_b(b,exponente)
        print("el resultado de su potencia es: ",result)
        if result % 2 ==0:
            par=par+1
        else:
            impar=impar+1
    except ValueError:
        error=error+1
        print("ingreso una letra")
    except StopIteration:
        error=error+1
        print("es mucho mas que el limite")


print("las potencias que intento calcular  son: ",poten)
print("los resultados pares son: ",par)
print("los resultados impares son: ",impar)
print("la cantidad de errores son: ",error)
