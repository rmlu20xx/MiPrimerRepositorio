seguir=True
#sw=0
while seguir: #sw==0: seguir==True:
    menu="""
    MENU
    1- SUMAR
    2- RESTAR
    3- MULTIPLICACIÓN
    4- SALIR
    """
    print(menu)
    op=int(input("Por favor digite la opción deseada..."))
    a=3
    b=4
    if op==1:
        s=a+b
        print("suma=",s)
    elif op==2:
        s=a-b
        print("resta=",s)
    elif op==3:
        s=a*b
        print("multiplicación=",s)
    elif op==4:
        print("Fin del Menu.")
        #sw=1
        seguir=False
    else:
        print("Opción incorrecta")