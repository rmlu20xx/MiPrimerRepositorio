def menu():
  print("**********************")
  print("MENU")
  print("1- SUMAR")
  print("2- RESTAR")
  print("3- Salir")
  print("***********************(^_^)")

def default():
  return "Opción Invalida"

def opcion1(a,b):
  a1=str(a)
  b1=str(b)
  r=a+b
  r1=str(r)
  f=a1+"+"+b1+"="+r1
  return f

def opcion2(a,b):
  #a1=str(a)
  #b1=str(b)
  r=a-b
  #r1=str(r)
  #f=a1+"-"+b1+"="+r1
  return r

def switch(case,a,b):
  switcher={
    1: opcion1(a,b),
    2: opcion2(a,b),
    3: "salida",
  }
  return switcher.get(case,default())

a=int(input("Ingrese primer valor: "))
b=int(input("Ingrese segundo valor: "))
menu()
opcion=int(input("Seleccione la opción: "))
print(switch(opcion,a,b))
#print(opcion1(a,b))
