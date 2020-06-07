import sys
from random import randint
from Individual import Individual
"""Importamos la libreria random para generar numero alaeatorios.
y randint para generar numeros enteros aleatorios
"""


class App(object):
    'Clase App'

    def __init__(self):
    
        'Define los atributos del objeto:'
    
        self.maxLengthObjetive = 300 'tamaño maximo = 300'
        self.minLengthObjetive = 1 'tamaño minimo = 1 '
        self.maxPopulation = 300 'poblacion maxima = 300'
        self.minPopulation = 100 'poblacion minima = 100'
        self.minRateMutation = 0.0 'rango de mutación maxima = 0.0 '
        self.maxRateMutation = 1.0 'rango de mutación minima = 1.0'
        self.populations = []
        self.inputParams()
        self.executeGeneticAlgorithm()

    def inputParams(self):
        'Define los parametros de entrada'
        self.inputObjetive() 'es para introducir el objeto de entrada'
        self.inputPopulation() 'introdce la poblacion definida en el rango de 100 a 300'
        self.inputRateMutation() 'introcucir el valor de la mutación definida en un rango dde 0.0 a a 1.0.'

    def inputObjetive(self):
        """función para inresar el objeto (un texto). 
        se define una condicion, para controlar si es que se a ingresado o no un texto, en caso de no ser asi
        se muestra una exception con algun mensaje y si el objeto es muy corto o muy extensomuestra una alerta.
        """
        self.objetive = input("Ingrese el texto objetivo: ")
        if (len(self.objetive) == 0):
            raise Exception("Exception: El objetivo no fue ingresado!")
        if (len(self.objetive) < self.minLengthObjetive):
            raise Exception("Exception: El objetivo es muy corto!")
        if (len(self.objetive) > self.maxLengthObjetive):
            raise Exception("Exception: El objetivo es muy extenso!")

    def inputPopulation(self):
        'Introducir la población'
        self.numberPopulation = int(
            input("Ingrese cantidad de individuos por poblacion [100 a 300]: "))
        if (self.numberPopulation == 0):
            raise Exception(
                "Exception: La poblacion de individuos es invalida!")
        if (self.numberPopulation < self.minPopulation):
            raise Exception(
                "Exception: La poblacion de individuos es muy reducida!")
        if (self.numberPopulation > self.maxPopulation):
            raise Exception(
                "Exception: La poblacion de individuos es muy extensa!")

    def inputRateMutation(self):
        'Funcion para introducir la mutación'
        self.rateMutation = float(
            input("Ingrese la tasa de mutacion [0 a 1]: "))
        if (self.rateMutation < self.minRateMutation):
            raise Exception(
                "Exception: La tasa de mutacion no puede ser menor de %s" % self.minRateMutation)
        if (self.rateMutation > self.maxRateMutation):
            raise Exception(
                "Exception: La tasa de mutacion no puede ser mayor de %s" % self.maxRateMutation)

    def executeGeneticAlgorithm(self):
        
       ' Esta fución que ejceutar el algoritmo'

        for _ in range(0, self.numberPopulation):
            individual = Individual()
            individual.generateGenes(len(self.objetive), self.objetive)
            self.populations.append(individual)
        self.generation = 0
        print("Buscando mejor individuo....")
        while True:
            self.evaluateMembersGeneration()
            self.selectMembersGeneration()
            self.reproductionMembersGeneration()

    def evaluateMembersGeneration(self):
       
       ' Función para evaluar los miembros de la generación y mostrar la generación, el individuo y el fitness obtenido por cada miembro.
'
        self.generation += 1
        print("\n*************** GENERACION %s\n" % self.generation)
        for _ in range(0, self.numberPopulation):
            print("Generacion[%s] | Individuo[%s]: %s | fitness: %s" % (
                self.generation, _, self.populations[_].getPhenotype(), self.populations[_].getFitness()))
            if (self.evaluateObjetive(self.populations[_])):
                sys.exit()

    def selectMembersGeneration(self):
        'Función para selecionar los miembos de la generación'

        self.parents = []
        'ciclo para recorrer y seleccionar a los nuevos miembros'
        for _ in range(0, self.numberPopulation):
            n = int(self.populations[_].getFitness()*100)
            #for j in range(0, n):
            if n>0:
                self.parents.append(self.populations[_])

    def reproductionMembersGeneration(self):
       
        'Funcion para la generacion de nuevos miembros'

        totalParents = len(self.parents)
        print("Padres seleccionados: ", totalParents)
        for i in range(0, self.numberPopulation):
            a = int(randint(0, (totalParents-1)))
            b = int(randint(0, (totalParents-1)))
            father = self.parents[a]
            mother = self.parents[b]
            children = father.cross(mother)
            children.mutate(self.rateMutation)
            self.populations[i] = children

    def evaluateObjetive(self, individual):
     '   Funcion que evalua el objeto  y devuelve un true en caso de ser encontrado, de lo contrario devuelve un false'
           
        if (individual.getFitness() == 1.0):
            print("Objetivo encontrado: %s" % individual.getPhenotype())
            return True
        return False

    def showIndividualPhenotype(self):
        'Funcion para mostrar el objeto'

        for j in range(0, self.numberPopulation):
            print("Individuo %s : %s" %
                  (j, self.populations[j].getPhenotype()))


if __name__ == "__main__":
    try:
        app = App()
    except (ValueError, FileNotFoundError, AttributeError, Exception) as ex:
        print(ex)
