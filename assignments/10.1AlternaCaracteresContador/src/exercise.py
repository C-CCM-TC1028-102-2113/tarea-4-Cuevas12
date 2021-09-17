def main():
  #escribe tu código abajo de esta línea
    num = int(input())
    for i in range(0,num,2):
        print("#")
        i += 1
        ##Hay que verificar el código, te está imprimiendo un caracter de más.
        if 1 < num:  
            print("%")
    pass
if __name__ == '__main__':
    main()
