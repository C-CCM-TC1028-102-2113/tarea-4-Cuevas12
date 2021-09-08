def main():
    #escribe tu código abajo de esta línea
    contador = 0
suma = 0
numero = 0
while numero >=0:
 numero= float(input())
 suma += numero
 contador += 1
 if contador != 0:
     promedio = suma/contador
     print(promedio)
 else:
     print()
    pass
if __name__=='__main__':
    main()
