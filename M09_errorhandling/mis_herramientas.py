class Herramientas:
    
    def __init__(self, lista_numeros):
        if type(lista_numeros) != list:
            self.lista = []
            raise ValueError('Error debe ingrasar una lista núemeros enteros')  
        else :
            self.lista = lista_numeros

    def esPrimo (self, x):
        numero_primo = True # Iniciamos suponiendo que el numero puede ser primo
        if type(x) == int:
            if x > 3:
                for i in range(2,x):
                    if x % i == 0:
                        numero_primo = False
                        break
            else:
                numero_primo = True
            return numero_primo
        else :
            raise ('Error, debe ser un nunero entero')
    
    def masRepetido (self, numeros):
        if type(numeros)==list:
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
        else:
            raise ('Error, debe ser una lista de numeros entero')
    
    def convertir (self, valor, origen, destino):
        datos_correctos = False
        if origen in ['C','F','K'] and destino in ['C','F','K']:
            datos_correctos = True
        else: 
            raise Exception ('Hay un error, se espera "C", "F" o "K"')
        
        if origen != destino and datos_correctos:
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
        elif origen == destino and datos_correctos:
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