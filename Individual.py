# !/usr/bin/env python
# -*- coding: utf-8 -*-

#import random module
from random import randint
import random
"""Importamos la libreria random para generar numero alaeatorios.
y randint para generar numeros enteros aleatorios
"""

class Individual(object):
    """Clase Individual.
    Dentro de esta clase define el comportamiento del individuo y Se crea un objeto.
    
    Con el metodo __int__ se inicializan los atributos del objeto que se a creado.
    """

    def __init__(self):
        'atributos del objeto'
        self.minNumberChar = 32
        self.maxNumberChar = 128
        'rango de la mutacion'
        self.minRateMutation = 0.0 'minimo'
        self.maxRateMutation = 1.0 'maximo'
        self.genes = [] 'arreglo utilizado en la funcion genes'

    def generateGenes(self, numberGenes, objetive):
        """ Función para genera los numeros aleatorios que se eencuentren dentro del rango:
            minNumberChart = 32
            maxNumberchart = 128
        los cuales son los atributos que tiene el objeto
        """
        self.numberGenes = numberGenes
        self.objetive = objetive
        'ciclo de iteraciones que genera los caracteres(genes establecidos por la condicion)'
        for _ in range(0, self.numberGenes):
            self.genes.append(
                chr(randint(self.minNumberChar, self.maxNumberChar)))

    def getPhenotype(self):
        'Función es para construir el Genotipo'
        
        return ''.join(self.genes).encode("utf-8") 'retorna una union de caracteres que se generaron de manera aleatoria'

    def getFitness(self):
        """función qu establece el fitness de manera aleatoria a partir de un ciclo:
            i es una variable que almacena cada caracter de la
            cadena ingresada en cada posición de Array.
        """
        score = 0 'variable que aumenta al recorrer el arreglo'
        for i in range(0, len(self.genes)): ' (self.genes) arreglo donde esta definido los atributos del objeto y contiene el numero total de caracteres 
                           ' de una cadena.'
            if self.genes[i] == self.objetive[i]:
                score += 1
        return float(score)/float(len(self.objetive)) 'Retorna el score en decimal'

    def cross(self, couple):
        """ Función que mezcla las caracteristicas de los padres entre los individuos de la población para crear nuevos individuos. 
            
        """
        children = Individual() 'bjeto que se instancia a la clase Individual()'
        children.generateGenes(self.numberGenes,self.objetive) 'generacion de nuevos genes'
        middlePoint = int(randint(1, len(self.genes) - 1))
        for i in range(0, len(self.genes)):
            if (i > middlePoint):
                children.genes[i] = self.genes[i]
            else:
                children.genes[i] = couple.genes[i]
        return children

    def mutate(self, rateMutation):
        """Funcion que modfica algunas partes del genotipo de forma aleatoria.

        Los numeros que se generan son flotantes y se encuentran dentro del rango de mutacion
        establecidos anteriormente

        """
        for i in range(0, len(self.genes)):
            randRateMutation = float(random.uniform(
                self.minRateMutation, self.maxRateMutation))
            if (randRateMutation < rateMutation):
                if (self.genes[i] != self.objetive[i]):
                    self.genes[i] = chr(
                        randint(self.minNumberChar, self.maxNumberChar))
