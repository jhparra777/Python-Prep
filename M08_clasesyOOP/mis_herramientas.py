class Herramientas:
    
    def __init__(self, lista_numeros):
        self.lista = lista_numeros

    def esPrimo (self, x):
        numero_primo = True # Iniciamos suponiendo que el numero puede ser primo
        if x > 3:
            for i in range(2,x):
                if x % i == 0:
                    numero_primo = False
                    break
        else:
            numero_primo = True
        return numero_primo
    
    def masRepetido (self, numeros):
        losNumeros = []
        vecesRepetidas = []
        for elemento in numeros:
            repite = numeros.count(elemento)
            if repite > 1 and elemento not in losNumeros:
                losNumeros.append(elemento)
                vecesRepetidas.append(repite)
        mayor = 0
        repite = 0
        for indice, elemento in enumerate (vecesRepetidas):
            if vecesRepetidas[indice] > repite:
                mayor = losNumeros[indice]
                repite = vecesRepetidas[indice]     
        return mayor, repite
    
    def convertir (self, valor, origen, destino):
        if origen != destino:
            if origen == 'C' and destino == 'F':
                resultado = (valor * 9/5) + 32
            elif origen == 'C' and destino == 'K':
                resultado =  (valor + 273.15)
            elif origen == 'F' and destino == 'C':
                resultado =  (valor - 32) * 5/9
            elif origen == 'F' and destino == 'K':
                resultado =  (valor - 32) * 5/9 + 273.15
            elif origen == 'K' and destino == 'C':
                resultado =  valor - 273.15
            elif origen == 'K' and destino == 'F':
                resultado =  (valor - 273.15) * 9/5 + 32
        else :
            resultado =  'no hay conversion'
        return resultado
    
    def factorial (self,numero):
        if (type(numero) != int):
            return 'El numero debe ser un entero'
        else:
            fact = 1
            i = 1
            while (i <= numero):
                fact *= i
                i = i + 1
        return fact  