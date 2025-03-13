
def menu ():
    print(f"------------------------------------")
anio= int(input("Ingrese un año: "));

def verificarAnio(anio):
    print(esBisiesto(anio));
    print(esPrimosumadigitos(anio));
        
def esBisiesto(anio):
    if ((anio % 4 == 0) and (anio ==0 and anio % 100 ==0 and anio % 400 ==0)):
        return True;
    else:
        return False;

def esPrimosumadigitos(anio):
    suma=sumaDigitos(anio);
    
    for i in range(2, suma):
        if suma % i == 0:
            return False;
    return True;
    
def sumaDigitos(anio):
    digitos = str(anio);
    suma=0;
    for digito in digitos:
        suma+int(digito);
    return suma;
