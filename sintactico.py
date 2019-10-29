# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 23:02:21 2019

@author: Admin
"""

"""
analizador sintactico

es la serie de funciones que representan a nuestro analizador sintactico,
es decir las funciones que representan a nuestraas producciones

6+3+1n

L()    -> E() n
E()    -> T()E1()

E1()   -> + T()E1()
E1()   -> ""

T()    -> F()T1()

T1()   -> * F()T1()
T1()   -> ""

//F()    -> ( E() )
F()    -> digito
"""
from lexico import Lexico
import sys

class Sintactico(object):
    def __init__(self):
        self.lexico = Lexico()
        self.error = False
        self.errores = open("errores.txt", "w")
        
    def trow_error(self):
        print("error sintactico")
        sys.exit
        
    def print_position_lex_data(self):
        try:
            print(f"posicion: {self.lexico.posicion} "\
                  f"caracter: {self.lexico.actualCaracter()} "\
                  f"caracter sig: {self.lexico.siguienteCaracter()}\n"
                  )
        except:
            pass
            
        

    def L(self):
        """
        El inicio de el analisis la palabra inicial
        """
        print("llamando a sintactico palabra inicial")
        self.print_position_lex_data()
        e  = self.E()
        self.error = self.lexico.coincidir("n")
        if not self.error :
            self.trow_error()
        print(f"valor final de e: {e}")
        
    def E(self):
        print("llamando a E")
        self.print_position_lex_data()
        t = self.T()
        e1 = self.E1();
        return t+e1
        
        
    def E1(self):
        print("llamando a E1")
        self.print_position_lex_data()
        caracter_actual = self.lexico.actualCaracter()
        
        if caracter_actual == "+":
            self.error = self.lexico.coincidir("+")
            if not self.error:
                self.trow_error()
            t = self.T()
            e1 = self.E1()
            return t+e1
        return 0
    
    def T(self):
        print("llamando a T")
        self.print_position_lex_data()
        f = self.F()
        self.T1()
        return f
    
    def T1(self):
        print("llamando a T1")
        self.print_position_lex_data()
        caracter_actual = self.lexico.actualCaracter()
        
        if caracter_actual == "*":
            self.error = self.lexico.coincidir("*")
            if not self.error:
                self.trow_error()
            self.F()
            self.T1()
        else:
            pass
            
        
    
    def F(self):
        print("llamando a F")
        self.print_position_lex_data()
        
        caracter_actual = self.lexico.actualCaracter()
        if self.lexico.esdigito(caracter_actual):
            self.error = self.lexico.coincidir(caracter_actual)
            if not self.error:
                self.trow_error()
            return int(caracter_actual)
            
        
    
    