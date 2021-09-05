#Mensaje de bienvenida (RF01)
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
#Usuario y contraseña predefinidos (RF02)
Usuario=51717 

#Código para invertir un numero. Con esto generamos el Password. (RF02)
invertir = 0
valor = int(Usuario)
while valor > 0:
    residuo = valor % 10
    invertir = (invertir * 10) + residuo
    valor //= 10
Password=invertir
#**********************************************************************************

#Se definien 2 terminos numericos para el captcha (RF03)
Termino1_Captcha=717
Termino2_Captcha=((7%5)*5-5-5+1 )
Suma_Captcha = Termino1_Captcha+Termino2_Captcha #Calculo del resultado de los 2 terminos de captcha (RF03)

try:  #Se usa captura de excepciones para indicarf al usuario el error que se produce al ingresar los datos
    Usuario1=int(input("Ingrese su usuario = "))
    if(Usuario1 != Usuario):
        print("Error") #Error al ingresar el usuario
    else:
        Password1=int(input("Ingrese el password = "))
        if(Password1 != Password):
            print("Error") #Error al ingresar al password
        else:
            #Se hace el calculo del captcha (RF03)  
            print("No eres un Robot Resuelve el Captcha ","( ",Termino1_Captcha," + ",Termino2_Captcha," )")
            Resultado_Captcha=int(input("El resultado del Captcha es = "))
            if (Resultado_Captcha != Suma_Captcha):
                print("Error") #Error al calcular el captcha (RF03)
            else:
                print("Sesión iniciada") #Mensaje de confirmación de inicio de sesión (RF04)
except:
    print("Error, El valor ingresado debe ser un valor numerico")
