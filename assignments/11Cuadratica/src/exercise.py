import math

def main():
    # Escribe tu código abajo de esta línea
    valorA=int(input("Da el valor de a: "))
    valorB=int(input("Da el valor de b: "))
    valorC=int(input("Da el valor de c: "))
    if (valorA==0) and (valorB==0):
        print("No tiene solucion")
    elif (valorA==0):
        raiz=-valorC/valorB
        print(raiz)
    else:
        discrim=valorB**2-4*valorA*valorC
        if (discrim)>0:
            x1=(-valorB+math.sqrt(discrim))/(2*valorA)
            x2=(-valorB-math.sqrt(discrim))/(2*valorA)
            print(x1)
            print(x2)
        elif (discrim < 0):
            print("Raices complejas")
        else:
            x=-valorB/(2*valorA)
            print(x)

if __name__ == '__main__':
    main()
