def main():
    #escribe tu código abajo de esta línea
    contador = 0
##Tener cuidado con la indentación.
suma = 0
numero = 0
while numero >=0:
 numero= float(input())
 suma += numero
 contador += 1
 if contador != 0: ## es recomendable utilizar esta condición numero >=0 para evitar que el negativo entre en el cálculo del promedio
     promedio = suma/contador
     print(promedio) ## Fuera del while para imprimir el resultado final del promedio
 else: ##Esta parte de código no es necesaria
     print() ##Esta parte de código no es necesaria
    pass
if __name__=='__main__':
    main()
