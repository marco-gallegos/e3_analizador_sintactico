# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 23:02:21 2019

@author: Admin
"""

"""
analizador lexico para nuestro ejercicio

debe leer la entrada de nuestro archivo e ir iterando de izq a der para
reconocer nuestro lenguaje

debe :
    guardar posicion
    funcion para iterar de caracter
"""
import re


class Lexico(object):
    def __init__(self, archivo_etrada = "entrada.txt"):
        self.tokens = {
                "(":"PARENTESISABRE",
                ")":"PARENTESISCIERRE",
                "+":"SUMA",
                "*":"MULTIPLICACION",
                "0":"DIGITO",
                "1":"DIGITO",
                "2":"DIGITO",
                "3":"DIGITO",
                "4":"DIGITO",
                "5":"DIGITO",
                "6":"DIGITO",
                "7":"DIGITO",
                "8":"DIGITO",
                "9":"DIGITO",
                }
        self.posicion=0
        self.palabra=""
        self.caracter_actual=""
        print("se creo lexico")
        self.programa = self.loadEntrada(archivo_etrada)
        
    def loadEntrada(self, archivo_entrada):
        archivo = open(archivo_entrada,"r")
        programa = archivo.read()
        programa = programa.replace("\n","").replace(" ","").replace("\t","")
        return programa
        
    
    def coincidir(self, caracter):
        """
        regresa booleano de si encontro el caracter que se le paso en la
        posicion que lleva.
        si coincidio se itera la posicion actual y devuelve el caracter
        """
        if self.programa[self.posicion] == caracter:
            print(f"coincide con : {caracter}\n")
            self.posicion += 1
            return caracter
        else:
            print(f"no coincide con {caracter}")
            return False
        
    def siguienteCaracter(self):
        """
        regresar el valor de el siguiente caracter ("token")
        """
        return self.programa[self.posicion+1]
    
    def actualCaracter(self):
        """
        regresar el valor actual, el caracter actual ("token")
        """
        return self.programa[self.posicion]
    
    def esdigito(self, caracter):
        """
        determina si el caracter es un digito
        """
        regex = "\d"
        resultado = re.match(regex, caracter)
        if resultado:
            return True
        else:
            return False
        
        
        
        
        
        
        
        
        
        