def main():
    height= int(input("Enter triangle height: "))
    #Escribe tu código debajo de esta línea
    a=0
    b=0
    while a<height:
        a=a+1
        b=height-a
        print (" "*b,"*"*a)
    pass


if __name__=='__main__':
    main()
